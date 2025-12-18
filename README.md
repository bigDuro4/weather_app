# weather_app

This project was something that didnt take that much time but there was just a couple of things to do regarding the syntax. What I found interesting was how easy it was to get the api from the weather app free of charge and then the only other issue was having to Ctrl+Shift+S to manual save every run

I didnt utilize the Zipcode number so it's important to note that you'll need to use unique names such as 'Hackettstown' if you live in Washington. The guy I researched for this lived in Houston so he didnt feel the need to use zipcode

The requests library is a fairly popular way to inteact with web services, in this case our API. This tool makes it so one could just input the url in order to scrape the data from the site itself. This was installed in the command window using pip

The apps function is having the user input their city as a string, once this occurs requests lib then fetches the data from the openweathermap url using the api key that was introduced under requests

JavaScript Object Notation (json) is then used to store and exchange the websites data and bring it into the app in the form of an array. Its important to note that the array itself is just raw information that doesnt have that much specificity so whats really important is cloud condition and temperature

