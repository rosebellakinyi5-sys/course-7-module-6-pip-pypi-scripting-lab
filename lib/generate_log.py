from datetime import datetime
import os
import json
import urllib.request

    # TO-DO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

def fetch_data():
    """Fetch data from a public API endpoint using standard libraries."""
    url = "https://typicode.com"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status == 200:
                return json.loads(response.read().decode())

    except Exception:
        return {"title":"Offline Data Recovery Mode"}
    return{}

def generate_log(data=None):
    """Generate a structured log file with API results."""

    if data is not None and not isinstance(data, list):
        raise ValueError("Expected a list for data parameter.")

    if data is None:
        post = fetch_data()
        title = post.get("title","No title found")
        print(f"Fetched Post Title: {title}")


        log_data = [
            "User logged in",
            "User updated profile",
            f"API Data Result: {title}",
            "Report exported"
        ]
    else:
        log_data = data

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    generate_log()