import main

user = input("Enter the username : ")

test = main.Spot(user)
data = test.get_playlist_user()
print(data)
