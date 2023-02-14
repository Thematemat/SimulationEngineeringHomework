from car import CarTrafficLights
from pedestrian import PedestrianCrosswalkLights

simulationTime = 1
CTL = CarTrafficLights(0, 0, 0, "sigR", "none", False)
PCL = PedestrianCrosswalkLights("sigG")
while simulationTime < 201:
    CTL.redLight()
    CTL.yellowLight()
    CTL.greenLight()
    if CTL.state == "sigR":
        PCL.state = "sigG"
    if CTL.state == "sigY":
        PCL.state = "sigR"
    if CTL.state == "sigG":
        PCL.state = "sigR"
    print("simulation time:", simulationTime, "current light for cars:", CTL.state, "current light for pedestrians:", PCL.state)
    if simulationTime == 70:
        CTL.button = True
        print("Button pressed!")
    simulationTime += 1
