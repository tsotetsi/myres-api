# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 08:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import myres.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=32)),
                ('mobile_number', models.CharField(max_length=16, validators=[myres.validators.E164Validator])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['email'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('NEW', 'NEW'), ('REVIEW', 'REVIEW'), ('APPROVED', 'APPROVED'), ('DECLINED', 'DECLINED'), ('DELETED', 'DELETED')], default='NEW', max_length=100, no_check_for_status=True)),
            ],
            options={
                'ordering': ['created', 'flat', 'status'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('info', models.TextField(verbose_name='Additional [optional] information')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, validators=[myres.validators.E164Validator])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationResidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('capacity', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, validators=[myres.validators.E164Validator])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResidenceFlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Flat')),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Residence')),
            ],
        ),
        migrations.CreateModel(
            name='ResidenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResidenceUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Residence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('number', models.CharField(max_length=54, verbose_name='Student Number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='residence',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.ResidenceType'),
        ),
        migrations.AddField(
            model_name='organizationresidence',
            name='residence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Residence'),
        ),
        migrations.AddField(
            model_name='flat',
            name='residence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Residence'),
        ),
        migrations.AddField(
            model_name='flat',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.FlatType'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myres.Student'),
        ),
        migrations.AddField(
            model_name='application',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myres.Flat'),
        ),
        migrations.AddField(
            model_name='application',
            name='residence',
            field=models.ManyToManyField(to='myres.Residence'),
        ),
        migrations.AlterUniqueTogether(
            name='residenceuser',
            unique_together=set([('user', 'residence')]),
        ),
        migrations.AlterUniqueTogether(
            name='residenceflat',
            unique_together=set([('residence', 'flat')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationuser',
            unique_together=set([('organization', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationresidence',
            unique_together=set([('organization', 'residence')]),
        ),
    ]
