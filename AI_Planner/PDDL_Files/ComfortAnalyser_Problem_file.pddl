(define (problem Analyze_Comfort)

    (:domain ComfortAnalyser)
    (:objects
        BrightnessSensor WeatherAPI ACStatus ThermostatStatus WindowSensor DoorSensor VentSensor AirQualitySensor NoiseSensor - sensor
        BrightnessState - sensor
        LightSource AC Thermostat WindowActuator DoorActuator VentActuator - actuator
        ;- season
        LightSoruceNotification ACNotification ThermostatNotification WindowNotification DoorNotification VentNotification NoiseNotification - notification
    )
    (:init
        (BrightnessSensor_Exists BrightnessSensor)
        (Brightness_High BrightnessState)
        (LightSource_Exists LightSource)
    )

    (:goal 
        (and
            (Brightness_Favourable BrightnessState)
        )
    )
)