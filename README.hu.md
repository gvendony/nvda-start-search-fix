# Start menü keresés javítása NVDA-hoz

[English description](README.md)

Ez az NVDA-bővítmény megakadályozza, hogy a Windows 11 Start menüjében keresve az NVDA a találat helyett az „Az összes” fület olvassa fel.

## A probléma

Amikor beírsz valamit a Start menü keresőjébe, az NVDA elkezdi olvasni a legjobb találatot. Ezt azonban megszakítja egy ilyen szöveg: „Az összes, fül, kijelölve, 1 per 3”, így a találatot nem hallod.

## Az ok

A találatlista egy WebView2-ben futó weboldal. Az oldal a találatok minden újrarajzolásakor kijelölés eseményt küld a legjobb találatra, utána pedig az „Az összes” szűrőfülre is. Az NVDA leállítja a beszédet, és a találati oldalon minden kijelölt elemet felolvas, ezért a fül elvágja a találatot, és a navigátor is a fülre ugrik.

## Mit csinál a bővítmény

A bővítmény figyelmen kívül hagyja a szűrőfülek kijelölési eseményeit a találati oldalon. Minden más változatlan marad, és Windows-fájlokat nem módosít.

## Telepítés

1. Töltsd le a `.nvda-addon` fájlt a [Releases](https://github.com/gvendony/nvda-start-search-fix/releases) oldalról.
2. Nyisd meg a fájlt, és hagyd jóvá a telepítést.
3. Indítsd újra az NVDA-t.

## Kompatibilitás

- Tesztelve: NVDA 2026.3, Windows 11 26H2, 26300.9711-es build.
- Legkisebb NVDA-verzió: 2025.2. A 2026.3-nál régebbi verziókat nem teszteltem.

## Ismert korlátok

- A szűrőfül nem szólal meg, ha úgy jelölődik ki, hogy a fókusz a keresőmezőben marad.
- A Tab billentyűvel a szűrőfülekre lépést nem teszteltem. Ennek működnie kell, mert a valódi fókuszváltás külön esemény.

## Fordítás forrásból

Python 3 szükséges. Futtasd ezt: `python build.py`. A bővítmény a `dist` mappába kerül.

## Licenc

GNU General Public License 2-es verzió. Lásd: [LICENSE](LICENSE).
