(define (domain EnergyOptimiser)
    ;EnergyOptimiser -  smart building optimization to reduce the energy consumption of the building.

    (:requirements
        :strips
        :typing
        :negative-preconditions
        :disjunctive-preconditions
        :existential-preconditions
    )

    (:types
        sensor actuator season - object
    )

    ;------------------------predicates----------------------------
    (:predicates
        
        (MotionSensor_Exists ?motionsensor - sensor)
        (Motion_Detected ?motiondetected - actuator)

        (BrightnessSensor_Exists ?brightsenexist - sensor)
        (LightSource_Exists ?lightexist - actuator)
        (Light_Off ?lightoff - actuator)

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

        (Thermostat_Exists ?thermostatexist - actuator)
        (IsThermostat_On ?isthermostaton - sensor)
        (Thermostat_On ?thermostaton - actuator)
        (Thermostat_Off ?thermostatoff - actuator)

    )

    ;------------------------------Actions----------------------------------

    (:action Action_Thermostat_Off
        :parameters     (
                            ?summer - season
                            ?isthermostaton ?motionsensor - sensor
                            ?thermostatexist ?thermostatoff ?motiondetected - actuator
                        )
        :precondition   (
                            and (
                                    or (
                                        and (Season_Summer ?summer)
                                        (Thermostat_Exists ?thermostatexist)
                                        (IsThermostat_On ?isthermostaton)
                                    )
                                    (
                                        and (MotionSensor_Exists ?motionsensor)
                                        (not (Motion_Detected ?motiondetected))
                                        (Thermostat_Exists ?thermostatexist)
                                        (IsThermostat_On ?isthermostaton)
                                    )
                                )
                        )
        :effect         (
                            and (Thermostat_Off ?thermostatoff)
                        )
    )

    (:action Action_AC_Off
        :parameters     (
                            ?winter - season
                            ?isacon ?motionsensor - sensor
                            ?acexist ?acoff ?motiondetected - actuator
                        )
        :precondition   (
                            and (
                                    or (
                                        and (Season_Winter ?winter)
                                        (AC_Exists ?acexist)
                                        (IsAC_On ?isacon)
                                    )
                                    (
                                        and (MotionSensor_Exists ?motionsensor)
                                        (not (Motion_Detected ?motiondetected))
                                        (AC_Exists ?acexist)
                                        (IsAC_On ?isacon)
                                    )
                                )
                        )
        :effect         (
                            and (AC_Off ?acoff)
                        )
    )

    (:action Action_Lights_Off
        :parameters     (
                            ?motionsensor ?brightsenexist  - sensor
                            ?motiondetected ?lightexist ?lightoff - actuator
                        )
        :precondition   (
                            and (MotionSensor_Exists ?motionsensor)
                            (not (Motion_Detected ?motiondetected))
                            (LightSource_Exists ?lightexist)
                        )
        :effect         ( 
                            and (Light_Off ?lightoff)
                        )
    )
    ;------------------------------------------------------------------
    
)