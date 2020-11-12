# py_royDataService_client

Roy Data Service Client
===================================

Client part is responsible for users to get data from the remote database. 

dataApi
-----------------------------------

Functions for getting data 

To start:
-----------------------------------

1. Prepare for Anaconda 3 64bit environment.
2. Email roycheng1997@gmail.com to request for a token.
3. Run the runDemo.py and see if it works. (This only works when I setup in my local computer)


Documents and Parameters
-----------------------------------

## Database and datatype

* uqer:
    * tradingData(>=1min)
    * tradingDataBase(>=1min)
    * tradingDataNight(>=1min)
    * tradingDataDaily(>=1d)
    * tradingDataCompare(>=1min)
    * mainContract(>=1d)
    * adjustForm(>=1d)
* ctp:(not yet)
    * tradingDataHFT(tick or >= 1s)
* fushare:
    * memberVolume_fs(1d)
    * rollingYield_fs(1d)    
    * spotPrice_fs(1d)  
* uqer_fundamental:
    * hedgeData(1d)
    * memberVolume(1d)
    * registeredWarehouseReceipt(1d)
* uqer_option: (more tickers HS300, 300ETF, 300ETF1, 50ETF)
    * optionTradingData(1d)
    * optionmemberVolume(1d)
    * optionGreeks(1d)
* mysteel:  (supported items see DICT_STEEL)
    * steelSpot(1d)    
* eia:
    * energyFutPriceDaily(1d)
    * positioning(1d) not implemented **yet**


Authors:
-----------------------------------

Yifan Song (https://github.com/Yifan-Song): Networks and Servers <br>
Xiao Cheng (https://github.com/RoyCheng1997): DataEngines and data service
