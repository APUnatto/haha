# # def card_deck():
# #     deck = []
# #     suits = ['spade', 'club', 'diamond', 'heart']
# #     for i in range(2, 11):
# #         for suit in suits:
# #             isuit = str(i) + ' ' + suit
# #             deck.append(isuit)
# #     for j in "JQKA":
# #         for suit in suits:
# #             jsuit = j + ' ' + suit
# #             deck.append(jsuit)
# #     return deck
# #
# #
# # # for card in card_deck():
# # #     print(card)
# # print(card_deck()[:5])
# #
# #
#
def liet_ke(mon_do):
    # for i in mon_do:
        # j = "Do thu " + str(k) + " la"
        # j = "Do thu la" % k
        # j = "Do thu {} la".format(k)
    if isinstance(mon_do, list):
        print("Do thu 3 la", mon_do[2])
    else:
        print ("Please insert a list")

# liet_ke(["sip", "thit", "duong", "tao", "chuoi"])

# inp = input("Nhap so:")
# liet_ke(in)

def thu_tiu(a,b):
    if a > 10:
        return a*b
    else:
        return a+b

thu_tiu(15,30)
print(thu_tiu(1,30))


