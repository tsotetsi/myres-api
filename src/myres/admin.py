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
    pass


@admin.register(OrganizationResidence)
class OrganizationResidenceAdmin(admin.ModelAdmin):
    pass


@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    pass


@admin.register(ResidenceUser)
class ResidenceUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ResidenceFlat)
class ResidenceFlatAdmin(admin.ModelAdmin):
    pass


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "myres.co.za backend-admin"
