# IoTLogiqConnectiv
##Services for User Engagement in Smart Buildings(Research Project)

Considering the advanced technological trends and approaches for deploying the Internet of Things IoT in smart buildings, the engagement of users can play a major role in the management of IoT systems in smart non-residential buildings. User engagement can bridge the gap between IoT systems with numerous expectations to make systems intelligent, manageable, effective, and efficient under the constraints of energy, improvising comfort, productivity, and information exchange. IoT systems that operate in isolated technology or vendor-specific silos restrain utilization, merit, and interoperability. 

The main goal of the research is to investigate a service that can improvise the management of IoT systems by taking feedback on smart environments and adding functionalities that can make users active participants in the operation of the building, The outcome of this research exploits the opportunities of chatbot services in this context and generic functionalities are developed to demonstrate the user engagement. 

A comprehensive architecture is suggested for putting such a system into practice. Approaches are described for the communication of chatbot services with the back-end IoT system of the building. An intelligent AI planning technique like PDDL is chosen for the composition of functionalities in the logic block of chatbot architecture. Methods are suggested to retrieve records of events, debug information, errors, etc. from the IoT system and provide automatic error reporting to administrators. The specifics of all the work done and the results are covered in further chapters of this report.

###Usage
The Implementation is divided into several python files.

In order to start the server run ```python server.py```.

Run ```TelegramBot.py```. Setup the ```.env``` environment file in your IDE. 

Connect with the ```IoTLogiqConnectiv``` Bot in Telegram. 

And finally, run the following commands:

Comfort Queries:
```
Set_Room_Temp_Comfortable
Set_Room_Light_Comfortable
Set_Room_Comfortable
```
Instructions:
```
Get_Room_Brightness
Get_Room_Temperature
Get_Season
Set_Lamp_Luminance <value>
Get_Lamp_Luminance
Set_Thermostat_Temperature <value>
Get_Thermostat_Temperature
Set_AC_Temperature <value>
Get_AC_Temperature
Set_Thermostat_Status <On/Off>
Set_AC_Status <On/Off>
Get_Thermostat_Status
Get_AC_Status
```

Energy Optimiser Queries:
```
Optimise_Room
```