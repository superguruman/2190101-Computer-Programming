class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return '('+str(self.value)+' '+str(self.suit)+')'
    
    def getScore(self):
        if self.value == 'A': return 1
        elif self.value in 'JQK': return 10
        return int(self.value)

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10
    
    def __lt__(self, rhs):
        v = '3 4 5 6 7 8 9 10 J Q K A 2'.split()
        vs = v.index(self.value)
        vr = v.index(rhs.value)
        return (vs, self.suit) < (vr, rhs.suit)
    
n = int(input())
cards = [] 
for i in range(n): 
    value, suit = input().split() 
    cards.append(Card(value, suit)) 
for i in range(n): 
    print(cards[i].getScore()) 
print("----------") 
for i in range(n-1): 
    print(Card.sum(cards[i], cards[i+1]))
print("----------") 
cards.sort() 
for i in range(n): 
    print(cards[i]) 