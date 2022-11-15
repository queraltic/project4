from sql_connection import engine
import pandas as pd

#GET

def get_everything ():
    query = """SELECT * FROM codificado;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_order ():
    query = """SELECT *
    FROM codificado
    ORDER BY overall DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")



def get_total_reviews():
    query = ("""SELECT COUNT(reviewText) as 'Total reviews' FROM codificado;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')


def get_name ():
    query = """SELECT *
    FROM codificado
    ORDER BY reviewerName NAME;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")




#GET SENTIMENTAL

#POST

def new_review(reviewerName, reviewerText,overall,summary,new):
    engine.execute(f""" INSERT INTO disney.disneyland_reviews (reviewerName, reviewerText,overall,summary,new)
    VALUES ('{reviewerName}', '{reviewerText}', '{overall}', '{summary}', '{new}');""")
    return f"Correctly introduced: {reviewerName}, {reviewerText}, {overall}, {summary}, {new}"

 