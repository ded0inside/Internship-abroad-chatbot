# Internship Abroad Help Chatbot

Link to project: [Internship Abroad Chatbot](https://github.com/ded0inside/Internship-abroad-chatbot)

Link to Wiki-Repository: [Chatbot Wiki](https://github.com/ded0inside/Internship-abroad-chatbot/wiki)
# Project Description

Title: Internship Abroad Help Chatbot

Description:
Project is designed to help students of Deggendorf University with their questions related to Internships Abroad. 

3 user personas were identified: International Students, European Students and Older students. 

They all have different requirements and questions, and our the is to be able to help them as much as possible. It will reduce the workload of Career-Service department of DIT.

# Prerequisites:
| Name | Version |
| ------ | ------ |
|Python | 3.10.11 |
|Rasa|3.6.15|

# Installation

To install Rasa, please type:

    pip3 install rasa


Create an inital model by typing:

    rasa init

Please copy our files and paste them into the respective files on the local installation.

You can download our *endpoints.yml* file. \
If you choose to install the default one, 
please enable the actions endpoint in it.

Or paste the lines below in your *endpoints.yml* file:

    action_endpoint:
        url: "http://localhost:5055/webhook" 

The *config.yml* file also requires some changes. \
You can download our file, or in the default file, uncomment the *pipeline* and  add:

    pipeline:
        ...
        - name: ResponseSelector # this is present by default
            epochs: 100
            constrain_similarities: true
        - name: ResponseSelector # please add this also
            epochs: 100
            constrain_similarities: true
            retrieval_intent: cv_resume_assistance
        ...

After the setup is complete, to ensure that everything has been installed properly and there are no missing values, please run:

    rasa data validate

if there are no errors, then
you can train the model locally using:

    rasa train

## Optional Installation:

The user has the ability to send an email to the student office through our Chatbot.

Email Sending Ability does not impact any other functions of the bot, but it requies additional downloads to work.

More information can be found here: https://developers.google.com/gmail/api/quickstart/python

Please install the *tokens.json* and *credentials.json* files from the repository. \
And place them in the root directory of the project.

To install the email sending functionality:

    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

The above command installs the following:
| Name | Version |
| ------ | ------ |
|google-api-core| 2.15.0|
|google-api-python-client|     2.113.0
|google-auth|                  2.25.2
|google-auth-httplib2|         0.2.0
|google-auth-oauthlib|         1.2.0
|google-pasta|                 0.2.0
|googleapis-common-protos|     1.62.0

Steps after installation:
1) Please trigger the *action_send_email* while using the Chatbot, by using the *custom_email* intent.

2) In a new machine, it *might* open a window in a browser, to ask you to verify the request.

    - Once the request has been verified, the email will be sent.

#### Test Email And Password 
This is the email which **sends** a message from the chatbot to the required person(s).

Email : helpinternship.dit@gmail.com \
password: internship1234

You can change the **receiver** email to get the response in your own email, or any other email. \
By default, it sends a message to my student email.

# Basic Usage

To start using the model, create two terminals,

In one terminal, please write:

    rasa run actions

In the other terminal, please write:

    rasa shell

You can start the conversation in the terminal where you wrote 'rasa shell`' with a greeting.

The bot will ask the user to fill some basic information, but you can deny it and go straight to questions.

We have the following key use cases:
1. General Information Gathering:
- This is crucial for all prospective students, as it provides them with an understanding of the   overall process and helps them get started on the right foot.
2. Eligibility Assessment:
- Determining eligibility is essential because it streamlines the internship search by matching students with opportunities they qualify for, reducing wasted effort.
3. Application Process Guidance:
- Guiding students through the application process ensures they complete necessary steps correctly and on time, which is fundamental to a successful application.
4. Resume/CV Assistance:
- Crafting an effective resume is a foundational requirement for securing internships, as it's often the first impression that employers or internship providers have of the candidates.
5. Document Checklist:
- Ensuring that students have all the necessary documents is vital to avoiding application rejections due to missing paperwork.
6. Visa and Legal Requirements:
- Understanding visa and legal requirements is critical for international students, as non-compliance can lead to visa issues and legal complications.

## Typical conversation

**user**: hi 

**bot**: Hey! I am Jarnathan.
Here to help you with your internship   abroad. \
Would you like to answer some questions
so that we could help you better?

**user**: No

**bot**: No worries! You can still ask your questions! \
            Although I won't be able to help you better. \
        Here are my use cases: 
1) General Information
2) Eligibility assessment
3) Application process guidance
4) CV Assistance
5) Document checklist
6) Visa and Legal requirements
7) Who can I contact
8) Custom Email
9) Fill/Reset Form \
(These are rasa buttons, which the user can click, or they can type their own question)

**user**: General Information

**bot**:Welcome to general information \
You can type in your questions, or directly find an answer for the ones listed below
1) Timing
2) Overall Description
3) Back to Main topics

**user**: How long should the internship be?

**bot**: Minimum internship duration in the training company must not be 
            less than 90 working days1 (18 full weeks). Public holidays, sick days,  
            any recreational leaves or any company holidays shall be excluded from this 
            minimum internship duration. You are responsible for ensuring that this 
            duration is complied with. Combined with the two block weeks of courses \
            accompanying the internship, this results in the required minimum internship 
            duration of 20 weeks. 

Do you have some more questions regarding general information? 
1) Yes
2) Go Back To Main topics
3) No more questions related to any topic

**user**: No more questions

**bot**: Are you satisfied with my answers?

**user**: Yes

**bot** would you like to give us some feedback?

**user**: No

**bot**: Thank you for your time! Hope you have a great day!


# Implementation of the Requests

### Uses cases
Uses cases were described before, but can also be found [here](https://github.com/ded0inside/Internship-abroad-chatbot/wiki/Key-Use-Cases).

### Personas
Detailed information about personas can be founded in corresponding
[Wiki page](https://github.com/ded0inside/Internship-abroad-chatbot/wiki/Personas)

### Example dialogs
All example dialogs can be founded in corresponding [Wiki page](https://github.com/ded0inside/Internship-abroad-chatbot/wiki/Sample-Dialogs)

### Dialog flow
[Link to the dialog flow diagrams](https://github.com/ded0inside/Internship-abroad-chatbot/wiki/Conversational-flow)

### domain.yml
[Domain file](https://github.com/ded0inside/Internship-abroad-chatbot/blob/main/domain.yml) has these main parts
- Intents which bot reactss on
- Forms which have been used to collect info from user
- Slots
- Responses of bot
- Declaration of the form validation action and sending email action.

#### Detailed descripton of forms 
We have 4 forms.
- basic information: This forms collects some basic information about the user like their name, degree program, citizenship, student email, student age and whether they have kids or not(For the older students).

- eligibility assesment form: This form asks the users a few questions to fill the following slots:
    - is_valid_semester: If the user is in the 5th is_valid_semester
    - has_enough_ects: if the user has enough ECTS to go for internship is_valid_semester
    - internship_duration: if the duration of the student's internship is enough.

- satisfaction_feedback: here we ask the user if they are satisfied and if they would like to give us some feedback. The slots used are:
    - satisfaction: checks if user is satisfied
    - give_feedback: checks if user wants to give give_feedback

- write_email: This form collects the user's questions and sends it as an email. The slots filled are:
    - subject: subject of the email
    - body: body of the email
    - mnr_number: matriculation number of the student.

#### Detailed description of slots
Slots can be explained as bot's "memory".
Following slots have been used:
- _german_ - boolean slot which represents if user is a german student or not
- _old_ - boolean slot which represents if user is an older student or not
- _degree_program_ - text slot which represents user's degree
- _name_ - text slot which represent's user's name
- _student_email_ - text slot which represent's user's email
- _satisfaction_ - boolean slot to check if user is satisfied or not
- _give_feedback_ - boolean slot to know if user wants to give feedback or not 
- _subject_ - text slot which represent's the subject of an extra questions email
- _body _ = text slot which represent's what user wants to ask in the extra questions email
- mnr_number: Text slot which stores the matriculation number of the student.

#### Detailed description of the responses
We used 3 different typse of response required for a bot flexability.They are: conditional (e.g. coordinator email), response with buttons (e.g. use case choosing) and the regular one.

### nlu.yml
[This file](https://github.com/ded0inside/Internship-abroad-chatbot/blob/main/data/nlu.yml) contain possible user's inputs which groupped by topics (like greeting, affirming etc.).

Two types of intents were used: usual one and regular expression. Regular expression was used to extract valid degree code. 

### stories.yml
[This file](https://github.com/ded0inside/Internship-abroad-chatbot/blob/main/data/stories.yml)
 contains the main conversation flow of our bot. 
In the start, we ask the user if they want to fill up a form to give us some information.
Then, we display them the use cases.
After every subtopic question answer action, we ask the user if they have more questions or not.
In case the user doesn't have any more questions, we initate the feedback form from the stories.

### rules.yml
[This file](https://github.com/ded0inside/Internship-abroad-chatbot/blob/main/data/rules.yml) defines the rule for our chatbot, we have defined activation and deactivation rules for all of the forms here. \
Additionally, we use the retrieval intents for "cv_resume_assistance" here.

### actions.py
[This file](https://github.com/ded0inside/Internship-abroad-chatbot/blob/main/actions/actions.py) contains the form validation action and the action to reset all slots \
It also contains the methods to send an email via rasa.

# Special Features
We have implemented some special features in this project to help the user more effectively.
Here is a list of them:
1. Basic Information Form:
- We use rasa forms to ask the user for some basic information. This helps us respond in a more personalized manner
2. Subtopic rules:
- We use retrieval intents, a feature of rasa which allows us to answer questions related to a sub topic without explicitly mapping them in stories
3. Helpful Buttons:
- After we respond to a user's question on a certain topic, we ask them if they have more questions related to that same topic, if they want to view other topics or if they are done and they would like to end the conversation. This gives our users lots of flexibility.
4. Ability to send emails
- If the user would like to send an email to the student office, in case they have questions we cannot answer or are not satisfied with the answers, they have the ability to do so through the chatbot.
5) Ability to reset slots:
- Users can reset all of the slots they filled, if they have filled them wrong or if they want.

# Contributing

We welcome contributions! Please follow these steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new pull request

Please ensure your code follows our coding standards.

# License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

# Contact

For questions or support, contact [ilia.dulkin@stud.th-deg.de](mailto:ilia.dulkin@stud.th-deg.de).
