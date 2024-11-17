class phone:
    def call(self):
        print("You can call")

    def voice(self):
        print("You can voice")

    def message(self):
        print("You can message")

class samsung(phone):
    def photo(self):
        print("You can take photo")


s = samsung()
s.call()
s.voice()
s.photo()
s.photo()

print(issubclass(samsung,phone))