def count_songs(n: int) -> dict:
    genres = {}
    for i in range(n):
        song = input(f"Enter song {i+1}: ")
        name, genre = song.split(" - ")
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1
    return genres

n = int(input("Enter the number of songs: "))
genres = count_songs(n)
for genre, count in genres.items():
    print(f"{genre}: {count}")
