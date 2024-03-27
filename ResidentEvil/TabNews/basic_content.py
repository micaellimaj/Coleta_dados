# %%
import requests
import pandas as pd
import datetime
import json

# %%

def get_response(**Kwargs):
    url= "https://www.tabnews.com.br/api/v1/contents/"
    resp = requests.get(url, params = Kwargs)
    return resp

def save_data(data, option='json'):

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    if option == 'json':
        with open(f"data/content/json/{now}.json", 'w') as open_file:
            json.dump(data, open_file, indent=4)

    elif option == 'dataframe':
        df = pd.DataFrame(data)
        df.to_parquet(f"data/content/parquet/{now}.parquet", index=False)

# %%

resp = get_response(page=1, per_page=100, strategy="new")
if resp.status_code == 200:
    print("Sucesso!")
#%%

data = resp.json()
data

#%%
save_data(data)

