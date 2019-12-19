def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    
    if max(len(w1),len(w2)) - min(len(w1),len(w2)) > 1:

        return False

    shortest = min(len(w1),len(w2))

    count = 0

    for i in range(shortest):
        
        if w1[i] != w2[i]:

            count += 1

        if count > 1:

            return False

    return True