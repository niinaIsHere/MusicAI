Määrittelydokumentti

Ohjelmointikielet:
Käytän ohjelman tekemiseen Pythonia. En osaa muita kieliä hyvin. 

Toteutus (algoritmi ja tietorakenne)
Aion toteuttaa projektin käyttämällä Markovin ketjua ja trie-tietorakennetta ja aion tehdä ohjelman, joka kuvailtiin esimerkkiprojektien aiheissa.
Ohjelma generoi nuottikulkuja harjoitusdatan perusteella. Nuottikulut tuotetaan Markovin ketjun avulla laskettujen siirtymätodennäköisyyksien perusteella:
harjoitusdatasta lasketaan, kuinka todennäköisesti tiettyä nuottijonoa seuraa jokin tietty nuotti. Todennäköisyydet talletetaan trie-tietorakenteeseen.
Tästä valitaan jokaisen nuotin seuraaja satunnaisesti, mutta painotettuna siirtymätodennäköisyyksillä.
Käyttäjä voi määrittää melodian pituuden ja nuotteja liikutaan eteenpäin, kunnes ollaan saavutettu tavoiteltava pituus.

Syötteet:
Markovin ketjun asteluku saadaan käyttäjältä syötteenä. Asteluku määrittää käyttäjän syötteenä antaman melodian alun pituuden.
Jos asteluku on yksi, käyttäjän täytyy antaa vain yksi nuotti alkumelodiaksi. Melodian alku määrittää generoitavan melodian tyylin ja siirtymien todennäköisyydet.
Lisäksi käyttäjä voi määrittää generoidun melodian pituuden antamalla siihen kuuluvien nuottien määrän. Melodiaa generoidaan, kunnes se on halutun pituinen.
Ohjelman tuloste on generoitu nuottikulku kirjoitettuna nuottien nimillä.

Ohjelman tarkoitus:
Ohjelman tarkoitus on demonstroida, miten esimerkiksi nuottikulkuja voidaan generoida tietyn algoritmin ja tietorakenteen avulla.
Samankaltainen lähestymistapa sopii muihinkin asioihin, kuin musiikkiin. Ohjelman avulla on kiinnostava myös havainnoida, miten asteluku ja ensimmäiset nuotit vaikuttavat lopputulokseen.
Ohjelman rajoitteita on esimerkiksi se, että siinä ei oteta nyt huomioon rytmiä tai harmoniaa, jotka ovat olennainen osa musiikkia.
Tämä kuitenkin tietyllä tavalla pelkistää ohjelman tarkastelemaan erityisesti nuottien asteita, joka on sinällään kiinnostava lähestymistapa.

Aika- ja tilavaativuudet:
Tarkoitus on päästä aikavaativuuteen O(N) käydessä läpi harjoitusdata ja laskemalla sen perusteella siirtymätodennäköisyydet.
Aikavaativuus on tämä, koska jokainen nuotti tarvitsee käydä läpi vain kerran ja päivittää siirtymät ohjelmalle.
Generoinnissa tavoitteena on päästä aikavaativuudeen O(n * (haluttu melodian pituus)), koska jokaiselle nuotille on käytävä läpi n-suuruinen tietorakenne. 
Tilavaativuus on O(K^n) pahimmassa tapauksessa, jossa jokainen nuottikulku esiintyy harjoitusdatassa. K tarkoittaa harjoitusdatan sisältämien erilaisten nuottien määrää.

Ohjelman ydin:
Ohjelman ydin on todennäköisyyksiin perustuva generointialgoritmi, joka suorittaa generoinnin. Tämän lisäksi ohjelmaan kuuluu datan käsittelyä ja rakenteiden muodostamista.

Kuulun tietojenkäsittelytieteen kandiohjelmaan (TKT), dokumentaatiossa aion käyttää englantia.
