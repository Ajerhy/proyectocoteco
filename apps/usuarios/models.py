
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import time

from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuarios.templatetags.utils import ROLES

class EstadoModelo(models.Model):
    descripcion = models.TextField('descripcion', blank=True, null=True)
    # id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True,null=False, blank=False, editable=False)
    direccion_ip = models.GenericIPAddressField(blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)  # , blank=True, null=True)
    modificacion = models.DateTimeField(auto_now=True)  # , blank=True, null=True)

    estado = models.BooleanField(default=True)
    # uc = models.ForeignKey(Usuario,on_delete=models.CASCADE)#usuario creo
    uc = models.IntegerField(blank=True, null=True)
    # um =models.ForeignKey(User,on_delete=models.CASCADE)#usuario modifico
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
"""
class UserManager(BaseUserManager):
    def create_user(self, usuario, email, password):
        if not email:
            raise ValueError('El Email o Correo Electronico  es obligatorio')
        user = self.model(email=self.normalize_email(email))
        user.usuario = usuario
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, password):
        user = self.create_user(usuario, email, password)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField('Usuario', max_length=15, unique=True)
    email = models.EmailField('Correo Electronico', max_length=50, unique=True)
    observaciones = models.TextField(blank=True, null=True)
    nombre = models.CharField('Nombres', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    perfil_img = models.ImageField(verbose_name='Imagen de Perfil', upload_to='images/%Y/%m/%d/', blank=True, null=True)
    roles = models.CharField(max_length=2,choices=ROLES, default='2')
    #
    #direccion_ip = models.GenericIPAddressField(blank=True, null=True)
    #uc = models.IntegerField(blank=True, null=True)
    #um = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email', ]

    def get_short_name(self):
        return self.usuario

    def get_full_name(self):
        return (self.usuario)

    def has_perm(self, perm, obj=None):
        "¿El usuario cuenta con los permisos en especificos?"
        return True

    def has_module_perms(self, app_label):
        "¿El usuario cuenta con los permisos para ver una app en especificos?"
        return True

    def __unicode__(self):
        return "%s" % (self.usuario)

    #        return "%s %s" % (self.usuario, self.apellido)

    def __str__(self):
        return "%s" % (self.usuario)

    #        return "%s %s" % (self.usuario, self.apellido)

    class Meta:
        ordering = ['-is_active']
        verbose_name_plural = "Usuarios"

#Token de Autenticacion
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
"""