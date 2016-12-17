import pandas

def create_email_csv():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    email_list = df[' email']
    email_list.to_csv('emails.csv')
