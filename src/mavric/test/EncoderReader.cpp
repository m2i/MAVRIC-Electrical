#define Phoenix_No_WPI // remove WPI dependencies
#include "ctre/Phoenix.h"
#include "ctre/phoenix/platform/Platform.h"
#include "ctre/phoenix/unmanaged/Unmanaged.h"
#include "ctre/phoenix/CANifier.h"
#include <string>
#include <thread>

//Create namespaces
using namespace ctre::phoenix;
using namespace ctre::phoenix::platform;
using namespace ctre::phoenix::motorcontrol;
using namespace ctre::phoenix::motorcontrol::can;

//Set up talon
TalonSRX Tal(1);

int main() {
    /* don't bother prompting, just use can0 */
    //std::count << "Please input the name of your can interface: ";
    std::string interface;
    //std::cin >> interface;
    interface = "can0";
    ctre::phoenix::platform::can::SetCANInterface(interface.c_str());

    //get encoder values
    pos = Tal.GetQuadraturePosition();
    vel = Tal.GetQuadratureVelocity();

    //print values
    printf("Position: %f  ", pos);
    printf("Velocity: %f\n", vel);
}