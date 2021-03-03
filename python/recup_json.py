import json
import urllib.request
d = "2021-03-03 19:00:00"
n = 2


def json_value(d, n):
    url = "http://www.infoclimat.fr/public-api/gfs/json?_ll=43.60426,1.44367&_auth=VkxRRgR6XX9TflJlVyFSe1I6ADVcKgkuB3sFZg1jUC0CZ187VjFVNQJrVCkEK1BlVHkHYwgzAToLblIyWigAfFY3UTwEYF09Uz9SMVdiUnlSfgB9XGIJLgd7BWYNZlAtAmNfOlY9VSkCbFQyBDRQelRgB2MIKAEmC2lSM1o2AGJWPFE0BG5dOFM%2FUjZXeFJ5UmcAYFxiCTIHMgVjDWdQOwJmX25WN1VkAmRUNQQqUGxUYQduCDIBMAtsUjBaNwB8VipRTAQUXSJTfFJyVzJSIFJ8ADVcPQll&_c=0464dd3a742e3bae76d62f057ac34762"
    OpenURL = urllib.request.urlopen(url)
    if(OpenURL.getcode() == 200):
        data = OpenURL.read()
        data_dict = json.loads(data)
        data_dict.pop("request_state")
        data_dict.pop("request_key")
        data_dict.pop("message")
        data_dict.pop("model_run")
        data_dict.pop("source")

        tableau = {}  # Dico

        for date, valeur in data_dict.items():
            vent_moyen = valeur['vent_moyen']
            vent_rafales = valeur['vent_rafales']
            vent_direction = valeur['vent_direction']
            tableau[date] = vent_moyen["10m"], vent_rafales["10m"], vent_direction["10m"]
    i = tableau[d][n]
