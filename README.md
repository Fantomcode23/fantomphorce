 # **Combat Carbon**
Combat Carbon is an all-in-one carbon emission tracking web application built that helps individuals calculate
their carbon emissions based on aspects like transportation, utilities, etc.
It includes a chatbot that answers questions and can make reccomendations to users on which route to 
use, it does so through a machine learning model utlising random forest regression.
It uses flask on the backend, and SQLite for database, along with RESTful API. Botpress was used to 
make the bots to include generative AI features integrated with the ML model.

**This project was created at FantomCode 2024 held in RV Institute of Technology and Management.**


<img width="950" alt="Screenshot 2024-05-17 at 4 04 41 AM" src="https://github.com/Fantomcode23/fantomphorce/assets/132202476/5df6b4dc-cade-4830-935f-265849fe25d0">

# **What are we trying to solve?**
Global warming is a pressing issue of modern times, where increased emissions lead to climate change. Recent heat 
waves in Bengaluru made us deeply think about climate change and its impact. Hence, we decided to build a emission tracker 
that tracks carbon emissions and in turn helps us reduce our emissions and do our bit to 
fight climate change. The main idea is that tracking can lead to more mindful consumption and hence a reduction in emissions
leading to lower overall emissions.

# Technology Stack 
## Web application
- HTML <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>
- CSS <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>
- Bootstrap <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer">
- Flask (Python)  <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a>
- Python <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
- SQLite <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>
- Postman API <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a>

## AI-ML powered chatbot
- BotPress 
- TensorFlow <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a>
- Pandas <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a>
- PyTorch <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a>
- Scikit learn <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a>
## Others 
- Git <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>
- C++ <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a>

# How to get started?
On VScode, open our repo.
Open the server.py file and python server.py
or run the server.py under local host.

# Problems with existing solutions
- Lack of appropriate AI ML model integrations.
- Lack of dedicated chatbots.
- Lack of one-stop solution.

# Solution
Our simple and intuitive Web based application tracks emissions and encourages to reduce the emissions.

# Working and features
- Sign in with user authentication using email OTP .
- Dashboard leading user to various features of the website
- Emission calculator which calculates total carbon emissions.
- Graphical representation of the calculated emissions with respective categories.
- ChatBot answering the user's questions.
- Machine Learning model using Random Forest Regression model to predict emissions based on transport routes.
- Database stores the entered user data for future usage.
- Advice page for suggestions under each category.

  
# We ran into the following challenges
- Integrating the flask based website with all the different components.
- Finding suitable dataset and problems training ML model appropriately.
- Integrating flask and the AI powered ML recomendation engine.

# Scope for further enhancements
- Improve UI.
- Introduce points based system to encourage users to stay motivated.
- Additional features to enhance User Experience like integration with google maps API to get automatic
  transport emissions.

# Team
 ## [Karthik Prakash](https://github.com/kart2004)
 ## [Gayathri Jayan](https://github.com/gaya3jayan-11)
 ## [Anshul B A](https://github.com/Anshul-B-A)
 ## [Sai Aiswarya](https://github.com/aiswarya200400)
