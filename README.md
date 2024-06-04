# Flappy Bird Game

## Descrizione
"Flappy Bird" è un semplice gioco basato su Pygame dove il giocatore controlla un uccello (o un pesce, o un aereo) che deve volare tra gli ostacoli senza colpirli. Questo progetto include tre temi diversi: Classic, Acquatic e Aero War, ciascuno con la propria grafica unica.

## Requisiti
- Python 3.x
- Pygame

## Installazione
1. Clona questo repository:
    ```bash
    git clone https://github.com/matteoabelli2007/FlappyBirdGame.git
    cd FlappyBirdGame
    ```
2. Installa Pygame:
    ```bash
    pip install pygame
    ```

## Utilizzo
1. Esegui il gioco:
    ```bash
    python FlappyBird.py
    ```
2. Seleziona il tema premendo uno dei seguenti tasti:
    - `C` per Classic
    - `A` per Acquatic
    - `W` per Aero War

3. Seleziona la difficoltà premendo uno dei seguenti tasti:
    - `E` per Easy
    - `M` per Medium
    - `H` per Hard

4. Durante il gioco:
    - Premi `SPACE` per far volare il tuo uccello (o pesce, o aereo).
    - Evita di colpire gli ostacoli.
    - Premi `ESC` per tornare al menu precedente.

## Struttura del Progetto
- `FlappyBird.py`: Il file principale che contiene tutto il codice del gioco.
- `bird.png`, `fish.png`, `plane.png`: Immagini dei personaggi per i vari temi.
- `pipe.png`, `tube.png`, `tower.png`: Immagini degli ostacoli per i vari temi.
- `background.png`, `spongebobBG.png`, `smashedCityBG.png`: Immagini di sfondo per i vari temi.

## Funzionalità
- **Temi Multipli**: Tre temi unici con grafica e personaggi diversi.
- **Diverse Difficoltà**: Tre livelli di difficoltà che influenzano la velocità del gioco.
- **Controlli Intuitivi**: Usa la barra spaziatrice per volare e `ESC` per navigare tra i menu.

## Screenshot
![Menu Temi](/screenshots/theme_menu.png)  
*Screenshot del menu di selezione dei temi.*

![Menu Difficoltà](/screenshots/difficulty_menu.png)  
*Screenshot del menu di selezione della difficoltà(classic).*

![Gioco in Corso - Classic](/screenshots/classic_gameplay.png)  
*Screenshot del gameplay nel tema Classic.*

![Gioco in Corso - Acquatic](/screenshots/acquatic_gameplay.png)  
*Screenshot del gameplay nel tema Acquatic.*

![Gioco in Corso - Aero War](/screenshots/aero_war_gameplay.png)  
*Screenshot del gameplay nel tema Aero War.*

![Game Over](/screenshots/game_over.png)  
*Screenshot della schermata di Game Over(classic).*

## FAQ
**Q: Come posso cambiare il tema?**  
A: All'avvio del gioco, seleziona il tema premendo `C` per Classic, `A` per Acquatic, o `W` per Aero War.

**Q: Come posso cambiare la difficoltà?**  
A: Dopo aver selezionato il tema, scegli la difficoltà premendo `E` per Easy, `M` per Medium, o `H` per Hard.

**Q: Come posso tornare al menu principale?**  
A: Premi `ESC` durante il gioco per tornare al menu di selezione della difficoltà. Premi `ESC` di nuovo per tornare al menu dei temi.

**Q: Come posso uscire dal gioco?**  
A: Premi `ESC` nel menu dei temi per uscire dal gioco.

**Q: Il gioco non funziona, cosa posso fare?**  
A: Assicurati di aver installato Python e Pygame correttamente. Controlla se ci sono errori nel terminale e prova a cercare una soluzione online o apri una issue su GitHub.

## Contribuire
Le richieste di pull sono benvenute. Per cambiamenti importanti, apri prima una issue per discutere cosa vorresti cambiare.

## Licenza
Questo progetto è licenziato sotto la licenza MIT - vedi il file [LICENSE](LICENSE) per i dettagli.

