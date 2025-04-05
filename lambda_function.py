import pandas as pd

def lambda_handler(event, context):
    data = {
        'name': ['Nolan', 'Christopher'],
        'movie': ['Inception', 'Interstellar']
    }

    df = pd.DataFrame(data=data)
    print(df)

    