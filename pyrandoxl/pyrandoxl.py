# pyrandoxl.py

import csv
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# Define the number of fake accounts to generate
num_accounts = 100

# Open the CSV file for writing
with open('fake_accounts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Name', 'Email', 'Password', 'Birthdate'])
    
    # Generate and write fake data for each account
    for _ in range(num_accounts):
        name = fake.name()
        email = fake.email()
        password = fake.password() # Note: Faker's password method generates a random password
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
        
        # Write the fake account data to the CSV file
        writer.writerow([name, email, password, birthdate.strftime('%Y-%m-%d')])

print("CSV file with fake accounts has been created.")
