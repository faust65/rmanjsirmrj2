from flask import Flask, request, jsonify, render_template
import random
import math

app=Flask(__name__)

@app.route('/')
def html():
    return render_template('index.html')

@app.route('/rl', methods=['POST'])
def rl():
    g=random.randrange(1, 101)
    
    if(0<=g<=30):
        msg=f"×0"
    elif(31<=g<=45):
        msg=f"×1"
    elif(46<=g<=55):
        msg=f"×2"
    elif(56<=g<=57):
        msg=f"×5"
    elif(58<=g<=59):
        msg=f"×10"
    elif(60<=g<=79):
        msg=f"×-1"
    elif(80<=g<=91):
        msg=f"×-2"
    elif(92<=g<=98):
        msg=f"×-5"
    elif(g==99 or g==100):
        msg=f"×-10"
        
    return jsonify({'message':msg})

@app.route('/gsg', methods=['POST'])
def gsg():
    data=request.get_json()
    stat=int(data.get('stat','0'))
    
    g=random.randrange(1, 101)
    
    if(g==1):
        msg=f"대성공({g})"
    elif(g==99 or g==100):
        msg=f"대실패({g})"
    elif(stat*14<g):
        msg=f"실패({g})"
    elif(stat*14>=g):
        msg=f"보통 성공({g})"
        if((stat*14)/2>g):
            msg=f"어려운 성공({g})"
            if((stat*14)/5>g):
                msg=f"극단적 성공({g})"
    

    return jsonify({'message':msg})
