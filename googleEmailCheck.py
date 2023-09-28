import argparse
import csv
import dns.resolver

# Function to check if the domain is using Google Workspace
def is_google_workspace_domain(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            if "google.com" in str(mx.exchange):
                return "Yes"
        return "No"
    except dns.resolver.NXDOMAIN:
        return "No"

# Create argument parser
parser = argparse.ArgumentParser(description="Check if email addresses are hosted on Google Workspace.")

# Add input and output file arguments
parser.add_argument("input_file", help="Path to the input CSV file")
parser.add_argument("output_file", help="Path to the output CSV file")

# Parse command-line arguments
args = parser.parse_args()

# Open the input CSV file for reading and the output CSV file for writing
with open(args.input_file, 'r', newline='') as input_file, \
     open(args.output_file, 'w', newline='') as output_file:

    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Read the header row from the input file
    header = next(csv_reader)

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

print(f"Results written to {args.output_file}")
