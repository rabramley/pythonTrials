import smtplib, argparse
from email.mime.text import MIMEText

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

    # create message body from a text file
    fp = open(textfile, 'rb')
    msg = MIMEText(fp.read())
    fp.close()

    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = fromAddress
    msg['To'] = toAddress

    s = smtplib.SMTP('localhost')
    s.sendmail(fromAddress, toAddress, msg.as_string())
    s.quit()

if __name__ == "__main__":
    main()