import flask
import csv

from flask import url_for, Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    # render_template method looks for the files in templates/folder
    return render_template('index.html')


# With this single entry, you can comment out the rest of the lines
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    # Create a function to store the data rxed in forms in database.txt
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


# Instead of the above function, where the data is written to a txt file, let's write to a csv file:

def write_to_csv(data):
    # Create a function to store the data rxed in forms in database.txt
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# For this to work, make some changes to the contact.html under <send> tab# See changes in line 75 and 62
@app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#    return 'Form Submitted! Thank you!'
# Use this function to get the contact data posted by the e-mail client
def get_data():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)                     # Call this function to store the data in database.txt
            write_to_csv(data)                     # Let's try to write to csv
            print(data)
            # import redirect method for this
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


# @app.route('/works.html')
# def works():
#    return render_template('works.html')

# @app.route('/work.html')
# def work():
#    return render_template('work.html')

# @app.route('/about.html')
# def about_us():
#    return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#    return render_template('contact.html')

# @app.route('/components.html')
# def component():
#    return render_template('components.html')
