(define (problem Analyze_Comfort)
(:domain ComfortAnalyser)
(:objects
	BrightnessSensor BrightnessState - sensor
	LightSource - actuator
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