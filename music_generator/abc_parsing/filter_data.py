# filtering songs in key of G major from original dataset into a separate file

with open("ireland.txt", "r", encoding="utf-8", errors="replace") as f:
    file = f.read()

rows = file.split('\n')

correct = 'K:G'
new_song = 'X:'
found = False

with open('gdata.txt', 'w') as outfile:
    for row in rows:
        if row == correct:
            found = True
        if new_song in row:
            found = False
        if found:
            outfile.write(row + '\n')

