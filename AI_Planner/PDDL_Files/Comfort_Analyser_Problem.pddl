(define (problem Analyze_Comfort)

    (:domain ComfortAnalyser)
    (:objects
        BrightnessSensor BrightnessState WeatherAPI ACStatus ThermostatStatus WindowSensor DoorSensor VentSensor AirQualitySensor NoiseSensor - sensor
        LightSource AC Thermostat WindowActuator DoorActuator VentActuator - actuator
        Summer Winter - season
        LightSoruceNotification ACNotification ThermostatNotification WindowNotification DoorNotification VentNotification NoiseNotification - notification
    )
    (:init
        (BrightnessSensor_Exists BrightnessSensor)
        (Brightness_Low BrightnessState)
        (LightSource_Exists LightSource)
    )

    (:goal 
        (and
            (Brightness_Favourable BrightnessState)
            (not (Brightness_Low BrightnessState))
            (LightSource_High LightSource)
        )
    )
)