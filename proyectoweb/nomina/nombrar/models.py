from django.db import models

# Creacion modelo ccargo.
class Cargo(models.Model):
    #campos
    descripcion = models.CharField(max_length=100, blank=False, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    #Definimos las clase meta
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['id']
    def __str__(self):
        return self.descripcion

# Creacion modelo departamento.
class Departamento(models.Model):
    #campos
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    #Definimos las clase meta
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['id']
    def __str__(self):
        return self.descripcion

# Creacion modelo Empleados.
class Empleado(models.Model):
    #campos
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    #Aqui se relaciona el modelo empleado con los modelos secundarios
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)

    #Definimos las clase meta
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']
    def __str__(self):
        return self.nombre,self.cedula,self.cargo,self.departamento,self.sueldo
