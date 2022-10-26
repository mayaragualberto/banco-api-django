# Generated by Django 4.1.2 on 2022-10-26 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0003_account_bank_branch_client_clientmanager_deposit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Saque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.conta')),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='account',
            name='client',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='branch',
        ),
        migrations.DeleteModel(
            name='ClientManager',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='withdraw',
            name='account',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='Transfer',
        ),
        migrations.DeleteModel(
            name='Withdraw',
        ),
    ]
