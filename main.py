from Animal_hierachy.Bird import Bird
from Animal_hierachy.Reptile import Reptile
from Animal_hierachy.Mammal import Mammal
from Animal_hierachy.Insect import Insect
from Animal_hierachy.Fish import Fish


def main():
    mammal1 = Mammal("Wolf", "male", 4, 70., False)
    fish1 = Fish("Shark", "female", 0, 40., 20.)
    bird1 = Bird("Eagle", "male", 2, 10., 2.)
    insect1 = Insect("Fly", "male", 6, 0.01, 2)
    reptile1 = Reptile("Snake", "female", 0, 3, 10)
    print(mammal1)
    print(fish1)
    print(bird1)
    print(insect1)
    print(reptile1)


if __name__ == '__main__':
    main()
