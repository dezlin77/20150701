import smtplib

my_email = "desean@gmail.com"
password = "abcd1234()"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password = password)
connection.sendmail(
  from_addr=my_email,
  to_addr="funfunfun@yahoo.com",
  msg="Subject:hi man\n\nThis is body of my email"
)
connection.close()

#new one

with smtplib.SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=my_email, password = password)
  connection.sendmail(
    from_addr=my_email,
    to_addr="funfunfun@yahoo.com",
    msg="Subject:hi man\n\nThis is body of my email"
  )


