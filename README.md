# MusicAI

Application generates melodies (note sequences) from optional user seed in chosen style and key and optionally saves them into a file.

## Use:
Clone repository

navigate to the project root, a folder named 'music_generator'. Path: MusicAI/music_generator:
```sh
cd music_generator
```
run the project with command: 
```sh
python src/main.py
```

### Input instructions:
1. Pick a style for your melodies from the options 'folk' and 'bach'. Folk melodies are generated based on a folk training dataset  
   and bach melodies based on songs by the classical composer J.S. Bach.
2. Pick a key for the generated melodies.  
          Possible keys:  
          C, Cm, D, Dm, E, Em, F, Fm, G, Gm, A, Am, B, Bm  
3. Give the degree of the Markov chain
4. With typing 'y' or 'n', choose whether you want to compose the beginning
5. If typed 'y', compose the beginning by writing note names separated by a whitespace only.  
       Instructions:  
       You have three octaves to use: lowest( C-B ), middle( c-b ), highest( c'-b' )  
       Flats and sharps are denoted with '^' and '_' in front of the note.  
          NOTE: Since the key is given, sharps and flats don't need to be denoted unless you want a note that doesn't belong in the key.  
       Examples:  
       Low c-sharp and c-flat: ^C, _C  
       Middle c-sharp and c-flat: ^c, _c  
       High c-sharp and c-flat: ^c', _c'  
       EXAMPLE MELODY (for the sake of format):  
          'c d e ^F G c' _d'  
7. Choose the length of the generated melody. The melody length includes the seed, so if you want a melody with 5 notes and give a seed of 5 notes  
   the generated melody will result in only the seed.
9. Choose how many songs you want to generate with these settings.
10. From the printed melodies, choose which ones you want to write into the output.txt file:  
    If you want all of them, write 'all',  
    if you want none of them, write '0',  
    if you want some of them, write their place in the order of generation:  
    generated 3 songs, you want the first and second one, write '1 2'.
11. Choose if you want to write the songs into an empty file or append onto previously saved melodies:  
    If you want to write into an empty file, write 'y',  
    if you want to keep the file contents, write something other than 'y'.

## Määrittelydokumentti

[Määrittelydokumentti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/maarittelydokumentti.md)

## Toteutusdokumentti

[Toteutusdokumentti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/toteutusdokumentti.md)

## Testausraportti

[Testausraportti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/testausraportti.md)

## Viikkoraportit

[Viikkoraportit](https://github.com/niinaIsHere/MusicAI/tree/main/documentation/viikkoraportit)
