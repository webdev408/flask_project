from flask import Flask, render_template, request

app = Flask(__name__)

submissions = []

@app.route('/', methods=['GET'])
def begin():
  return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
  skills = ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'React', 'Git', 'React Query', 'Data Science', 'google colab', 'Tailwind']
  applications = ['VS Code', 'PyCharm', 'Jupyter Notebook',  'Postman', 'Git', 'Github']
  return render_template('about.html', skills=skills, applications=applications)
  
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # return render_template('contact.html', name=name, email=email, message=message)
    submissions.append({'name': name, 'email': email, 'message': message})   
  return render_template('contact.html', submissions=submissions)

if __name__ == '__main__':
  app.run(debug=True)
