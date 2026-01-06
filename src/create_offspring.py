def create_offspring(parents):
    offsprings = []
    # Emparejar padres (0 con 1, 2 con 3, etc.)
    for selected_parents in range(0, len(parents), 2):
        if selected_parents + 1 < len(parents):
            parent1 = parents[selected_parents]
            parent2 = parents[selected_parents + 1]
            
            # Mitades de cada padre
            parent1_left_half = parent1[:2]
            parent1_right_half = parent1[2:]
            parent2_left_half = parent2[:2]
            parent2_right_half = parent2[2:]

            # Crear descendientes combinando mitades
            offspring1 = parent1_left_half + parent2_right_half  # izquierda de parent1 + derecha de parent2
            offspring2 = parent2_left_half + parent1_right_half  # izquierda de parent2 + derecha de parent1
            
            offsprings.append(offspring1)
            offsprings.append(offspring2)
    
    return offsprings