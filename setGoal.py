def setLuminanceHighGoal(problem_file_path):
    brGoal = str("(define (problem Analyze_Comfort)\n(:domain ComfortAnalyser)\n(:objects\n\tBrightnessSensor "
                 "BrightnessState - sensor\n\tLightSource - actuator\n)\n\n(:init\n\t(BrightnessSensor_Exists "
                 "BrightnessSensor)\n\t(Brightness_Low BrightnessState)\n\t(LightSource_Exists "
                 "LightSource)\n)\n\n(:goal\n \t(and\n\t(Brightness_Favourable BrightnessState)\n\t(not ("
                 "Brightness_Low BrightnessState))\n\t(LightSource_High LightSource)\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(brGoal)
    f.close()
    return True

def setLuminanceLowGoal(problem_file_path):
    brGoal = str("(define (problem Analyze_Comfort)\n(:domain ComfortAnalyser)\n(:objects\n\tBrightnessSensor "
                 "BrightnessState - sensor\n\tLightSource - actuator\n)\n\n(:init\n\t(BrightnessSensor_Exists "
                 "BrightnessSensor)\n\t(Brightness_High BrightnessState)\n\t(LightSource_Exists "
                 "LightSource)\n)\n\n(:goal\n \t(and\n\t(Brightness_Favourable BrightnessState)\n\t(not ("
                 "Brightness_High BrightnessState))\n\t(LightSource_Low LightSource)\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(brGoal)
    f.close()
    return True

def setTemperatureHighGoal(problem_file_path):
    brGoal = str()
    with open(problem_file_path, 'w') as f:
        f.write(brGoal)
    f.close()
    return True

def setTemperatureLowGoal(problem_file_path):
    brGoal = str()
    with open(problem_file_path, 'w') as f:
        f.write(brGoal)
    f.close()
    return True
