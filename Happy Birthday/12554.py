from sys import stdin

def main():
    num_of_names = int(stdin.readline().strip())
    names = []
    song = 'Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you'
    song = song.split(' ')
    while num_of_names != 0:
        names.append(stdin.readline().strip())
        num_of_names -= 1
    num_of_names = len(names)
    if num_of_names > 16:
        song_idx = 0
        for idx, name in enumerate(names):
            name_idx = idx
            print(name + ': ' + song[song_idx])
            if song_idx == len(song) - 1:
                song_idx = 0
            else:
                song_idx += 1
        name_idx = 0
        while song_idx != 16:
            print(names[name_idx] + ': ' + song[song_idx])
            song_idx += 1
            if name_idx == len(names) - 1:
                name_idx = 0
            else:
                name_idx += 1
    else:
        name_idx = 0
        for word in song:
            print(names[name_idx] + ': ' + word)
            if name_idx == len(names) - 1:
                name_idx = 0
            else:
                name_idx += 1
if __name__ == '__main__':
    main()
