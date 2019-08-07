# scrapy-learn

data
    scrapy简单使用学习

    涉及xpath使用

    start_requests函数

    return item  <>  yield item


    scrapy.Request(url, meta, callbakc=func)
    
 mypipeimage
     图片的简单抓取，使用内置的pipeline
     深度抓取内容，没做深度限制
   
  image
     继承内置的pipeline，重写了图像下载的方法，实现了图片重命名,在setting中设置的路径下继续设置存储位置
     内置的方法和自定义的方法在传递参数上有一些不同
     
   
 

