# Generated by Django 3.1 on 2021-11-16 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestor_topics', '0002_auto_20211116_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topic',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topic',
            name='tipo_valor',
            field=models.CharField(choices=[('charfield', 'Charfield'), ('decimalfield', 'Decimalfield'), ('floatfield', 'Floatfield'), ('integerfield', 'Integerfield'), ('positiveintegerfield', 'Positiveintegerfield'), ('bigintegerfield', 'Bigintegerfield'), ('smallintegerfield', 'Smallintegerfield'), ('booleanfield', 'Booleanfield')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='usuario_en_publish',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ValorTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_created=True)),
                ('charfield', models.CharField(blank=True, max_length=5000, null=True)),
                ('decimalfield', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('floatfield', models.FloatField(blank=True, null=True)),
                ('integerfield', models.IntegerField(blank=True, null=True)),
                ('positiveintegerfield', models.PositiveIntegerField(blank=True, null=True)),
                ('bigintegerfield', models.BigIntegerField(blank=True, null=True)),
                ('smallintegerfield', models.SmallIntegerField(blank=True, null=True)),
                ('booleanfield', models.BooleanField(blank=True, null=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valores', to='gestor_topics.topic')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valores_publicados', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Valor de Topic',
                'verbose_name_plural': 'Valores de Topics',
                'ordering': ('-creado',),
            },
        ),
    ]