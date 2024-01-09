import datetime
import json
import pandas as pd
from pandas.io.json import json_normalize


def convert_data(infile_path, outfile_path):
    today = datetime.date.today()
    today_string = today.strftime('%Y-%m-%d')
    start_date_string = (today + datetime.timedelta(days=-180)).strftime('%Y-%m-%d')

    data = None
    with open(infile_path) as inf:
        data = json.load(inf)
        for k, v in data.items():
            df = json_normalize(v)
            # Remove recovered column data
            df = df.drop(columns='recovered')
            # Regularize date string to zero padding
            df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
            mask = (df['date'] >= start_date_string) & (df['date'] <= today_string)
            data[k] = df.loc[mask].to_dict('r')

    with open(outfile_path, 'w') as outf:
        json.dump(data, outf, ensure_ascii=False)
