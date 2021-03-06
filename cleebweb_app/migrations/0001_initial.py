# Generated by Django 4.0.5 on 2022-06-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatchLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('legion_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('win_lose', models.BooleanField(choices=[(False, 'LOSE'), (True, 'WIN')], default=True)),
                ('attack_target', models.CharField(max_length=100)),
                ('debuff_target', models.CharField(max_length=100)),
                ('front_type', models.BooleanField(choices=[(False, '特殊'), (True, '通常')], default=True)),
                ('absence', models.CharField(max_length=150)),
                ('detail', models.TextField()),
            ],
        ),
    ]
