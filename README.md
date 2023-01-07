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
