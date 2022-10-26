# Generated by Django 4.1.2 on 2022-10-26 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0002_conta_deposite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.CharField(max_length=250)),
                ('account_type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('branch_code', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ClientManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.account')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.account')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.account')),
            ],
        ),
        migrations.RemoveField(
            model_name='deposite',
            name='conta',
        ),
        migrations.DeleteModel(
            name='Conta',
        ),
        migrations.DeleteModel(
            name='Deposite',
        ),
        migrations.AddField(
            model_name='bank',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.branch'),
        ),
        migrations.AddField(
            model_name='account',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.bank'),
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.client'),
        ),
    ]
