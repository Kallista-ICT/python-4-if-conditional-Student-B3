score = int(input("What year were you born in:"))

if score >= 1928 and score <= 1945: #Year Silent_Generation condition
    Year = 'Silent_Generation'
elif score >= 1946 and score <= 1964: #Year Baby_Boomer condition
    Year = 'Baby_Boomer'
elif score >= 1965 and score <= 1980: #Year Generation_X condition
    Year = 'Generation X'
elif score >=1981 and score <= 1996: #Year Millenials condition
    Year = 'Millenials'
elif score >=1997 and score <= 2012: #Year Generation_Z condition
    Year = 'Generation_Z'
elif score >=2013 and score <= 2026: #Year Generation_Alpha condition
    Year = 'Generation_Alpha'
else: #Invalid Year Condition
    Year = 'invalid year'


print(f"You were born in {Year}")