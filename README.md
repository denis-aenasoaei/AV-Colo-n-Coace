# AV-Colo-n-Coace

## Team: ##
1. Aenășoaei Denis - Data Preparation
2. Balan Maria - Data Preparation
3. Lupancu Camelia - Dialogue
4. Oica Andra - Interface
5. Plătică Alexandru-Gabriel - Dialogue
6. Volosincu Bogdan - Speech to text



It takes a lot of time to plan a vacation. From manually searching for hotels to booking rooms and searching for tourist attractions around the area. It’s time consuming, so we have thought of a solution. Colo-n coace aims to help you discover Romania from a new perspective: you only interact with our application by inputting the destination along with the time period and it will do the rest. According to your preferences, it will search for hotels perfectly tailored to your needs, book rooms for you or your family and help you be more relaxed in exploring the secrets of Romania.


## Course Page: ##
https://sites.google.com/view/virtualassistants-fii/project-resources

## Project Google Drive ##
https://drive.google.com/drive/folders/1KQ-z0Htn-Vm3sZRbpU-XRVCLpucg4VkK

## Steps to get your local project working ##
Preparing virtual environment (Once)
```
python -m pip install virtualenv==20.13.1
python -m virtualenv cc
```
Activating it on Mac OS / Linux (Each time, before running project)
```
source cc/Scripts/activate
```
Windows (Each time, before running project)
```
cc/Scripts/activate
```
To deactivate it use
```
deactivate
```

Install required python libraries <!-- Add new libraries to the 'req.txt' gradually -->
```
python -m pip install -r req.txt
```

Run Django server locally at *http://127.0.0.1:8000/*
```
python manage.py runserver
```
<!-- python manage.py migrate -->