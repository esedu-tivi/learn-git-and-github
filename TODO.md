# TODO

Tavoitteena on parantaa olemassa olevaa Pygame-peliä pienillä muutoksilla. Valitse yksi tai useampi alla olevista tehtävistä ja toteuta ne. 

## Tehtävät

1. **Vaihda pelaajan väri**
   - Muuta pelaajan suorakulmion väri esimerkiksi vihreäksi tai keltaiseksi.

2. **Lisää taustaväri**
   - Vaihda pelin taustaväri joksikin muuksi kuin valkoiseksi.

3. **Lisää toinen vihollinen**
   - Lisää peliin toinen vihollinen, joka liikkuu eri suuntaan tai nopeudella.

4. **Lisää pistelaskuri**
   - Näytä ruudulla pistelaskuri, joka kasvaa ajan myötä, kun pelaaja väistää vihollista.

5. **Rajoita pelaajan liikkuminen**
   - Varmista, että pelaaja ei voi liikkua ruudun ulkopuolelle.

6. **Muuta vihollisen nopeutta**
   - Tee vihollisesta nopeampi tai hitaampi.

7. **Lisää uudelleenkäynnistysvaihtoehto**
   - Salli pelaajan käynnistää peli uudelleen painamalla esimerkiksi "R"-näppäintä pelin päätyttyä.

8. **Lisää äänitehosteita**
   - Soita ääni, kun pelaaja törmää viholliseen.

9. **Muuta vihollisen muoto**
   - Tee vihollisesta ympyrä suorakulmion sijaan.

10. **Lisää taukotoiminto**
    - Salli pelaajan keskeyttää ja jatkaa peliä painamalla "P"-näppäintä.

## Ohjeet

1. Valitse yksi tai useampi tehtävä yllä olevasta listasta.
2. Muokkaa koodia tarvittavissa tiedostoissa toteuttaaksesi ominaisuuden.
3. Testaa muutokset varmistaaksesi, että ne toimivat odotetusti.
4. Palauta muokattu koodi ja lyhyt selitys siitä, mitä muutit.

## Esimerkki palautuksesta

Jos valitset tehtävän, jossa pelaajan väri vaihdetaan, selityksesi voisi näyttää tältä:

> **Tehtävä:** Vaihdoin pelaajan värin vihreäksi.  
> **Muokattu tiedosto:** `game.py`  
> **Lisätty/muutettu koodi:**
```python
# Muutettu pelaajan väri sinisestä vihreäksi
pygame.draw.rect(self.screen, (0, 255, 0), self.player)