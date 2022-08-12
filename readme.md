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

Make sure you have Python installed:

```bash
python3 --version
```

If not, install with:

```bash
sudo apt-get install python3
```

It is highly recommended you create a virtual environment and activate it before the next steps:

```bash
python3 -m venv venv
source venv\bin\activate
```
Now it is time to install all the project dependencies:

```bash
pip install -r requirements.txt
```

As simple as that! You are now ready now to fire the rpoject up.

## Usage



## Notes



### Hardest Thing To Solve



### Dirty Code Areas



### If Able To Finish



## Author

Samuel Martinez Odriozola

smohuff@gmail.com