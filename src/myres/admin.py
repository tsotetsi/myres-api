from django.contrib import admin

from myres.models import User, FlatType, ResidenceType, Residence, ResidenceUser, Flat, ResidenceFlat, Student, \
                         Application, Organization, OrganizationResidence, OrganizationUser


@admin.register(FlatType)
class FlatTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ResidenceType)
class ResidenceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone_number',)


@admin.register(OrganizationResidence)
class OrganizationResidenceAdmin(admin.ModelAdmin):
    list_display = ('organization', 'residence',)
    list_filter = ('organization__name',)


@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'capacity', 'email', 'phone_number',)
    list_filter = ('type',)


@admin.register(ResidenceUser)
class ResidenceUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ResidenceFlat)
class ResidenceFlatAdmin(admin.ModelAdmin):
    list_display = ('residence', 'flat',)
    list_filter = ('residence__name',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('number', 'type', 'info',)
    list_filter = ('type__name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('number', 'user', 'residence',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('status', 'applicant', 'flat', 'created',)
    list_filter = ('status', 'created',)


#admin.site.site_header = "myres.co.za backend-admin"
