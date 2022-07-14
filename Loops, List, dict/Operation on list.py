n = [12, 75, 150, 180, 145, 525, 50]

for i in range(len(n)):
    if n[i]>500:
        break
    elif n[i]>150:
        continue
    elif n[i]%5==0:
        print(n[i])
    