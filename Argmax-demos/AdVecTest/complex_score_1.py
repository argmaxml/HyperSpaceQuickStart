def score_function_recommendation(Q, V):
    score = 1.0
    r_sum = 0.0
    r_max = 0.0
    
    if match("categories"):
        r_sum = rarity_sum("categories")
        r_max = rarity_max("categories")
        combined = r_sum + r_max
        if match("ios"):
            score = r_sum/combined
        else:
            score = r_max/combined
            
        
    if match("bundle_id"):
        score = 0.0


    return score
    