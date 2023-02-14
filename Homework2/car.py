class CarTrafficLights:
    def __init__(self, redTime, yellowTime, greenTime, state, previousState, button):
        self.redTime = redTime
        self.yellowTime = yellowTime
        self.greenTime = greenTime
        self.state = state
        self.previousState = previousState
        self.button = button


    def redLight(self):
        if self.state == "sigR":
            self.redTime += 1
        if self.redTime == 61:
            self.previousState = self.state
            self.state = "sigY"
            self.redTime = 0

    def yellowLight(self):
        if self.previousState == "sigR":
            if self.state == "sigY":
                self.yellowTime += 1
            if self.yellowTime == 6:
                self.previousState = self.state
                self.state = "sigG"
                self.yellowTime = 0
        if self.previousState == "sigG":
            if self.state == "sigY":
                self.yellowTime += 1
            if self.yellowTime == 5:
                self.previousState = self.state
                self.state = "sigR"
                self.yellowTime = 0

    def greenLight(self):
        if self.state == "sigG":
            self.greenTime += 1
        if self.button == True:
            if self.greenTime == 60:
                self.button = False
                self.previousState = self.state
                self.state = "sigY"
                self.greenTime = 0
