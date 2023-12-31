# Generated by Django 4.0.6 on 2023-12-10 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='producer', to='operation.producer')),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='contract', to='operation.contract')),
            ],
        ),
        migrations.CreateModel(
            name='StatementProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='operation.product')),
                ('statement_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='statement', to='operation.statement')),
            ],
        ),
        migrations.AddField(
            model_name='statement',
            name='products',
            field=models.ManyToManyField(through='operation.StatementProduct', to='operation.product'),
        ),
    ]
