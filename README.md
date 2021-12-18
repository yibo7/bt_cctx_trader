# backtrader、ccxt简介和安装
    其实在量化领域，有大量可用框架，比如vnpy，就已经集成了很多数字货币的交易所，可以直接进行回测和在线交易。在这里之所以没有用vnpy，纯粹是因为vnpy对mac用户相当不友好，一个python的框架居然在mac上需要繁琐的安装步骤，甚至很难正常运行。backtrader和ccxt的组合能解决以下问题：

    对于bitmex（期货交易首选，无他）上无法提取历史数据的问题，ccxt能提供了从2017年开始的所有的ohlcv数据
    ccxt直接支持python、php、javascript，在开发环境上给了我们更多的选择，更易于在UI上获得更好的用户体验。
    backtrader则是直接集成了ccxt
    因为这些用户体验的原因，我选择了backtrader+ccxt，但不代表这是最好的选择，如果有更好的方案，欢迎大家多交流，给我留言

# ccxt
python官网对于ccxt的介绍是
即一个封装了诸多数字货币交易平台的api的开源库。

支持python、php、javascript三种语言，github上可以下载源码。

ccxt结构明确，易于使用，所有api被封装成统一格式的接口，返回数据被封装成统一格式的字典，基本省去了api开发时间。

其安装很简单：

> pip3 install ccxt

# backtrader
backtrader是一个量化策略的回测分析平台，与其他的框架一样，事件响应机制，支持股票和各种期货交易。
项目的地址：https://github.com/backtrader/backtrader
安装方式：

> pip3 install backtrader

当然，我们说过选择backtrader的原因是它集成了ccxt。但官方版本是没有集成ccxt的。
而是在分支上：https://github.com/bartosh/backtrader/tree/ccxt
因此，我们得通过以下方式安装：
> pip install --upgrade git+https://github.com/bartosh/backtrader.git@ccxt

# matplotlib
如果要调用.plot()方法，观看回测图表，还需要安装matplotlib，目前不支持太高版的matplotlib
pip install matplotlib==3.2.2