import os
import re


plan_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\plan.txt")

def readActions():
    try:
        ac = []
        with open(plan_file_path, "r") as f:
            action = f.readlines()
            # print(action)
            for i in action:
                act = re.search("^([^\w\-]+)*([\w\-]+)", i).group(2)
                ac.append(act)
            return ac
    except Exception as e:
        # log.log_debug("Func=" + __name__ + " : " + "Log=Plan doesn't exist.")
        print(e)

'''
if __name__ == "__main__":
   # actions = []
    actions = readActions()
    print(actions)
'''