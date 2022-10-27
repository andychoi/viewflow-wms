# WMS
A Django-based workflow management system using viewflow \
Installation \
--Dependencies \
i Python3 \
--steps \
i. clone repo \
```
git clone https://github.com/andychoi/viewflow-wms.git

```
ii. setup virtual environment 'https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/' \
    python -m venv .venv
    source .venv/bin/activate
iii. initialize virtual environment and install requirements from requirements.txt (
    pip install -r requirements.txt
iv. python manage.py makemigrations
v.  python manage.py migrate

    python manage.py createsuperuser
    
vi. run server from base directory: 

    python manage.py runserver 0.0.0.0:8000


