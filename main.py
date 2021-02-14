from flask import Flask, request
app = Flask(__name__)

@app.route('/') 
def hello_world(): 
    return "Ka beta perpendicular"
    
@app.route('/webhook', methods=['POST'])
def webhook():
  req = request.get_json(silent=True, force=True)
  sum = 0
  query_result = req.get('queryResult')
  print('-----')
  print(query_result)
  print('-----')
  print(type(query_result))
  print('-----')
#   print(query_result.get('action'))
  intentv1 = query_result.get('intent')
  intentv2 = intentv1.get('displayName')
  print('-----')
  print(intentv1)
  print('-----')
  print(intentv2)
  if intentv2 == 'add.numbers':
        
        num1 = int(query_result.get('parameters').get('number'))
        num2 = int(query_result.get('parameters').get('number1'))
        sum = str(num1 + num2)
        print('here num1 = {0}'.format(num1))
        print('here num2 = {0}'.format(num2))
        fulfillmentText = 'The sum of the two numbers is '+sum



      
    #   sum = str(num1 + num2)
    #   print('here num1 = {0}'.format(num1))
    #   print('here num2 = {0}'.format(num2))
  
  if intentv2 == 'multiply.numbers':
        num1 = int(query_result.get('parameters').get('number'))
        num2 = int(query_result.get('parameters').get('number1'))
        product = str(num1 * num2)
        print('here num1 = {0}'.format(num1))
        print('here num2 = {0}'.format(num2))
        fulfillmentText = 'The product of the two numbers is '+product

  return {
        "fulfillmentText": fulfillmentText,
        "displayText": '25',
        "source": "webhookdata"
    }
    
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) 