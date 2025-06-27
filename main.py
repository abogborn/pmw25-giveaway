import csv
import datetime
import random
import json
import re

with open("required-script-info.json") as file:
    required_data = json.load(file)

with open(required_data["tiltifyCSV"]) as csv_input1:
    with open(required_data["googleCSV"]) as csv_input2:
        with open("pmw25_groomed-entries.csv", "w", newline='') as csv_output:
            input_reader1 = csv.reader(csv_input1)
            input_reader2 = csv.reader(csv_input2)
            output_writer = csv.writer(csv_output)
            validated_entry = []
            for row in input_reader1:
                # if "+" in row[3]:
                #     pass
                if row[3].lower() not in validated_entry:
                    output_writer.writerow(row)
                    validated_entry.append(row[3].lower())
            for row in input_reader2:
                # Figure this out for Google CSV entries and integrating them into the giveaway script
                if row[1].lower() not in validated_entry:
                    output_writer.writerow(['Google', 'Free', 'Entry', row[1].lower(), row[2], row[3], row[0], row[4], row[5], row[6], '', '', '', ''])
                    validated_entry.append(row[1].lower())

winners = int(input("How many giveaways would you like to choose winners for? Please only insert numbers. "))

def main(entries, timeframe_enabled, timeframe_start, timeframe_end):
    return winner_selection(entries, timeframe_enabled, timeframe_start, timeframe_end)

def timeframe_check(begin, end, entry):
    split_value = "."
    datetime_format = "%Y-%m-%d %H:%M:%S"
    datetime_begin = datetime.datetime.strptime(begin, datetime_format)
    datetime_end = datetime.datetime.strptime(end, datetime_format)
    try:
        datetime_winner = datetime.datetime.strptime(entry[6].split(split_value)[0], datetime_format)
    except:
        return False
    if datetime_begin < datetime_winner < datetime_end:
        return entry
    else:
        return False

def winner_selection(data, timeframe_enabled, timeframe_start, timeframe_end):
    successful_winner = False
    while successful_winner == False:
        winner = random.choice(data)
        if winner[0] == "Donation ID":
            break
        if timeframe_enabled == "y":
            timeframe_winner = timeframe_check(timeframe_start, timeframe_end, winner)
            if timeframe_winner != False:
                return timeframe_winner
            else:
                continue
        else:
            return winner

with open("pmw25_groomed-entries.csv") as giveaway:
    giveaway_reader = csv.reader(giveaway)
    entries = list(giveaway_reader)
    counter = winners
    while counter > 0:
        winner = main(entries, required_data["timeframeEnabled"], required_data["timeframeStart"], required_data["timeframeEnd"])
        if winner != None:
            print(winner)
            counter -= 1