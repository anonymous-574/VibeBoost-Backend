# Generated by Django 5.1 on 2024-10-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_input'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Input_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Input',
        ),
        migrations.DeleteModel(
            name='React',
        ),
    ]