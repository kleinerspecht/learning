import re
pattern = r"^([A-Z])([a-z' ]+):([A-Z ]+)$"

final_artist = ''
final_song = ''

while True:
    command = input()
    if command == 'end':
        break
    match = re.match(pattern, command)
    if match:
        artist = f'{match.group(1)}{match.group(2)}'
        key = len(artist)
        song = f'{match.group(3)}'
        print(artist)
        for i in artist:
            if i.isalpha():
                sum = ord(chr(key)) + ord(i)
                if sum > ord('z'):
                    n = sum - ord('z')
                    final_artist = final_artist + (chr(ord('a') + n-1))
                else:
                    final_artist = final_artist + (chr(ord(i) + key))
            else:
                print(i)
        print(final_artist)
        final_artist = ''
        #TODO -- Finish incrementation for artist!!!
