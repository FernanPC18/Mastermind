from random import choices
from src.constants import COLOR_LIST

def generate_first_population():
    population = []

    for i in range(80): #bucle que se repite 80 veces
        color_numbers = choices(range(0, 6), k=4)  # Genera 4 números aleatorios del 0 al 5
        individual = [] 
        
        for number in color_numbers: 
            individual.append(COLOR_LIST[number]) #añade un color segun su posicion (si es 0, R; si es 1, G...) a individual
        
        population.append(individual) #cuando se completa un individuo, se añade esa lista a population
    
    return population