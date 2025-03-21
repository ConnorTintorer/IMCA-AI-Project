import csv
import os

input_file = "raw_response.csv" 
output_file = "output.csv"

def format_table():
    all_keywords = set()
    image_data = []
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) < 2:
                continue  # Skip invalid rows

            filename = row[0].strip()
            id_num = os.path.splitext(filename)[0]
            id_num = id_num.split("_")[0]
            
            keywords = row[1].strip().strip('"').split(", ")  # Convert keyword string into a list
            
            all_keywords.update(keywords)  # Add keywords to the set

            # Store the filename and associated keywords
            image_data.append((filename, id_num, set(keywords)))

    # Step 2: Sort keywords to ensure consistent column order
    sorted_keywords = sorted(all_keywords)

    # Step 3: Write structured output to CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write header
        # writer.writerow(["filename"] + [f"Sum of {key}" for key in sorted_keywords])
        writer.writerow(["filename", "id"] + [f"Sum of {key}" for key in sorted_keywords])

        # Write image data with presence tracking
        for filename, id_num, keywords in image_data:
            row = [filename, id_num] + [1 if key in keywords else 0 for key in sorted_keywords]
            writer.writerow(row)
            
if __name__ == '__main__':
    format_table()