import os
import sys
import pandas as pd
import datetime
import mlflow
from sklearn.feature_extraction.text import CountVectorizer


def load_df(file_path):

    df = pd.read_csv(file_path)

    return df

def bucket_name():

    return 's3://projeto-mlops-us-east-1-prod'

def input_file_path(file_name):

    return f'{bucket_name()}/ingestion/structured/{file_name}'

def output_file_path(run_id, model_alias):

    return f'{bucket_name()}/model-output/{model_alias}/dt=20250511/{run_id}.parquet'

def vectorized_df(df):
    
    vec_df = pd.DataFrame(df)
    vec_text = CountVectorizer().fit_transform(vec_df['text'])
    
    return vec_text

def return_model(run_id, model_alias):

    model_data = f'{bucket_name()}/artifacts/3/{run_id}/artifacts/{model_alias}/'
    model = mlflow.pyfunc.load_model(model_data)

    return model

def write_prediction(df, pred, output_file):

    df = pd.DataFrame(df['text'])
    df['predict'] = pred
    df.to_parquet(output_file, index=False)

def call_model(df, run_id, output_file, model_alias):

    model = return_model(run_id, model_alias) 
    data = vectorized_df(df)  
    pred = model.predict(data)
      
    write_prediction(df=df, pred=pred, output_file=output_file)
    

def amzse_predict(run_id, df, model_alias):

    #ref_date = datetime(year=int(year), month=int(month), day=int(day))

    call_model(
        df=df,
        run_id=run_id,
        output_file=output_file_path(run_id, model_alias),
        model_alias=model_alias
    )


def run():

    file_name="final_data.csv"
    model_alias = "teste"

    run_id = sys.argv[1]

    df = load_df(input_file_path(file_name))
    
    amzse_predict(run_id, df, model_alias)

if __name__ == '__main__':
    run()
