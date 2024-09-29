import subprocess
import re

def git_history_with_line_changes(file_path, print_details=True):
    """
    Retrieves the complete commit history for a specified file along with the changes made in each commit.

    Parameters:
    file_path (str): The path to the file to analyze.
    print_details (bool): If True, prints the changes for each commit. Default is True.

    Returns:
    list: A list of dictionaries containing details for each commit along with the changes.
    """
    history_list = []  # List to store details of each commit with line changes

    # Execute git log with patch to show changes
    process = subprocess.Popen(
        ['git', 'log', '-p', '--follow', '--', file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Read the output line by line
    current_commit = None
    commit_details = {}
    current_line_number = 0

    for line in process.stdout:
        line = line.rstrip()  # Remove trailing newline characters

        # Check for commit lines
        if line.startswith('commit '):
            if current_commit:  # If there is a current commit, save its details
                history_list.append(commit_details)

            # Start a new commit details dictionary
            current_commit = line.split()[1]  # Extract commit ID
            commit_details = {'commit_id': current_commit, 'changes': []}
        
        elif line.startswith('Author:'):
            commit_details['commit_author'] = line[8:].strip()  # Extract author
            commit_details['commit_email'] = line.split('<')[1].strip('>')  # Extract email

        elif line.startswith('Date:'):
            commit_details['commit_date'] = line[8:].strip()  # Extract date

        elif line.startswith('    '):  # Lines starting with spaces are commit messages
            if 'commit_message' not in commit_details:  # Ensure to store commit message once
                commit_details['commit_message'] = line.strip()  # Extract commit message

        elif line.startswith('+') and not line.startswith('+++'):
            # Lines starting with '+' are additions
            change_line = line[1:].strip()  # Remove the '+' sign
            commit_details['changes'].append({'type': 'added', 'line': change_line, 'line_number': current_line_number})

        elif line.startswith('-') and not line.startswith('---'):
            # Lines starting with '-' are deletions
            change_line = line[1:].strip()  # Remove the '-' sign
            commit_details['changes'].append({'type': 'removed', 'line': change_line, 'line_number': current_line_number})

        # Increment line number for each line processed
        if not line.startswith('commit '):
            current_line_number += 1

    # Add the last commit details if any
    if current_commit:
        history_list.append(commit_details)

    if print_details:
        for commit in history_list:
            print(f"\033[1;36mCommit Id:\033[0m {commit['commit_id']}")
            print(f"\033[1;35mAuthor:\033[0m {commit.get('commit_author', 'Unknown')}")
            print(f"\033[1;31mEmail:\033[0m {commit.get('commit_email', 'No email')}")
            print(f"\033[1;38;5;214mDate:\033[0m {commit.get('commit_date', 'Unknown')}")
            print(f"\033[0;33mMessage:\033[0m {commit.get('commit_message', 'No message')}")
            print("\033[1;32mChanges:\033[0m")
            for change in commit['changes']:
                print(f"  {'+' if change['type'] == 'added' else '-'} Line {change['line_number']}: {change['line']}")
            print()

    return history_list  # Return the list of commit details with line changes

def generate_html_report_history(report_details, file_path, output_html='history_report.html'):
    """
    Generates an HTML report based on the commit history details.

    Parameters:
    report_details (list): A list of dictionaries containing commit details and changes.
    file_path (str): The path to the file analyzed.
    output_html (str): The name of the output HTML file. Default is 'history_report.html'.
    """
    # HTML header and table structure
    html_content = f"""
    <html>
    <head>
        <title>Git History Report for {file_path}</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            .commit-id {{ color: #1e90ff; }}
            .author {{ color: #2e8b57; }}
            .email {{ color: #ff6347; }}
            .date {{ color: #ffa500; }}
            .message {{ color: #4682b4; }}
            .added {{ color: #28a745; }}
            .removed {{ color: #dc3545; }}
        </style>
    </head>
    <body>
        <h1>Git History Report for {file_path}</h1>
        <table>
            <tr>
                <th>Commit ID</th>
                <th>Author</th>
                <th>Email</th>
                <th>Date</th>
                <th>Commit Message</th>
                <th>Changes</th>
            </tr>
    """

    # Add rows to HTML content based on the report details
    for commit in report_details:
        changes_html = ""
        for change in commit['changes']:
            changes_html += f"<span class='{change['type']}'>{'+' if change['type'] == 'added' else '-'} Line {change['line_number']}: {change['line']}</span><br>"

        html_content += f"""
            <tr>
                <td class="commit-id">{commit['commit_id']}</td>
                <td class="author">{commit.get('commit_author', 'Unknown')}</td>
                <td class="email">{commit.get('commit_email', 'No email')}</td>
                <td class="date">{commit.get('commit_date', 'Unknown')}</td>
                <td class="message">{commit.get('commit_message', 'No message')}</td>
                <td>{changes_html}</td>
            </tr>
        """
    
    # Close the HTML tags
    html_content += """
        </table>
    </body>
    </html>
    """
    
    # Save the HTML report to a file
    with open(output_html, 'w') as file:
        file.write(html_content)

    print(f"HTML report generated: {output_html}")

# Example usage
file_path = 'main.py'
commit_history = git_history_with_line_changes(file_path=file_path)
generate_html_report_history(report_details=commit_history, file_path=file_path)
