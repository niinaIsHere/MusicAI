# MusicAI

Application generates melodies (note sequences) from optional user seed in chosen key.

## Use:
Clone repository

navigate to the project root, a folder named 'music_generator'

run the project with command: python src/main.py

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
7. Choose the length of the generated melody.

The melody length includes the seed, so if you want a melody with 5 notes and give a seed of 5 notes the generated melody will result in only the seed.

## Määrittelydokumentti

[Määrittelydokumentti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/maarittelydokumentti.md)

## Toteutusdokumentti

[Toteutusdokumentti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/toteutusdokumentti.md)

## Testausraportti

[Testausraportti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/testausraportti.md)

## Viikkoraportit

[Viikkoraportit](https://github.com/niinaIsHere/MusicAI/tree/main/documentation/viikkoraportit)
