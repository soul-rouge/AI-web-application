Tutorial followed to create virtual env: "https://fastapi.tiangolo.com/virtual-environments/"
Tutorial followed for the rest of the code: "https://www.youtube.com/watch?v=iqrS7Q174Ac"
FastAPI documentation: "https://fastapi.tiangolo.com/"

Tip: Run an interactive window along with the .py file by opening command pallete and selecting the option "Run selection/line in interactive window". It lets us explore various variables and all.


Steps followed to create this project:
1. Created the folder Flask-Docker.
2. ran "python -m venv .venv" in its terminal.
    python: use the program called python
    -m: call a module as a script, we'll tell it which module next
    venv: use the module called venv that normally comes installed with Python
    .venv: create the virtual environment in the new directory .venv
3. VS code asked a prompt that a new environment was created, do you want to use it for this folder.
4. Run ".venv\Scripts\Activate.ps1" to activate the virtual env, so that any Python command you run or package you install uses it.
    Tips: Do this every time you start a new terminal session to work on the project.
          Every time you install a new package in that environment, activate the environment again.
5. To check if the virtual env is active, use "Get-Command python".
6. Upgrade pip using "python -m pip install --upgrade pip", because Many exotic errors while installing a package are solved by just upgrading pip first.
7. Use "echo "*" > .venv/.gitignore" to exclude .venv from .gitignore file.
8. Now, you may install a package directly using pip or use a text file that includes all the requirements for the project, run "pip install -r requirements.txt".
9. Once you are done working on your project you can deactivate the virtual environment using "deactivate" later.
10. Create model.py file and save it. Try running it using "python model.py". Libraries used in model.py should also be installed using requirements.txt.
11. follow the above mentioned youtube tutorial.
12. After making the main.py file, run "uvicorn main:app --reload" to run the application and click on the link it is running on to see it.
    main:app means import app from file main. add "/docs" to the link to see various responses.
13. install docker desktop.
14. run "docker init" to create all the required docker files for your application. when it asks for the command to run your app, type "uvicorn main:app --reload --port 8000 --host 0.0.0.0".
15. "python-multipart" is needed inside "requirements.txt" for file upload in the web application.
16. add below code to Dockerfile because transformers library needs rust compiler.
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
17. make the few minor changes as instructed in the video.
18. now that we have our docker file, build docker image by running "docker compose up --build". now the app will be running from inside our docker container. make sure docker desktop is also running otherwise it gives error. open the link in docker desktop software to see the running web application.


