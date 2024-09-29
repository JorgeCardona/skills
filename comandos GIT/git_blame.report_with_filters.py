import subprocess
import re
from datetime import datetime

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
            current_commit['commit_date'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
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

def generate_blame_html_report(report_details, file, output_html='blame_report.html'):
    """
    Generates an HTML report from the commit details of a file with column filters, sorting, and styled headers.

    Parameters:
    report_details (list): A list of dictionaries containing commit details for each line.
    file (str): The name of the file for which the report is generated.
    output_html (str): The name of the output HTML file. Default is 'blame_report.html'.
    """
    # HTML table header with filters, sorting, and styling
    html_content = f"""
    <html>
    <head>
        <title>Git Blame Report for {file}</title>
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
        <h1>Git Blame Report for {file}</h1>
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
    
    # Save the HTML file with utf-8 encoding
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Styled GIT BALME HTML report with sorting and filters generated: {output_html}")

# Usage of the functions
file_path = 'main.py'
report_details = git_blame_with_commit_details(file_path=file_path)
generate_blame_html_report(report_details=report_details, file=file_path)
