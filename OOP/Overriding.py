class IPhone6:
    def home(self):
        print("home button is pressed")


class IphoneX(IPhone6):
    def home(self):
        print("home button is touched")
        super().home()


i6 = IPhone6()
i6.home()

ix = IphoneX()
ix.home()
