# Generated by Django 4.0.6 on 2023-01-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220831_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='service_type',
            field=models.CharField(choices=[('Graphic Designing', 'Graphic Designing'), ('Web development', 'Web development'), ('Marketing', 'Marketing'), ('SEO', 'SEO'), ('Tech solutions', 'Tech solutions'), ('Data Analysis', 'Data Analysis')], max_length=100),
        ),
    ]
