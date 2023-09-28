import csv
import dns.resolver

# Function to check if the domain is using Google Workspace
def is_google_workspace_domain(domain):
    try:
        mx_records = dns.resolver.query(domain, 'MX')
        for mx in mx_records:
            if "google.com" in str(mx.exchange):
                return "Yes"
        return "No"
    except dns.resolver.NXDOMAIN:
        return "No"

# Input and output file paths
input_file_path = "GoogleEmail.csv"
output_file_path = "output.csv"

# Open the input CSV file for reading and the output CSV file for writing
with open(input_file_path, 'r', newline='') as input_file, \
     open(output_file_path, 'w', newline='') as output_file:

    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Read the header row from the input file
    header = next(csv_reader)

    # Add a new column header for Google Workspace status
    header.append("Google Workspace")

    # Write the updated header to the output file
    csv_writer.writerow(header)

    # Iterate through the rows in the input CSV
    for row in csv_reader:
        email = row[0]  # Assuming the email address is in the first column
        domain = email.split('@')[1]
        google_workspace_status = is_google_workspace_domain(domain)

        # Add the Google Workspace status to the row
        row.append(google_workspace_status)

        # Write the updated row to the output file
        csv_writer.writerow(row)

print(f"Results written to {output_file_path}")
