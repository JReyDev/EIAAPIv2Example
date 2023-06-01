import requests
import pandas as pd

def eiav2_api(series):
    v2_api = 'YOUR_KEY_HERE'
    parameters = f'&facets[series][]={series}&frequency=weekly&data[]=value&sort[0][column]=period&sort[0][direction]=asc'
    url = 'https://api.eia.gov/v2/petroleum/sum/sndw/data/?api_key=' + v2_api + parameters
    
    response = requests.get(url)
    json_data = response.json()
    
    if response.status_code == 200:
            print ('Successful Connection!!!')
    else:
            print ('Error: Unable to connect')

    data_df = pd.DataFrame(json_data['response']['data'], columns=['period','value'])
    data_df.rename(columns={'period':'Date'},inplace=True)

    data_df.to_csv(json_data['response']['data'][0]['series-description'] + ' Weekly' + '.csv', encoding = 'utf-8', index=False)

#This pulls the data for U.S. Ending Stocks of Crude Oil (Thousand Barrels) Weekly and saves it to a csv file
eiav2_api('WCRSTUS1')
