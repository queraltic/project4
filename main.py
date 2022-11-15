from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import sql_queries as esecuele
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())


   

@app.route("/order/")
def order ():
    return jsonify(esecuele.get_order())


@app.route("/total_reviews")
def total_reviews ():
    return jsonify(esecuele.get_total_reviews())


@app.route("/name/")
def get_name ():
    return jsonify(esecuele.get_order())



####### POST
@app.route("/insertreview", methods=["POST"])
def new_review ():

    reviewerName = request.form.get("reviewerName")
    reviewerText= request.form.get("reviewerText")
    overall= request.form.get("overall")
    summary = request.form.get("summary")
    new = request.form.get("new")

    return esecuele.new_review(reviewerName, reviewerText,overall,summary,new)

#this will check that the name is the main
if __name__ == '__main__': 
    app.run(port=9000, debug=True)