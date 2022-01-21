## git 사용법   
### 초기설정   
    $ git config --global user.name "아이디"   
    $ git config --global user.email "이메일주소"    
### 온라인 저장소 만들기   
    repositories -> new   
    새 폴더 생성 -> git bash로 열기   
    $ echo "README에 들어갈 내용" >> README.md   
    $ git init   
    $ git add README.md   
    $ git commit -m "메세지"   
    $ git branch -M main   
    $ git remote add origin https://github.com/아이디/저장소이름.git   
    $ git push -u origin main   

## git 명령어   
    $ git init: 현재 폴더를 로컬 저장소로 지정   
    $ git status: 로컬 저장소의 상태 확인   
    $ git add .: 작업 공간의 파일들을 준비 영역에 추가   
    $ git commit -m "메세지": 로컬 저장소에 최종 저장한다   
    $ git branch -M main: 기본 branch 생성   
    $ git remote add origin(별칭) Git_Repo_주소: 로컬 저장소와 원격 저장소 연결   
    $ git remote -v: 별칭 내역을 확인   
    $ git push -u origin main: 로컬 저장소의 파일들을 원격 저장소로 옮김   