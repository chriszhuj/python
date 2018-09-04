1，创建项目可以在终端使用scrapy startproject 项目名称创建，会自动生成spiders目录，items.py，middlewares.py，pipelines.py，settings.py文件
2，通过scrapy genspider 爬虫名称 域名 生成爬虫文件，eg. history.py
3，scrapy crawl history 执行爬虫，添加 -o xxx.csv(json,jl)参数，可以将数据导出，json和jl的区别可百度。调试爬虫：scrapy parse

