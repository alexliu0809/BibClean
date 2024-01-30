import re

# Define the regular expression pattern for matching the title field in a BibTeX entry
title_pattern = re.compile(r"\btitle\s*=\s*{([^{}]+)}")

# Open the BibTeX file for reading
with open("bibtex_file.bib", "r") as f:
    # Read in the entire file
    file_content = f.read()

    # Split the file content into individual BibTeX entries
    entries = file_content.split("@")[1:]

    # Loop through each entry
    for entry in entries:
        # Extract the title field
        title_match = title_pattern.search(entry)
        if title_match:
            title = title_match.group(1)

            # Capitalize the first letter of each word in the title
            title = " ".join(word.capitalize() for word in title.split())

            # Replace the original title field with the capitalized version
            entry = title_pattern.sub(r"title = {%s}" % title, entry)

        # Print the modified BibTeX entry
        print("@" + entry)