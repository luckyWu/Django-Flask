from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from whoosh.qparser import QueryParser
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import TEXT, ID, Schema
from jieba.analyse import ChineseAnalyzer
from app.models import News

def index_create(request):
    analyser = ChineseAnalyzer()  # 导入中文分词工具
    """
    使用whoosh首先要建立schema对象，第一次创建索引时，必须定义索引的模式。该模式列出了索引中的字段。
    字段是索引中每个文档的一条信息，例如其标题或文本内容。
    下面使用到的schema索引对象。
    whoosh.fields.ID:这种类型只是将字段的整个值索引（并可选地存储）为一个单元（也就是说，它不会将其分解为单个单词）。
                     这对于文件路径，URL，日期，类别等字段很有用。
    whoosh.fields.STORED:此字段与文档一起存储，但未编入索引。此字段类型未编入索引且无法搜索。
                         这对于要在搜索结果中向用户显示的文档信息很有用。
    whoosh.fields.TEXT:此类型用于正文。它索引（并可选地存储）文本并存储术语位置以允许短语搜索。
    """
    schema = Schema(title=TEXT(stored=True, analyzer=analyser),
                    content=TEXT(analyzer=analyser))  # 创建索引结构

    ix = create_in("index", schema=schema, indexname='index')  # test为索引创建的地址，indexname为索引名称
    writer = ix.writer()
    # 读取文件内容
    datas = News.objects.all()
    for data in datas:
        news_title = data.title
        news_content = data.content
        writer.add_document(title=news_title,content=news_content)
    writer.commit()

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

    if request.method == "POST":
        data = request.POST.get('sea')
        if data:
            new_dict = [] # 存储检索结果
            code = ''
            index = open_dir("index", indexname='index')  # 读取建立好的索引
            with index.searcher() as searcher:
                parser = QueryParser("content", index.schema)  # 生成查询字段的对象
                find = data  # input("请输入检索内容：")  # find表示要查询的内容
                myquery = parser.parse(find)  # 在content字段查询
                results = searcher.search(myquery)  # , limit=None)  # limit为搜索结果的限制，默认为10
                for result1 in results:
                    code = 200
                    new_dict.append(dict(result1))
                if not new_dict:
                    code = 100
            return render(request,'index.html',{'content': new_dict})



