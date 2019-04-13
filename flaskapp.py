


import flask as fl
#import os #USED??
#from datetime import datetime #USED??
#from flask import Flask, request, flash, url_for, redirect, render_template, abort, send_from_directory

# CUSTOM MODULES
# --------------

import gtfsviewer as gv



# Flask Initialize Variables
app = fl.Flask(__name__)            	# Define Application Object
app.config.from_pyfile("flaskapp.cfg")	# Configure Application Object



# Function to Get GTFS Exchange Feed
@app.route("/api/agencies", methods=["POST"])
def apiAgencies():
	return gv.getAgencies(fl.request.json["uuid"])
	#return gv.getAgencies(fl.request.args.get("uuid")) ## WORKS FOR 'GET'

# Function to Get Trip Map
@app.route("/api/createmap", methods=["POST"])
def apiCreateMap():
	return gv.createTripMap(fl.request.json["uuid"], fl.request.json["agency_id"], fl.request.json["route_id"], fl.request.json["datetime"])

# Function to Get GTFS Exchange Feed
@app.route("/api/gtfs", methods=["GET"])
def apiGTFS():
    return gv.getGTFS()

# Function to Get Agency Route Data
@app.route("/api/routes", methods=["POST"])
def apiRoutes():
	return gv.getRoutes(fl.request.json["uuid"], fl.request.json["agency_id"])
	#return gv.getAgencies(fl.request.args.get("uuid")) ## WORKS FOR 'GET'

# Function to Get Bus Stop Points
@app.route("/api/stops", methods=["POST"])
def apiGetStopPoints():
    return gv.getStopPoints(fl.request.json["uuid"], fl.request.json["agency_id"], fl.request.json["bounds"])

# Function to Create Unique User ID
@app.route("/api/uuid", methods=["GET"])
def apiCreateUUID():
    return gv.createUUID()

# URL REFERENCE FUNCTIONS
# -----------------------

# Function to Route Index Page
@app.route("/")
def index():
    return fl.render_template("index.html")

# Function to Route Static Resources
@app.route("/<path:resource>")
def serveStaticResource(resource):
    return fl.send_from_directory("static/", resource)




# Run Application
if __name__ == "__main__":
    app.run()


