%~d0
cd %~dp0
cd ../../

rem first time
rem python manage.py syncdb
rem python manage.py convert_to_south gmc
rem python manage.py schemamigration gmc --init


rem after changed models
rem following command will collect changes from last migration, so must initial if never init
rem the changes will collected in <app>/migrations
python manage.py schemamigration <appName> --auto

rem following command will apply all changes in <app>/migrations
python manage.py migrate <appName>