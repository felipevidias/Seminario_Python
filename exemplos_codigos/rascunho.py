from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'


from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


##import pandas as pd

##data = {'Nome': ['Ana', 'Bruno', 'Carlos'], 'Idade': [23, 25, 27]}
##df = pd.DataFrame(data)
##print(df)




