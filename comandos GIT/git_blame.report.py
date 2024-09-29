import subprocess
import re

def git_blame_with_commit_details(file_path, print_details=True):
    """
    Executes 'git blame' on the specified file and retrieves commit details for each line.
    
    Parameters:
    file_path (str): The path to the file to analyze with 'git blame'.
    print_details (bool): If True, prints the commit details for each line. Default is True.
    
    Returns:
    list: A list of dictionaries containing details for each line in the file.
    """
    details_list = []  # List to store details for each line

    # Execute git blame with the corresponding options
    process = subprocess.Popen(
        ['git', 'blame', '-l', '--color-lines', '--color-by-age', file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Read the output line by line
    for line in process.stdout:
        # Extract the commit ID by removing ANSI color sequences
        commit_id = re.sub(r'\x1b\[[0-9;]*m', '', line).split()[0]

        # Obtain the line number using a regular expression
        line_number_match = re.search(r'[^0-9]*([0-9]+)\)', line)
        line_number = line_number_match.group(1) if line_number_match else 'Unknown'

        # Get the content of the line by removing the line number and color sequences
        content_line = re.sub(r'\x1b\[[0-9;]*m', '', re.sub(r'^.*[0-9]+\) ', '', line))

        # Retrieve commit details
        commit_message = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%s', commit_id], text=True).strip()
        commit_author = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%an', commit_id], text=True).strip()
        commit_email = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%ae', commit_id], text=True).strip()
        commit_date = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%ad', '--date=short', commit_id], text=True).strip()

        # Store the details in a dictionary
        details_list.append({
            'line_number': line_number,
            'content_line': content_line,
            'commit_id': commit_id,
            'commit_message': commit_message,
            'commit_author': commit_author,
            'commit_email': commit_email,
            'commit_date': commit_date,
        })

        if print_details:
            # Print the line with the commit details
            print(
                f"\033[1;34mLine Number:\033[0m {line_number} - "
                f"\033[1;32mContent:\033[0m {content_line}  - "
                f"\033[0;33mCommit Message:\033[0m {commit_message} - "
                f"\033[1;36mCommit Id:\033[0m {commit_id} - "
                f"\033[1;35mAuthor:\033[0m {commit_author} - "
                f"\033[1;31mEmail:\033[0m {commit_email} - "
                f"\033[1;38;5;214mDate:\033[0m {commit_date}"
            )

    return details_list  # Return the list of dictionaries

def generate_html_report(report_details, file, output_html='blame_report.html'):
    """
    Generates an HTML report from the commit details of a file.

    Parameters:
    report_details (list): A list of dictionaries containing commit details for each line.
    file (str): The name of the file for which the report is generated.
    output_html (str): The name of the output HTML file. Default is 'blame_report.html'.
    """
    # HTML table header
    html_content = f"""
    <html>
    <head>
        <title>Git Blame Report for {file}</title>
        <style>
            table {{width: 100%; border-collapse: collapse;}}
            th, td {{border: 1px solid black; padding: 8px; text-align: left;}}
            th {{background-color: #f2f2f2;}}
            tr:nth-child(even) {{background-color: #f9f9f9;}}
            .commit-id {{color: #1e90ff;}}
            .author {{color: #2e8b57;}}
            .email {{color: #ff6347;}}
            .date {{color: #ffa500;}}
            .content {{color: #4682b4;}}
        </style>
    </head>
    <body>
        <h1>Git Blame Report for {file}</h1>
        <table>
            <tr>
                <th>Line Number</th>
                <th>Content</th>
                <th>Commit ID</th>
                <th>Commit Message</th>
                <th>Author</th>
                <th>Email</th>
                <th>Date</th>
            </tr>
    """

    # Add rows to the HTML content based on the report details
    for detail in report_details:
        html_content += f"""
            <tr>
                <td>{detail['line_number']}</td>
                <td class="content">{detail['content_line']}</td>
                <td class="commit-id">{detail['commit_id']}</td>
                <td>{detail['commit_message']}</td>
                <td class="author">{detail['commit_author']}</td>
                <td class="email">{detail['commit_email']}</td>
                <td class="date">{detail['commit_date']}</td>
            </tr>
        """
    
    # Close the HTML
    html_content += """
        </table>
    </body>
    </html>
    """
    
    # Save the HTML file
    with open(output_html, 'w') as file:
        file.write(html_content)

    print(f"HTML report generated: {output_html}")

# Usage of the functions
file_path = 'main.py'
report_details = git_blame_with_commit_details(file_path=file_path)
generate_html_report(report_details=report_details, file=file_path)
