(define (domain ComfortAnalyser)
    ;ComfortAnalyser -  It is a logical block for performing the tasks based on the comfort queries of the user. 
    ;                   It automatically adjusts the sensors to its comfort level by monitoring the environmental sensors.

    (:requirements
        :strips
        :typing
        :negative-preconditions
        :disjunctive-preconditions
        :existential-preconditions
    )

    (:types
        sensor actuator season notification - object
    )

    ;------------------------predicates----------------------------
    (:predicates
        
        (BrightnessSensor_Exists ?brightsenexist - sensor)
        (Brightness_High ?brighthigh - sensor)
        (Brightness_Low ?brightlow - sensor)
        (Brightness_Favourable ?brightfav - sensor)
        
        (LightSource_Exists ?lightexist - actuator)
        (LightSource_High ?lighthigh - actuator)
        (LightSource_Low ?lightlow - actuator)
        (LightSource_High_Notify ?lighthighnotify - notification)
        (LightSource_Low_Notify ?lightlownotify - notification)
        
        (Season_Summer ?summer - season)
        (Season_Winter ?winter - season)
        
        (Weather_Sunny ?envsunny - sensor)
        (Weather_Raining ?envraining - sensor)
        (Weather_Windy ?envwindy - sensor)
        (Weather_Snowing ?envsnowing - sensor)
        
        (Atmosphere_Cold ?envcold - sensor)
        (Atmosphere_Hot ?envhot - sensor)
        (Atmosphere_Normal ?envnormal - sensor)

        (AC_Exists ?acexist - actuator)
        (IsAC_On ?isacon - sensor)
        (AC_On ?acon - actuator)
        (AC_Off ?acoff - actuator)
        (AC_High ?achigh - actuator)
        (AC_Low ?aclow - actuator)
        (AC_High_Notify ?achighnotify - notification)
        (AC_Low_Notify ?aclownotify - notification)
        
        (Thermostat_Exists ?thermostatexist - actuator)
        (IsThermostat_On ?isthermostaton - sensor)
        (Thermostat_On ?thermostaton - actuator)
        (Thermostat_Off ?thermostatoff - actuator)
        (Thermostat_High ?thermostathigh - actuator)
        (Thermostat_Low ?thermostatlow - actuator)
        (Thermostat_High_Notify ?thermostathighnotify - notification)
        (Thermostat_Low_Notify ?thermostatlownotify - notification)
        
        (WindowSensor_Exists ?winsenexist - sensor)
        (WindowActuator_Exists ?winactexist - actuator)
        (IsWindow_Open ?windowopen - sensor)
        ;(IsWindow_Closed ?windowclosed - sensor)
        (MakeWindow_Open ?makewinopen - actuator)
        (MakeWindow_Close ?makewinclose - actuator)
        (MakeWindow_Open_Notify ?makewinopennotify - notification)
        (MakeWindow_Close_Notify ?makewinclosenotify - notification)
        
        (DoorSensor_Exists ?doorsenexist - sensor)
        (DoorActuator_Exists ?dooractexist - actuator)
        (IsDoor_Open ?dooropen - sensor)
        ;(IsDoor_Closed ?doorclosed - sensor)
        (MakeDoor_Open ?makedooropen - actuator)
        (MakeDoor_Close ?makedoorclose - actuator)
        (MakeDoor_Open_Notify ?makedooropennotify - notification)
        (MakeDoor_Close_Notify ?makedoorclosenotify - notification)
        
        (VentSensor_Exists ?ventsenexist - sensor)
        (VentActuator_Exists ?ventactexist - actuator)
        (IsVent_Open ?ventopen - sensor)
        ;(IsVent_Closed ?ventclosed - sensor)
        (MakeVent_Open ?makeventopen - actuator)
        (MakeVent_Close ?makeventclose - actuator)
        (MakeVent_Open_Notify ?makeventopennotify - notification)
        (MakeVent_Close_Notify ?makeventclosenotify - notification)
        
        (AirQualitySensor_Exists ?airsenexist - sensor)
        (Oxygen_Low ?suffocative - sensor)
        (Smoke_Detected ?smoke - sensor)

        (NoiseSensor_Exists ?noisesenexist - sensor)
        (IsNoise_High ?noisehigh - sensor)
        (Notify_HighNoise ?notifynoise - notification)
    )
    

    ;------------------------------Actions----------------------------------

    

    ;--------------------------light------------------------------
    (:action Action_Increase_Brightness
        ; If the light brightness is low then make light brightness favourable by increasing it. 
        :parameters     (
                            ?brightsenexist ?brightlow ?brightfav - sensor 
                            ?lightexist ?lighthigh - actuator
                        )
        :precondition   (
                            and (BrightnessSensor_Exists ?brightsenexist)
                            (LightSource_Exists ?lightexist)
                            (Brightness_Low ?brightlow)
                            (not (Brightness_Favourable ?brightfav))
                        )
        :effect         (
                            and (Brightness_Favourable ?brightfav) 
                            (not (Brightness_Low ?brightlow))
                            (LightSource_High ?lighthigh)
                        )
    )
    
    (:action Action_Decrease_Brightness
        ; If the light brightness is high then make light brightness favourable by decreasing it.
        :parameters     (
                            ?brightsenexist ?brighthigh ?brightfav - sensor 
                            ?lightexist ?lightlow - actuator
                        )
        :precondition   (
                            and (BrightnessSensor_Exists ?brightsenexist)
                            (LightSource_Exists ?lightexist)
                            (Brightness_High ?brighthigh)
                            (not (Brightness_Favourable ?brightfav))
                        )
        :effect         (
                            and (Brightness_Favourable ?brightfav) 
                            (not (Brightness_High ?brighthigh))
                            (LightSource_Low ?lightlow)
                        )
    )

    
    (:action Notification_Increase_Brightness
        ; If the light brightness is low then notify to increase light brightness to make it favourable. 
        :parameters     (
                            ?brightsenexist ?brightlow ?brightfav - sensor 
                            ?lightexist - actuator
                            ?lighthighnotify - notification
                        )
        :precondition   (
                            and (BrightnessSensor_Exists ?brightsenexist)
                            (not (LightSource_Exists ?lightexist))
                            (Brightness_Low ?brightlow)
                            (not (Brightness_Favourable ?brightfav))
                        )
        :effect         (
                            and (Brightness_Favourable ?brightfav) 
                            (not (Brightness_Low ?brightlow))
                            (LightSource_High_Notify ?lighthighnotify)
                        )
    )
    
    (:action Notification_Decrease_Brightness
        ; If the light brightness is high then notify to decrease light brightness to make it favourable.
        :parameters     (
                            ?brightsenexist ?brighthigh ?brightfav - sensor 
                            ?lightexist - actuator
                            ?lightlownotify - notification
                        )
        :precondition   (
                            and (BrightnessSensor_Exists ?brightsenexist)
                            (not (LightSource_Exists ?lightexist))
                            (Brightness_High ?brighthigh)
                            (not (Brightness_Favourable ?brightfav))
                        )
        :effect         (
                            and (Brightness_Favourable ?brightfav) 
                            (not (Brightness_High ?brighthigh))
                            (LightSource_Low_Notify ?lightlownotify)
                        )
    )


    
    ;-----------------------------Door------------------------------

    (:action Action_Door_Open
        ;If air quality sensor exists and it detects low oxygen in room and/or when smoke increases, open the door.
        :parameters     (
                            ?doorsenexist ?dooropen ?suffocative ?smoke ?airsenexist - sensor
                            ?dooractexist ?makedooropen - actuator
                        )
        :precondition   (
                            and (DoorSensor_Exists ?doorsenexist)
                            (DoorActuator_Exists ?dooractexist)
                            (AirQualitySensor_Exists ?airsenexist)
                            (not (IsDoor_Open ?dooropen))
                            (or (Oxygen_Low ?suffocative)(Smoke_Detected ?smoke))
                        )
        :effect         (
                            and (MakeDoor_Open ?makedooropen)
                            (IsDoor_Open ?dooropen)
                        )
    )
    
    (:action Action_Door_Close
        ;It is highly recommended that you close all windows and doors when the air conditioner is turned on. 
        ;In addition to cooling efficiency, leaving the doors and windows open will also put stress on the air conditioner.
        :parameters     (
                            ?doorsenexist ?dooropen ?isacon - sensor
                            ?dooractexist ?makedoorclose - actuator
                        )
        :precondition   (
                            and (DoorSensor_Exists ?doorsenexist)
                            (DoorActuator_Exists ?dooractexist)
                            (IsDoor_Open ?dooropen)
                            (IsAC_On ?isacon)
                        )
        :effect         (
                            and (MakeDoor_Close ?makedoorclose)
                            (not (IsDoor_Open ?dooropen))
                        )
    )

    
    (:action Notification_Door_Open
        ;If door sensor and actuator do not exist and it detects low oxygen in room and/or when smoke increases, notify to open the door.
        :parameters     (
                            ?doorsenexist ?suffocative ?smoke ?airsenexist - sensor
                            ?dooractexist - actuator
                            ?makedooropennotify - notification
                        )
        :precondition   (
                            and (not (DoorSensor_Exists ?doorsenexist))
                            (not (DoorActuator_Exists ?dooractexist))
                            (AirQualitySensor_Exists ?airsenexist)
                            (or (Oxygen_Low ?suffocative)(Smoke_Detected ?smoke))
                        )
        :effect         (
                            and (MakeDoor_Open_Notify ?makedooropennotify)
                        )
    )

    (:action Notification_Door_Close
        ; If door sensor and actuator does not exist, notify to close door when AC is on.
        :parameters     (
                            ?doorsenexist ?dooropen ?isacon - sensor
                            ?dooractexist - actuator
                            ?makedoorclosenotify - notification
                        )
        :precondition   (
                            and (not (DoorSensor_Exists ?doorsenexist))
                            (not (DoorActuator_Exists ?dooractexist))
                            (IsAC_On ?isacon)
                        )
        :effect         (
                            and (MakeDoor_Close_Notify ?makedoorclosenotify)
                        )
    )



    ;--------------------------Ventilation--------------------------

    (:action Action_Vents_Open
        ;If air quality sensor exists and it detects low oxygen in room and/or when smoke increases, open the vents.
        :parameters     (
                            ?ventsenexist ?ventopen ?suffocative ?smoke ?airsenexist - sensor
                            ?ventactexist ?makeventopen - actuator
                        )
        :precondition   (
                            and (VentSensor_Exists ?ventsenexist)
                            (VentActuator_Exists ?ventactexist)
                            (AirQualitySensor_Exists ?airsenexist)
                            (not (IsVent_Open ?ventopen))
                            (or (Oxygen_Low ?suffocative)(Smoke_Detected ?smoke))
                        )
        :effect         (
                            and (MakeVent_Open ?makeventopen)
                            (IsVent_Open ?ventopen)
                        )
    )

    (:action Action_Vents_Close
        ;Vents should be closed when there is no smoke in room and oxygen level is okay
        :parameters     (
                            ?ventsenexist ?ventopen ?suffocative ?smoke ?airsenexist - sensor
                            ?ventactexist ?makeventclose - actuator
                        )
        :precondition   (
                            and (VentSensor_Exists ?ventsenexist)
                            (VentActuator_Exists ?ventactexist)
                            (AirQualitySensor_Exists ?airsenexist)
                            (IsVent_Open ?ventopen)
                            (or 
                                (not (Oxygen_Low ?suffocative))
                                (not (Smoke_Detected ?smoke))
                            )
                        )
        :effect         (
                            and (MakeVent_Close ?makeventclose)
                            (not (IsVent_Open ?ventopen))
                        )
    )


    (:action Notification_Vents_Open
        ;If vent sensor and actuator do not exist and it detects low oxygen in room and/or when smoke increases, notify to open the vents.
        :parameters     (
                            ?ventsenexist ?suffocative ?smoke ?airsenexist - sensor
                            ?ventactexist - actuator
                            ?makeventopennotify - notification
                        )
        :precondition   (
                            and (not (VentSensor_Exists ?ventsenexist))
                            (not (VentActuator_Exists ?ventactexist))
                            (AirQualitySensor_Exists ?airsenexist)
                            (or (Oxygen_Low ?suffocative)(Smoke_Detected ?smoke))
                        )
        :effect         (
                            and (MakeVent_Open_Notify ?makeventopennotify)
                        )
    )

    (:action Notification_Vents_Close
        ;If vent sensor and actuator do not exist and when there is no smoke in room and oxygen level is okay, notify to close the vents.
        :parameters     (
                            ?ventsenexist ?suffocative ?smoke ?airsenexist - sensor
                            ?ventactexist - actuator
                            ?makeventclosenotify - notification
                        )
        :precondition   (
                            and (not (VentSensor_Exists ?ventsenexist))
                            (not (VentActuator_Exists ?ventactexist))
                            (AirQualitySensor_Exists ?airsenexist)
                            (or 
                                (not (Oxygen_Low ?suffocative))
                                (not (Smoke_Detected ?smoke))
                            )
                        )
        :effect         (
                            and (MakeVent_Close_Notify ?makeventclosenotify)
                        )
    )


    
    ;----------------------------noise--------------------------------

    (:action Notify_Noise_Reduction
        ; If the noise is too high, notify to make it low to feel comfortable.
        :parameters     (
                            ?noisesenexist ?noisehigh - sensor
                            ?notifynoise - notification
                        )
        :precondition   (
                            and (NoiseSensor_Exists ?noisesenexist)
                            (IsNoise_High ?noisehigh)
                        )
        :effect         (
                            and (Notify_HighNoise ?notifynoise)
                            (not (IsNoise_High ?noisehigh))
                        )
    )


    
    ;----------------------------windows------------------------------
    
    (:action Action_Windows_Open
        ;Windows should be open when- 1) It is sunny outside and AC is off and outside temperature is not cold
        ;                             2) It is summer and AC is off
        ;                             3) AC does not exist and it is summer
        ;                             4) If the room is suffocative or has smoke
        :parameters     (
                            ?summer - season
                            ?envsunny ?winsenexist ?windowopen ?isacon ?envcold ?airsenexist ?suffocative ?smoke - sensor
                            ?winactexist ?makewinopen ?acexist - actuator
                        )
        :precondition   (
                            and (WindowSensor_Exists ?winsenexist)
                            (WindowActuator_Exists ?winactexist)
                            (not (IsWindow_Open ?windowopen))
                            (or (
                                    and (AC_Exists ?acexist) 
                                    (Weather_Sunny ?envsunny) 
                                    (not (IsAC_On ?isacon)) 
                                    (not (Atmosphere_Cold ?envcold))
                                )
                                (
                                    and (AC_Exists ?acexist) 
                                    (Season_Summer ?summer) 
                                    (not (IsAC_On ?isacon))
                                )
                                (
                                    and (not (AC_Exists ?acexist))
                                    (Season_Summer ?summer)
                                )
                                (
                                    and (AirQualitySensor_Exists ?airsenexist)
                                    (
                                        or (Oxygen_Low ?suffocative)
                                        (Smoke_Detected ?smoke)
                                    )
                                )
                            )
                        )
        :effect         (
                            and (MakeWindow_Open ?makewinopen)
                            (IsWindow_Open ?windowopen)
                        )
    )
    
    (:action Action_Windows_Close
        ;Windows should be closed when- 1) It is cold outside in winter
        ;                               2) It is windy outside in winter
        ;                               3) It is cold and windy both outside in winter
        ;                               4) It is raining outside
        ;                               5) It is snowing outside
        ;                               6) If AC is on
        :parameters     (
                            ?winter - season
                            ?envcold ?envwindy ?envraining ?envsnowing ?winsenexist ?windowopen ?isacon - sensor
                            ?winactexist ?makewinclose ?acexist - actuator
                        )
        :precondition   (
                            and (WindowSensor_Exists ?winsenexist)
                            (WindowActuator_Exists ?winactexist)
                            (IsWindow_Open ?windowopen)
                            (or (
                                    and (Season_Winter ?winter)
                                    (Atmosphere_Cold ?envcold)
                                )
                                (
                                    and (Weather_Windy ?envwindy)
                                    (Season_Winter ?winter)
                                )
                                (
                                    and (Weather_Windy ?envwindy)
                                    (Atmosphere_Cold ?envcold)
                                )
                                (
                                    and (Weather_Windy ?envwindy)
                                    (Atmosphere_Cold ?envcold)
                                    (Season_Winter ?winter)
                                )
                                (Weather_Raining ?envraining)
                                (Weather_Snowing ?envsnowing)
                                (and (AC_Exists ?acexist)
                                (IsAC_On ?isacon))
                            )
                        )
        :effect         (
                            and (MakeWindow_Close ?makewinclose)
                            (not (IsWindow_Open ?windowopen))
                        )
    )


    (:action Notification_Windows_Open
        ;It should be notified to open windows when - There are not sensor and acctuators on windows 
        ;                                             and
        ;                                             1) It is sunny outside and AC is off and outside temperature is not cold
        ;                                             2) It is summer and AC is off
        ;                                             3) AC does not exist and it is summer
        ;                                             4) If the room is suffocative or has smoke
        :parameters     (
                            ?summer - season
                            ?envsunny ?winsenexist ?isacon ?envcold ?airsenexist ?suffocative ?smoke - sensor
                            ?winactexist ?acexist - actuator
                            ?makewinopennotify - notification
                        )
        :precondition   (
                            and (not (WindowSensor_Exists ?winsenexist))
                            (not (WindowActuator_Exists ?winactexist))
                            (or (
                                    and (AC_Exists ?acexist) 
                                    (Weather_Sunny ?envsunny) 
                                    (not (IsAC_On ?isacon)) 
                                    (not (Atmosphere_Cold ?envcold))
                                )
                                (
                                    and (AC_Exists ?acexist) 
                                    (Season_Summer ?summer) 
                                    (not (IsAC_On ?isacon))
                                )
                                (
                                    and (not (AC_Exists ?acexist))
                                    (Season_Summer ?summer)
                                )
                                (
                                    and (AirQualitySensor_Exists ?airsenexist)
                                    (
                                        or (Oxygen_Low ?suffocative)
                                        (Smoke_Detected ?smoke)
                                    )
                                )
                            )
                        )
        :effect         (
                            and (MakeWindow_Open_Notify ?makewinopennotify)
                        )
    )
    
    (:action Notification_Windows_Close
        ;It should be notified to close windows when - There are not sensor and acctuators on windows 
        ;                                               and
        ;                                               1) It is cold outside in winter
        ;                                               2) It is windy outside in winter
        ;                                               3) It is cold and windy both outside in winter
        ;                                               4) It is raining outside
        ;                                               5) It is snowing outside
        ;                                               6) If AC is on
        :parameters     (
                            ?winter - season
                            ?envcold ?envwindy ?envraining ?envsnowing ?winsenexist ?isacon - sensor
                            ?winactexist ?acexist - actuator
                            ?makewinclosenotify - notification
                        )
        :precondition   (
                            and (not (WindowSensor_Exists ?winsenexist))
                            (not (WindowActuator_Exists ?winactexist))
                            (or (
                                    and (Season_Winter ?winter)
                                    (Atmosphere_Cold ?envcold)
                                )
                                (
                                    and (Weather_Windy ?envwindy)
                                    (Season_Winter ?winter)
                                )
                                (
                                    and (Weather_Windy ?envwindy)
                                    (Atmosphere_Cold ?envcold)
                                )
                                (
                                    and (Weather_Windy ?envwindy)
                                    (Atmosphere_Cold ?envcold)
                                    (Season_Winter ?winter)
                                )
                                (Weather_Raining ?envraining)
                                (Weather_Snowing ?envsnowing)
                                (and (AC_Exists ?acexist)
                                (IsAC_On ?isacon))
                            )
                        )
        :effect         (
                            and (MakeWindow_Close_Notify ?makewinclosenotify)
                        )
    )
    

    
    ;---------------------------temperature---------------------------
        
    ;--------------------------summer----------------------------
    ; AC will only operate in summer
    (:action Action_Thermostat_Off
        :parameters     (
                            ?summer - season
                            ?thermostaton - sensor
                            ?thermostatexist ?thermostatoff - actuator
                        )
        :precondition   (
                            and (Season_Summer ?summer)
                            (Thermostat_Exists ?thermostatexist)
                            (IsThermostat_On ?thermostaton)
                        )
        :effect         (
                            and (Thermostat_Off ?thermostatoff)
                        )
    )
    
    (:action Action_IncreaseTemperature_Summer
        :parameters     (
                            ?summer - season
                            ?isacon ?envcold ?envnormal - sensor
                            ?acexist ?achigh - actuator
                        )
        :precondition   (
                            and (Season_Summer ?summer)
                            (AC_Exists ?acexist)
                            (IsAC_On ?isacon) ;This will only increase temp if AC is on 
                            (Atmosphere_Cold ?envcold)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (AC_High ?achigh)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Cold ?envcold))
                        )
    )

    (:action Notification_IncreaseTemperature_Summer
        :parameters     (
                            ?summer - season
                            ?envcold ?envnormal - sensor
                            ?acexist - actuator
                            ?achighnotify - notification
                        )
        :precondition   (
                            and (Season_Summer ?summer)
                            (not (AC_Exists ?acexist))
                            (Atmosphere_Cold ?envcold)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (AC_High_Notify ?achighnotify)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Cold ?envcold))
                        )
    )
    
    (:action Action_DecreaseTemperature_Summer
        :parameters     (
                            ?summer - season
                            ?acexist ?acon ?aclow - actuator
                            ?isacon ?envhot ?envnormal - sensor
                        )
        :precondition   (
                            and (Season_Summer ?summer)
                            (AC_Exists ?acexist)
                            ;(IsAC_On ?isacon)
                            (Atmosphere_Hot ?envhot)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (AC_On ?acon)
                            (AC_Low ?aclow)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Hot ?envhot))
                        )
    )

    (:action Notification_DecreaseTemperature_Summer
        :parameters     (
                            ?summer - season
                            ?envhot ?envnormal - sensor
                            ?acexist - actuator
                            ?aclownotify - notification
                        )
        :precondition   (
                            and (Season_Summer ?summer)
                            (not (AC_Exists ?acexist))
                            (Atmosphere_Hot ?envhot)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (AC_Low_Notify ?aclownotify)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Hot ?envhot))
                        )
    )
    
    ;--------------------------winter----------------------------
    ; Heater thermostat will only operate in winter
    (:action Action_AC_Off
        :parameters     (
                            ?winter - season
                            ?isacon - sensor
                            ?acexist ?acoff - actuator
                        )
        :precondition   (
                            and (Season_Winter ?winter)
                            (AC_Exists ?acexist)
                            (IsAC_On ?isacon)
                        )
        :effect         (
                            and (AC_Off ?acoff)
                        )
    )

    (:action Action_IncreaseTemperature_Winter
        :parameters     (
                            ?winter - season
                            ?thermostatexist ?thermostaton ?thermostathigh - actuator
                            ?isthermostaton ?envcold ?envnormal - sensor
                        )
        :precondition   (
                            and (Season_Winter ?winter)
                            (Thermostat_Exists ?thermostatexist)
                            ;(IsThermostat_On ?isthermostaton)
                            (Atmosphere_Cold ?envcold)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (Thermostat_On ?thermostaton)
                            (Thermostat_High ?thermostathigh)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Cold ?envcold))
                        )
    )

    (:action Notification_IncreaseTemperature_Winter
        :parameters     (
                            ?winter - season
                            ?thermostatexist - actuator
                            ?envcold ?envnormal - sensor
                            ?thermostathighnotify - notification
                        )
        :precondition   (
                            and (Season_Winter ?winter)
                            (not (Thermostat_Exists ?thermostatexist))
                            (Atmosphere_Cold ?envcold)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (Thermostat_High_Notify ?thermostathighnotify)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Cold ?envcold))
                        )
    )
    
    (:action Action_DecreaseTemperature_Winter
        :parameters     (
                            ?winter - season
                            ?thermostatexist ?thermostatlow - actuator
                            ?isthermostaton ?envhot ?envnormal - sensor
                        )
        :precondition   (
                            and (Season_Winter ?winter)
                            (Thermostat_Exists ?thermostatexist)
                            (IsThermostat_On ?isthermostaton)
                            (Atmosphere_Hot ?envhot)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (Thermostat_Low ?thermostatlow)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Hot ?envhot))
                        )
    )

    (:action Notification_DecreaseTemperature_Winter
        :parameters     (
                            ?winter - season
                            ?thermostatexist - actuator
                            ?envhot ?envnormal - sensor
                            ?thermostatlownotify - notification
                        )
        :precondition   (
                            and (Season_Winter ?winter)
                            (not (Thermostat_Exists ?thermostatexist))
                            (Atmosphere_Hot ?envhot)
                            (not (Atmosphere_Normal ?envnormal))
                        )
        :effect         (
                            and (Thermostat_Low_Notify ?thermostatlownotify)
                            (Atmosphere_Normal ?envnormal)
                            (not (Atmosphere_Hot ?envhot))
                        )
    )
    
    ;------------------------------------------------------------------
    
)