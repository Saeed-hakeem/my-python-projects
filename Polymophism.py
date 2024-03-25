class animal:
    def __init__(self):
        pass

    def speak(self):
        print("I am an animal i have a sound")

class dog(animal):
    def __init__(self):
        pass
    def speak(self):
        print("I am a dog i bark")

class cat(animal):
    def __init__(self):
        pass
    def speak(self):
        print("i am a cat i meeaooow")

dog1=dog()
dog1.speak()

cat1=cat()
cat1.speak()