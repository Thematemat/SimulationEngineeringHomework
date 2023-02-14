#include <iostream>
#include <conio.h>
using namespace std;
int main() {
    double totalSymTime = 0;
    const double stepSize = 0.01;
    const double momentInertia = 3800;
    double yawRate = 0;
    double yaw = 0;
    while(totalSymTime <= 10){
        yawRate = ((0.3 * totalSymTime * stepSize) / momentInertia) + yawRate;
        yaw = yawRate * stepSize + yaw;
        cout << "Simulation Time = " << totalSymTime <<" | Yaw Rate = "<< yawRate << " | Yaw = " << yaw << endl;
        totalSymTime = totalSymTime + stepSize;
    }
    getch();
    return 0;
}