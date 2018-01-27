def getInt(prompt,max, min = 1):
    while 1:
        try:
            ret = int(input(prompt))
            if ret <= max and ret >= min:
                return ret
            else:
                print("invalid entry")
        except:
            print("invalid options")

class ListOption:
    def __init__(self,description):
        self.description = description
    @staticmethod
    def getOptionFromList(list):
        i = 0
        for item in list:
            i += 1
            print(str(i)+")" + item.description)
        choice = getInt("Choice = ",i)
        return list[choice-1]

class Choice(ListOption):
    def __init__(self,description,newEncounter):
        super().__init__(description)
        self.newEncounter = newEncounter

class Encounter:
    def __init__(self,description):
        self.description = description
        self.choices = []
    def enact(self):
        print(self.description)
        e = ListOption.getOptionFromList(self.choices)
        return e.newEncounter

def game():

    a = Encounter("Abe")
    b = Encounter("Bob")
    c = Encounter("Carl")
    d = Encounter("Doug")

    choicesA = [Choice("b", b), Choice("c", c), Choice("d", d)]
    choicesB = [Choice("a", a), Choice("c", c), Choice("d", d)]
    choicesC = [Choice("a", a), Choice("b", b), Choice("d", d)]
    choicesD = [Choice("a", a), Choice("b", b), Choice("c", c)]

    a.choices = choicesA
    b.choices = choicesB
    c.choices = choicesC
    d.choices = choicesD
    currentEncounter = a
    while 1:
        currentEncounter = currentEncounter.enact()

game()
