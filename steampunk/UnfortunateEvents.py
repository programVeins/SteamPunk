

from seriesOf import unfortunateEvents

countOlafSeen = true
countOlafDisguised = true

class Baudelaires:
    # Baudelaire stats
    age = 0
    IQ = 0
    unlucky = True

    def spotOlaf():
        if countOlafSeen and countOlafDisguised:
            print("Mr. Poe, That's count olaf!")
            # Chances are, Mr. Poe won't believe the orphans
            stayHopeless()
        elif countOlafNotSeen:
            # Chances are, well, pretty low
            stayHappy()

violet = Baudelaires(age = 12, IQ = 130)
klaus = Baudelaires(age = 11, IQ = 150)
sunny = Baudelaires(age = 2, IQ = 40)
