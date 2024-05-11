from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Frontend developer',
    'location': 'Remote',
    'salary': 'Rs. 8,00,000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Ernakulam, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 4,
    'title': 'Backend developer',
    'location': 'San Francisco, USA',
    'salary': 'Rs. 12,00,00'
  }
  
]

@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS, company_name='proxima century')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)