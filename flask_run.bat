@ECHO OFF

call %~d0%~p0app\development\Scripts\activate

cd %~d0%~p0

set FLASK_DEBUG=1

set FLASK_APP=app_main/

set FLASK_ENV=development

flask run