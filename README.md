# NEWS API

# Author
Francis Mwangi Maina [chui]

# Description
This project is about creating  an application that will help one list and preview news articles from various sources.   

# User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
 See various news sources

 Select the ones they prefer

 See the image,description and time the news article was created
 
Click on an article and read it fully fron the news

## SetUp/Installation Requirements
python

pip

virtualvenv

# Cloning
In your terminal
 $ git clone https://github.com/mainafrancis/news-api/
$ cd news-api

# Running the Application
 Creating the virtual environment
$ python3.8 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python

  # Setting up the API key
   To be able to gather article info from the News API you will need an API Key.

  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it:

          export NEWS_API_KEY='<Your-Api-Key>'
          python3.8 manage.py server

  * Insert the API Key you received from News Api where <Your-Api-Key> is

 ### Testing the Application
 
   To run the test for the class files:
    $ python3.8 manage.py tests

 ### Technologies Used
 
     python(flask)
     

 ### License
 
    MIT License

Copyright (c) 2022 [Francis Mwangi Maina] [c.h.u.i]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




