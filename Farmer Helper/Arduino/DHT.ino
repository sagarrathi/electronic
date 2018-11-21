#include <dht.h>
#include <Wire.h>
#include "RTClib.h"
#include <SPI.h>
#include <SD.h>



dht DHT;//CREATING DHT11 OBJECT
RTC_DS1307 RTC;//CREATING RTC OBJECT
int BH1750_address=0x23;//BH1750 ADDRESS
File root;//SD CARD  
File dataFile;//SD CARD OBJECT FILE


#define DHT11_PIN 22
#define RainPin A0
#define SoilPin A1
const int chipSelect=10; //53 FOR 2560

/*PIN FOR 2560 debug
#define DHT11_PIN 22
#define RainPin A0
#define SoilPin A1
const int chipSelect=53; 
*/


int unsigned sensorData[15];

void setup()
{
  Wire.begin(9600);
  BH1750_Init(BH1750_address);
  delay(200);
  RTC.begin(); 
  Serial.begin(9600);
  
  
  pinMode(10, OUTPUT);//53 for 2560
  
  if (!SD.begin(10)) {
                     Serial.println("initialization failed!");
                     sensorData[0]=1;
                     return;
                     }
 Serial.println("initialization done.");
 
 dataFile = SD.open("DATA.CSV", O_CREAT | O_APPEND | O_WRITE | O_READ); //if I comment this out then the list files works
 dataFile.close();
  Serial.println("Created File: DATA.CSV");

}








void loop()
{
//DATA ACQUIRE
sensorData[0]=1;sensorData[1]=1;sensorData[2]=1;

 
  //RTC DATA ACQUIRE & Error Check
 Serial.print("RTC:"); 
 if(! RTC.isrunning()){Serial.print("Error ");sensorData[1]=1;} 
 else {Serial.print("OK ");sensorData[1]=0;}
  
  
 
  //DHT11 DATA ACQUIRE & Error Check
  Serial.print("DHT11:");
  int chk = DHT.read11(DHT11_PIN);
  switch (chk)
  {
    case DHTLIB_OK:  
                Serial.print("OK ");sensorData[2]=0;
                break;
    case DHTLIB_ERROR_CHECKSUM: 
                Serial.print("Checksum error ");sensorData[2]=1;
                break;
    case DHTLIB_ERROR_TIMEOUT: 
                Serial.print("Time out error ");sensorData[2]=2;
                break;
    default: 
                Serial.print("Unknown error "); sensorData[2]=3;
                break;
  }
  
  
  //YL83 DATA ACQUIRE
  int RainValue=analogRead(RainPin);
  RainValue=map(RainValue,0,1023,1023,1);
  
  //YL69 DATA ACQUIRE
  int SoilValue=analogRead(SoilPin);
  SoilValue=map(SoilValue,0,1023,1023,1);
  
  //BH1750 DATA ACQUIRE
  int LightValue=BH1750_DATA_ACQUIRE();
  


// DISPLAY DATA
  //RTC DS1307 DISPLAY
 DateTime now=RTC.now();
  Serial.print("Time:");
  Serial.print(now.year(), DEC);sensorData[3]=now.year();
  Serial.print(':');
  Serial.print(now.month(), DEC);sensorData[4]=now.month();
  Serial.print(':');
  Serial.print(now.day(), DEC);sensorData[5]=now.day();
  Serial.print(' ');
  Serial.print(now.hour(), DEC);sensorData[6]=now.hour();
  Serial.print(':');
  Serial.print(now.minute(), DEC);sensorData[7]=now.minute();
  Serial.print(':');
  Serial.print(now.second(), DEC);sensorData[8]=now.second();
  
  
  //DHT11 DISPLAY
  Serial.print(" Hum:");
  Serial.print(DHT.humidity,1);sensorData[9]=DHT.humidity;
  Serial.print(" Temp:");
  Serial.print(DHT.temperature, 1);sensorData[10]=DHT.temperature;
  

  //YL83 RAIN SENSOR DISPLAY 
  Serial.print(" Rain:");
  Serial.print(RainValue);sensorData[12]=RainValue;
  
  //YL69 SOIL SENSOR DISPLAY
  Serial.print(" Soil:");
  Serial.print(SoilValue);sensorData[13]=SoilValue;

  //BH1750 LIGHT SENSOR DISPLAY
  Serial.print(" Light:");
  Serial.println(LightValue);sensorData[14]=LightValue;
  sensorData[14]='\0';
  
  
  
  //array to string conversion
  String dataString="";
  
  for(int i=0;i<=2;++i)
   {
    dataString +=String(sensorData[i]);
    dataString +=',';
   }
   for(int i=3;i<=5;++i)
   {
    dataString +=String(sensorData[i]);
    dataString +='/';
   }
   dataString.setCharAt(dataString.length()-1,'\0');
   dataString+=',';
   for(int i=6;i<=8;++i)
   {
    dataString +=String(sensorData[i]);
    dataString +='/';
   }
   dataString.setCharAt(dataString.length()-1,'\0');
   dataString+=',';
   for(int i=9;i<14;++i)
   {
    dataString +=String(sensorData[i]);
    dataString +=',';
   }
   
  Serial.println();
  
  
  //Writing data to sd card
  dataFile  = SD.open("DATA.CSV", FILE_WRITE);
  if (dataFile) 
    {
    dataFile.println(dataString);
    Serial.println("Done");
    } 
  else 
  Serial.println("Not Done");
  Serial.println(dataString);
  
  delay(2000);
  dataFile.close();
}




void BH1750_Init(int address)
  {
   Wire.beginTransmission(address);
   Wire.write(0x10); //resolution
   Wire.endTransmission();
  }

int BH1750_DATA_ACQUIRE()
  {
  int val,*buff;
  buff=readRegister(BH1750_address,BH1750_address,2);
  val=(buff[0]<<8|buff[1])/1.2;
  return val;
  }



void writeRegister(int deviceAddress, byte address, byte val)
  {
  Wire.beginTransmission(deviceAddress);
  Wire.write(address);
  Wire.write(val);
  Wire.endTransmission();
  }

int* readRegister(int deviceAddress, byte address,int num)
  {
  int buff[num],i=0;
  Wire.beginTransmission(deviceAddress);
  Wire.write(address);
  Wire.endTransmission();
  Wire.beginTransmission(deviceAddress);
  Wire.requestFrom(deviceAddress, num);
  while(Wire.available()){
  while(i<=num)
    {buff[i]=Wire.read();i++;}
  }
  Wire.endTransmission();
  return buff;
  }
















