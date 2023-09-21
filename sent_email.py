import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, message, to_email, image_path):
    # Email configuration
    from_email = "example@gmail.com"  # Replace with your email address
    password = "example passkey"  # Replace with your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach text message
    msg.attach(MIMEText(message, 'plain'))

    # Attach images

    image = open(image_path, 'rb').read()
    image_name = image_path.split("/")[-1]
    image_mime = MIMEImage(image, name=image_name)
    msg.attach(image_mime)

    # Create a SMTP session and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

def execute():
    recipient_email = "example2@gmail.com"  # Replace with the recipient's email address
    email_subject = "Sample Subject"
    email_message = "This is a sample email with pictures."

    # List of image file paths to attach to the email
    image_path = "opencv_frame.png"  # Replace with actual image file paths

    send_email(email_subject, email_message, recipient_email, image_path)
