from .base import *


env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env'))                                # os : 경로 관련 모듈(base_dir와 .env의 경로)

while True:
    line = local_env.readline()                                                 # .env에 있는 파일을 =를 기준으로 왼쪽을 key, 오른쪽을 value로 집어넣기
    if not line:                                                                #dict에 저장을 하다가 더이상 읽을 파일이 없다면 line은 NONE이 된다.
        break                                                                   #더이상 읽을 파일이 없어 NONE이 되므로 break.
    line = line.replace('\n', '')                                               #
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!                      시크릿키
SECRET_KEY = env_list['SECRET_KEY']                                             # 조건만 맞으면 .env에 있는 secret_key값을 들고옴

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# 데이터베이스 세팅
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
