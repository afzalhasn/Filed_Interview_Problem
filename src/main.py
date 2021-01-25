import os

import os,sys
import json
from flask import Flask,request,jsonify
from flask_cors import CORS
import traceback
from interfaces.API.api import APICreator
from common.logger import Logger

api = APICreator()

app =Flask(__name__)
cors = CORS(app)
@app.route('/payment',methods=['POST'])
def main():
    try:
        input_data = request.json
        return api.process_payment(input_data)
    except Exception as e:
        print(str(e)+traceback.print_exc())
        sys.exit()

if __name__ == "__main__":
    
    if 'PORT_NUM' not in os.environ:
        print(f"No port number specified. Using the default port number of 5005")
        Logger.log_info(f"No port number specified. Using the default port number of 5005")
        port_number = 5005
    else:
        port_number = int(os.environ['PORT_NUM'])
    app.run(host="0.0.0.0",port=port_number,debug=False)
