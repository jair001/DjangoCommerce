### Django ecommerce

## install
1.- Activar entorno virtual
2.- Instalar dependencias del proyecto
3.- Crear proyecto Django, ejecutar

### MODELS - ORM 

SQL
select * from item where stock=True

ItemModel.objects.all()
ItemModel.objects.filter(stock=True)

create table item

##MIGRACIONES
-MAKEMIGRATIONS:
'python manage.py makemigrations <name-app>'

-MIGRATE:
'python manage.py migrate <name-app>'