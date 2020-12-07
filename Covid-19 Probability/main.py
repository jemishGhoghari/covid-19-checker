from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
import os

# image passing #
PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
# image passing #

file = open('model.pkl', 'rb')
clf = pickle.load(file)

@app.route('/', methods = ['GET', 'POST'])
def process_data():
	if request.method == "POST":
		mydict = request.form
		fever = int(mydict['fever'])
		age = int(mydict['age'])
		pain = int(mydict['pain'])
		runnynose = int(mydict['runnyNose'])
		diffbreath = int(mydict['diffbreath'])
		diabitis = int(mydict['diabitis'])
		inputFeatures = [fever, pain, age, runnynose, diffbreath, diabitis]
		Infprob = clf.predict_proba([inputFeatures])[0][1]
		return render_template('load.html', inf = round(Infprob * 100))
	return render_template('index.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	if request.method == 'POST':
		mycontact = request.form
		firstname = str(mycontact['firstname'])
		lastname = str(mycontact['lastname'])
		country = str(mycontact['country'])
		subject = str(mycontact['subject'])
		return render_template('contact_save.html', firstname = firstname, lastname = lastname, country = country, message = subject)
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
	return render_template('contact.html', user_image = full_filename)

@app.route('/about', methods = ['GET', 'POST'])
def about():
	team1 = os.path.join(app.config['UPLOAD_FOLDER'], 'team1.png')
	team2 = os.path.join(app.config['UPLOAD_FOLDER'], 'team2.png')
	team3 = os.path.join(app.config['UPLOAD_FOLDER'], 'team3.png')
	return render_template('about.html', team1 = team1, team2 = team2, team3 = team3)

@app.route('/team-contact', methods = ['GET', 'POST'])
def team_contact():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
	return render_template('contact.html', user_image = full_filename)


if __name__ == '__main__':
	app.run(debug = True)