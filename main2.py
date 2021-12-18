
import backtrader as bt
import pandas as pd


class TestStrategy(bt.Strategy):
    def next(self):
        print("fff")


if __name__ == '__main__':
    # print(ccxt.exchanges)
    cerebro = bt.Cerebro()
    df = pd.read_csv('data/1.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    # df['openinterest'] = 0 # 换手率
    bt_data = bt.feeds.PandasData(dataname = df)
    cerebro.adddata(bt_data)
    cerebro.addstrategy(TestStrategy)
    cerebro.run()
    cerebro.plot(style='candle')

