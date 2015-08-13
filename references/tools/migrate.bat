%~d0
cd %~dp0
cd ../../
rem first time
python manage.py syncdb
rem python manage.py convert_to_south gmc
python manage.py schemamigration gmc --auto
python manage.py migrate