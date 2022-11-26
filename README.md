# FooriendServer


git에서 데이터베이스와 가상환경까지 관리하지는 않도록 설정하는 것이 일반적이라
여기서 고대로 pull 하셔도 파이참을 실행해서 추가 작업을 하셔야 하기 때문에!

그냥 서버 작업 폴더를 통채로 구글드라이브에 올려두었습니다

https://drive.google.com/file/d/1sHom_Hb8dch0ozhMNK4l7-TJEur-d2dn/view?usp=share_link
여기서 다운로드 받으신 뒤에

대충 C에 풀어두시고 (경로에 한글만 없다면 어디든 ok)
manage.py 파일이 있는 FooriendServer폴더의 위치에서 cmd를 실행해서

pip install django
pip install Pillow  
하면 필요한 프로그램 설치는 됐습니다
(혹시 제가 누락한 것이 있다면 어떡하지 경고창에 뜨는 걸 설치해주시면 됩니다.. 잘 모르겠으면 캡쳐해서 연락주십쇼 미리 죄송합니다.)
그 뒤로는
venv\Scripts\activate.bat
python manage.py runserver
이 두 명령어만 실행하면 됩니다.
설치는 한번만 하시면 되고
서버를 다시 열고 싶으면 
 # FooriendServer폴더 위치에서 cmd 실행 > venv어쩌구 명령어 복붙 > 런서버 명령어 복붙
이렇게 하시면 됩니다.
