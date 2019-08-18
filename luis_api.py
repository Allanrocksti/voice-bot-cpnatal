import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json

headers = {
    "Ocp-Apim-Subscription-Key": "8cd51b2f9b594164ad87f4d8b88b6d3b",
    "Content-Type": "application/json; charset=utf-8"
}

params = urllib.parse.urlencode({
    "appId": "8536448d-6aed-4191-98f7-3227cb74f409",
    "versionId": "0.1"
})


def postMsg(array):
    body = json.dumps(array)
    try:
        conn = http.client.HTTPSConnection(
            'westus.api.cognitive.microsoft.com')
        conn.request("POST", "/luis/api/v2.0/apps/8536448d-6aed-4191-98f7-3227cb74f409/versions/0.1/examples?%s" % params,
                     body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return(data)
    except Exception as e:
        print("\n -----------Errouuu -----------\n")
        return (e)


def createEntities():
    mock = [
        {
            "name": "cenario",
            "sublists": [
                {"canonicalForm": "previsto", "list": []},
                {"canonicalForm": "planejado", "list": []},
                {"canonicalForm": "planejamento", "list": []},
                {"canonicalForm": "realizado", "list": []},
                {"canonicalForm": "realização", "list": []},
                {"canonicalForm": "projetado", "list": []},
                {"canonicalForm": "projeção", "list": []},
                {"canonicalForm": "prevista", "list": []},
                {"canonicalForm": "planejada", "list": []},
                {"canonicalForm": "realizada", "list": []},
                {"canonicalForm": "projetada", "list": []},
                {"canonicalForm": "atrasado", "list": []},
                {"canonicalForm": "atraso", "list": []}
            ]
        },
        {
            "name": "estrutura",
            "sublists": [
                {"canonicalForm": "cenpes", "list": []},
                {"canonicalForm": "pddp", "list": []},
                {"canonicalForm": "pdep", "list": []},
                {"canonicalForm": "pdrgn", "list": []},
                {"canonicalForm": "pdiso", "list": []}
            ]
        },
        {"name": "valor", "sublists": [
            {"canonicalForm": "valor", "list": []}]},
        {
            "name": "mes",
            "sublists": [
                {"canonicalForm": "janeiro", "list": []},
                {"canonicalForm": "fevereiro", "list": []},
                {"canonicalForm": "marco", "list": []},
                {"canonicalForm": "abril", "list": []},
                {"canonicalForm": "maio", "list": []},
                {"canonicalForm": "junho", "list": []},
                {"canonicalForm": "julho", "list": []},
                {"canonicalForm": "agosto", "list": []},
                {"canonicalForm": "setembro", "list": []},
                {"canonicalForm": "outubro", "list": []},
                {"canonicalForm": "novembro", "list": []},
                {"canonicalForm": "dezembro", "list": []}
            ]
        },
        {"name": "ano", "sublists": [
            {"canonicalForm": "integer", "list": []}]},
        {
            "name": "acumulado",
            "sublists": [{"canonicalForm": "acumulado", "list": []}]
        },
        {
            "name": "agencia",
            "sublists": [
                {"canonicalForm": "aneel", "list": []},
                {"canonicalForm": "anp", "list": []}
            ]
        },
        {
            "name": "tipo_obrig",
            "sublists": [
                {"canonicalForm": "interna", "list": []},
                {"canonicalForm": "externa", "list": []},
                {"canonicalForm": "total", "list": []}
            ]
        },
        {
            "name": "quantidade",
            "sublists": [{"canonicalForm": "quantidade", "list": []}]
        }
    ]

    for item in mock:
        body = json.dumps(item)
        try:
            conn = http.client.HTTPSConnection(
                'westus.api.cognitive.microsoft.com')
            conn.request("POST", "/luis/api/v2.0/apps/8536448d-6aed-4191-98f7-3227cb74f409/versions/0.1/closedlists?%s" % params,
                         body, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            print(data)
            # return(data)
        except Exception as e:
            print(e)
            # return (e)


def teste_exaple(text):
    headers = {
        'Content-Type': "application/json",
        'Ocp-Apim-Subscription-Key': "8cd51b2f9b594164ad87f4d8b88b6d3b"
    }
    payload = ""
    text = urllib.parse.quote(text)
    path = "example=%si&patternDetails=true&multiple-intents=true" % text
    path = "/luis/webapi/v2.0/apps/8536448d-6aed-4191-98f7-3227cb74f409/versions/0.1/predict?" + path
    try:
        conn = http.client.HTTPSConnection(
            "westus.api.cognitive.microsoft.com")
        conn.request(
            "GET", path, payload, headers)

        res = conn.getresponse()
        data = res.read()
        conn.close()
        return(data.decode("utf-8"))
    except Exception as e:
        print("error")
        return (e)


# print(teste_exaple("janeiro é dms"))
