# Toteutusdokumentti

## Ohjelman yleisrakenne

MusicAI sisältää documentation ja music_generator kansiot. music_generator sisältää datan, testit, testidatan ja ohjelman erillisissä kansioissa.

Ohjelma on jaettu eri moduuleihin käyttötarkoituksen mukaan. Moduuleja on kuusi: data, input_validation, input, trie, trainer ja generator.

Data.py:ssa käsitellään data valmiiksi ohjelman käyttöön. Siellä mm. suodatetaan sopiva sävellaji alkuperäisestä datatiedostosta käyttäjän syötteen perusteella. Sopivista kappaleista parsetaan melodiat ohjelman ymmärtämään muotoon. Datasettejä on kaksi vaihtoehtoa, joista käyttäjä valitsee toisen.

Input-moduuli hoitaa käyttäjältä syötteiden pyytämisen. Input_validionin avulla tarkistetaan, että syötteet kelpaavat.

Trie sisältää trien rakenteen ja siihen suoraan liittyvät metodit, kuten nuottien muunnos luvuiksi ja triestä melodian etsiminen. Trainer-moduuli sisältää vain yhden metodin, joka syöttää harjoitusdatan trieen.

Generator sisältää generoivan moduulin ja sävellajimuunnokseen tarvittavan moduulin. Generator palauttaa ohjelman lopullisen syötteen, joka on siis käyttäjän syötteiden perusteella generoitu melodia.

Main.py:ssä pyydetään ensin käyttäjältä sävellaji, sitten käsitellään data sen mukaan. Sen jälkeen pyydetään loput syötteet ja harjoitetaan trie ja generoidaan melodia syötteiden perusteella.

## Saavutetut aika- ja tilavaativuudet

Aikavaativuutta testattu mittaamalla generoinnin viemä aika eri pituisilla melodioilla ilman käyttäjän antamaa seediä G-duurisävellajissa asteella 1. Suoritusajat olivat seuraavat:

100 säveltä:  
0.00047760800043761265  
1000 säveltä:  
0.004281972000171663  

Huomaamme, että kun generoitujen sävelten määrä kasvaa kymmenkertaiseksi, myös generoinnin viemä aika kasvaa suunnilleen kymmenkertaiseksi. Tästä voimme päätellä, että aikavaativuus on O(n).

Aikavaativuus O(n) selittyy sillä, että generointi tekee aina niin sanotusti saman operaation lisätessään uuden sävelen melodiaan. Triestä etsitään sopiva n-grammi ja mahdollisista seuraajista arvotaan seuraava ääni.

## Puutteet ja parannukset?

Datatiedostot sisältävät melko eri määrän kappaleita eri sävellajeissa, joten eri sävellajit eivät ole ns. tasa-arvoisessa asemassa datan suhteen. Bach-kappaleita ei ole ollenkaan sävellajeissa Fm tai Bm, joka on selkeä puute. Muutenkin mollisävellajeja on Bach-datasetissä vähän verrattuna duureihin. Lisäksi datasettejä on nyt vain kaksi ja lisää vaihtoehtoja olisi ollut hyvä.

Yksi puute ohjelmassa on, että kappaleiden etumerkit transponoidaan mukaan tietyllä tavalla tarpeettomasti, koska abc-notaatiossa esim 'K:G' tarkoittaa jo sitä, että tiedostetaan esimerkiksi f olevan f#. Apply_key - metodin olisi siis voinut jättää poiskin, kunhan output.txt sisällytettäisiin sävellajin merkkaava rivi.

## Laajojen kielimallien käyttö:

Olen käyttänyt Copilottia käytännön kysymyksissä, kuten liittyen tiedostojen järjestämiseen ja esimerkiksi import-ongelmiin säästääkseni aikaa. Olen lisäksi välillä varmistanut omaa suunnitteluni suuntaa siten, että kysyn onko tämä järkevä suunta tai järjestys tehdä asioita. Käyttänyt siis työn tukena lähinnä nopeana Googlena.

## Lähteet:

https://en.wikipedia.org/wiki/Trie  
https://en.wikipedia.org/wiki/Markov_chain  
https://abcnotation.com/  
https://trillian.mit.edu/~jc/music/abc/mirror/home.quicknet.nl/ireland.abc


