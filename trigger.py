import os
from logics.logic import convert_data


INFILE_PATH = os.environ.get('GITHUB_WORKSPACE') + "/docs/timeseries.json"
OUTFILE_PATH = 'output/data.json'

if __name__ == '__main__':
    convert_data(
        infile_path=INFILE_PATH,
        outfile_path=OUTFILE_PATH
    )
