#include "ADS1299.h"

ADS1299 ADS;

boolean deviceIDReturned = false;
boolean startedLogging = false;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  // Serial.println("ADS1299-bridge has started!");
  
  ADS.setup(48, 53, 40, 41); // (DRDY pin, CS pin, START pin, RESET pin  );
  delay(10);  //delay to ensure connection
  
  ADS.RESET();

 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(deviceIDReturned == false) {
    ADS.getDeviceID(); //Funciton to return Device ID
    
    // //prints dashed line to separate serial print sections
    // Serial.println("----------------------------------------------");
    
    // //Read ADS1299 Register at address 0x00 (see Datasheet pg. 35 for more info on SPI commands)
    // ADS.RREG(0x00);
    // Serial.println("----------------------------------------------");

    // //PRINT ALL REGISTERS... Read 0x17 addresses starting from address 0x00 (these numbers can be replaced by binary or integer values)
    // ADS.RREG(0x00, 0x17);
    // Serial.println("----------------------------------------------");
    
    // //Write register command (see Datasheet pg. 38 for more info about WREG)
    // ADS.WREG(CH1SET, 0b01100000);
    // Serial.println("----------------------------------------------");
    
    // //Repeat PRINT ALL REGISTERS to verify that WREG changed the CONFIG1 register
    // ADS.RREG(0x00, 0x17);
    // Serial.println("----------------------------------------------");
    
    //Start data conversions command
    ADS.START(); //must start before reading data continuous
    deviceIDReturned = true;
  }

  //print data to the serial console for only the 1st 10seconds of 
  while(millis()<30000){
    if(startedLogging == false){
      // Serial.print("Millis: "); //this is to see at what time the data starts printing to check for timing accuracy (default sample rate is 250 sample/second)
      // Serial.println(millis());
      startedLogging = true;
    }
    
    //Print Read Data Continuous (RDATAC) to Ardiuno serial monitor... 
    //The timing of this method is not perfect yet. Some data is getting lost 
    //and I believe its due to the serial monitor taking too much time to print data and not being ready to recieve to packets
    ADS.updateData();  
  }
}
