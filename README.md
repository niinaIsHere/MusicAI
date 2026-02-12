# MusicAI

Application generates melodies in G-major

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
       Examples:
       Low c-sharp and c-flat: ^C, _C
       Middle c-sharp and c-flat: ^c, _c
       High c-shar and c-flat: ^c', _c'
5. Choose the length of the generated melody.

Right now the application supports generation only for seeds that are less than or equal to the Markov chain degree.
If seed is equal in length to the degree, no notes will be generated and the melody will just be the seed.

## Määrittelydokumentti

## Toteutusdokumentti

## Testausraportti

## Viikkoraportit
