# EasyBroker Software Developer Intern Website Project

This website connects to the public staging area API of EasyBroker:

> https://api.stagingeb.com/playground

It consists of 2 main pages, the properties list, and the property page.

## Properties List

- Shows 15 properties per page.
- Includes pagination links as to navigate to any page.
- Only includes published properties.
- Each item in the list displays its public ID, title, property type, location and a image thumbnail.

## Property Page

When a user clicks on a property in the list, they will be lead into that property detailed information page using the properties/{property_id} endpoint.

The page displays the following information:

- Public ID.
- Title.
- Description.
- A slideshow with the first 3 photos.
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
source venv\bin\activate
```
Now it is time to install all the project dependencies:

```bash
pip install -r requirements.txt
```

As simple as that! You are now ready to fire the rpoject up.

## Usage

If you just followed the installation steps, you should have your virtual environemnt active right now.

If not, open a terminal in the folder where the project and the virtual environment resides, you can activate it like this:

```bash
source venv\bin\activate
```
Now we should run the server hosting the website:

```bash
python manage.py runserver
```

After running the server you should see a line like this one:

```bash
Starting development server at http://127.0.0.1:8000/
```

Type that url in your prefered web browser, and voila! You are now ready to navigate the website.

## Notes

This project has been built using the "Divide and Conquer" method. By dividing this task (project) into small, bite size tasks, and conquering each one by one, it was manageable to complete all the requirements of the project.

Because of the desire to complete all basic requirements within the narrow time constraints, the testing code was not created/implemented until the end of the development cycle. Having a more generous and relaxed time constraint, I would have chosen a "Test-driven Development" style.

### Hardest Thing To Solve

Every step of the way was a very exciting and interesting challenge to overcome. There were many of these challenges I was very happy to be able to complete!

But I think the issue that proved to be the hardest to overcome was actually one of the simplest and silliest. When trying to complete a succesfull POST request with the contact form, EBs API would just not accept it and return a "422" code. And the error message attached to it was not very helpful. Needless to say, I ended up banging my head against the wall with this issue for hours, just to end up changing the parameters name from "data" to "json" in the off-chance that this could be the issue, me trying to pass the correct argument through the wrong parameter. And there we go, code "200", success!

Without a doubt a bittersweet moment. I was happy that the problem had been resolved! I was pretty sad I wasted hours of the project in such a silly error. But hey! You live, you learn.

### If Able To Finish

Originally it was my desire to use class-based views instead of function-based views with Django. Because of the time constraint, I decided to start the project with function-based views, and first complete the following:

#### Priority:

- Meet the project requirements with function-based views.
- Refactor my code as to achieve clean and efficient code
- Create some decent test coverage
- Create some decent documentation.

If able to complete this priority list, and still have time available:

#### Nice to have:

- Convert the function-based views into class-based views.
- Give the HTML and CSS code some love, just to make things a bit prettier.

The good news are, the priority list was completed inside the time frame!

The bad news on the other hand... Not much time was left, so I decided to spend the little time left refactoring the code some more, and doing some minor visual upgrades to the website.

### Dirty Code Areas

After constant refactoring, I don't particularly find any code area particularly dirty. That being said, I would of liked to have cleaner and more scalable code by using class-based views (CBV) instead of function-based views (FBV). Sadly I was not able to switch from FBV to CBV inside the given time frame.

## Author

Samuel Martinez Odriozola

smohuff@gmail.com