# GitHub

## github
GitHub: 소프트웨어 개발 프로젝트를 위한 소스코드 관리 서비스

## github 사용법
    1. 로컬 저장소를 git 저장소로 초기화한다
	2. 로컬 저장소에서 작업 파일을 수정 및 저장한다
	3. github 원격저장소 연결정보를 추가한다
	4. 파일을 commit할 branch로 이동한다
	5. 작업 파일을 stage 영역에 올린다
	6. stage 영역에 올린 파일에 대한 commit message를 입력하고 commit한다
	7. commit한 것을 원격저장소에 push한다

## 명령어
 - 디렉토리 생성 <br/>
   $ mkdir <현재 경로에 생성할 디렉토리명>
 - 디렉토리 이동 <br/>
   $ cd <이동할 하위 디렉토리명>
 - 로컬 저장소에 git 저장소로 초기화 <br/>
   $ git init
 - 원격 저장소에 GitHub 원격저장소 연결정보 추가 <br/>
   $ git remote add <이름> <주소>
 - 원격 저장소 연결조회 <br/>
   $ git remote -v
 - 해당 branch로 이동 <br/>
   $ git checkout -b <branch명>
 - 작업 파일을 stage 영역에 올림 (특정 파일만 또는 전체 파일) <br/>
   $ git add <파일명>  <br/>
   $ git add .  
 - stage 영역에 올라와있는 파일을 commit 메시지를 입력하고 commit <br/>
   $ git commmit -m "commit 설명"
 - commit한 목록 확인 <br/>
   $ git log
 - 원격 저장소에 변경사항 올리기 <br/>
   $ git push <이름> <branch명>