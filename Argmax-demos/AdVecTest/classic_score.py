def score_function_recommendation(Q, V):
    score = 1.0
    r_sum = 0.0
    r_max = 0.0
    
    if match("categories"):
        r_sum = rarity_sum("categories")
    if V["ios"]:
        score *= 2
        
    if match("bundle_id"):
        score = 0.0


    return score
    