
scores = [10, 20, 42, 50, 75, 20]

scoresB = [33,121,3523,4423,23423]

def average(list):

    total = 0
    total_number_of_scores = 0


    for item in list:
        total += item
        total_number_of_scores += 1
        

    average = total / total_number_of_scores
    return average;

average(scores)
average(scoresB)