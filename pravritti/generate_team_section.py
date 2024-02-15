import csv

def read_contacts_from_csv(csv_file):
    contacts = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            role = row['role']
            if role not in contacts:
                contacts[role] = []
            contacts[role].append(row)
    return contacts

def generate_html_section(contacts):
    html = ''
    for role, members in contacts.items():
        html += f'<div class="role-section">\n'
        html += f'<h2>{role.capitalize()}s</h2>\n'
        html += '<div class="tiles">\n'
        for member in members:
            html += '<div class="tile">\n'
            html += f'<strong>{member["name"]}</strong>\n'
            html += f'<p>Email: {member["email"]}</p>\n'
            html += f'<p>Phone: {member["phone"]}</p>\n'
            html += '</div>\n'
        html += '</div>\n'
        html += '</div>\n'
    return html

def generate_html(contacts):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Team Contacts</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f7f7f7;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            .role-section {
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                padding: 20px;
                margin-bottom: 20px;
            }
            h2 {
                color: #555;
                font-size: 20px;
                margin-bottom: 10px;
            }
            .tiles {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
            }
            .tile {
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                padding: 20px;
                width: calc(33.33% - 20px);
                transition: transform 0.3s ease;
            }
            .tile:hover {
                transform: translateY(-5px);
            }
            .tile strong {
                color: #007bff;
                font-size: 18px;
                display: block;
                margin-bottom: 10px;
            }
            .tile p {
                margin: 0;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <h1>Team Contacts</h1>
    '''
    html += generate_html_section(contacts)
    html += '''
    </body>
    </html>
    '''
    return html

def main():
    csv_file = 'team_data.csv'
    contacts = read_contacts_from_csv(csv_file)
    html_content = generate_html(contacts)
    
    with open('team_contacts.html', 'w') as file:
        file.write(html_content)
    print("HTML file generated successfully!")

if __name__ == "__main__":
    main()
