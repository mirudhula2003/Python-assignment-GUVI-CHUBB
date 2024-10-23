l = [
    ('Aarav', 200),
    ('Vivaan', 150),
    ('Aarav', 100),
    ('Aditya', 300),
    ('Vivaan', 200),
    ('Riya', 250)
]
tot={}
for i,j in l:
    if i in tot:
        tot[i]+=j
    else:
        tot[i]=j
tot=sorted(tot.items())
print(*tot)
