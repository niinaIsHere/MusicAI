# Testausraportti

## Mitä testattu, miten?

Käytin pytestiä yksikkötesteihin. Kaiken kaikkiaan 39 testiä.

Testasin koko ohjelman toiminnan kahdella testillä test_full:ssa. Määrittelin syötteet vakioiksi tiedostoon ja niiden avulla tein test_pipeline() - testin, joka vie menee ohjelman toiminnan läpi ja tarkistaa, että lopputulos on oikeanlainen. Testi tarkistaa, että generoitu melodia on halutun pituinen ja että se alkaa seedillä. Lisäksi testasin, että generoidun melodian transitiot löytyvät triestä. Toinen pipeline testi on samanlainen, mutta se käyttää datana oikeaa dataa ja testaa generoidun melodian transitiot alkuperäistä dataa vasten.

Testasin datan käsittelyä tekemällä testidatatiedostot ja käyttämällä niitä testeissä. Testasin tiedoston valmistelemista, datan suodattamista, parsaamista ja kirjoittamista tiedostoon sekä tiedoston tyhjentämistä. Testejä datan käsittelylle on viisi. Filter ja parse testeissä on luotu testin sisällä testidatatiedostoa vastaava oikea tuloste ja testin lopuksi tarkistetaan, että metodin tulos ja oikea tulos on sama. Datan kirjoittamista tiedostoon varten on tehty tiedosto testidatan outputtaamiselle. Testi-output tiedoston tyhjentäminenkin testataan.
 
Testasin trien toimintaa viidellä testillä. Testasin trieen melodian lisäämistä lisäämällä melodian ja tarkistamalla, että melodia on triessä. Testasin, että etsimällä triessä olematonta melodiaa palautetaan None. Testasin, että trien frekvenssit ovat oikein lisäämällä tietyn määrän tiettyjä melodiakulkuja ja tarkistamalla, että niillä etsiessä seuraajien frekvenssit ovat oikeat. Testasin nuottinimien muunnosta luvuiksi ja toisinpäin testaamalla, että alkuperäinen melodia ja muunnosten jälkeinen melodia on sama.

Testasin generoimista kuudella testillä. Kaikissa käytin testejä varten rakennettua trietä. Testasin ns. päästä-päähän testin, jossa katsoin, että generoidusta melodiasta jokainen testin asteen n-grammi löytyy alkuperäisestä triestä. Testasin, että melodia alkaa annetulla 'seed' sekvenssillä, ja että se toimii myös ilman seediä ja seedillä, joka on pidempi kuin trien aste. Testasin, että generoitu melodia on 'length'-syötteen mittainen ja että kaikki generoidut nuotit ovat triessä. Testasin myös, että kaikki generoidut transitiot löytyvät triestä. Generointiin täytyi vielä lisätä sävellajin korjaaja ja testasin sitä sekä sävellajilla, johon tulee ylennykset, että sellaisella johon tulee alennukset.

Syötteen validoinnin testeissä testasin jokaista syötetyyppiä siten, että kaikki hyväksymättömät syötteet huomataan varmasti. Testasin myös jokaista yhdellä validilla syötteellä. 

## Minkälaiset syötteet:

Test_full varten tein testidatatiedoston full_test_data.txt. Datan käsittelyä varten tein tiedostot filter_test_data.txt, parse_test_data.txt, prep_file_test_data.txt, joihin loin testidatan. Otin lähinnä sopivia otteita oikeasta datasta, ja muokkasin niitä tarvittaessa, jotta ne edustavat tarpeeksi eri tilanteita. Trien testaamiseen loin joka testissä oman datansa. Dataa ei tarvittu trie-testeissä paljoa. Generoinnin testaamisessa loin test_generation moduulissa omassa metodissaan test-trien, johon suunnittelin melodiat siten, että generoinnin testaus onnistuu hyvin. Generoinnin sävellajitesteihin loin syötteiksi sopivan sävellajin ja melodian. Syötteen validoinnin testauksessa loin itse testisyötteet. Esimerkiksi test_valid_seed testissä loin itse mahdollisimman kattavan seedin, jotta kaiken tyyppiset validit nuotit käydään läpi.

## Miten voi toistaa?

Testit voi toistaa vain ajamalla ne, koska ne sisältävät kaikki syötteet itsessään. Test_full.py testit menevät läpi vain C ja Am sävellajeissa, koska niissä ei ole vaadittu apply_key - metodin käyttöä. Sävellaji testeissä valmiiksi C.
