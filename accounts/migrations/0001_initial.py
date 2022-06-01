# Generated by Django 4.0.4 on 2022-06-01 02:45

from django.db import migrations, models

def populate_usertype(apps, schemaeditor):
    user_types = {
        "reader": "A subscriber to the newspaper",
        "journalist": "A staff member that creates content",
        "editor": "A staff member in charge of editing",
    }
    UserType = apps.get_model('accounts', 'UserType')
    for name, desc in user_types.items():
        user_type = UserType(name=name, description=desc)
        user_type.save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RunPython(populate_usertype)
    ]