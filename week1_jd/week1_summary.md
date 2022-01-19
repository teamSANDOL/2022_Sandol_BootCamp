# Github

## 깃허브 사용법

1. 로컬 저장소를 깃 저장소로 초기화 한다.
2. 로컬 저장소에서 파일을 생성, 수정을 한다.
3. 파일들을 stage 영역에 올린다.
4. stage 영역에 올린 것을 커밋 메시지를 작성하면서 커밋을 기록한다.
5. 커밋 내역을 원격 저장에 push 한다.

## 명령어

- git init : 로컬 저장소를 깃 저장소로 초기화
- git add 파일이름 : 생성, 수정한 파일을 stage 영역에 올림
- git commit -m "커밋 메시지" : add 명령어 이후 커밋 메시지를 작성하면서 커밋을 기록
- git log : 커밋 내역을 확인
- git remote : 원격 저장소 목록 확인
- git remote add origin <url> : url주소(원격 저장소)를 origin 이름으로 remote 생성
- git push origin 브랜치이름 : 브랜치를 origin(원격 저장소)으로 push
- git branch 브랜치이름 : 브랜치 생성
- git chekcout 브랜치이름 : 해당 브랜치로 이동
- git pull origin 브랜치이름 : origin(원격 저장소) 브랜치의 커밋 내역을 로컬 저장소로 가져옴
