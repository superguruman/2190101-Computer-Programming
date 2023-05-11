class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return "(" + str(self.value) + " " + str(self.suit) + ")"
    
    def next1(self):
        nxt = Card(self.value, self.suit)
        nxt.next2()
        return nxt
        
    def next2(self):
        v = "3 4 5 6 7 8 9 10 J Q K A 2 3".split()
        s = "club diamond heart spade club".split()
        self.suit = s[s.index(self.suit)+1]
        if self.suit == 'club':
            self.value = v[v.index(self.value)+1]
        
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])