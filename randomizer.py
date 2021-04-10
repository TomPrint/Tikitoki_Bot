import random

def randomizing():
    x= ["This is cool!", "Wow", "It is great", "OMG", "Super!"]
    value = random.choice(x)
    return (str(value))

print(randomizing())
