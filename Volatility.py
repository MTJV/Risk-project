
def practice():
    #Data manipulation
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #pull data
    import yfinance as yf

    vix = yf.download('^VIX', start ='2012-01-01', end = '2012-12-31', auto_adjust=True)

    sp500 = yf.download('^GSPC', start ='2012-1-01',end='2012-12-31', auto_adjust=True)

    sp500['Returns'] = (sp500['Close'].pct_change())*100 # normalize to pct
    sp500['Volatility'] = sp500['Returns'].shift(-1).rolling(30).std()  # does not need to be normalized as

    sp500['Ann Volatility'] = sp500['Volatility']*np.sqrt(252)                                                         # gets calculated based on the normalized figure

    fig1 = plt.figure(figsize=(8,6))

    plt.plot(sp500.index,sp500['Ann Volatility'], color='blue', label = 'Realized volatility')
    plt.plot(vix.index,vix['Close'], color = 'red', label ='Implied volatility (^VIX)')
    plt.legend()

    plt.title('Implied vs Realized volatility 2012', size=20)
    plt.ylabel('% annualized', size = 15, color = 'black' )







    st.title('Risk premium')
    st.subheader('How is uncertainty priced in markets?')
    st.markdown("""In capital markets, risk is constantly being priced and analyzed by the :red[implied volatility]. 
    The factor is tracked by the ticker :green[^VIX] and it's constantly updated based on underlying SP500 options pricing,
    which reflect current risk sentiment. It's forward looking, and is gauging how volatile the markets
     will be in the next 30 days, with a higher value implying higher anticipated volatility.  
       As we are using historical data, :blue[realized volatility] is always based on past price movements — 
    there is no way to know next months :blue[realized volatility] in real time. Here, I've computed :blue[realized volatility] from the SP500
     over a one-month forward window and annualized to match the VIX scale.""")


    st.pyplot(fig1)

    st.markdown("""As we can see from the figure, there is a distinction between the :red[IV] (implied volatility) 
            and the :blue[RV] (realized volatility). Forecasting (or the attempt to) in markets plays a central role. 
              I find this relationship particularly interesting, as it showcases how accurate and trusted these forecasts are. Of course 
            the :red[IV] does not only showcase the inaccuracy of the forecasting. 
            This gap highlights how markets consistently assign a premium to uncertainty. :red[Implied volatility] isn’t just a forecast
             — it also reflects the price investors are willing to pay for protection against downside risk.""")
    
    st.text('Analysis by Mikael Valtonen, 2025')

practice()


