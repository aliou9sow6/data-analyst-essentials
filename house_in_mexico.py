# Déclaration de variables
nom = "Alice"  # Chaîne de caractères
age = 30       # Entier
taille = 1.75  # Flottant

my_list = [nom, age, taille]  # Liste
my_tuple = (nom, age, taille) # Tuple
# Affichage des variables
#print(age, nom, taille)

for item in my_list:
    print(item," ", end="")
print("\n")
    
for item in my_tuple:
    print(item," ", end="")
print("\n")
# Déclaration de fonctions  
def say_hello():
    if(taille > 1.70):
        print("Hello! My name is", nom, "and I'm tall")
    else:
        print("Hello! My name is", nom, "and I'm short")
# Appel de la fonction say_hello()
say_hello()

# Déclaration de classes
class Person:
    def __init__(self, nom, age, taille):
        self.nom = nom
        self.age = age
        self.taille = taille
    def greet(self):
        print(f"Hello! My name is {self.nom} my age is : {self.age} and my tail is {self.taille}")
        if(self.taille > 1.70):
            print(" and I'm tall")
        else:
            print(" and I'm short")      

# Création d'une instance de la classe Person
person_1 = Person("Alice", 30, 1.75)
person_1.greet() # Appel de la méthode greet() de l'instance person_1