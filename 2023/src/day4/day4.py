import re

with open('input') as f:
    data = f.read().strip().split('\n')
    total_score = 0
    for line in data:
        i = line.index('|')
        j = line.index(': ')
        a, b, c = line[:j], line[j + 1:i].split(" "), line[i+1:].split(" ")
        b = [int(x) for x in b if x.isdigit()]
        c = [int(x) for x in c if x.isdigit()]        
        winners = [i for i in b if i in c]
        score = 1
        
        if len(winners) > 1:
            for _ in range(len(winners) - 1):
                score *= 2
        if len(winners) == 0:
            score = 0
        if len(winners) == 1:
            score = 1
    
        total_score += score
        
        
    print(total_score)