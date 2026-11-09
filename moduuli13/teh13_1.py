from flask import Flask, jsonify

app = Flask(__name__)

def check_primery(number):
  if number < 2:
      return False

  div = 2
  while div * div  <= number:
      if number % div == 0:
          return False
      div += 1
  return True

@app.route('/alkuluku/<int:number>')


def primery(number):
    answer = {
        "Number": number,
        "isPrime": check_primery(number),
    }
    return jsonify(answer)

if __name__ == '__main__':
    app.run(use_reloader=True, host ='127.0.0.1', port=3000 )