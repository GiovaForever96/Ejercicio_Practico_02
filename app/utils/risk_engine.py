def calculate_risk(population, density):

    if population > 100_000_000:
        score = 3
    elif population > 20_000_000:
        score = 6
    else:
        score = 8

    if density > 300:
        score += 1
        
    if score <= 4:
        level = "Bajo"
        badge = "Low"
    elif score <= 7:
        level = "Medio"
        badge = "Medium"
    else:
        level = "Alto"
        badge = "High"

    return score, level, badge