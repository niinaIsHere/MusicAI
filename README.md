# MusicAI

Application generates melodies (note sequences) from optional user seed in chosen key.

## Use:
Clone repository

navigate to the project root, a folder named 'music_generator'

run the project with command: python src/main.py

1. Give the degree of the Markov chain
2. With typing 'y' or 'n', choose whether you want to compose the beginning
3. If typed 'y', compose the beginning by writing note names separated by a wihtespace only.  
       Instructions:  
       You have three octaves to use: lowest( C-B ), middle( c-b ), highest( c'-b' )  
       Flats and sharps are denoted with '^' and '_' in front of the note.
          NOTE: Since the key is given, sharps and flats don't need to be denoted unless you want a note that doesn't belong in the key.  
       Examples:  
       Low c-sharp and c-flat: ^C, _C  
       Middle c-sharp and c-flat: ^c, _c  
       High c-sharp and c-flat: ^c', _c'  
5. Choose the length of the generated melody.

Right now the application supports generation only for seeds that are less than or equal to the Markov chain degree.  
If seed is equal in length to the degree, no notes will be generated and the melody will just be the seed.

## Määrittelydokumentti

[Määrittelydokumentti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/maarittelydokumentti.md)

## Toteutusdokumentti

[Toteutusdokumentti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/toteutusdokumentti.md)

## Testausraportti

[Testausraportti](https://github.com/niinaIsHere/MusicAI/blob/main/documentation/testausraportti.md)

## Viikkoraportit

[Viikkoraportit](https://github.com/niinaIsHere/MusicAI/tree/main/documentation/viikkoraportit)
