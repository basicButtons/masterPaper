import baostock as bs
import pandas as pd
from utils import convertDfToCsvList, lowerStockCodeList, saveCodeCsv
from test import loadIndex, saveIndex
#### 登陆系统 ####


def login():
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)


# 盈利能力
def getProfileData(code, year, quarter):
    profit_list = []
    rs_profit = bs.query_profit_data(code=code, year=year, quarter=quarter)
    while (rs_profit.error_code == '0') & rs_profit.next():
        profit_list.append(rs_profit.get_row_data())
    result_profit = pd.DataFrame(profit_list, columns=rs_profit.fields)
    # 打印输出
    rescsvData = convertDfToCsvList(result_profit)
    return rescsvData
    # print(result_profit)

#      code     pubDate    statDate    roeAvg  npMargin gpMargin           netProfit    epsTTM           MBRevenue      totalShare       liqaShare
# 0  sh.600000  2017-08-30  2017-06-30  0.074617  0.342179           28522000000.000000  1.939029  83354000000.000000  28103763899.00  28103763899.00


# 营运能力
def getOperationData(code, year, quarter):
    operation_list = []
    rs_operation = bs.query_operation_data(
        code, year, quarter)
    while (rs_operation.error_code == '0') & rs_operation.next():
        operation_list.append(rs_operation.get_row_data())
    result_operation = pd.DataFrame(
        operation_list, columns=rs_operation.fields)
    rescsvData = convertDfToCsvList(result_operation)
    return rescsvData
# 打印输出
# print(result_operation)

#    code     pubDate    statDate NRTurnRatio NRTurnDays INVTurnRatio INVTurnDays CATurnRatio AssetTurnRatio
# 0  sh.600000  2017-08-30  2017-06-30                                                                   0.014161


# 成长能力
def getGrowthData(code, year, quarter):
    growth_list = []
    rs_growth = bs.query_growth_data(code, year, quarter)
    while (rs_growth.error_code == '0') & rs_growth.next():
        growth_list.append(rs_growth.get_row_data())
    result_growth = pd.DataFrame(growth_list, columns=rs_growth.fields)
    rescsvData = convertDfToCsvList(result_growth)
    return rescsvData
# 打印输出
# print(result_growth)

#         code     pubDate    statDate YOYEquity  YOYAsset     YOYNI YOYEPSBasic    YOYPNI
# 0  sh.600000  2017-08-30  2017-06-30  0.120243  0.101298  0.054808    0.021053  0.052111


# 偿债能力
def getBlanceData(code, year, quarter):
    balance_list = []
    rs_balance = bs.query_balance_data(code, year, quarter)
    while (rs_balance.error_code == '0') & rs_balance.next():
        balance_list.append(rs_balance.get_row_data())
    result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)
    rescsvData = convertDfToCsvList(result_balance)
    return rescsvData
# 打印输出
# print(result_balance)

#         code     pubDate    statDate currentRatio quickRatio cashRatio YOYLiability liabilityToAsset assetToEquity
# 0  sh.600000  2017-08-30  2017-06-30                                       0.100020         0.933703     15.083598

# 现金流量


def getCashData(code, year, quarter):
    cash_flow_list = []
    rs_cash_flow = bs.query_cash_flow_data(
        code, year, quarter)
    while (rs_cash_flow.error_code == '0') & rs_cash_flow.next():
        cash_flow_list.append(rs_cash_flow.get_row_data())
    result_cash_flow = pd.DataFrame(
        cash_flow_list, columns=rs_cash_flow.fields)
    resCsvData = convertDfToCsvList(result_cash_flow)
    return resCsvData
# 打印输出
# print(result_cash_flow)

#         code     pubDate    statDate CAToAsset NCAToAsset tangibleAssetToAsset ebitToInterest    CFOToOR    CFOToNP    CFOToGr
# 0  sh.600000  2017-08-30  2017-06-30                                                           -3.071550  -8.976439  -3.071550


# 杜邦指数
def getDupontDate(code, year, quarter):
    dupont_list = []
    rs_dupont = bs.query_dupont_data(code, year, quarter)
    while (rs_dupont.error_code == '0') & rs_dupont.next():
        dupont_list.append(rs_dupont.get_row_data())
    result_dupont = pd.DataFrame(dupont_list, columns=rs_dupont.fields)
    resCsvData = convertDfToCsvList(result_dupont)
    return resCsvData

# 打印输出
# print(result_dupont)
#         code     pubDate    statDate dupontROE dupontAssetStoEquity dupontAssetTurn dupontPnitoni dupontNitogr dupontTaxBurden dupontIntburden dupontEbittogr
# 0  sh.600000  2017-08-30  2017-06-30  0.074617            15.594453        0.014161      0.987483     0.342179        0.776088


# 业绩快报
def getQuickData():
    rs = bs.query_performance_express_report(
        "sh.600000", start_date="2015-01-01", end_date="2017-12-31")
    # print('query_performance_express_report respond error_code:'+rs.error_code)
    # print('query_performance_express_report respond  error_msg:'+rs.error_msg)

    result_list = []
    while (rs.error_code == '0') & rs.next():
        result_list.append(rs.get_row_data())
        # 获取一条记录，将记录合并在一起
    result = pd.DataFrame(result_list, columns=rs.fields)
    resCsvData = convertDfToCsvList(result)
    return resCsvData
    #### 结果集输出到csv文件 ####
    # result.to_csv("D:\\performance_express_report.csv",
    #             encoding="gbk", index=False)
# print(result)

#   code     pubDate    statDate dupontROE dupontAssetStoEquity dupontAssetTurn dupontPnitoni dupontNitogr dupontTaxBurden dupontIntburden dupontEbittogr
# 0  sh.600000  2017-08-30  2017-06-30  0.074617            15.594453        0.014161      0.987483     0.342179        0.776088

# 需要转化为以下格式
#  date  period  value  field   symbol
# 其中data 为其发布日 也就是 pubDate period 是上个周期的最后一天， value是 field 对应的值， symbol 是 对应的股票的 编码

# 结果集输出到csv文件
# result_profit.to_csv("D:\\profit_data.csv", encoding="gbk", index=False)


#### 登出系统 ####
def logout():
    bs.logout()


def getReport(code, year, quarter):
    reportData = []
    profileData = getProfileData(code, year, quarter)
    cashData = getCashData(code, year, quarter)
    balanceData = getBlanceData(code, year, quarter)
    growData = getGrowthData(code, year, quarter)
    dupontData = getDupontDate(code, year, quarter)
    operatorData = getOperationData(code, year, quarter)
    reportData = reportData + balanceData + cashData + \
        growData + profileData + dupontData+operatorData
    return reportData


def main(start_year: int, end_year: int):
    currentIndex = loadIndex()
    login()

    args = [(year, quarter) for quarter in range(1, 5)
            for year in range(start_year - 1, end_year + 1)]
    for index in range(currentIndex+1, len(lowerStockCodeList)):
        code = lowerStockCodeList[index]
        codeDataList = []
        for year, quarter in args:
            report = getReport(code, year, quarter)
            codeDataList = codeDataList + report
        if len(codeDataList) != 0:
            saveCodeCsv(code, codeDataList)
            saveIndex(index)
            print("code : ", code)
        else:
            break
    logout()


main(2015, 2023)
