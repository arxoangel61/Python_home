time = int(input("Enter time: "))

hour = time // 3600
minutes = time % 3600 // 60
seconds = time % 60

print(f"{hour}:{minutes}:{seconds}")
