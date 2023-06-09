import baostock as bs
import pandas as pd
from utils import convertDfToCsvList, removeDotList, saveCodeCsv, stockCode
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
    if len(profit_list) > 0:
        return profit_list[0]
    else:
        return []

# 营运能力


def getOperationData(code, year, quarter):
    operation_list = []
    rs_operation = bs.query_operation_data(
        code, year, quarter)
    while (rs_operation.error_code == '0') & rs_operation.next():
        operation_list.append(rs_operation.get_row_data())
    if len(operation_list) > 0:
        return operation_list[0]
    else:
        return []

#    code     pubDate    statDate NRTurnRatio NRTurnDays INVTurnRatio INVTurnDays CATurnRatio AssetTurnRatio
# 0  sh.600000  2017-08-30  2017-06-30                                                                   0.014161


# 成长能力
def getGrowthData(code, year, quarter):
    growth_list = []
    rs_growth = bs.query_growth_data(code, year, quarter)
    while (rs_growth.error_code == '0') & rs_growth.next():
        growth_list.append(rs_growth.get_row_data())
    if len(growth_list) > 0:
        return growth_list[0]
    else:
        return []


#         code     pubDate    statDate YOYEquity  YOYAsset     YOYNI YOYEPSBasic    YOYPNI
# 0  sh.600000  2017-08-30  2017-06-30  0.120243  0.101298  0.054808    0.021053  0.052111


# 偿债能力
def getBlanceData(code, year, quarter):
    balance_list = []
    rs_balance = bs.query_balance_data(code, year, quarter)
    while (rs_balance.error_code == '0') & rs_balance.next():
        balance_list.append(rs_balance.get_row_data())
    if len(balance_list) > 0:
        return balance_list[0]
    else:
        return []


#         code     pubDate    statDate currentRatio quickRatio cashRatio YOYLiability liabilityToAsset assetToEquity
# 0  sh.600000  2017-08-30  2017-06-30                                       0.100020         0.933703     15.083598

# 现金流量


def getCashData(code, year, quarter):
    cash_flow_list = []
    rs_cash_flow = bs.query_cash_flow_data(
        code, year, quarter)
    while (rs_cash_flow.error_code == '0') & rs_cash_flow.next():
        cash_flow_list.append(rs_cash_flow.get_row_data())
    if len(cash_flow_list) > 0:
        return cash_flow_list[0]
    else:
        return []


#         code     pubDate    statDate CAToAsset NCAToAsset tangibleAssetToAsset ebitToInterest    CFOToOR    CFOToNP    CFOToGr
# 0  sh.600000  2017-08-30  2017-06-30                                                           -3.071550  -8.976439  -3.071550


# 杜邦指数
def getDupontDate(code, year, quarter):
    dupont_list = []
    rs_dupont = bs.query_dupont_data(code, year, quarter)
    while (rs_dupont.error_code == '0') & rs_dupont.next():
        dupont_list.append(rs_dupont.get_row_data())
    if len(dupont_list) > 0:
        return dupont_list[0]
    else:
        return []


#         code     pubDate    statDate dupontROE dupontAssetStoEquity dupontAssetTurn dupontPnitoni dupontNitogr dupontTaxBurden dupontIntburden dupontEbittogr
# 0  sh.600000  2017-08-30  2017-06-30  0.074617            15.594453        0.014161      0.987483     0.342179        0.776088


#### 登出系统 ####
def logout():
    bs.logout()


def getReport(code, year, quarter):
    reportData = []
    profileData = getProfileData(code, year, quarter)
    operatorData = getOperationData(code, year, quarter)
    growData = getGrowthData(code, year, quarter)
    balanceData = getBlanceData(code, year, quarter)
    cashData = getCashData(code, year, quarter)
    dupontData = getDupontDate(code, year, quarter)
    reportData = reportData + profileData + operatorData + \
        growData + balanceData + cashData + dupontData
    return reportData


currentIndex = stockCode.index("SH.600528")


def main(start_year: int, end_year: int):
    login()

    args = [(year, quarter) for quarter in range(1, 5)
            for year in range(start_year - 1, end_year + 1)]
    for index in range(0, len(stockCode)):
        if index >= currentIndex:
            code = stockCode[index]
            codeDataList = []
            for year, quarter in args:
                report = getReport(code, year, quarter)
                if len(report) != 0:
                    codeDataList.append(report)
            saveCodeCsv(code, codeDataList)
            print("code : ", code)
        else:
            continue
    logout()


main(2015, 2023)
