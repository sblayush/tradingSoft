
tradingSoft
-----------

A simple web applcation to view the stock market charts. I have made use of the anyChart api to plot interactive charts using angularJS. In the backend there is a python server running tornado server. The charts are interactive as one can draw on them and interact accordingly.

SO FAR:
1. Daily Update Data: download EOD data from NSEIndia website and update all the stocks.
2. Options to sort the data and remove duplicate data points.
3. Interact with charts by drawing on them and save the drwaings for future reference.
4. Portfolio for personal shares list.
5. Provision for EMA and SMA.

TODO:
1. Move all data from file system to database.
2. Add login page for different users.
3. Add intraday data.
4. Add more indicators.
5. Add provision for modifying the stock data in case of splits/dividents.
6. Increse security, ie, not all files sjhould be accessible from outside.
