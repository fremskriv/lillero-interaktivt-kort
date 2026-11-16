# Lillero på Squarespace

1. Åbn `lillero-kodeblok.html` i en teksteditor og kopiér **hele indholdet**.
2. Tilføj én **Code Block** på Lillero-siden i Squarespace. Vælg HTML, indsæt koden, og slå **Display Source** fra, hvis indstillingen vises.
3. Gem og test sidens besøgsvisning, gerne i et privat browservindue. JavaScript kan være deaktiveret i redigeringsvisningen.

Billedet er allerede tilkoblet. Der kræves ingen separat CSS, Code Injection eller iframe. Kortets højde følger indholdet, også når en infoboks åbnes på mobil. Kortets CSS er isoleret i Shadow DOM, så det ikke ændrer resten af siden.

Squarespace-abonnementet skal understøtte JavaScript i Code Blocks (Core, Plus, Advanced eller et understøttet ældre abonnement). Se https://support.squarespace.com/hc/en-us/articles/206543167

## Ret tekst, links og grafik

- Søg efter `const hotspots` i kodeblokken. Her redigeres `title`, `description` og koordinaterne `x`/`y` (procenter).
- Hvert punkt har `href: null`. Erstat `null` med en rigtig URL i anførselstegn, fx `href: '/restaurant'`. Et link vises først, når både `href` og `ctaLabel` er udfyldt. Det gælder både mobil og desktop.
- Kortbilledet ligger på en fast GitHub-version. For at udskifte det: upload det nye billede til Squarespace, og erstat `<img src="...">` med billedets fulde URL. Bevar proportionerne, eller tilpas prikplaceringerne.
- Skiltene KAJAK, LEGEPLADS og WC OG BAD samt numrene 11 og 14 ligger som HTML oven på billedet.
- Gem den opdaterede kodeblok i GitHub og indsæt den igen på Squarespace. GitHub-ændringer opdaterer ikke automatisk Squarespace.

## Udvikling og kontrol

`lillero-kodeblok.html` er den færdige fil til Squarespace og kan redigeres direkte. `generate.py` kan genskabe den fra projektets `index.html` med Python 3; **det overskriver direkte ændringer i kodeblokken**, så kør det kun, hvis ændringerne er bevaret andetsteds.

Test kortet i den faktiske Squarespace-side på mobil og desktop: vandret rulning, infobokse, links og lukkekryds. Under 760 px bruges mobilvisning med vandret rulning og infoboks under kortet. Denne tilpasning bruger browserens bredde, så giv kortet en bred/full-width sektion frem for en smal kolonne på desktop.

Der er ingen automatisk timeout på infoboksene. De lukkes med kryds, Escape, klik udenfor eller klik på samme prik.

## Udført kontrol

Kodeblokken er testet indlejret på en lokal testside i desktopvisning og ved 390 px mobilbredde: indlæsning af det eksterne kortbillede, åbning af infoboks, mobilboksens automatiske højde, lukkekryds og klik uden for kortet. Omgivende sidestil blev holdt adskilt. Ikke afprøvet i Lilleros Squarespace-editor eller på fysiske telefoner.
