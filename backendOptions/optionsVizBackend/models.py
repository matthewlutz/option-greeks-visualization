#this class sets up the model for the options data

from django.db import models

class OptionsModel(models.Model):
    Option_type = (
        ('CALL', 'Call'),
        ('PUT', 'Put'),
    )

    option_type = models.CharField(max_length=4, choices=Option_type, help_text="The type of the option (Call or Put)")
    strike_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Strike price of the option")
    expiration_date = models.DateField(help_text="Expiration date of the option")
    underlying_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Current price of the underlying asset")
    volatility = models.DecimalField(max_digits=10, decimal_places=4, help_text="Implied volatility of the underlying asset")
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Risk-free interest rate")
    dividend_yield = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Dividend yield of the underlying asset (if any)")

    # Greeks
    delta = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="Delta")
    gamma = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="Gamma")
    theta = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="Theta")
    vega = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="Vega")
    rho = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="Rho")

    #useful for debugging
    def __str__(self):
        return f"{self.get_option_type_display()} - Strike: {self.strike_price}, Exp: {self.expiration_date}"