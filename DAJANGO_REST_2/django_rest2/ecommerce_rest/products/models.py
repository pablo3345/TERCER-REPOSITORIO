from itertools import product
from django.db import models
from simple_history.models import HistoricalRecords # esta libreria es para saber todo el historial del usuario (hay que instalarla en la consola)
from base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):#fijarme que hereda de BaseModel osea hereda sus carcteristicas y atributos, esta clase en español significa unidad de medida
    """Model definition for MeasureUnit."""

    # todo: Define fields here
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords(user_model="users.User", inherit=True)# registro del historial
     
     
     
    @property
    def _history_user(self):
        return self.changed_by# cada ves que usamos el historial en este caso en especial debemos usar una configuracion adicional, los dos metodos de abajo
                              #para que la aplicacion registre que usuario ha efectuado el cambio, lod dos metodos  def _history_user
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    class Meta:
        """Meta definition for MeasureUnit."""

        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description

class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""

    # todo: Define fields here
    description = models.CharField('Descripcion', max_length=50, unique=True, null=False, blank=False)

    historical = HistoricalRecords(user_model="users.User", inherit=True)
 
    @property
    def _history_user(self):
        return self.changed_by# cada ves que usamos el historial en este caso en especial debemos usar una configuracion adicional, los dos metodos de abajo
                              #para que la aplicacion registre que usuario ha efectuado el cambio, lod dos metodos  def _history_user
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'

    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description

class Indicator(BaseModel): # este modelo es si hay ofertas, si le puedo hacer un descuento del 20% un producto
    """Model definition for Indicator."""

    # todo: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0) # PositiveSmallIntegerField significa que es un entero, descount_value  en español es el valor que se va a descontar
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords(user_model="users.User", inherit=True)
 
    @property
    def _history_user(self):
        return self.changed_by# cada ves que usamos el historial en este caso en especial debemos usar una configuracion adicional, los dos metodos de abajo
                              #para que la aplicacion registre que usuario ha efectuado el cambio, lod dos metodos  def _history_user
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        """Unicode representation of Indicator."""
        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%' 

class Product(BaseModel):
    """Model definition for Product."""

    # todo: Define fields here
    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)
    
    historical = HistoricalRecords(user_model="users.User", inherit=True) 
 
    @property
    def _history_user(self):
        return self.changed_by# cada ves que usamos el historial en este caso en especial debemos usar una configuracion adicional, los dos metodos de abajo
                              #para que la aplicacion registre que usuario ha efectuado el cambio, los dos metodos  def _history_user
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
  
    
    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    '''@property
    def stock(self):
        from django.db.models import Sum
        from apps.expense_manager.models import Expense

        expenses = Expense.objects.filter(
            product=self,
            state=True
        ).aggregate(Sum('quantity'))

        return expenses'''
