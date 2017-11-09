### What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?

1. Takes in a file with text, reads it, cleans it, converts to a dictionary.
1. Choose random word based on stochastic sampling.
1. Combine random words into a sentence.
1. Returns sentence.
1. Uses a Flask server to display the sentence
1. Shipped to Heroku to view on the web.
1. Connected to a PostGres database.

I am in progress of refactoring the application into Classes and modules.

### Are the names of files, modules, functions, and variables appropriate and accurate?

Most are accurately named, I can certainly improve some of the names.

### Would a new programmer be able to understand the names without too much contextual knowledge?

I think I should be more specific. I tend to not use vowels, but perhaps this can get confusing. I also have a line of list comprehension that is really hard to understand. I tried refactoring it, but did not get the same results.

### What are the scopes of variables and are they appropriate for their use case?

Most if not all variables are in the local scope. I do have 
### If there are global variables, why are they needed?
