from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrape_mars
from pymongo import MongoClient
import pymongo

# flask
app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# conn = "mongodb://localhost:27017/mission_to_mars"

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
 
    
    # mars = client.db.mars.find_one()
    mars = mongo.db.mars.find_one()
    
    # Return template and data
    return render_template("index.html", mars = mars)

# Route that will trigger the scrape function    
@app.route("/scrape")
def scrape():

    # Run the scrape function
    # mars = client.db.mars
    mars = mongo.db.mars
    mars_web = scrape_mars.scrape_news()
    mars_web = scrape_mars.scrape_marsImage()
    mars_web = scrape_mars.scrape_marsFacts()
    mars_web = scrape_mars.scrape_marsH1Cerberus()
    mars_web = scrape_mars.scrape_marsH2Schiaparelli()
    mars_web = scrape_mars.scrape_marsH3SyrtisMajor()
    mars_web = scrape_mars.scrape_marsH4VallesMarineris()
    
    # Update the Mongo Database using update and upsert=True
    mars.update({}, mars_web, upsert=True)
    
    # Redirect back to home page
    return redirect("/", code=302)

# # Given Already
if __name__ == "__main__":
    app.run(debug=True)