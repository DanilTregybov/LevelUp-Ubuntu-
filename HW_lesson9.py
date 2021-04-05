#работа с дробями сложение, вычитание,умножение,деление HW
# работа с дробями сложение, вычитание,умножение,деление HW
# import math
#
#
# class Fraction:
#     def __init__(self, num, denom, celoe=0):
#         self.celoe = celoe
#         self.num = num
#         self.denom = denom
#
#     # def decorator(method):
#     #     def wrapper(celoe,numerator,denomirator):
#     #
#     #         if numerator > denomirator:
#     #             celoe = numerator // denomirator
#     #         num = numerator % denomirator
#     #     return "{},{}/{}".format(celoe, numer, denomirator)
#     #     return wrapper
#
#     def add(self, otherfract):
#         celoe = self.celoe + otherfract.celoe
#         a_num = self.num * otherfract.denom + self.denom * otherfract.num
#         a_denom = self.denom * otherfract.denom
#         common = (math.gcd(a_num, a_denom))
#         numerator = a_num // common
#         denomirator = a_denom // common
#         return celoe, numerator, denomirator
#
#     def mul(self, other):
#         if self.celoe == 0:
#             celoe = self.celoe - other.celoe
#             m_num = self.num * other.num
#             m_denom = self.denom * other.denom
#             common = (math.gcd(m_num, m_denom))
#             numerator = m_num // common
#             denomirator = m_denom // common
#             return celoe, numerator, denomirator
#         elif self.celoe != 0:
#             new_selfnum = (self.celoe * self.denom) + self.num
#             new_selfdemon = self.denom
#             new_othernum = (other.celoe * other.denom) + other.num
#             new_otherdenom = other.denom
#             numerator = new_selfnum * new_othernum
#             denomirator = new_selfdemon * new_otherdenom
#             common = (math.gcd(numerator, denomirator))
#             return numerator//common,denomirator//common
#
#     def subtraction(self, otherfract):
#         celoe = self.celoe - otherfract.celoe
#         s_num = self.num * otherfract.denom - self.denom * otherfract.num
#         s_denom = self.denom * otherfract.denom
#         common = (math.gcd(s_num, s_denom))
#         numerator = s_num // common
#         denomirator = s_denom // common
#         return celoe, numerator, denomirator
#
#     def division(self, other):
#         if self.celoe == 0:
#             celoe = self.celoe - other.celoe
#             numerator = self.num * other.denom
#             denomirator = self.denom * other.num
#             return celoe, numerator, denomirator
#         elif self.celoe != 0:
#             new_selfnum = (self.celoe * self.denom) + self.num
#             new_selfdemon = self.denom
#             new_othernum = (other.celoe * other.denom) + other.num
#             new_otherdenom = other.denom
#             numerator = new_selfnum * new_otherdenom
#             denomirator = new_selfdemon * new_othernum
#             return numerator, denomirator
#
#
# f1 = Fraction(1, 6, 2)
#
# f2 = Fraction(2, 5, 3)
#
# f1.add(f2)
# f1.mul(f2)
# print(f1.add(f2))
# f1.mul(f2)
# print(f1.mul(f2))
# f1.subtraction(f2)
# print(f1.subtraction(f2))
# f1.division(f2)
# print(f1.division(f2))

# My Project (Uno)



class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """ Возращает количество очков которое дает карта """
        if self.rank in "TJQK":
         return 10
        else:
         return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return self.rank,self.suit


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    def name(self):
        return "{}".format(self.name())
    def add_card(self,card):
        self.cards.append(card)
    def value(self):
        res = 0
        aces = 0
        for card in self.cards:
          res += card.card_value()
          if card.get_rank() == "A":
                aces += 1
          if res  + aces * 10 <= 21:
              res += aces * 10
        return res
    def result(self):
        return "Name{} :{}".format(self.name(),self.cards)
import random
class Deck:
    def __init__(self):
        ranks = "23456789TJKQA"
        suits = "DCHS"
        self.cards = [Card(r,s)for r in ranks for s in suits]
        random.shuffle(self.cards)

    def distribution_card (self):
        return self.cards.pop()
class Game:

    def new_game(self,deck,player,dealer):

        player.add_card(deck.distribution_card())
        player.add_card(deck.distribution_card())

        dealer.add_card(deck.distribution_card())
        print(dealer)
        print("="*20)
        print(player)

        in_game = True
        while (player.value()) <21 :
            ans = input("Hit or stand?(h/s) ")
            if ans == "h":
                player.add_card(deck.distribution_card())
                print(player)
                if player.value() > 21:
                    print("You lose")
                    in_game  = False
            else:
                print("You stand")
                break
        print("="*20)
        if in_game:
            while dealer.value() < 17:
                dealer.add_card(deck.distribution_card())
                print(dealer)
                if dealer.value() > 21:
                    print("Dealer bust")
                    in_game = False
        if in_game:
            if player.value() > dealer.value():
                print("You win")
            else:
                print("Dealer win")

deck = Deck()
player = Player("Player")
dealer = Player("Dealer")
game = Game()
game.new_game(deck,player,dealer)