import smtplib, argparse
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
    args = getArgs()
    email(args.toAddress, args.fromAddress)
    print 'Done'


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--toAddress", required=True, help="Email recipient")
    parser.add_argument("-f", "--fromAddress", required=True, help="Email sender")
    return parser.parse_args()

def email(toAddress, fromAddress):
    textfile = 'TestEmail.txt'

    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = 'Here is the data'
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg.preamble = 'This is the data data'

    bodyText = text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

    body = MIMEText(bodyText, 'plain')
    msg.attach(body)

    fp = open('data.csv', 'rb')
    csv = MIMEBase('text', 'csv')
    csv.set_payload(fp.read())
    fp.close()
    csv.add_header("Content-Disposition", "attachment", filename='YourData.csv')
    msg.attach(csv)

    s = smtplib.SMTP('localhost')
    s.sendmail(fromAddress, toAddress, msg.as_string())
    s.quit()

if __name__ == "__main__":
    main()