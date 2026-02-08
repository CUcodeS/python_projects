"""
COMP.CS.100, Ohjlemointi 1, Projekti 2
Susanna Kupari, 151625787
susanna.kupari@tuni.fi

Ohjelma pyytää käyttäjää syöttämään meriveden korkeutta ilmaisevia arvoja ja
ilmoittaa niiden suurimman ja pienimmän arvon, mediaanin, keskiarvon ja
keskihajonnan.
"""

from math import sqrt


def tulosta_arvot(korkeuserot, mediaani, keskiarvo, keskihajonta):
    """Funktio tulostaa näytöllä parametreina saatavat arvot. Selitteet
    arvoille on annettu listana, josta sopiva selite tulostetaan arvon eteen.

    :param korkeuserot: float, meriveden korkeuden pienin ja suurin arvo
    :param mediaani: float, meriveden korkeutta kuvaavien arvojen mediaani
    :param keskiarvo: float, meriveden korkeutta kuvaavien arvojen keskiarvo
    :param keskihajonta: float, meriveden korkeutta kuvaavien arvojen
           keskihajonta
    :return: Ei paluuarvoa, tulostaa näytölle parametrien arvot selitteineen
    """
    # Arvojen tulostuksessa on hyödynnetty listaa, jotta voidaan f-stringin
    # avulla asettaa tulostusleveys, jotta arvot ovat siististi samalla
    # rivillä. Muuttuja selite kuvaa tulosteessa mistä arvosta on kyse.
    #         0           1           2          3        4
    selite = ["Minimum:", "Maximum:", "Median:", "Mean:", "Deviation:"]

    print(f"{selite[0]:<11}{min(korkeuserot):.2f} cm")
    print(f"{selite[1]:<11}{max(korkeuserot):.2f} cm")
    print(f"{selite[2]:<11}{mediaani:.2f} cm")
    print(f"{selite[3]:<11}{keskiarvo:.2f} cm")
    print(f"{selite[4]:<11}{keskihajonta:.2f} cm")


def laske_keskihajonta(keskiarvo, lista_korkeuksista):
    """Funktio saa parametreina listan meriveden korkeuksista sekä listan
    keskiarvon ja laskee listan keskihajonnan hyödyntämällä varianssin laskevaa
    funktiota laske_varianssi(), jota kutsutaan tässä funktiossa.

    :param keskiarvo: float, listan keskiarvo
    :param lista_korkeuksista: float, lista meriveden korkeuksista
    :return: float, palauttaa listan keskihajonnan
    """

    varianssi = laske_varianssi(keskiarvo, lista_korkeuksista)
    keskihajonta = sqrt(varianssi)
    return keskihajonta


def laske_varianssi(keskiarvo, lista_korkeuksista):
    """Funktio saa parametreina listan meriveden korkeutta kuvaavista arvoista
    sekä niiden keskiarvon. Näiden avulla lasketaan varianssi, jota käytetään
    keskihajonnan laskemiseen.

    :param keskiarvo: Meriveden korkeuksien keskiarvo
    :param lista_korkeuksista: Lista meriveden korkeuksista
    :return: Palauttaa varianssin arvon
    """

    arvo_varianssin_laskemiseen = (keskiarvo - lista_korkeuksista[0]) ** 2
    for arvo in range(1, len(lista_korkeuksista)):
        arvo_varianssin_laskemiseen += (keskiarvo - lista_korkeuksista[arvo]) \
                                       ** 2

    varianssi = arvo_varianssin_laskemiseen / (len(lista_korkeuksista) - 1)
    return varianssi


def laske_mediaani(lista_korkeuksista):
    """Funktio saa parametrina listan meriveden korkeuksista. Lista
    järjestetään suuruusjärjestykseen, josta otetaan listan mediaani, joka
    palautetaan kutsuvalle funktiolle.

    :param lista_korkeuksista: float, lista meriveden korkeuksista
    :return: float, palauttaa mediaanin
    """

    järjestetty_lista = sorted(lista_korkeuksista)
    if len(järjestetty_lista) % 2 == 0:
        # Jos listassa on parillinen määrä arvoja, lasketaan mediaanit ensin
        # jakamalla listan pituus kahdella. Koska listan pituus on yhtä
        # suurempi kuin viimeisen arvon indeksi, on listan pituus myös
        # parillinen, jolloin saadaan oikean puoleisen mediaanin indeksi.
        # Tällöin indeksi-1 on vasemman puoleisen mediaanin indeksi.
        indeksi_mediaanille = int(len(järjestetty_lista) / 2)
        mediaanit = [järjestetty_lista[indeksi_mediaanille],
                     järjestetty_lista[indeksi_mediaanille-1]]
        mediaani = laske_keskiarvo(mediaanit)
    else:
        # Selvitetään listan mediaani indeksin avulla. Koska ensimmäisen arvon
        # indeksi on 0, on viimeisen arvon indeksi tällöin listan pituus - 1.
        # Kun saatu luku jaetaan kahdella, saadaan mediaanin indeksi.
        indeksi_mediaanille = int((len(järjestetty_lista) - 1) / 2)
        mediaani = järjestetty_lista[indeksi_mediaanille]

    return mediaani


def laske_keskiarvo(lista_korkeuksista):
    """Funktio saa parametrina listan meriveden korkeuksista ja laskee
    keskiarvon korkeusarvoille.

    :param lista_korkeuksista: float, lista meriveden korkeuksista
    :return: float, palauttaa meriveden korkeuden keskiarvon
    """
    # Kahden ensimmäisen arvon summa lasketaan jo ennen silmukkaan siirtymistä,
    # jotta on helpompi lisätä summaan seuraava arvo silmukassa.
    summa = lista_korkeuksista[0] + lista_korkeuksista[1]
    indeksi = 2
    while indeksi < len(lista_korkeuksista):
        summa += lista_korkeuksista[indeksi]
        indeksi += 1

    keskiarvo = summa / len(lista_korkeuksista)
    return keskiarvo


def pienin_ja_suurin_mittaustulos(lista_korkeuksista):
    """Funktio saa parametrina listan meriveden korkeuksista ja palauttaa
    listan pienimmän ja suurimman arvon.

    :param lista_korkeuksista: float, lista meriveden korkeuksista
    :return: float, palauttaa pienimmän ja suurimman arvon
    """

    pienin_arvo = min(lista_korkeuksista)
    suurin_arvo = max(lista_korkeuksista)
    return pienin_arvo, suurin_arvo


def lisää_arvo():
    """Funktio pyytää käyttäjää syöttämään arvoja, joista muodostetaan lista.
    Kun käyttäjä syöttää tyhjän rivin ja arvoja on annettu vähintään kaksi,
    palautetaan lista main-funktiolle. Jos arvoja on annettu vähemmän,
    tulostetaan error-tuloste.

    :return: float, palauttaa meriveden korkeuksista koostuvan listan
    """
    lista_korkeuksista = []

    arvo = True
    while arvo:
        meriveden_korkeus = input()
        if meriveden_korkeus != "":
            laskettava_meriveden_korkeus = float(meriveden_korkeus)
            lista_korkeuksista.append(laskettava_meriveden_korkeus)

        if meriveden_korkeus == "" and len(lista_korkeuksista) < 2:
            print("Error: At least two measurements must be entered!")
            break

        if meriveden_korkeus == "" and len(lista_korkeuksista) >= 2:
            arvo = False
            return lista_korkeuksista


def main():
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    lista_korkeuseroista = lisää_arvo()

    # Jos funktio lisää_arvo() palauttaa arvoja eli listan, siirytään
    # käsittelemään listan arvoja kutsumalla funktioita. Jos funktio palauttaa
    # None, ohjelman toiminta päättyy.
    if lista_korkeuseroista != None:
        korkeuserot = pienin_ja_suurin_mittaustulos(lista_korkeuseroista)
        mediaani = laske_mediaani(lista_korkeuseroista)
        keskiarvo = laske_keskiarvo(lista_korkeuseroista)
        keskihajonta = laske_keskihajonta(keskiarvo, lista_korkeuseroista)

        tulosta_arvot(korkeuserot, mediaani, keskiarvo, keskihajonta)


if __name__ == "__main__":
    main()
