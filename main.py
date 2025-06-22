import csv
import datetime
import random

#filename = input("What is the file name of the input file placed in the same directory as this script?  Please include the full \"filename.csv\" in your input here.\n")
filename = "tiltify-export-plastic-model-weekender-2x24-campaign-donations-v2__2024-05-23-2024-05-25.csv"
#timeframe_beginning = input("What is the earliest time you'd like to define for the giveaway window used?  Format: \"YYYY-MM-DD HH:MM:SS\". (Use 24hr value in HH section.)\n")
timeframe_beginning = "2024-05-23 20:00:00"
#timeframe_end = input("What is the latest time you'd like to define for the giveaway window used?  Format: \"YYYY-MM-DD HH:MM:SS\". (Use 24hr value in HH section.)\n")
timeframe_end = "2024-05-24 16:30:00"
split_value = "."
datetime_format = "%Y-%m-%d %H:%M:%S"
datetime_beginning = datetime.datetime.strptime(timeframe_beginning, datetime_format)
datetime_end = datetime.datetime.strptime(timeframe_end, datetime_format)

with open(filename) as input:
    with open("pmw25_groomed-entries.csv", "w", newline='') as output:
        input_reader = csv.reader(input)
        output_writer = csv.writer(output)
        validated_entry = []
        for row in input_reader:
             if "+" in row[3]:
                 pass
             if row[3].lower() not in validated_entry:
                 output_writer.writerow(row)
                 validated_entry.append(row[3].lower())

with open("pmw25_groomed-entries.csv") as giveaway:
    giveaway_reader = csv.reader(giveaway)
    entries = list(giveaway_reader)
    successful_winner = False
    while successful_winner == False:
        winner = random.choice(entries)
        try:
            datetime_winner = datetime.datetime.strptime(winner[6].split(split_value)[0], datetime_format)
            if datetime_beginning < datetime_winner < datetime_end:
                successful_winner = True
                print(winner)
            else:
                continue
        except:
            continue
