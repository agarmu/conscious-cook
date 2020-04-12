<h1 align = "center">The Conscious Cook</h1>
<h4 align = "center"> Making the earth cleaner, one meal at a time!</h4>

## Inspiration
The inspiration for this chrome extension was the fact that people are very unaware about the amount of carbon their food releases on a daily basis. We wanted to create a simple way for people to become aware of the carbon emissions for their food, and also make suggestions on how to become more ecologically mindful when it comes to choosing ingredients.

## What It Does
Our project reads the recipe on the screen and picks out the ingredients that emit a high amount of carbon per calorie. We suggest alternatives to that ingredient based on its food class and carbon emission data.

## How We Built it
We used our chrome extension to search our page for an ingredients section, and then we took in the data  of each ingredient, including the amount, and passed it into our database where we search for viable alternatives for that ingredient. We created a Flask API to communicate between our backend and frontend. Our extension takes in the Carbon emission data of the ingredient and suggests a food that is similar but with lower carbon emissions so that users can try to be more mindful of where their food comes from.


## Challenges We Ran Into
A big challenge we encountered during the making of this project was the database behind the backend of our project. Mukul tried configuring the database with Selenium, however, the database he was referring to for the info involved a captcha which prevented Selenium fro working cohesively with the APIs of Jainil. We solved this issue by inputting the data into a CSV and formatting it into a json file which Jainil could use. We ran into a lot of issues with the selection of ingredients. Parsing the site's ingredients and picking out key words that we could use to search in our database was both tedious and difficult. We also struggled putting together the Popper for the extension, so we switched to an alert in order to display our suggestions.

## Accomplishments We're Proud of
We solved the database issue by manually inputting the data into a google sheets, allowing us to collaborate together. This data was exported as a CSV file and converted to json file which we could use directly in our back-end processing. This intuitive approach to data helped us create an accurate and reliable database.

## What We Learned
We learned that it is very hard to come up with a working solution to a problem in just 24 hours. We also learned that many websites are not machine-friendly and the format styling of a majority are vastly different from one another. Conscious Cook was first supposed to be an extension where we could look up alternate recipes in a popup window, but we ran out of time so we just implemented a suggestion window to display the suggestions to each ingredient.

## What's Next for Conscious Cook
We aim to improve Conscious Cook by working to show more alternates to certain ingredients based on the recipe in our extension, so we not only tell people about their unhealthy eating habits but enable them to stay healthier.

#### [See our devpost submission and vote for us!](https://devpost.com/software/conscious-cook-w4siby)
