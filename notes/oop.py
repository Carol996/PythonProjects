

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






''' code below calls all classes above named Game

if __name__ == '__main__':
    x = Game()
    print('{} {}'.format(x.var1, x.var2))

'''
if __name__ == '__main__':
