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

def setThermostatHighGoal(problem_file_path):
    # AC_Off, Action_IncreaseTemperature_Winter
    thGoal = str("(define (problem Analyze_Comfort)\n(:domain ComfortAnalyser)\n(:objects\n\twinter - "
                 "season\nAC Thermostat - actuator\n\tACState EnvSensor ThermostatState - sensor\n)\n\n(:init\n\t("
                 "Season_Winter winter)\n\t(AC_Exists AC)\n\t(IsAC_On ACState)\n\t(Thermostat_Exists Thermostat)\n\t("
                 "IsThermostat_On ThermostatState)\n\t(Atmosphere_Cold EnvSensor)\n)\n\n(:goal\n \t(and\n\t(AC_Off "
                 "AC)\n\t(Thermostat_High Thermostat)\n\t(Atmosphere_Normal EnvSensor)\n\t(not (Atmosphere_Cold "
                 "EnvSensor))\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(thGoal)
    f.close()
    return True

def setThermostatLowGoal(problem_file_path):
    # AC_Off, Action_DecreaseTemperature_Winter
    thGoal = str("(define (problem Analyze_Comfort)\n(:domain ComfortAnalyser)\n(:objects\n\twinter - "
                 "season\nAC Thermostat - actuator\n\tACState EnvSensor ThermostatState - sensor\n)\n\n(:init\n\t("
                 "Season_Winter winter)\n\t(AC_Exists AC)\n\t(IsAC_On ACState)\n\t(Thermostat_Exists Thermostat)\n\t("
                 "IsThermostat_On ThermostatState)\n\t(Atmosphere_Hot EnvSensor)\n)\n\n(:goal\n \t(and\n\t(AC_Off "
                 "AC)\n\t(Thermostat_Low Thermostat)\n\t(Atmosphere_Normal EnvSensor)\n\t(not (Atmosphere_Hot "
                 "EnvSensor))\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(thGoal)
    f.close()
    return True

def setACHighGoal(problem_file_path):
    # Action_Thermostat_Off, Action_IncreaseTemperature_Summer
    acGoal = str("(define (problem Analyze_Comfort)\n(:domain ComfortAnalyser)\n(:objects\n\tsummer - "
                 "season\nAC Thermostat - actuator\n\tACState EnvSensor ThermostatState - sensor\n)\n\n(:init\n\t("
                 "Season_Summer summer)\n\t(AC_Exists AC)\n\t(IsAC_On ACState)\n\t(Thermostat_Exists Thermostat)\n\t("
                 "IsThermostat_On ThermostatState)\n\t(Atmosphere_Cold EnvSensor)\n)\n\n(:goal\n \t(and\n\t(AC_High "
                 "AC)\n\t(Thermostat_Off Thermostat)\n\t(Atmosphere_Normal EnvSensor)\n\t(not (Atmosphere_Cold "
                 "EnvSensor))\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(acGoal)
    f.close()
    return True

def setACLowGoal(problem_file_path):
    # Action_Thermostat_Off, Action_DecreaseTemperature_Summer
    acGoal = str("(define (problem Analyze_Comfort)\n(:domain ComfortAnalyser)\n(:objects\n\tsummer - "
                 "season\nAC Thermostat - actuator\n\tACState EnvSensor ThermostatState - sensor\n)\n\n(:init\n\t("
                 "Season_Summer summer)\n\t(AC_Exists AC)\n\t(IsAC_On ACState)\n\t(Thermostat_Exists Thermostat)\n\t("
                 "IsThermostat_On ThermostatState)\n\t(Atmosphere_Hot EnvSensor)\n)\n\n(:goal\n \t(and\n\t(AC_Low "
                 "AC)\n\t(Thermostat_Off Thermostat)\n\t(Atmosphere_Normal EnvSensor)\n\t(not (Atmosphere_Hot "
                 "EnvSensor))\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(acGoal)
    f.close()
    return True

def setSummerOptimiserGoal(problem_file_path):
    acGoal = str("(define (problem Optimise_Energy)\n(:domain EnergyOptimiser)\n(:objects\n\tsummer - "
                 "season\nAC Thermostat MotionDetected LightSource - actuator\n\tACState ThermostatState MotionSensor "
                 "BrightnessSensor - sensor\n)\n\n(:init\n\t(Season_Summer summer)\n\t(AC_Exists AC)\n\t(IsAC_On "
                 "ACState)\n\t(Thermostat_Exists Thermostat)\n\t(IsThermostat_On ThermostatState)\n\t;("
                 "Motion_Detected MotionDetected)\n\t(MotionSensor_Exists MotionSensor)\n\t(BrightnessSensor_Exists "
                 "BrightnessSensor)\n\t(LightSource_Exists LightSource)\n)\n\n(:goal\n \t(and\n\t(Thermostat_Off "
                 "Thermostat)\n\t(Light_Off LightSource)\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(acGoal)
    f.close()
    return True

def setWinterOptimiserGoal(problem_file_path):
    acGoal = str("(define (problem Optimise_Energy)\n(:domain EnergyOptimiser)\n(:objects\n\twinter - "
                 "season\nAC Thermostat MotionDetected LightSource - actuator\n\tACState ThermostatState MotionSensor "
                 "BrightnessSensor - sensor\n)\n\n(:init\n\t(Season_Winter winter)\n\t(AC_Exists AC)\n\t(IsAC_On "
                 "ACState)\n\t(Thermostat_Exists Thermostat)\n\t(IsThermostat_On ThermostatState)\n\t;("
                 "Motion_Detected MotionDetected)\n\t(MotionSensor_Exists MotionSensor)\n\t(BrightnessSensor_Exists "
                 "BrightnessSensor)\n\t(LightSource_Exists LightSource)\n)\n\n(:goal\n \t(and\n\t(AC_Off "
                 "AC)\n\t(Light_Off LightSource)\n)\n)\n)")
    with open(problem_file_path, 'w') as f:
        f.write(acGoal)
    f.close()
    return True


