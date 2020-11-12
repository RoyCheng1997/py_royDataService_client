# py_royDataService_client

Roy Data Service Client
===================================

Client part is responsible for users to get data from the remote database. 

dataApi
-----------------------------------

Functions for getting data. More functions will be added here

To start:
-----------------------------------

1. Prepare for Anaconda 3 64bit environment.
2. Email roycheng1997@gmail.com to request for a token.
3. Run the runDemo.py and see if it works. (This only works when I setup in my local computer)


Documents and Parameters
-----------------------------------

## Database and datatype

The first level denotes the data source. The second level is the datatype that you should used in the request argument.

* uqer:
    * tradingData (>=1min)
    * tradingDataBase (>=1min)
    * tradingDataNight (>=1min)
    * tradingDataDaily (>=1d)
    * tradingDataCompare (>=1min)
    * mainContract (>=1d)
    * adjustForm (>=1d)
* ctp:(not yet)
    * tradingDataHFT (tick or >= 1s)
* fushare (stop updating):
    * memberVolume_fs (1d)
    * rollingYield_fs (1d)    
    * spotPrice_fs (1d)  
* uqer_fundamental:
    * hedgeData (1d)
    * memberVolume (1d)
    * registeredWarehouseReceipt (1d)
* uqer_option: (more tickers HS300, 300ETF, 300ETF1, 50ETF)
    * optionTradingData (1d)
    * optionmemberVolume (1d)
    * optionGreeks (1d)
* mysteel:  (supported items see DICT_STEEL)
    * steelSpot (1d)    
* eia:
    * energyFutPriceDaily (1d)
    * positioning (1d) not implemented **yet**

## Supported frequency:

* tick: tick data, not supported yet
* 1_s: second level
* 1_min: minute level
* 1_h: hourly level
* 1_d: daily level
* 1_w: weekly level
* 1_m: monthly level

## Supported tickers:

* China futures ticker upper case + '000' (which denotes the main/front contract), i.e, M000
* China futures ticker contract, i.e, M1905
* 'HS300', '300ETF', '300ETF1', '50ETF' (only for options access)
* 'WTI', 'RG', 'RBOB', 'HO', 'Propane', 'NGSpot', 'NG' (eia data)
* Spot product name (mysteel data)

Authors:
-----------------------------------

Yifan Song (https://github.com/Yifan-Song): Networks and Servers <br>
Xiao Cheng (https://github.com/RoyCheng1997): DataEngines and data service

Note: this server is only for personal use, all users must be qualified. Data is updated weekly.