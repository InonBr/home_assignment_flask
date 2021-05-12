# Home Assignment Flask

## test deployed app
1. The app was deployed using **Heroku**, the link is:  https://blooming-temple-57087.herokuapp.com/
2. In the email I sent you, you can find **postman's** file, please use it in order to test the app.
3. Overall, we have two users routes, login and createUser.
4. We also have few massages routes like creating a massage, getting massages and more.
5. All massages route are protected, so make sure placing the user token that your getting after creating a new user or logging in as **Authorization**

## run app locally
1. In order to run the app locally, enter the base directory and activate the virtual environment by using this commends: `source venv/bin/activate`.
2. Next, we need to install all the requirements from the file `requirements.txt`, using this commends:  `pip3 install -r ./requirements.txt`.
3. In the email I've sent you, you can find a **.env** file, please place it in the root directory of the app.
4. Run the app by using the **run_flask_app** file `./run_flask_app`, or just simply run `FLASK_APP=main.py FLASK_ENV=development flask run`.
5. Now, you can simply test the app using **postman**.