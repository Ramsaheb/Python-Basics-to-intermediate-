def format(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")
    

format(name = "ironman", power = "Dimmag")
format(name = "ironman")