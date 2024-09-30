import subprocess
import re
from datetime import datetime
import os

def git_blame_with_commit_details(file_path, print_details=False):
    """
    Executes 'git blame' on the specified file and retrieves commit details for each line.
    
    Parameters:
    file_path (str): The path to the file to analyze with 'git blame'.
    print_details (bool): If True, prints the commit details for each line. Default is False.
    
    Returns:
    list: A list of dictionaries containing details for each line in the file.
    """
    details_list = []  # List to store details for each line

    # Execute git blame and retrieve all commit ids at once
    blame_output = subprocess.check_output(
        ['git', 'blame', '--line-porcelain', file_path],
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

            if print_details:
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

def generate_blame_html_report(report_details, file_to_read, directory_to_save_report='/report/blame', report_name_to_save='blame_report'):
    """
    Generates an HTML report of Git blame details for a specified file.

    This function creates a styled HTML report containing a table with Git blame information, 
    including line numbers, content, commit IDs, commit messages, authors, emails, and commit dates.
    The report allows for filtering and sorting of the displayed data.

    Parameters:
    report_details (list of dict): A list containing dictionaries with Git blame details for each line, 
                                    where each dictionary should include:
        - line_number (int): The line number in the file.
        - content_line (str): The content of the line.
        - commit_id (str): The ID of the commit.
        - commit_message (str): The message associated with the commit.
        - commit_author (str): The author of the commit.
        - commit_email (str): The email of the author.
        - commit_date (str): The date of the commit.
    file_to_read (str): The name of the file for which the Git blame report is generated.
    directory_to_save_report (str, optional): The path to the directory where the report will be saved. Defaults to '/report/blame'.
    report_name_to_save (str, optional): The base name for the report file. Defaults to 'blame_report'.

    Returns:
    None: The function saves the generated HTML report to the specified directory and prints a confirmation message.
    """
    
    report_name, report_directory = generate_report_name_and_report_directory(directory_to_save_report, report_name_to_save, file_to_read)

    # HTML table header with filters, sorting, and styling
    html_content = f"""
    <html>
    <head>
        <title>Git Blame Report for {file_to_read}</title>
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
        <h1>Git Blame Report for {file_to_read}</h1>
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
    
    # Save the HTML file with ISO-8859-1 encoding
    with open(report_directory, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Styled GIT BLAME HTML report with sorting and filters generated: {report_name}")

# Usage of the functions
file_path = 'C:\\Users\\USUARIO\\Documents\\satellite_notifier\\main.py'
report = git_blame_with_commit_details(file_path, print_details=True)
generate_blame_html_report(report, file_path)
