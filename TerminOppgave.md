Her er en oppdatert versjon av `README.md` med samme oppsett som den første, men en mer avslappet tone:  

---

# VG2 TerminOppgave  

Dette prosjektet er en nettside som kombinerer brukersystem (registrering og innlogging), noen spill (Snake og Pizza-klikker), og en kontaktside. Målet er å lage en fungerende webapp der man lærer både frontend og backend, med en database som lagrer informasjon.  

## Prosjektoversikt  

**Formål:**  
Oppgaven er å lage en nettside som kombinerer ulike funksjoner for å lære hvordan ting henger sammen – fra designet brukerne ser, til hvordan data lagres i en database.  

**Hovedfunksjoner:**  
- Brukere kan lage konto, logge inn og logge ut.  
- Snake-spill og Pizza-klikker-spill som kjører direkte i nettleseren.  
- En "Kontakt oss"-side hvor meldinger kan sendes inn.  
- En "Om oss"-side som viser data fra databasen (brukerliste).  

---

## Teknologier brukt  

### Backend  
- **Python (Flask)**: Brukes for å lage rutene til nettsiden og koble den til databasen.  
- **MySQL**: Lagrer data som brukerkontoer, meldinger fra kontaktskjemaet og spillstatistikk.  

### Frontend  
- **HTML**: Bygger opp sidene.  
- **CSS**: Står for designet.  
- **JavaScript**: Brukes til interaktivitet, som popup-vinduer og spillene.  

---

## Filstruktur og forklaring  

### **Hovedfiler i prosjektet:**  

- **`program.py`**  
Hovedkoden for nettsiden. Den tar seg av alt fra brukerinformasjon til spillene og kontaktsiden.  
  - `get_db_connection()`: Kobler nettsiden til MySQL-databasen.  
  - `/register`, `/login`, `/logout`: Ruter for å registrere, logge inn og ut brukere.  
  - `/omoss`: Viser en liste over brukere fra databasen.  
  - `/kontaktoss`: Viser kontaktskjemaet og lagrer meldinger.  
  - `/snake` og `/Pizza`: Ruter som laster inn spillene.  

- **`templates/`**  
Her ligger alle sidene som vises i nettleseren, lagd i HTML:  
  - `home.html`: Hovedsiden som samler alt.  
  - `register.html` og `login.html`: Sider for registrering og innlogging.  
  - `kontaktoss.html`: Kontaktskjemaet.  
  - `omoss.html`: Viser brukere fra databasen.  

- **`static/`**  
CSS- og JavaScript-filene som gir design og interaktivitet:  
  - `style.css`: Gjør nettsiden pen.  
  - `javascript.js`: Inneholder popup-funksjoner og koden for spillene.  

- **`database.sql`**  
SQL-script som lager tabellene for databasen. Det er fire tabeller:  
  - `Brukere`: Lagrer brukernavn, e-post og passord.  
  - `snake`: For poeng i Snake (foreløpig ikke ferdig).  
  - `kobling`: Brukes til å knytte brukere til spillstatistikk (også under arbeid).  
  - `tickets`: Lagrer meldinger fra "Kontakt oss"-siden.  

---

## Spillene  

### **Snake:**  
Snake-spillet er laget med JavaScript og CSS.  
- Det bruker et grid-system for spilleområdet.  
- Eplet vises tilfeldig, og slangen beveger seg i retningen du styrer.  
- Poengsummen øker når slangen spiser et eple.  

### **Pizza-klikker:**  
Dette er et klikkespill hvor du samler pizza ved å klikke på en pizzaknapp.  
- Teller opp pizzaene automatisk når du klikker.  
- Enkelt, men morsomt for å lære hvordan JavaScript fungerer.  

---

## Installasjon  

1. **Installer Flask**  
   Først må du ha Flask. Installer det med:  
   ```bash
   pip install flask
   ```  

2. **Sett opp MySQL-databasen**  
   Kjør `database.sql` i MySQL for å lage tabellene.  

3. **Start prosjektet**  
   I terminalen, kjør:  
   ```bash
   python program.py
   ```  
   Gå til `http://localhost:4500` i nettleseren for å teste siden.  

---

## Ekstra info  

- MySQL-databasen må kjøre for at nettsiden skal fungere (bruk `get_db_connection()` i `program.py` for å koble til).  
- Hvis du vil endre designet, er det bare å redigere `style.css` i mappen `static/`.  
- Spillene kan også tilpasses i `javascript.js`.  

**Håper det hørtes bra ut!**
