(define (problem Optimise_Energy)
(:domain EnergyOptimiser)
(:objects
	winter - season
AC Thermostat MotionDetected LightSource - actuator
	ACState ThermostatState MotionSensor BrightnessSensor - sensor
)

(:init
	(Season_Winter winter)
	(AC_Exists AC)
	(IsAC_On ACState)
	(Thermostat_Exists Thermostat)
	(IsThermostat_On ThermostatState)
	;(Motion_Detected MotionDetected)
	(MotionSensor_Exists MotionSensor)
	(BrightnessSensor_Exists BrightnessSensor)
	(LightSource_Exists LightSource)
)

(:goal
 	(and
	(AC_Off AC)
	(Light_Off LightSource)
)
)
)