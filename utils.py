import json


def formatResponseJson(responseJson):
    newJson = json.loads(responseJson)
    intent = ""
    entities = []
    intentScore = 0

    for intentPrediction in newJson["intentPredictions"]:
        if intentPrediction["score"] > intentScore:
            intentScore = intentPrediction["score"]
            intent = intentPrediction["name"]

    for entityPrediction in newJson["entityPredictions"]:
        entities.append(entityPrediction)

    obj = ({
        intent: {}
    })

    for item in entities:
        obj[intent] = ({
            **obj[intent],
            item["entityName"]: item["phrase"]
        })

    return obj

    ''' print(newJson["entityPredictions"]) '''
