

from flask import Flask , render_template 
 


app = Flask(__name__)


@app.route("/")
def indexpage():
   return render_template("index.html")

 
@app.route("/sum/<inputnumber1>/<inputnumber2>")
def summation( inputnumber1 , inputnumber2 ): 

   try:
      displayvalue = int(inputnumber1) + int(inputnumber2)
      displayvalue =  "The result of sum between " + str(inputnumber1) + " and " + str (inputnumber2) + " is " +  str(displayvalue)
   
   except:   
      displayvalue =  "You are using miss data type for operation"
 
   return render_template("index.html" ,    result= displayvalue )    
 



@app.route("/concat/<value1>/<value2>")
def concat( value1 , value2 ): 

   displayvalue = str(value1) + str(value2)
   displayvalue =  "The result of concatination between " + str(value1) + " and " + str (value2) + " is " +  str(displayvalue)
    
   return render_template("index.html" ,    result= displayvalue )   



 
if __name__ == "__main__":
   app.run(host='0.0.0.0' ,  port=80 ,debug=True)
 