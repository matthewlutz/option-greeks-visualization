import mibian
import numpy as np

def calculate_greeks(option_type, underlying_price, strike_price, interest_rate, days_to_expiration, volatility):
    """
    Calculate and return the Greeks for a given option using Mibian.

    Parameters:
    - option_type: 'CALL' or 'PUT'
    - underlying_price: Current price of the underlying asset
    - strike_price: Strike price of the option
    - interest_rate: Annual risk-free interest rate as a percentage (e.g., 1.5 for 1.5%)
    - days_to_expiration: Days until the option expires
    - volatility: Implied volatility as a percentage (e.g., 20 for 20%)

    Returns:
    A dictionary containing the calculated Greeks.
    """

    #represent the interest rate and volatility as a decimal
    interest_rate /= 100
    volatility /= 100

    #represent dte in years
    days_to_expiration = days_to_expiration / 365

    #call
    if option_type.upper() == 'CALL':
        bs = mibian.BS([underlying_price, strike_price, interest_rate, days_to_expiration], volatility=volatility)    
    else: #put
        bs = mibian.BS([underlying_price, strike_price, interest_rate, days_to_expiration], volatility=volatility, call=False)



    #extract greeks
    greeks = {
        'delta': bs.callDelta if option_type.upper() == 'CALL' else bs.putDelta,
        'gamma': bs.gamma,
        'theta': bs.callTheta if option_type.upper() == 'CALL' else bs.putTheta,
        'vega': bs.vega,
        'rho': bs.callRho if option_type.upper() == 'CALL' else bs.putRho,
    }

    return greeks

#genreates an array of underlying prices
def generate_price_range(underlying_price, price_delta, num_points):
    lower_bound = underlying_price * (1 - price_delta)
    upper_bound = underlying_price * (1 + price_delta)
    return np.linspace(lower_bound, upper_bound, num_points) #creates an array of num_points between lower_bound and upper_bound


#generate an array of days to expiration, 0 to dte, num_points
def generate_dte_range(dte, num_points):
    return np.linspace(0, dte, num_points)




def calculate_greeks_range(option_type, underlying_prices, strike_price, interest_rate, days_to_expirations, volatility):
    results = []
    for underlying_price in underlying_prices:
        for dte in days_to_expirations:
            greeks = calculate_greeks(option_type, underlying_price, strike_price, interest_rate, dte, volatility)
            results.append({
                'underlying_price': underlying_price,
                'days_to_expiration': dte,
                **greeks
            })

    return results
