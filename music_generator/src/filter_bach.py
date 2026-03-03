
with open('melodies/test_bach.txt', 'r') as og_file:
    content = og_file.read()
    rows = content.split('\n')

caching = False
cache = []
stem_song = False
with open('melodies/realbach.txt', 'a') as real_file:
    for row in rows:
        real_file.write(row + '\n')
