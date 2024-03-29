# Generated by Django 5.0.2 on 2024-02-11 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_type', models.CharField(choices=[('CALL', 'Call'), ('PUT', 'Put')], help_text='The type of the option (Call or Put)', max_length=4)),
                ('strike_price', models.DecimalField(decimal_places=2, help_text='Strike price of the option', max_digits=10)),
                ('expiration_date', models.DateField(help_text='Expiration date of the option')),
                ('underlying_price', models.DecimalField(decimal_places=2, help_text='Current price of the underlying asset', max_digits=10)),
                ('volatility', models.DecimalField(decimal_places=4, help_text='Implied volatility of the underlying asset', max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, help_text='Risk-free interest rate', max_digits=5)),
                ('dividend_yield', models.DecimalField(decimal_places=2, default=0, help_text='Dividend yield of the underlying asset (if any)', max_digits=5)),
                ('delta', models.DecimalField(blank=True, decimal_places=4, help_text='Delta', max_digits=10, null=True)),
                ('gamma', models.DecimalField(blank=True, decimal_places=4, help_text='Gamma', max_digits=10, null=True)),
                ('theta', models.DecimalField(blank=True, decimal_places=4, help_text='Theta', max_digits=10, null=True)),
                ('vega', models.DecimalField(blank=True, decimal_places=4, help_text='Vega', max_digits=10, null=True)),
                ('rho', models.DecimalField(blank=True, decimal_places=4, help_text='Rho', max_digits=10, null=True)),
            ],
        ),
    ]
