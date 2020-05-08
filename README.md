## 说明

测试使用 Flask 搭建 API接口，主要依赖 `pycorrector` 和 `jieba` 处理相关的文本内容，根据请求返回相应的数据。

## 示例

包括了两个接口，分别是文本纠错接口和敏感词检测接口，在调用接口前需要启动服务：

```bash
$ export FLASK_APP=api.py
$ flask run --host=0.0.0.0
```

下面是调用敏感词检查接口：

```bash
  $ curl -i -H "Content-Type: application/json" -X POST -d  '{"id": 123, "text": "历史学系"}' http://localhost:5000/text/api/v1.0/taboo

      HTTP/1.0 200 OK
      Content-Type: application/json
      Content-Length: 236
      Server: Werkzeug/0.11.15 Python/3.6.10
      Date: Thu, 07 May 2020 03:27:30 GMT

      {
      "cost_time": 0.00012493133544921875,
      "data": {
          "taboo_status": false,
          "words": []
      },
      "description": "it's successfull that check taboo words",
      "id": 123,
      "status": 200,
      "text": "\u5386\u53f2\u5b66\u7cfb"
      }
```

下面是词语错误接口:

```bash
  $ curl -i -H "Content-Type: application/json" -X POST -d  '{"id": 123, "text": "历史学系"}' http://localhost:5000/text/api/v1.0/correct
      HTTP/1.0 200 OK
      Content-Type: application/json
      Content-Length: 186
      Server: Werkzeug/0.11.15 Python/3.6.10
      Date: Wed, 06 May 2020 08:57:16 GMT

      {
      "cost_time": 0.017215967178344727,
      "description": "it's successfull that check words",
      "id": 123,
      "report": false,
      "status": 200,
      "text": "\u5386\u53f2\u5b66\u7cfb"
      }
```

