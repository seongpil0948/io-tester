# Structure
procedure(by role) > suite(by module) > case(by unit)
service
- io-box-front (service)
  - common (procedure) 
    - login (suite)
      - redirect to login (case)
      - redirect  to signUp
      - fail to login
  - shop (procedure)
    - login (suite)
      - wrong password (case)
      - not exist
      - success login and redirect to main
- io-box-admin

## Issues
- 각 패키지에 _main__.py 를 배치하여 각각 실행 가능하도록 하려했지만..
vscode 디버깅이 모듈 실행을 못하는 이슈로 main.py 로 대체하여 실행.
