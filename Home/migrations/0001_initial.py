# Generated by Django 3.0.8 on 2020-07-31 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CodeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_group_name', models.CharField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Code Group',
                'verbose_name_plural': 'Code Groups',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(max_length=100, unique=True)),
                ('data_rate', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Networks',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_setting', models.CharField(blank=True, default='Setting_1', max_length=100)),
                ('customer_rate', models.FloatField(blank=True, default=15)),
                ('agent_rate', models.FloatField(blank=True, default=20)),
                ('services_note', models.TextField(blank=True, default='services note')),
                ('minimum_withdrawal', models.IntegerField(blank=True, default=100)),
                ('minimum_airtime', models.IntegerField(blank=True, default=100)),
                ('minimum_data', models.IntegerField(blank=True, default=100)),
                ('call_contact', models.CharField(blank=True, max_length=13)),
                ('whatsapp_contact', models.CharField(blank=True, max_length=13)),
                ('email_contact', models.EmailField(blank=True, max_length=254)),
                ('how_to', models.TextField(blank=True)),
                ('faq', models.TextField(blank=True)),
                ('about_us', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Site Setting',
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_balance', models.FloatField(blank=True)),
                ('wallet_status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wallet',
                'verbose_name_plural': 'Wallets',
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resolution',
                'verbose_name_plural': 'Resolutions',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Resolution')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(max_length=100, unique=True)),
                ('account_type', models.CharField(choices=[('Agent', 'Agent'), ('User', 'User'), ('Not Specified', 'Not Specified')], default='Not Specified', max_length=20)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT - Abuja', 'FCT - Abuja'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], default='Kano', max_length=15)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(blank=True, default='---- --- ----', max_length=12)),
                ('account_type_change_counter', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_slug', models.CharField(max_length=100, unique=True)),
                ('verification_code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('recipient', models.CharField(default='08012345678', max_length=15)),
                ('description', models.CharField(default='Order', max_length=100)),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='No Description')),
                ('amount', models.CharField(blank=True, max_length=10)),
                ('charges', models.CharField(blank=True, max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(blank=True, default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('amount', models.FloatField(default=100.0)),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
                ('code_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.CodeGroup')),
            ],
            options={
                'verbose_name': 'Code',
                'verbose_name_plural': 'Codes',
            },
        ),
    ]
