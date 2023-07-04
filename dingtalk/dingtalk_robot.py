import requests
import json
import random

def openaicheck():
	url = "https://luckbaby8.club/v1/chat/completions"
	a = random.randint(0, 10)
	b = random.randint(0, 10)
	print(a)
	print(b)
	sumstr = "%s+%s等于多少" % (a, b)
	params = {
	    "model": "gpt-3.5-turbo-0301",
		"messages": [{"role": "user", "content": sumstr}]
	}
	headers = {"Content-Type": "application/json",
			# "Authorization": "Bearer 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"
	 		   # "Authorization": "Bearer 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"
	}
	try:
		response_str = requests.post(url, json=params, headers=headers, timeout=5).content
		response_json = json.loads(response_str)
		print(response_json)
	except requests.exceptions.HTTPError as e:
		print("HTTP error occurred:", e)
		return

	try:
		isAt = True
		error = response_json["error"]
		message = "错误预警: %s" % error["message"]
	except KeyError:
		isAt = False
		message = "健康预警: 我还在!"
		
	dingTalkRobot(message, isAt)
	

def dingTalkRobot(message, isAt=False):
	url = "https://oapi.dingtalk.com/robot/send?access_token=94c6e1681740fc1eed3df734a775bb129086532a0ecb37627aa32b309cf58d38"
	params = {
		"at": {
	    	"isAtAll": isAt
	    },
	    "text": {
	    	"content": message
	    },
	    "msgtype": "text"
	}
	headers = {"Content-Type": "application/json"}
	response_str = requests.post(url, json=params, headers=headers).content
	response_json = json.loads(response_str)
	print(response_json)

openaicheck()


