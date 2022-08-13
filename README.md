# EB API Consuming Web-Project

This website connects to the public staging area API of EasyBroker:

> https://api.stagingeb.com/playground

It consists of 2 main pages, the properties list, and the property page.

## Properties List

- Shows 15 properties per page.
- Includes pagination links as to navigate to any page.
- Only includes published properties.
- Each item in the list displays its public ID, title, property type, location and a image thumbnail.

## Property Page

When a user clicks on a property in the list, they will be taken into that property detailed information page using the properties/{property_id} endpoint.

The page displays the following information:

- Public ID.
- Title.
- Description.
- A slideshow with all available photos.
- Property type.
- Location

Also included in this page, is a contact form to create new leads. This contact form is directly sent to EB's API using its contact_requests endpoint.

### Contact Form

The contact form must include the following:

- Name.
- Phone number.
- E-mail address.
- A message.
- The property_id of the property page where this form is being sent from. *This value is set by default.*

## Screenshots

![Home](https://i.imgur.com/E1pCLlM.png)

![Page 15](https://i.imgur.com/vKNoARQ.png)

![EB-B5439](https://i.imgur.com/CNccg6M.png)

## Installation

Start by downloading the repository and placing it in a folder of your choosing. 

For the following commands, run a terminal from that folder, or navigate to it inside a terminal.

Make sure you have Python installed:

```bash
python3 --version
```

If not, install with:

```bash
sudo apt-get install python3
```

It is highly recommended you create a virtual environment and activate it before the next step:

```bash
python3 -m venv venv
source venv/bin/activate
```
Now it is time to install all the project dependencies:

```bash
pip install -r requirements.txt
```

As simple as that! You are now ready to fire up the project.

## Usage

If you just followed the installation steps, you should have your virtual environment active right now.

If not, open a terminal in the folder where the project and the virtual environment resides, you can activate it with:

```bash
source venv/bin/activate
```

![Activating the virtual environment](https://i.imgur.com/nvOEeiy.png)

Now we should run the server hosting the website:

```bash
python manage.py runserver
```

After running the server you should see a line like this one:

```bash
Starting development server at http://127.0.0.1:8000/
```

Type that url in your prefered web browser, and voila! You are now ready to navigate the website.

If you wish to run the unit tests, you can do so like this:

```bash
python manage.py test
```

The test file can be found here:

> ebproject / tests.py

## Notes

This project has been built using the "Divide and Conquer" method. By dividing this task (project) into small, bite size tasks, and conquering each one by one, it was manageable to complete all the requirements of the project.

Because of the desire to complete all basic requirements within the narrow time constraints, the testing code was not created/implemented until the end of the development cycle. Having a more generous and relaxed time constraint, I would have chosen a "Test-driven Development" style.

#### **Regarding the API Key:**

This project treats the API key for what it is, a publicly available API key.

Being a public API key, no effort was done in order to conceal it. If this were a private API key, it would of remain hidden, never hard-coded, never saved in a file as to make it impossible for it to be "accidentally" commited into the online repository. The private key would of been stored **only** as a environment variable.

### Hardest Thing To Solve

Every step of the way was a very exciting and interesting challenge to overcome. There were many of these challenges I was very happy to be able to complete!

Definetly the hardest thing to solve were the unit tests. I have had some experience with them, but mostly locally contained simple stuff, this without a doubt was a very nice challenge.

Oscar Z. from the EB team, before commencing this project, was kind enough to point out that this area was a area of oportunity for me (Clearly my unit-testing in the first mini-project was not very impressive), and shared a very nice RealPython.com post about "Mocking External APIs in Python", it was of extreme value for this project. I learned a lot with the post and by working on it on this project, and I am very happy with what I was able to accomplish. That said, I still require more reading and experimenting to fully wrap my head around these concepts. I definetly see the tests in this project as extraordinary first steps.

### If Able To Finish

Originally it was my desire to use class-based views instead of function-based views with Django. Because of the time constraint, I decided to start the project with function-based views, and first complete the following:

#### **Priority:**

- Meet the project requirements with function-based views.
- Refactor my code as to achieve clean and efficient code
- Create some decent test coverage
- Create the documentation.

If able to complete this priority list, and still have time available:

#### **Nice to have:**

- Convert the function-based views into class-based views.
- Give the HTML and CSS code some love, just to make things prettier.

The good news are, the priority list was completed inside the time frame! Yay!

The bad news on the other hand... Not much time was left after finishing the priority list, so I decided to spend the little time left refactoring the code some more, moving code concerned with HTML from views.py to the corresponding .html files, improving the documentation and doing some minor visual upgrades to the website.

Am I happy with the progress done given the time constraints? Yes, yes I am. Would of loved 24 more hours to really smooth out all of the rough edges and have much better error handling, really making it pop! But for a 72 hour project, I am very happy with the results.

### Dirty Code Areas

After constant refactoring, I don't find any code area particularly dirty. Of course, that does not mean there is no room for improvement. That being said, I would of liked to have cleaner and more scalable code by using class-based views (CBV) instead of function-based views (FBV). Sadly I was not able to switch from FBV to CBV inside the given time frame.

## Author

Samuel O.

smohuff@gmail.com