# My very first attempt on API
import requests 
#a very useful package for creating your own RESTful API
#Though this does not have real data and url, 
#this shows the basic structure of a RESTful API


#to help out fill in the parameters later, we create a function called _url
def _url(path):
	return 'https://todo.example.com' + path

def get_tasks():
	return requests.get(_url('/tasks/'))


def describe_task(task_id):
	return requests.get(_url('/tasks/{:d}/'.format(task_id)))


def add_task(summary , description=""):
	return requests.post(_url('/tasks/{:d}/'), json={ 'summary':summary , 'description':description})

def task_done(task_id):
	return requests.delete(_url('/tasks/{:d}/'.format(task_id)))


def update_task(task_id , summary , description):
	#It is better to have explicit parameters when declaring your functions
	#as compared to having them in a dictionary right away
	url = _url('/tasks/{:d}/'.format(task_id))
	return requests.put(url, json={'summary':summary , 'description':description})
