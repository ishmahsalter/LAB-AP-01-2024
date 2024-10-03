import random
def kartu():
  return random.randint(1, 11)
def hitung_total(giliran):
  return sum(giliran)
def blackjack():
  print("Welcome to Blackjack!")
  giliran_player = [kartu()]
  giliran_dealer = [kartu()]

  while True:
    player_total = hitung_total(giliran_player)
    print(f"Total kartu Anda sekarang adalah: {player_total}")
    choice = input("Apakah masih akan mengambil kartu? (y/n) ")

    if choice.lower() == 'y':
      giliran_player.append(kartu())
      if player_total > 21:
        print("Anda kalah!")
        break
    elif choice.lower() == 'n':
      break

  print(f"Kartu dealer adalah: {giliran_dealer[0]}")

  while hitung_total(giliran_dealer) < 17:
    giliran_dealer.append(kartu())
    print(f"Kartu dealer sekarang adalah: {hitung_total(giliran_dealer)}")

  player_total = hitung_total(giliran_player)
  dealer_total = hitung_total(giliran_dealer)

  if player_total > 21:
    print("Anda kalah! Kartu anda melebihi 21")
  elif dealer_total > 21:
    print("Anda menang! Kartu dealer melebihi 21")
  elif player_total > dealer_total:
    print("Anda menang!")
  elif player_total < dealer_total:
    print("Dealer menang!")
  else:
    print("Seri!")

blackjack()