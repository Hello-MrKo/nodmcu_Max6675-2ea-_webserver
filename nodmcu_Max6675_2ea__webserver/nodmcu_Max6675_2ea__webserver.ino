
// ESP8266 NodeMCU 온습도 센서 모니터 
//  날짜 : 2023 - 05-19


#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include "max6675.h"


// 온도 센서 1 설정 
int thermoDO = 12;       //GPIO 12(D6)    
int thermoCLK = 14;      //GPIO 14(D5)
int thermo1CS = 15;       //GPIO 15(D8)    
float temp1;
MAX6675 thermocouple1(thermoCLK, thermo1CS, thermoDO);

// 온도 센서 2 설정 
int thermo2CS = 5;       //GPIO 5(D1)

float temp2;
MAX6675 thermocouple2(thermoCLK, thermo2CS, thermoDO);


/*Put your SSID & Password*/
const char* ssid = "Mr koko";               // 공유기 이름 
const char* password = "88888888";             // 공유기 비밀번호 

ESP8266WebServer server(80);

              
 
void setup() {
  Serial.begin(115200);
  delay(100);
  
  Serial.println("Connecting to ");
  Serial.println(ssid);

  //connect to your local wi-fi network
  WiFi.begin(ssid, password);

  //check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected..!");
  Serial.print("Got IP: ");  Serial.println(WiFi.localIP());

  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);

  server.begin();
  Serial.println("HTTP server started");

}
void loop() {
  
  server.handleClient();
  
}

void handle_OnConnect() {
 temp1=thermocouple1.readCelsius();          // Gets the values of the temperature
 temp2=thermocouple2.readCelsius();          // Gets the values of the temperature 
  server.send(200, "text/html", SendHTML(temp1,temp2)); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}

String SendHTML(float temp1,float temp2){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>ESP8266 Weather Report</title>\n";
  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;}\n";
  ptr +="p {font-size: 24px;color: #444444;margin-bottom: 10px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<div id=\"webpage\">\n";

  
  ptr +="<h1>NodeMCU_Max6675</h1>\n";
  
  ptr +="<p id='temperature1'>Temperature1: ";
  ptr +=(float)temp1;
  ptr +=" Cel</p>";
  
  ptr +="<p id='temperature2'>Temperature2: ";
  ptr +=(float)temp2;
  ptr +=" Cel</p>";
  
  ptr +="</div>\n";
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}


