from flask import Flask,render_template,request,redirect,session,flash,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from datetime import date
from flask_mail import Mail
from flask_mail import Message

resume_Verification="0"
stage1="1"
stage2="2"
hrRound="3"
reject="-1"
approve="-2"
pending="-3"
UPLOAD_FOLDER = './static/resume/'
UPLOAD_IMAGE='./static/images/includes'
ALLOWED_EXTENSIONS = {'pdf'} 
ALLOWED_EXTENSIONS_IMAGE={'jpg','png','jpeg'}
currentDate=date.today()

app=Flask(__name__)
app.config['SECRET_KEY']= "afhbrjbnjbc" 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_IMAGE'] = UPLOAD_IMAGE
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/recruitement_management_system'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "sufi.taken@gmail.com",
    MAIL_PASSWORD = "Affan@s1"
)
mail = Mail(app)
db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def allowed_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_IMAGE


class users(db.Model):
    sno =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(56), nullable=False)
    email = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(10), nullable=False)



class job_details(db.Model):
    job_id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String,nullable=False)
    name_of_job = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=True)
    CTC = db.Column(db.String,nullable=True)
    apply_by = db.Column(db.DateTime, nullable=True)
    experience = db.Column(db.String, nullable=False)
    applicant = db.Column(db.String, nullable=True)
    about_the_job = db.Column(db.String, nullable=False)
    skill_required = db.Column(db.String, nullable=False)
    who_can_apply = db.Column(db.String, nullable=False)
    num_of_opening = db.Column(db.String, nullable=False)
    job_status = db.Column(db.String, nullable=False)
    slug	 = db.Column(db.String, nullable=False)
    img	 = db.Column(db.String, nullable=False)
   

class applicant(db.Model):
    s_no = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    jobIdentity = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    resumeFile = db.Column(db.String, nullable=False)
    applicant_state = db.Column(db.String, nullable=False)
    transfer_status = db.Column(db.String, nullable=False)
    
    
@app.route("/")
def home():
     jobRecord=job_details.query.filter(
         job_details.job_status.like("opend")
     ).all()[0:6]
     print(jobRecord)
     return render_template("index.html",jobRecord=jobRecord,userNameSess=session['nameSession'] if "nameSession" in session else None)

@app.route('/jobDetails/<string:slug>/<string:job_id>',methods=['GET'])
def jobDetails(slug,job_id):

    jobDetails = job_details.query.filter(
        job_details.job_id.like(job_id),
        job_details.slug.like(slug)
        ).all()
    session['jobIdSession']=jobDetails[0].job_id
    return render_template("jobDetails.html",jobDetails=jobDetails,userNameSess=session['nameSession'] if "nameSession" in session else None)

@app.route("/user",methods=['GET','POST'])
def user():
     if request.method == 'POST':
         print("here reaches")
         print(request.form)
#------------------------------------------------------------------------------------------------
#<|============================= Signup  functionality ======================|>
#------------------------------------------------------------------------------------------------

         if "signUp" in request.form:
             print("if condition true")
             name = request.form['name']
             email = request.form['email']
             password = request.form['password']
             userRecord = users.query.filter(
               users.email.like(email)
             ).all()
             userFound=len(userRecord)
             if userFound<=0:
                 print(name+email+password)
                 entry=users(name=name, email=email,password=password)
                 db.session.add(entry)
                 db.session.commit()
                 return render_template("login.html",msg='')
             else:
                return render_template("login.html",msg="Username already exist pls try again!!!")
#------------------------------------------------------------------------------------------------
#<|=============================END Signup  functionality ======================|>
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
#<|============================= Login  functionality ======================|>
#------------------------------------------------------------------------------------------------

         else:
             print("else condition true")
             userName = request.form['userName']
             pas = request.form['pas']
             print("record")
             userRecord = users.query.filter(
                     users.email.like(userName),
                     users.password.like(pas)
             ).all()
             userFound=len(userRecord)
             if userFound>0 and userRecord[0].email==userName:
                 session['nameSession']=userRecord[0].name
                 session['emailSession']=userRecord[0].email
                 return redirect("/")
             elif userName=="admin@123" and pas=="admin@123":
                 session["adminSession"]=userName
                 return redirect("/adminPanel")

             else:
                  return render_template("login.html", msg="Invalid username and password!!!")

#------------------------------------------------------------------------------------------------
#<|=============================END Login  functionality ======================|>
#------------------------------------------------------------------------------------------------
     elif session.get('nameSession') is not None:
       
         print(session['nameSession'])
         return redirect("/")
     else:
         return render_template("login.html",msg='')

@app.route("/signOut")
def signOut():
    session['nameSession']=None
    session['emailSession']=None
    session['jobIdSession']=None
    return render_template("login.html",msg='')

@app.route("/adminSignOut")
def adminsignOut():
     session['adminSession']=None
     return render_template("login.html",msg='')

@app.route("/submit-applicant",methods=['POST'])
def applicantForm():
     if request.method == 'POST':
        file = request.files['resume']
        contact = request.form['cont']
        if file and allowed_file(file.filename):
            flash('Not allowed file')
            filename = secure_filename(file.filename)
            renamefileName=session['emailSession'][0:8]+"_"+str(session['jobIdSession']) +"_"+str(currentDate)+"."+filename.split('.',1)[1]
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],renamefileName))
          
            enterRec=applicant(name=session['nameSession'],username=session["emailSession"], jobIdentity=session["jobIdSession"], contact=contact, resumeFile=renamefileName, applicant_state=resume_Verification,transfer_status=pending)
            db.session.add(enterRec)
            db.session.commit()
            mail.send_message('New message from Medigo',
                          sender="sufi.taken@gmail.com",
                          recipients =[session["emailSession"]],
                          body = "Your application has been successfully submitted!!!"
                          )
            return redirect('/')
     
@app.route('/adminPanel',methods=['GET','POST'], defaults={'btn': None,'id': None})
@app.route('/adminPanel/<string:btn>/<string:id>',methods=['GET','POST'])
def admin(btn,id):
    if session['adminSession']!=None:
       

        if request.method=='POST':
          comName=request.form['comName'].capitalize()
          nameOfJob=request.form['nameOfJob'].capitalize()
          jobLocate=request.form['jobLocate'].capitalize()
          startDate=request.form['startDate'].capitalize()
          CTC=request.form['CTC']
          applyBy=request.form['applyBy']
          exp=request.form['exp'].capitalize()
          applicantData=request.form['applicant']
          aboutJob=request.form['aboutJob'].capitalize()
          skillReq=request.form['skillReq']
          whoApply=request.form['whoApply'].capitalize()
          numOfOpening=request.form['numOfOpening']
          jobStatus=request.form['jobStatus']
          slugName=request.form['slugName']
          jobImage=request.files['jobImage']
          addjobBtn=request.form['addJob'] if "addJob" in request.form else None
          updateJobBtn=request.form['updateJob'] if "updateJob" in request.form else None
          jobID=request.form['jobID']
        
          if addjobBtn=="Add job":
              
              if jobImage and allowed_image(jobImage.filename):
                  flash('Not allowed file')
                  filename = secure_filename(jobImage.filename)
                  renamefileName=slugName+"_"+str(currentDate)+"."+filename.split('.',1)[1]
                  jobImage.save(os.path.join(app.config['UPLOAD_IMAGE'],renamefileName))
                  enterRec=job_details(company_name=comName, name_of_job=nameOfJob, location=jobLocate, start_date=startDate, CTC=CTC, apply_by=applyBy, experience=exp,applicant=applicantData, about_the_job=aboutJob, skill_required=skillReq, who_can_apply=whoApply, num_of_opening=numOfOpening,job_status=jobStatus, slug=slugName, img=renamefileName)
                  db.session.add(enterRec)
                  db.session.commit()
                  return redirect("/adminPanel")
          if updateJobBtn=="Update job":
              updateRecord = job_details.query.filter(
                job_details.job_id.like(jobID)
              ).first()
              updateRecord.company_name=comName
              updateRecord.name_of_job=nameOfJob
              updateRecord.location=jobLocate
              updateRecord.start_date=startDate
              updateRecord.CTC=CTC
              updateRecord.apply_by=applyBy
              updateRecord.experience=exp
              updateRecord.applicant=applicantData
              updateRecord.about_the_job=aboutJob
              updateRecord.num_of_opening=numOfOpening
              updateRecord.job_status=jobStatus
              updateRecord.slug=slugName
              db.session.commit()
              return redirect("/adminPanel")


        elif btn=="edit" and id!=None:
             singlejobRecord = job_details.query.filter(
                job_details.job_id.like(id),
             ).all()
             return render_template("adminMain.html",singlejobRecord=singlejobRecord,adminSession=session['adminSession'],stageAppliRecord='',stageSelectedjobRecord='')

        else:
             selectedjobRecord=[]
             appliRecord=applicant.query.filter().all()
             jobRecord=job_details.query.filter().all()
             for i in range(0,len(appliRecord)):
                 selectedRecord=job_details.query.filter(
                     job_details.job_id.like(appliRecord[i].jobIdentity)
                 ).all()
                 selectedjobRecord.append(selectedRecord)   
             return render_template("adminMain.html",jobRecord=jobRecord,adminSession=session['adminSession'],applicantRecord=appliRecord,selectedjobRecord=selectedjobRecord)
    else:
        return redirect("/user")



@app.route("/Stage/<string:stageId>",methods=['GET','POST'])
def Stage(stageId):
    if request.method=='GET':
        stageSelectedjobRecord=[]
        stageAppliRecord=applicant.query.filter(
                applicant.applicant_state.like(stageId)

        ).all()
        jobRecord=job_details.query.filter().all()
        for i in range(0,len(stageAppliRecord)):
            selectedRecord=job_details.query.filter(
                     job_details.job_id.like(stageAppliRecord[i].jobIdentity)
            ).all()
            stageSelectedjobRecord.append(selectedRecord)
        print(stageAppliRecord)
        print(stageSelectedjobRecord)
        return render_template("adminMain.html",jobRecord=jobRecord,adminSession=session['adminSession'],stageAppliRecord=stageAppliRecord,stageSelectedjobRecord=stageSelectedjobRecord,applicantRecord="",selectedjobRecord="")

@app.route("/action/<string:btn>/<string:Sno>",methods=['GET','POST'])
def commonAction(btn,Sno):
    if request.method=='GET':
        appRec=applicant.query.filter(
                applicant.s_no.like(Sno)

             ).first()
        findStage=" Resume Verification " if appRec.applicant_state=="0" else " Stage I " if appRec.applicant_state=="1" else " Stage II " if appRec.applicant_state=="2" else " HR Round/Final Round " if appRec.applicant_state=="3" else " None "
        if btn=="veiw":
             
             workingdir = os.path.abspath(os.getcwd())
             filepath = workingdir + '/static/resume/'
             return send_from_directory(filepath,appRec.resumeFile)
        elif btn=="approve":
            msgFrame = "<b>Hello,"+appRec.name+" </b><br><p>I hope you will be safe in the priod of covid. Your application has been approved from "+findStage+" and Forwarded to the Higher Round. I am informing you be ready for interveiw. your interveiw  will tack place through your given mobile Number.</p><br> Best of Luck!!!"
         
            state=int(appRec.applicant_state)
            if(state<3):
                state=state+1
                appRec.applicant_state=state
                appRec.transfer_status=pending
                db.session.commit()
                msg = Message("New message from Medigo",
                  sender="sufi.taken@gmail.com",
                  recipients=[appRec.username])
                msg.html = msgFrame
                mail.send(msg)
                return redirect("/adminPanel")
            else:
                appRec.transfer_status=approve
                db.session.commit()
                msg = Message("New message from Medigo",
                  sender="sufi.taken@gmail.com",
                  recipients=[appRec.username])
                msg.html = msgFrame
                mail.send(msg)
                return redirect("/adminPanel")
        else:
            msgFrame = "<b>Hello,"+appRec.name+" </b><br><p>I hope you will be safe in the priod of covid. Your application has been rejected from "+findStage+"</p><br> Best of Luck!!!"
            appRec.transfer_status=reject
            db.session.commit()
            msg = Message("New message from Medigo",
                  sender="sufi.taken@gmail.com",
                  recipients=[appRec.username])
            msg.html = msgFrame
            mail.send(msg)
            return redirect("/adminPanel")


            
@app.route("/contact",methods=['GET','POST'])
def contactPage():
    if request.method=='POST':
        
        name=request.form.get("name")
        email=request.form.get("email")
        subject=request.form.get("subject")
        msg=request.form.get("message")
        sendMessage=request.form.get("sendMessage")
        
        
        if sendMessage=="Send Message":
            print(sendMessage)
            mail.send_message(subject,
                          sender="sufi.taken@gmail.com",
                          recipients =["mdsufiyanidrisi786@gmail.com"],
                          body = "Contact By "+name+" whose email id is "+email+"\n"+msg
                          )
                          
            return render_template("contact.html")
    
    else:
        return render_template("contact.html")
  
app.run(host='localhost',port=8080,debug=True)