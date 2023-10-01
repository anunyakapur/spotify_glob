##SPOTIFY EXERCISE GLOB
import csv
import glob

def main():
    all_files = glob.glob("regional-ca-daily-2023-09-*")
    result_unformatted = parse_files(all_files)
    result_formatted = format_dict(result_unformatted)
    return result_formatted

def format_dict(dictionary):
    for key in dictionary:
        print(key, dictionary[key])

def determine_date(file):
    index = file.find("y")
    d = file[index+2:index+12]
    return d

def parse_files(filenames):
    song_popularity_dict = {}
    for filename in filenames:
        date = determine_date(filename)
        
        with open(filename) as file_in:
            reader = csv.DictReader(file_in)

            for line in reader:
                artist = line["artist_names"]
                song = line["track_name"]
                streams = int(line["streams"])
                song_name_by_artist = f'{song} by {artist}'

                final = add_to_dict(song_popularity_dict, song_name_by_artist, date, streams)
                  
    return final

def add_to_dict(song_popularity_dict, song_name_by_artist, date, streams):
    
    if song_name_by_artist not in song_popularity_dict:
        song_popularity_dict[song_name_by_artist] = {}
    song_popularity_dict[song_name_by_artist][date] = streams

    return song_popularity_dict

print(main())
