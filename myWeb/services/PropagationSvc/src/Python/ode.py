# imports

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json


# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

prependStr = "/propagatorsvc/webapi/"

class Health(Resource): 
    def get(self):
        if(request.method == 'GET'): 
    
            data = "up"
            return jsonify({'data': data}) 
api.add_resource(Health,prependStr+'health' ,methods = ['GET']) 

class Satellite(Resource):
    def get(self):
        tle1 = 1
        tle2 = 2
        return tle1 
api.add_resource(Satellite, prependStr+'satellite')

 
#Example TLE
#line0 = "gps2-1"
#t0line1 = "1 19802U          89047.62969209 0.00000063  00000+0  99999-4 0    12"
#t0line2 = "2 19802  55.1112 216.5595 0090439 180.2459 179.7401  2.01416203    02" 

class Propagate(Resource):
    def get(self):
        tlePassed = request.args.get('tle')
        t2 = request.args.get('t2')

        tle = json.loads(tlePassed)

        splitTLE = []
        for k,v in a.iteritems():
           splitTLE.append(v)
        
        return splitTLE[0] 
api.add_resource(Propagate, prependStr+'propagate')


# Run app
if __name__ == '__main__':
    app.run(port='5002')
     