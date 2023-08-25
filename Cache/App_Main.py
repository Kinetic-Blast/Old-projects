import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re
import boto3
import glob
import datetime
from botocore.client import Config
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

###########ALL CREDS AND AWS COGNITO RESOURCES HAVE BEEN WIPED FROM THE PROJECT################

#Varaible
LocalPath =os.path.expanduser("~/Desktop/test/*")
LocalPath2 = os.path.expanduser("~/Desktop/test/")


#####################  Pages ######################

def Main():

    MAINroot = tk.Tk()
    MAINroot.configure(background="#DDCECD"), MAINroot.geometry("550x300")
    MAINroot.resizable(width=False, height=False)

    username_text = Label(text="Email:", bg="#DDCECD")
    username_guess = Entry(MAINroot)

    username_text.place(relx=0.35, rely=0.3, anchor=CENTER)
    username_guess.place(relx=0.5, rely=0.30, anchor=CENTER)

    password_text = Label(text="Password:", bg="#DDCECD")
    password_guess = Entry(MAINroot, show="*")

    password_text.place(relx=0.335, rely=0.4, anchor=CENTER)
    password_guess.place(relx=0.5, rely=0.4, anchor=CENTER)

    login = tk.Button(MAINroot, text="Login", padx=10, pady=5, fg="white", bg="#19647E",
                      command=lambda: Login(username_guess.get().lower(), password_guess.get(),MAINroot))
    register = tk.Button(MAINroot, text="Register", padx=10, pady=5, fg="white", bg="#19647E", command= lambda:RegisterPage(MAINroot))
    Forgot_Password = tk.Button(MAINroot, text="Forgot Password", padx=10, pady=5, fg="white", bg="#19647E",
                                command=ForgotPasswordEmail)

    login.place(relx=0.5, rely=0.52, relwidth=0.4, relheight=0.075, anchor=CENTER)
    register.place(relx=0.5, rely=0.6, relwidth=0.4, relheight=0.075, anchor=CENTER)
    Forgot_Password.place(relx=0.5, rely=0.68, relwidth=0.4, relheight=0.075, anchor=CENTER)

    MAINroot.mainloop()


# -----------------------------------------------------------------
def ForgotPasswordEmail():

    PASSEroot = tk.Tk()
    PASSEroot.configure(background="#DDCECD"), PASSEroot.geometry("300x150")
    PASSEroot.resizable(width=False, height=False)

    PASSE_text = Label(PASSEroot, text="Enter the email address associated with the account", bg="#DDCECD")
    PASSE_Input = Entry(PASSEroot)

    PASSE_text.place(relx=0.5, rely=0.3, anchor=CENTER)
    PASSE_Input.place(relx=0.5, rely=0.5, anchor=CENTER)

    PASSE_email = tk.Button(PASSEroot, text="Submit", padx=10, pady=5, fg="white", bg="#19647E",
                            command=lambda: PasswordVerify(PASSE_Input.get(),1))
    PASSE_email.place(relx=0.5, rely=0.75, relwidth=0.4, relheight=0.25, anchor=CENTER)


#------------------------------------------------------------------------------------------------------------
def RegisterPage(MAINroot):
    REGroot = tk.Tk()
    REGroot.configure(background="#DDCECD"), REGroot.geometry("550x300")
    REGroot.resizable(width=False, height=False)

    Email_text = Label(REGroot, text="Email:", bg="#DDCECD")
    Email_Input = Entry(REGroot)

    Email_text.place(relx=0.35, rely=0.3, anchor=CENTER)
    Email_Input.place(relx=0.5, rely=0.30, anchor=CENTER)

    Password_text1 = Label(REGroot, text="Password:", bg="#DDCECD")
    Password_Input1 = Entry(REGroot, show="*")

    Password_text1.place(relx=0.335, rely=0.4, anchor=CENTER)
    Password_Input1.place(relx=0.5, rely=0.4, anchor=CENTER)

    Password_text2 = Label(REGroot, text="Retype Password:", bg="#DDCECD")
    Password_Input2 = Entry(REGroot, show="*")

    Password_text2.place(relx=0.30, rely=0.5, anchor=CENTER)
    Password_Input2.place(relx=0.5, rely=0.5, anchor=CENTER)

    Register_Button = tk.Button(REGroot, text="Register", padx=10, pady=5, fg="white", bg="#19647E",
                                command=lambda: Verify(Email_Input.get().lower()
                                                       , Password_Input1.get(), Password_Input2.get(),REGroot,MAINroot))

    Register_Button.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.075, anchor=CENTER)
#------------------------------------------------------------------------------------------------------------

def ForgotPassword(email):
    PASSroot = tk.Tk()

    PASSroot.configure(background="#DDCECD"), PASSroot.geometry("550x300")
    PASSroot.resizable(width=False, height=False)

    PASSCode_text = Label(PASSroot, text="Verify Code:", bg="#DDCECD")
    PASSCode_Input = Entry(PASSroot)

    PASSCode_text.place(relx=0.325, rely=0.3, anchor=CENTER)
    PASSCode_Input.place(relx=0.5, rely=0.30, anchor=CENTER)

    PASSroot.configure(background="#DDCECD"), PASSroot.geometry("550x300")
    PASSroot.resizable(width=False, height=False)

    RESET_text1 = Label(PASSroot, text="New Password:", bg="#DDCECD")
    RESET_Input1 = Entry(PASSroot, show="*")

    RESET_text1.place(relx=0.31, rely=0.4, anchor=CENTER)
    RESET_Input1.place(relx=0.5, rely=0.4, anchor=CENTER)

    RESET_text2 = Label(PASSroot, text="Retype Password:", bg="#DDCECD")
    RESET_Input2 = Entry(PASSroot, show="*")

    RESET_text2.place(relx=0.3, rely=0.5, anchor=CENTER)
    RESET_Input2.place(relx=0.5, rely=0.5, anchor=CENTER)

    Forgot_Password_Confirm = tk.Button(PASSroot, text="Submit", padx=10, pady=5, fg="white", bg="#19647E",
                                        command=lambda: ConfirmPasswordReset(PASSCode_Input.get()
                                                                             , RESET_Input1.get(), RESET_Input2.get(),
                                                                             email))

    Forgot_Password_Confirm.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.075, anchor=CENTER)

#------------------------------------------------------------------------------------------------------------

def Verify(email, password1, password2,REGroot,MAINroot):
    print(email)
    print(password1)
    print(password2)

    if checkEmail(email) == True and checkPassword(password1, password2) == True:
        VERroot = tk.Tk()
        VERroot.configure(background="#DDCECD"), VERroot.geometry("250x100")
        VERroot.resizable(width=False, height=False)

        Code_text = Label(VERroot, text="Check Your Email For Verification Code", bg="#DDCECD")
        Code_Input = Entry(VERroot)

        Code_text.place(relx=0.5, rely=0.3, anchor=CENTER)
        Code_Input.place(relx=0.5, rely=0.5, anchor=CENTER)

        Code_Password = tk.Button(VERroot, text="Submit", padx=10, pady=5, fg="white", bg="#19647E",
                                  command=lambda: emailVerify(email, Code_Input.get(),VERroot,REGroot,MAINroot))
        Code_Password.place(relx=0.5, rely=0.75, relwidth=0.4, relheight=0.25, anchor=CENTER)

    else:
        errormessage = ""
        if checkEmail(email) == False:
            errormessage += "Please enter a valid email. "
        if checkPassword(password1, password2) == False:
            errormessage += "Passwords do not match. "
        messagebox.showinfo(" ERROR ", errormessage, icon="warning")
    import createAccount

    createAccount.createAccount(email, password1)
#------------------------------------------------------------------------------------------------------------

#App
def Run_App(s3,domain):

    #call s3 get files for array
    #call local files to get array

    APProot = tk.Tk()
    APProot.configure(background="#DDCECD"), APProot.geometry("750x750")
    APProot.resizable(width=False, height=False)

    LocalFrame = tk.Frame(APProot, bg="#FFFFFF")  # local
    LocalHeader = tk.Frame(APProot, bg="#28AFB0")  # Header Local
    Headerlocal = Label(LocalHeader, text="Local Files",font = "Helvetica 20 bold italic",bg = "#28AFB0",fg = "#FFFFFF")

    LocalFrame.place(relwidth=0.4, relheight=0.65, relx=0.53, rely=0.09)
    LocalHeader.place(relwidth=0.4, relheight=0.075, relx=0.53, rely=0.005)
    Headerlocal.pack(pady = 10)

    OnlineFrame = tk.Frame(APProot, bg="#FFFFFF")  # Online
    OnlineHeader = tk.Frame(APProot, bg="#28AFB0")  # Header Online
    HeaderOnline = Label(OnlineHeader, text="Online Files",font = "Helvetica 20 bold italic",bg = "#28AFB0",fg = "#FFFFFF")

    OnlineFrame.place(relwidth=0.4, relheight=0.65, relx=0.1, rely=0.09)
    OnlineHeader.place(relwidth=0.4, relheight=0.075, relx=0.1, rely=0.005)
    HeaderOnline.pack(pady = 10)

    ListLocal = tk.Button(APProot, text="Refresh Local", padx=10, pady=5, fg="white", bg="#19647E", command = lambda: getLocalFiles(LocalFrame))
    ListOnline = tk.Button(APProot, text="Refresh Cloud", padx=10, pady=5, fg="white", bg="#19647E", command = lambda: getCloudFiles(s3,domain,OnlineFrame))
    SyncButton = tk.Button(APProot, text="SYNC", padx=10, pady=5, fg="white", bg="#19647E", command = lambda: syncCloud(s3,domain,APProot,OnlineFrame,LocalFrame))

    ListLocal.place(relwidth=0.4, relheight=0.075, relx=0.53, rely=0.75)
    ListOnline.place(relwidth=0.4, relheight=0.075, relx=0.1, rely=0.75)
    SyncButton.place(relwidth=0.4, relheight=0.075, relx=0.1, rely=0.85)

    APProot.mainloop()

#####################  Non-Page Functions ######################

def getLocalFiles(LocalFrame:tk.Frame):
    LocalFiles = glob.glob(LocalPath)

    for widget in LocalFrame.winfo_children():
        widget.destroy()

    for file in LocalFiles:
        TempLable = tk.Label(LocalFrame, text=os.path.basename(file))
        TempLable.pack()

def getCloudFiles(s3,domain,OnlineFrame:tk.Frame):
    bucket = s3.Bucket(domain)

    for widget in OnlineFrame.winfo_children():
        widget.destroy()

    for file in bucket.objects.all():
        label4 = tk.Label(OnlineFrame, text = file.key)
        label4.pack()

def syncCloud(s3,domain,APProot,OnlineFrame:tk.Frame,LocalFrame:tk.Frame):

    temp = datetime.datetime.now()
    syncTime = Label(APProot, text=("Last Synced: " + temp.strftime("%m/%d/%Y, %H:%M:%S")), fg="#000000",bg = "#DDCECD")
    syncTime.place(relwidth=0.4, relheight=0.075, relx=0.53, rely=0.85)

    bucket = s3.Bucket(domain)

    tempbucketArray = bucket.objects.all()
    tempLocalFiles = glob.glob(LocalPath)

    realbucketArray = []
    realLocalArray = []

    for all in tempbucketArray:
        realbucketArray.append(all.key)

    for all in tempLocalFiles:
        realLocalArray.append(os.path.basename(all))


    print(realLocalArray)
    print(realbucketArray)

    temp = (list(set(realLocalArray) - set(realbucketArray)))
    temp2 = (list(set(realbucketArray) - set(realLocalArray)))

    temp3 = temp+temp2
    print(temp3)

    for item in temp3:
        if(realLocalArray.__contains__(item) ==True and realbucketArray.__contains__(item) == False):
             bucket.upload_file(LocalPath2+item,item)

        if(realLocalArray.__contains__(item)== False and realbucketArray.__contains__(item) == True):
            s3.Object(domain, item).delete()

    getLocalFiles(LocalFrame)
    getCloudFiles(s3,domain,OnlineFrame)


def PasswordVerify(email,temp):
    # Forgot Password

    client = boto3.client(
        'cognito-idp',
        aws_access_key_id='',
        aws_secret_access_key='',
        config=Config(signature_version='s3v4')
    )

    print(email)

    try:
        response = client.forgot_password(
            ClientId='',

            UserContextData={
                'EncodedData': 'string'
            },
            Username=email,
            AnalyticsMetadata={
                'AnalyticsEndpointId': 'string'
            },
            ClientMetadata={
                'string': 'string'
            }
        )

        if (temp != 2 ):
            ForgotPassword(email)
    except:
        messagebox.showinfo("ERROR", "INVALID VERIFICATION CODE ", icon="warning")
#------------------------------------------------------------------------------------------------------------
def ConfirmPasswordReset(code, password1, password2, email):
    client = boto3.client(
        'cognito-idp',
        aws_access_key_id='',
        aws_secret_access_key='',
        config=Config(signature_version='s3v4')
    )

    try:
        response = client.confirm_forgot_password(
            ClientId='',
            Username=email,
            ConfirmationCode=code,
            Password=password1,
            AnalyticsMetadata={
                'AnalyticsEndpointId': 'string'
            },
            UserContextData={
                'EncodedData': 'string'
            },
            ClientMetadata={
                'string': 'string'
            }
        )
        if checkEmail(email) == True and checkPassword(password1, password2) == True and PasswordVerify(email,2) == True:
            messagebox.showinfo(" SUCCESS ", 'Password Reset Successfully')
            print('We made it!')
    except:
        print('Failure')
#------------------------------------------------------------------------------------------------------------
# VERIFIES EMAIL ADDRESSS
def emailVerify(email, code, VERroot,REGroot,MAINroot):
    import verificationCheck
    import createUserBucket
    import addUserToAdminBucket
    verificationCheck.verificationCheck(email, code)
    createUserBucket.main(email)

    #     print('User Created')
    # else:
    #     print("user not created")
    # addUserToAdminBucket.main(email)

    connectToBucket(email,VERroot,REGroot,MAINroot)


# HERE THE USER CAN NOW BE ROUTED TO APP TO SEE THEIR FILES

#------------------------------------------------------------------------------------------------------------
# CHECK FOR VALID EMAIL
def checkEmail(email):
    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        print("valid")
        return True
    else:
        print("invalid")
        return False
    # return re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)

#------------------------------------------------------------------------------------------------------------
# CHECK FOR VALID PASSWORD
def checkPassword(password1, password2):
    if password1 == password2:
        print('pass valid')
        return True
    else:
        print('pass invalid')
        return False

#------------------------------------------------------------------------------------------------------------
def Login(email, password,MAINRoot):
    MAINRoot.destroy()
    print(email)
    print(password)

    client = boto3.client(
        'cognito-idp',
        aws_access_key_id='',
        aws_secret_access_key='',
        config=Config(signature_version='s3v4')
    )

    try:
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password

            },
            ClientMetadata={
                'string': 'string'
            },
            ClientId='',
            AnalyticsMetadata={
                'AnalyticsEndpointId': 'string'
            },
            UserContextData={
                'EncodedData': 'string'
            }

        )
        #CONNECTS THE USER TO BUCKET UPON SUCCESFUL LOGIN
        connectToBucket(email)
        print("Success")

    except Exception:
        print("Error")
        messagebox.showinfo("ERROR", " INVALID ACCOUNT CREDENTIALS ", icon="warning")

#------------------------------------------------------------------------------------------------------------
def connectToBucket(email,VERroot,REGroot,MAINroot):
    VERroot.destroy()
    REGroot.destroy()
    MAINroot.destroy()
    domain = email.split('@')[0]

    BUCKET_NAME = domain

    s3 = boto3.resource(
        's3',
        aws_access_key_id='',
        aws_secret_access_key='',
        config=Config(signature_version='s3v4')
    )

    Run_App(s3,domain)


Main()
