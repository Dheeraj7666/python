def read_feedback_files(filenames):
    feedback_data = []
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(": ")
                    feedback_data.append({
                        "name": data[0],
                        "rating": int(data[1].split(" - ")[0]),
                        "comment": " - ".join(data[1].split(" - ")[1:])
                    })
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
    return feedback_data

def process_feedback_data(feedback):
    total_entries = len(feedback)
    total_rating = sum(entry["rating"] for entry in feedback)
    average_rating = total_rating / total_entries if total_entries else 0.0
    return total_entries, average_rating

def write_summary_report(summary_data, feedback):
    total_entries, average_rating = summary_data

    with open("feedback_summary.txt", 'w') as file:
        file.write(f"Total Feedback Entries: {total_entries}\n")
        file.write(f"Average Rating: {average_rating:.2f}\n\n")
        file.write("Feedbacks:\n")
        for entry in feedback:
            file.write(f"{entry['name']}: {entry['rating']} - {entry['comment']}\n")

filenames = ["feedback1.txt", "feedback2.txt", "feedback3.txt"]
feedback_data = read_feedback_files(filenames)
summary_data = process_feedback_data(feedback_data)
write_summary_report(summary_data, feedback_data)

