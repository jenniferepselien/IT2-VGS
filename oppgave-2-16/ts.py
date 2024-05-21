import json


with open('spotify-weekly-top-songs-global-uke2-2023.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def song_with_most_weeks(data):
    max_weeks = 0
    song_name = ''
    for song in data:
        if song['uker_paa_listen'] > max_weeks:
            max_weeks = song['uker_paa_listen']
            song_name = song['navn']
    return song_name, max_weeks


def total_streams_taylor_swift(data):
    total_streams = 0
    for song in data:
        if 'Taylor Swift' in song['artist']:
            total_streams += song['antall_streams']
    return total_streams


def song_with_most_increase(data):
    max_increase = 0
    song_name = ''
    for song in data:
        increase = song['forrige_plassering'] - song['plassering']
        if increase > max_increase:
            max_increase = increase
            song_name = song['navn']
    return song_name, max_increase


most_weeks_song, weeks = song_with_most_weeks(data)
print(f"Sangen med flest uker på toppen er '{most_weeks_song}' med {weeks} uker.")

total_streams = total_streams_taylor_swift(data)
print(f"Totalt antall strømmer av Taylor Swift-sanger på topplisten er {total_streams}.")

most_increase_song, increase = song_with_most_increase(data)
print(f"Sangen som har økt mest i plassering fra forrige uke til denne er '{most_increase_song}' med en økning på {increase} plasser.")
