import subprocess
import re
from datetime import datetime
import os

def generate_report_name_and_report_directory(directory_to_save_report, report_name_to_save, file_to_read):
    """
    Generates the name and full directory path for saving an HTML report.

    This function creates the specified directory if it does not exist and constructs 
    a report file name using the provided report name and file name.

    Parameters:
    directory_to_save_report (str): The relative or absolute path to the directory where the report will be saved.
    report_name_to_save (str): The base name for the report file.
    file_to_read (str): The name of the file related to the report, which will be appended to the report name.

    Returns:
    tuple: A tuple containing:
        - report_name (str): The complete name of the report file, including the .html extension.
        - report_directory (str): The full path to the report file, including the directory and file name.
    """
    
    current_directory = os.getcwd()
    final_directory = f'{current_directory}{directory_to_save_report}'

    # Normalize the report directory path to avoid issues on Windows
    final_directory = final_directory.replace('/', '\\')
    file_to_read = file_to_read.replace(':', '_').replace('/', '\\').replace('/', '_').replace('\\', '_')

    # Create the directory if it does not exist
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    report_name = f'{report_name_to_save}_{file_to_read}.html'

    report_directory = os.path.join(final_directory, report_name)

    return report_name, report_directory

def git_blame_with_commit_details(blame_file_path, blame_print_details=False):
    """
    Executes 'git blame' on the specified file and retrieves commit details for each line.
    
    Parameters:
    blame_file_path (str): The path to the file to analyze with 'git blame'.
    blame_print_details (bool): If True, prints the commit details for each line. Default is False.
    
    Returns:
    list: A list of dictionaries containing details for each line in the file.
    """
    details_list = []  # List to store details for each line

    # Execute git blame and retrieve all commit ids at once
    blame_output = subprocess.check_output(
        ['git', 'blame', '--line-porcelain', blame_file_path],
        text=True
    ).splitlines()

    current_commit = {}

    for line in blame_output:
        if line.startswith('author '):
            current_commit['commit_author'] = line[7:].strip()
        elif line.startswith('author-mail '):
            # Remove angle brackets from the email address
            current_commit['commit_email'] = line[12:].strip('<>')
        elif line.startswith('author-time '):
            # Convert the author time (UNIX timestamp) to YYYY-MM-DD format
            timestamp = int(line[12:].strip())
            current_commit['commit_date'] = datetime.utcfromtimestamp(timestamp).strftime('%a %b %d %H:%M:%S %Y -0500')
        elif line.startswith('summary '):
            current_commit['commit_message'] = line[8:].strip()
        elif re.match(r'^[0-9a-f]{40} ', line):
            commit_id, line_number = line.split()[:2]
            current_commit['commit_id'] = commit_id
            current_commit['line_number'] = line_number
        elif line.startswith('\t'):
            # This is the content line
            current_commit['content_line'] = line[1:].strip()
            details_list.append(current_commit.copy())

            if blame_print_details:
                print(
                    f"\033[1;34mLine Number:\033[0m {current_commit['line_number']} - "
                    f"\033[1;32mContent:\033[0m {current_commit['content_line']}  - "
                    f"\033[0;33mCommit Message:\033[0m {current_commit['commit_message']} - "
                    f"\033[1;36mCommit Id:\033[0m {current_commit['commit_id']} - "
                    f"\033[1;35mAuthor:\033[0m {current_commit['commit_author']} - "
                    f"\033[1;31mEmail:\033[0m {current_commit['commit_email']} - "
                    f"\033[1;38;5;214mDate:\033[0m {current_commit['commit_date']}"
                )

    return details_list  # Return the list of dictionaries

def generate_blame_html_report(blame_report_details, blame_file_to_read, blame_directory_to_save_report='/report/blame', blame_report_name_to_save='blame_report'):
    """
    Generates an HTML report of Git blame details for a specified file.

    This function creates a styled HTML report containing a table with Git blame information, 
    including line numbers, content, commit IDs, commit messages, authors, emails, and commit dates.
    The report allows for filtering and sorting of the displayed data.

    Parameters:
    blame_report_details (list of dict): A list containing dictionaries with Git blame details for each line, 
                                    where each dictionary should include:
        - line_number (int): The line number in the file.
        - content_line (str): The content of the line.
        - commit_id (str): The ID of the commit.
        - commit_message (str): The message associated with the commit.
        - commit_author (str): The author of the commit.
        - commit_email (str): The email of the author.
        - commit_date (str): The date of the commit.
    blame_file_to_read (str): The name of the file for which the Git blame report is generated.
    blame_directory_to_save_report (str, optional): The path to the directory where the report will be saved. Defaults to '/report/blame'.
    blame_report_name_to_save (str, optional): The base name for the report file. Defaults to 'blame_report'.

    Returns:
    None: The function saves the generated HTML report to the specified directory and prints a confirmation message.
    """
    
    report_name, report_directory = generate_report_name_and_report_directory(blame_directory_to_save_report, blame_report_name_to_save, blame_file_to_read)

    # HTML table header with filters, sorting, and styling
    html_content = f"""
    <html>
    <head>
        <title>Git Blame Report for {blame_file_to_read}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
            }}
            h1 {{
                text-align: center;
                color: #4a90e2;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border: 1px solid #ddd;
            }}
            th {{
                background: linear-gradient(90deg, #4a90e2, #50c878);
                color: white;
                font-weight: bold;
                cursor: pointer;
                text-align: center;
                position: relative;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }}
            th:hover {{
                background: linear-gradient(90deg, #50c878, #4a90e2);
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            .commit-id {{color: #1e90ff;}}
            .author {{color: #2e8b57;}}
            .email {{color: #ff6347;}}
            .date {{color: #ffa500;}}
            .content {{color: #4682b4;}}
            input {{
                width: 95%;
                padding: 8px;
                margin: 8px 0;
                box-sizing: border-box;
                border-radius: 4px;
                border: 1px solid #ccc;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            th:after {{
                content: " ⬍";
                font-size: 14px;
                color: white;
                padding-left: 8px;
            }}
        </style>
        <script>
            // Function to filter the table
            function filterTable(columnIndex) {{
                var input, filter, table, tr, td, i, txtValue;
                input = document.getElementsByTagName("input")[columnIndex];
                filter = input.value.toUpperCase();
                table = document.getElementById("blameTable");
                tr = table.getElementsByTagName("tr");
                
                for (i = 1; i < tr.length; i++) {{
                    td = tr[i].getElementsByTagName("td")[columnIndex];
                    if (td) {{
                        txtValue = td.textContent || td.innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                            tr[i].style.display = "";
                        }} else {{
                            tr[i].style.display = "none";
                        }}
                    }}       
                }}
            }}

            // Function to sort the table
            function sortTable(columnIndex) {{
                var table, rows, switching, i, x, y, shouldSwitch, dir, switchCount = 0;
                table = document.getElementById("blameTable");
                switching = true;
                dir = "asc"; // Set the sorting direction to ascending initially
                
                while (switching) {{
                    switching = false;
                    rows = table.rows;
                    
                    for (i = 1; i < (rows.length - 1); i++) {{
                        shouldSwitch = false;
                        x = rows[i].getElementsByTagName("td")[columnIndex];
                        y = rows[i + 1].getElementsByTagName("td")[columnIndex];
                        
                        if (dir == "asc") {{
                            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {{
                                shouldSwitch = true;
                                break;
                            }}
                        }} else if (dir == "desc") {{
                            if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {{
                                shouldSwitch = true;
                                break;
                            }}
                        }}
                    }}
                    
                    if (shouldSwitch) {{
                        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                        switching = true;
                        switchCount++;
                    }} else {{
                        if (switchCount == 0 && dir == "asc") {{
                            dir = "desc";
                            switching = true;
                        }}
                    }}
                }}
            }}
        </script>
    </head>
    <body>
        <h1>Git Blame Report for {blame_file_to_read}</h1>
        <table id="blameTable">
            <tr>
                <th onclick="sortTable(0)">Line Number<br><input type="text" onkeyup="filterTable(0)" placeholder="Filter by line number"></th>
                <th onclick="sortTable(1)">Content<br><input type="text" onkeyup="filterTable(1)" placeholder="Filter by content"></th>
                <th onclick="sortTable(2)">Commit ID<br><input type="text" onkeyup="filterTable(2)" placeholder="Filter by commit ID"></th>
                <th onclick="sortTable(3)">Commit Message<br><input type="text" onkeyup="filterTable(3)" placeholder="Filter by commit message"></th>
                <th onclick="sortTable(4)">Author<br><input type="text" onkeyup="filterTable(4)" placeholder="Filter by author"></th>
                <th onclick="sortTable(5)">Email<br><input type="text" onkeyup="filterTable(5)" placeholder="Filter by email"></th>
                <th onclick="sortTable(6)">Date<br><input type="text" onkeyup="filterTable(6)" placeholder="Filter by date"></th>
            </tr>
    """

    # Add rows to the HTML content based on the report details
    for detail in blame_report_details:
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
    
    # Save the HTML file with ISO-8859-1 encoding
    with open(report_directory, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Styled GIT BLAME HTML report with sorting and filters generated: {report_name}")

def generate_html_report_history(history_report_details, history_file_to_read, history_directory_to_save_report='/report/log_history', history_report_name_to_save='history_report'):
    """
    Generates an HTML report based on the commit history details with column filters, sorting, and styled headers.

    Parameters:
    history_report_details (list): A list of dictionaries containing commit details and changes.
    history_file_to_read (str): The path to the file analyzed.
    history_report_name_to_save (str): The name of the output HTML file. Default is 'history_report.html'.
    """

    report_name, report_directory = generate_report_name_and_report_directory(history_directory_to_save_report, history_report_name_to_save, history_file_to_read)
    # HTML table header with filters, sorting, and styling
    html_content = f"""
    <html>
    <head>
        <title>Git History Report for {history_file_to_read}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
            }}
            h1 {{
                text-align: center;
                color: #4a90e2;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border: 1px solid #ddd;
            }}
            th {{
                background: linear-gradient(90deg, #4a90e2, #50c878);
                color: white;
                font-weight: bold;
                cursor: pointer;
                text-align: center;
                position: relative;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }}
            th:hover {{
                background: linear-gradient(90deg, #50c878, #4a90e2);
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            .commit-id {{color: #1e90ff;}}
            .author {{color: #2e8b57;}}
            .email {{color: #ff6347;}}
            .date {{color: #ffa500;}}
            .message {{color: #4682b4;}}
            .added {{color: #388e3c;}}  /* Darker green for additions */
            .removed {{color: #ff6347;}} /* Red for deletions */
            input {{
                width: 95%;
                padding: 8px;
                margin: 8px 0;
                box-sizing: border-box;
                border-radius: 4px;
                border: 1px solid #ccc;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
        </style>
        <script>
            // Function to filter the table
            function filterTable(columnIndex) {{
                var input, filter, table, tr, td, i, txtValue;
                input = document.getElementsByTagName("input")[columnIndex];
                filter = input.value.toUpperCase();
                table = document.getElementById("historyTable");
                tr = table.getElementsByTagName("tr");
                
                for (i = 1; i < tr.length; i++) {{
                    td = tr[i].getElementsByTagName("td")[columnIndex];
                    if (td) {{
                        txtValue = td.textContent || td.innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                            tr[i].style.display = "";
                        }} else {{
                            tr[i].style.display = "none";
                        }}
                    }}       
                }}
            }}

            // Function to sort the table
            function sortTable(columnIndex) {{
                var table, rows, switching, i, x, y, shouldSwitch, dir, switchCount = 0;
                table = document.getElementById("historyTable");
                switching = true;
                dir = "asc"; // Set the sorting direction to ascending initially
                
                while (switching) {{
                    switching = false;
                    rows = table.rows;
                    
                    for (i = 1; i < (rows.length - 1); i++) {{
                        shouldSwitch = false;
                        x = rows[i].getElementsByTagName("td")[columnIndex];
                        y = rows[i + 1].getElementsByTagName("td")[columnIndex];
                        
                        if (dir == "asc") {{
                            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {{
                                shouldSwitch = true;
                                break;
                            }}
                        }} else if (dir == "desc") {{
                            if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {{
                                shouldSwitch = true;
                                break;
                            }}
                        }}
                    }}
                    
                    if (shouldSwitch) {{
                        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                        switching = true;
                        switchCount++;
                    }} else {{
                        if (switchCount == 0 && dir == "asc") {{
                            dir = "desc";
                            switching = true;
                        }}
                    }}
                }}
            }}
        </script>
    </head>
    <body>
        <h1>Git History Report for {history_file_to_read}</h1>
        <table id="historyTable">
            <tr>
                <th onclick="sortTable(0)">Commit ID<br><input type="text" onkeyup="filterTable(0)" placeholder="Filter by commit ID"></th>
                <th onclick="sortTable(1)">Author<br><input type="text" onkeyup="filterTable(1)" placeholder="Filter by author"></th>
                <th onclick="sortTable(2)">Email<br><input type="text" onkeyup="filterTable(2)" placeholder="Filter by email"></th>
                <th onclick="sortTable(3)">Date<br><input type="text" onkeyup="filterTable(3)" placeholder="Filter by date"></th>
                <th onclick="sortTable(4)">Commit Message<br><input type="text" onkeyup="filterTable(4)" placeholder="Filter by commit message"></th>
                <th onclick="sortTable(5)">Changes<br><input type="text" onkeyup="filterTable(5)" placeholder="Filter by changes"></th>
            </tr>
    """

    # Add rows to the HTML content based on the report details
    for commit in history_report_details:
        changes_html = ""
        for change in commit['changes']:
            line_style = "added" if change['type'] == 'added' else "removed"
            changes_html += f"<span class='{line_style}'>{'+' if change['type'] == 'added' else '-'} Line {change['line_number']}: {change['line']}</span><br>"

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
    
    # Save the HTML report to a file with ISO-8859-1 encoding
    with open(report_directory, 'w', encoding='ISO-8859-1') as file:
        file.write(html_content)

    print(f"GIT HISTORY HTML report generated: {history_report_name_to_save}")

def git_history_with_line_changes(history_file_path, history_print_details=False):
    """
    Retrieves the complete commit history for a specified file along with the changes made in each commit.

    Parameters:
    history_file_path (str): The path to the file to analyze.
    history_print_details (bool): If True, prints the changes for each commit. Default is True.

    Returns:
    list: A list of dictionaries containing details for each commit along with the changes.
    """
    history_list = []  # List to store details of each commit with line changes

    # Execute git log with patch to show changes
    process = subprocess.Popen(
        ['git', 'log', '-p', '--follow', '--', history_file_path],
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

    if history_print_details:
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

# Usage of the functions
file_path = 'C:\\Users\\USUARIO\\Documents\\satellite_notifier\\main.py'
report = git_blame_with_commit_details(file_path, blame_print_details=True)
generate_blame_html_report(report, file_path)

file_path = 'C:\\Users\\USUARIO\\Documents\\satellite_notifier\\.github\workflows\\main.yml'
report = git_history_with_line_changes(file_path)
generate_html_report_history(report, file_path)
