def SolveComfortQuery(message):
    if message == "Set_Room_Temp_Comfortable":



def ClassifyInput(message):
    msg = message.text.split("_")
    if "Comfortable" in msg:
        solve = SolveComfortQuery(message)
        print(solve)
        query = "ComfortQuery"
        return query

def getAnswer(message):
    if ClassifyInput(message) == "ComfortQuery":
        msg = "Comfort Set!"
        return msg


