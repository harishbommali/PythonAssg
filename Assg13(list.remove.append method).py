CricketPlayers=['V.kohli','Rohitshama','M.S.Dhoni','Stevesmith','FafDuplesis','K.L.Rahul']
n=input('Enter the name of your favorite CricketPlayer :')
if n in CricketPlayers:
    print('the player was in the list')
    CricketPlayers.remove(n)
    print('You removed the name of your favorite CricketPlayer in the list')
    for i in CricketPlayers:
        print(i)
else:
    print('the player was is not in the list')
    CricketPlayers.append(n)
    print('You have added the name of your favorite CricketPlayer in the list')
    for i in CricketPlayers: 
        print(i)
