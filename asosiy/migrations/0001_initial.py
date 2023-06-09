# Generated by Django 4.1.5 on 2023-04-05 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('davlat', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='')),
                ('prezident', models.CharField(max_length=50)),
                ('coach', models.CharField(max_length=50)),
                ('yili', models.DateField()),
                ('eng_qim_tr', models.CharField(max_length=50)),
                ('eng_qim_sotuv', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hozirgi_mavsum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hozirgi_mavsum', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('t_yil', models.DateField()),
                ('tr_narxi', models.IntegerField()),
                ('millat', models.CharField(max_length=50)),
                ('pozitsiya', models.CharField(choices=[('Forward', 'Forward'), ('Midfielder', 'Midfielder'), ('Defender', 'Defender'), ('Keeper', 'Keeper')], max_length=50)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='futbolchilari', to='asosiy.club')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narxi', models.IntegerField()),
                ('tax_narx', models.IntegerField()),
                ('mavsum', models.CharField(max_length=50)),
                ('eski', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sotuvlari', to='asosiy.club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.player')),
                ('yangi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sotib_olganlar', to='asosiy.club')),
            ],
        ),
    ]
