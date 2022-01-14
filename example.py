time = int(input('Enter the time in seconds: '))
h = time // 3600
minutes = (time // 60) - (h * 60)
seconds = time % 60
print(f'{h:02}:{minutes:02}:{seconds:02}')

