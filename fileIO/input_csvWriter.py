import csv

with open("new_collected_names.csv", "a", newline="") as csvfile:
    spam_writer = csv.writer(csvfile, delimiter=" ",
                             quotechar="|",
                             quoting=csv.QUOTE_MINIMAL
                             )
    spam_writer.writerow(["Spam"] * 5 + ["Baked Beans"])
    spam_writer.writerow(["Spam", "Lovely Spam", "Wonderful Spam"])
    spam_writer.writerow(["Spam", "Lovely Spam", "Wonderful Spam"])
    spam_writer.writerow(["banana", "apple", "cherry", "pineapple", "mango"])
