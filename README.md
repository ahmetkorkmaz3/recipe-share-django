# Yemek Tarifi Paylaşım Web Uygulaması
Django Project.
 ## Kurulum
 Bilgisayarınızda python3 ve pip kurulu olması gerekmektedir. Kurulu değilse ;
```bash
	sudo apt install python3
	sudo apt install python3-pip
```
diyerek kurulumları yapabilirsiniz.
Sonrasında virtualenv kurulması gerekiyor.
```bash
	pip install virtualenv
```
Kurulumlar sorunsuz bir şekilde yapıldı ise virtualenv için dosya oluşturarak virtualenv başlatıyoruz.
```bash
	mkdir venv/
	cd venv/
	virtualenv -p python3 env
```
Virtualenv başlatıldıktan sonra aktif etmemiz gerekiyor.
```bash
	source venv/env/bin/activate
```

Virtualenv aktif edildikten sonra projeyi lokalinize çekerek projeyi çalışır duruma getirebiliriz. Proje dosyasının konumuna giderek (requirements.txt dosyasının bulunduğu dizin):

```bash
	pip install -r requirements.txt
```
kodunu çalıştırmanız gerekiyor. Gereksinimler kuruluyor...
Gereksinimler kurulduktan sonra:
```bash
	cd hipo/
```
diyerek bir dizin ileriye gitmeniz gerekiyor. Burada manage.py ile işlemleri gerçekleştireceğiz.
```bash
	python manage.py makemigrations
	python manage.py migrate
```
Admin paneli için kullanıcı oluşturmak isterseniz :
```bash
	python manage.py createsuperuser
```

Sırada projeyi çalıştırmak kaldı :muscle:
```bash
	python manage.py runserver
```
Proje https://127.0.0.1:8000 adresinde çalışır durumda :smile: :dancer:
