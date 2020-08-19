# The SHIELD
We are team of engineers working towards the goal of mitigating online child abuse using NLP by predicting child grooming pattern.

*Warning few examples might contain explicit language. <br />
The Flask webserver was built using the Flask tutorial.* <br />

*Remember to replace Pusher ID tags with your own.*

### Results:

#### Image output of website

![Image of project](https://github.com/snehkothari28/The_SHIELD/blob/master/media/whole%20screenshot.jpeg)

#### GIF output of website

![Output sample](https://github.com/snehkothari28/The_SHIELD/blob/master/media/sample.gif)


### Running the chat server


#### Run the Flask app

- CD to the Flask folder - api:

```
    $ cd api
```

- Create a virtual environment:

```
python3 -m venv env
```

- Activate the virtual environment:

```
  source env/bin/activate
```

On windows? Activate it with the below:

```
  source env/Scripts/activate
```

- Install the dependencies:

```
pip install -r requirements.txt
```

- Download NLTK corpora:

$ python -m textblob.download_corpora lite

- Finally run the app:

```
 flask run
```

Check the URL where Flask is running - [http://localhost:5000](http://localhost:5000). You will get a text "Pong!".

#### Run the Vue app

Open a new terminal window, then cd into the repo folder

Install dependencies:

```
npm install
```

Then run the app:

```
    $ npm run serve
```

## Built With

- [Flask](http://flask.pocoo.org/) - A microframework for Python
- [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
- [Vue.js](https://vuejs.org/) - A JavaScript Framework for building User Interfaces
