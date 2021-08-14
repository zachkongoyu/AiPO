import requests
import datetime
import pandas as pd

cookies = {
	'zh_choose': 's',
	'traderDataSite': 'CfDJ8EK9ezdhIfdHkebvhjzgO2kqb_u1YO5pvIpvJZhNPyZ15H5Dawy4wnUViHJu4_-vtpimJ1TyKEgBfABY_S36gPvPB8QkmFt-5MQFU-DsWqexmXqHqgQfxuWgZ3qmHs9zG0zm6e-x5bb-qxIrx1I53Jg',
	'firstaipo': 'yes',
}

headers = {
	'Connection': 'keep-alive',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'RequestVerificationToken': 'CfDJ8EK9ezdhIfdHkebvhjzgO2nIMd-MdgheP9Y0Eo7BI0FqdWY6PfFUmOVdCcEuTDirn_hbEHAxHH4s7bvmaCT8sFq4eLxP4DEZsC6M6galyPJTXc8y_raJcgte7DBrD4iUg28n9SRv117Uz5vues2HqdE',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
	'Sec-GPC': '1',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://aipo.myiqdii.com/broker/index',
	'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
	('stockType', '0'),
	('type', '0'),
	('pageIndex', '1'),
	('pageSize', '700'),
	('searchKey', ''),
)

response = requests.get('https://aipo.myiqdii.com/Home/GetTurnoverChangeInfo', headers=headers, params=params, cookies=cookies)

null = float('NaN')

d = eval(response.content)

required = ['创盈服务', '中投信息', '富途证券', '汇丰证券', '海通国际', '中银国际']
today = datetime.date.today()

try:
	df_rank = pd.read_excel('broker_rank.xlsx', index_col=0)
	df_turnover = pd.read_excel('broker_turnover.xlsx', index_col=0)

	df_rank.index = pd.to_datetime(df_rank.index)
	df_turnover.index = pd.to_datetime(df_turnover.index)
except:
	df_rank = pd.DataFrame()
	df_turnover = pd.DataFrame()

d_rank = dict()
d_turnover = dict()

for i, broker in enumerate(d['data']['dataList']):
	print(broker['shortName'], broker['turnover'], broker['ranking'])
	

df_rank = pd.concat([df_rank, pd.DataFrame(d_rank)])
df_turnover = pd.concat([df_turnover, pd.DataFrame(d_turnover)])

print(df_rank)
print(df_turnover)

df_rank.to_excel('broker_rank.xlsx')
df_turnover.to_excel('broker_turnover.xlsx')