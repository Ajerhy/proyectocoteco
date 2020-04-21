from django.contrib import admin

"""
from django.contrib.auth.admin import UserAdmin

from apps.usuarios.models import Usuario

from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ManyToManyWidget


class ImportExportUsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
        import_id_fields = ('usuario',)
        fields = ['id','usuario','email', 'is_active','is_superuser', 'is_staff','password']
#'nombre','apellido',

class PersonalizadaUsuarioAdmin(UserAdmin,ImportExportModelAdmin):
    resource_class = ImportExportUsuarioResource

    add_fieldsets = (
        (None, {
            'fields': ('usuario', 'password1', 'password2'),
        }),)
    list_display = ('id','usuario', 'email','roles' , 'is_active','is_superuser', 'is_staff','last_login')
    # 'password',
    search_fields = ('usuario',)
    ordering = ('usuario',)
    list_filter = ('is_superuser',)
    filter_horizontal = ("groups", "user_permissions")
    #fieldsets = ()
    fieldsets = (
        ('Usuario', {'fields': ('usuario', 'password')}),
        ('Persona Informacion', {'fields': ('nombre',
                                     'apellido',
                                     'email',
                                     'roles',
                                     'perfil_img',
                                    'observaciones'
                                     )}),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions')}),
    )


#admin.site.register(Usuario, PersonalizadaUsuarioAdmin)
"""