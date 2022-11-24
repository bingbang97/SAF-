# final_back



### 초기 설정

```bash
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate
```



### 영화 정보 불러오기

```bash
python init.py

python manage.py migrate

python manage.py loaddata genre_data.json movie_data.json
```

