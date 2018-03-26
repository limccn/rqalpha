import json
import pickle
import pandas as pd
import argparse

# 递归函数，根据对象内容返还json对象
# dataframe 仅能限制于table对象
# 仅支持dataframe或dict
def transToJson (ObjectParams):
	# DataFrame情况下直接返回转化的json对象
	if isinstance(ObjectParams,pd.DataFrame):
		return json.loads(ObjectParams.to_json(orient='table',force_ascii=False))
	else:
		#dist 先判断存不存在对应的DataFrame
		for key in ObjectParams:
			objTmp = ObjectParams[key]
			if isinstance(objTmp,pd.DataFrame) :
				break
		else:
			# 正常说明循环正常结束，都是dict
			return json.loads(json.dumps(ObjectParams))
		
		#未正常结束说明有DataFrame对象
		objJson = {}
		for key in ObjectParams:
			objJson[key] = transToJson(ObjectParams[key])

		# 返回对应的JSON对象
		return objJson

#获取对应的参数
parser = argparse.ArgumentParser(description="pkl to json")
parser.add_argument('--path', type=str, default=None)
parser.add_argument('--fileName',type=str, default=None)
args = parser.parse_args()
path = args.path
fileName = args.fileName

# 判断参数都存在
if not path is None and not fileName is None:
	objJson = {}
	try:
		# 读取对应的pkl文件
		dictData = pd.read_pickle(path+fileName+'.pkl')
		# 递归获取json对象
		objJson = transToJson(dictData)
		#strJson写入对应的Json文件
		json.dump(objJson,open(path+fileName+".json", 'w'),ensure_ascii=False,indent=4)
	except FileNotFoundError:
		# 文件未找到
		print('Not found File')
	except IOError:
		# IO异常
		print('IO Error')
	except PermissionError:
		# 权限问题
		print('Not accessible.')
else:
	# 参数错误
	print('Params Error!')


	
	
