# SendAnEmail

In my ever expanding mission to learn more with python i decided to give emails a shot. i had done it once a few years ago but that old code didnt end up working. i use twilio for sending texts and while logging in i saw an ad about their email service SendGrid, i decided to give it a shot. with youtube tutorials and a walthrough process along with a few modifications of their original code i got it to work. once that happened i added a few variables, asked for input, used my own environmental variables and have my own twist on SendGrids python email code. i plan on altering it further but whats here will work for now.

to register for an account you have to include your own email, even your home address. and youre only able to send from the email you registered with, so you will see the from email variable is the environmental variable and the other variables of the email are from input from a user.

i run this code with python3, trying to do so with python2.x results in ImportError: No module named sendgrid.
