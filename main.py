import csv
import datetime
import random

split_value = "."
datetime_format = "%Y-%m-%d %H:%M:%S"

filename = input("What is the file name of the Tiltify CSV placed in the same directory as this script?  Please include the full \"filename.csv\" in your input here.\n")

if input("Do you want to set a timeframe in which the donation must be made to win? (y/n)\n").lower() == "y":
    timeframe_conditional = True
    timeframe_beginning = input("What is the earliest time you'd like to define for the giveaway window used?  Format: \"YYYY-MM-DD HH:MM:SS\". (Use 24hr value in HH section.)\n")
    timeframe_end = input("What is the latest time you'd like to define for the giveaway window used?  Format: \"YYYY-MM-DD HH:MM:SS\". (Use 24hr value in HH section.)\n")
    datetime_beginning = datetime.datetime.strptime(timeframe_beginning, datetime_format)
    datetime_end = datetime.datetime.strptime(timeframe_end, datetime_format)
else:
    timeframe_conditional = False

if input("Do you want this giveaway to be US and Canada only? (y/n)\n").lower() == "y":
    region_conditional = True
    region_filename = input("What is the file name of the Google Form CSV placed in the same directory as this script?  Please include the full \"filename.csv\" in your input here.\n")
else:
    region_conditional = False

with open(filename) as input:
    with open("pmw25_groomed-entries.csv", "w", newline='') as output:
        input_reader = csv.reader(input)
        output_writer = csv.writer(output)
        validated_entry = []
        for row in input_reader:
             # if "+" in row[3]:
             #     pass
             if row[3].lower() not in validated_entry:
                 output_writer.writerow(row)
                 validated_entry.append(row[3].lower())

with open("pmw25_groomed-entries.csv") as giveaway:
    giveaway_reader = csv.reader(giveaway)
    entries = list(giveaway_reader)
    if region_conditional == True:
        with open(region_filename) as region:
            region_reader = csv.reader(region)
            region_source = list(region_reader)
    successful_winner = False
    while successful_winner == False:
        winner = random.choice(entries)
        if timeframe_conditional == True:
            try:
                datetime_winner = datetime.datetime.strptime(winner[6].split(split_value)[0], datetime_format)
                if datetime_beginning < datetime_winner < datetime_end:
                    if region_conditional == True:
                        for row in region_source:
                            if row[1].lower() == winner[3].lower():
                                if "NO" in row[4]:
                                    successful_winner = True
                                else:
                                    break
                    else:
                        successful_winner = True
                        print(winner)
                else:
                    continue
            except:
                continue
        else:
            successful_winner = True
            print(winner)