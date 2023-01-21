

#parent class
class Organism:
    name = 'unknown'
    species = 'unknown'
    legs = None
    arms = None
    dna = 'Seq A'
    origin = 'unknown'
    carbon_based = True


    def info(self):
        msg = '\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}'.format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg


#child class instance
class human(Organism):
    name = 'McDonald'
    species = 'Homo Sapiens'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = '\nCreates a deadly weapon using a paper clip.'
        return msg


#another child class
class dog(Organism):
    name = 'Spark'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bit(self):
        msg = '\nEmits a loud growl and bites target'
        return msg

#another child class instance
class bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def replication(self):
        msg = '\nCells begin to multiply at a fast rate'
        return msg






''' code below calls all classes above named Game

if __name__ == '__main__':
    x = Game()
    print('{} {}'.format(x.var1, x.var2))

'''


if __name__ == '__main__':
    human = human()
    print(human.info())
    print(human.ingenuity())

    dog = dog()
    print(dog.info())
    print(dog.bit())

    bacteria = bacterium()
    print(bacteria.info())
    print(bacteria.replication())
