from django.db import models

# Crear la tabla de empleados 
class Empleado(models.Model):
    cedula = models.ForeignKey('Cedula', models.DO_NOTHING, db_column='cedula', primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
# Crear la tabla Servivios
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    

# Crear la tabla de registros 
class Registro(models.Model):
    id_registro = models.AutoField(primary_key=True)
    cedula = models.ForeignKey('Cedula', models.DO_NOTHING, db_column='cedula')
    id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='id_servicio')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.id_registro    
   