# Home Assignment Flask

## test deployed app
1. The app was deployed using **Heroku**, the link is:  https://blooming-temple-57087.herokuapp.com/
2. In the email I sent you, you can find **Postman's** file, please use it in order to test the app.
3. Overall, we have two users routes, login and createUser.
4. We also have few messages routes like creating a message, getting messages and more.
5. All message routes are protected, so make sure to place the user token that you get after creating a new user or logging in the head under: **Authorization**

## run app locally
1. In order to run the app locally, enter the base directory and activate the virtual environment by using this command: `source venv/bin/activate`.
2. Next, we need to install all the requirements from the file `requirements.txt`, using this command:  `pip3 install -r ./requirements.txt`.
3. In the email I've sent you, you can find a **.env** file, please place it in the root directory of the app.
4. Run the app by using the **run_flask_app** file `./run_flask_app`, or just simply run `FLASK_APP=main.py FLASK_ENV=development flask run`.
5. Now, you can simply test the app using **Postman**.