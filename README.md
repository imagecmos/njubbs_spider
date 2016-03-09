##spider report<br>

github：  [imagecmos](https://github.com/imagecmos/spider.git)<br><br>

** * *
代码部分主要分为三块：<br>

1.	数据抓取<br>
编程语言选择的是Python，oh不，是整个项目用的都是Python，关于为什么选择Python我要多说几句，刚开始我曾苦恼用什么语言写爬虫呢，Java也行，C++也行，Python也行，最后之所以选择了Python，原因就是用其他的我不会写爬虫。好了，开始撸起来，主要用的几个库是*urllib2*，*Beautifulsoup*,*MySQLdb*<br>
2.	数据处理<br>
数据处理部分主要就是对保存好的数据进行分词，词性标注，中文做到比较好的自然语言处理就是哈工大的平台，在[科大讯飞](http://www.xfyun.cn)的开放平台上可以免费使用，还有个较好的中文分词库是[jieba分词](https://github.com/fxsjy/jieba.git),使用时发现在处理大量数据时速度还是有点慢，不得不自己加个多线程。还有些其他的数据就要自己代码解决，比如发帖时间，板块等数据的分析。
3.	数据可视化<br>
这部分算是最累人的，写了差不多五个小时才把图全部画出来。图库用的是[matplotlib](http://matplotlib.org),功能很强大。<br>

废话不多说，直接上图(还是废话一下吧，对于图中分类不准确的词我是原样保留了，因为这恰恰反映了当前NLP还存在的问题)<br>
![](http://7xqin1.com1.z0.glb.clouddn.com/Location.png)
在所有的十大标题中，**南京**在地点分类中夺魁，其实不想也应该能知道这个结果，南京大学的BBS不是南京难不成还是上海？好吧，上海排在第三，足以说明上海在长三角地区的影响力。
![](http://7xqin1.com1.z0.glb.clouddn.com/forum.png)
最热的竟然不是girl版，不是girl版，girl版，版
![](http://7xqin1.com1.z0.glb.clouddn.com/followMost.png)
![](http://7xqin1.com1.z0.glb.clouddn.com/followLast.png)
如果你有颈椎病，这两张图应该能治好你，回复最多和最少的十大贴，给你，不谢
![](http://7xqin1.com1.z0.glb.clouddn.com/person_name.png)
传闻是帝国主义安插在我党内部的"代理人"是被同学们提到最多的人名，不对，第六名的那个单字的是谁，我不了解，谁能告诉我
![](http://7xqin1.com1.z0.glb.clouddn.com/postsovertime.png)
在十大贴的发帖时间分布上，上午十点，下午四点，晚上九点这三个时间点附近我想问，大家都喜欢那个时候发帖吗？
![](http://7xqin1.com1.z0.glb.clouddn.com/sportWord.png)
在关于体育的话题中，足球占据了整个前十名，我是篮球迷，让我哭一会
![](http://7xqin1.com1.z0.glb.clouddn.com/week.png)
在一周的十大分布中，周一和周五贡献的最多，难道这两天都很无聊？
![](http://7xqin1.com1.z0.glb.clouddn.com/EnglishWord.png)
被提及最多的英文单词是offer，可能在我抓取的这近三个月里是大家找实习，申请学校比较多的时间段
![](http://7xqin1.com1.z0.glb.clouddn.com/author.png)
最后的最后，上十大最多的那位同学，我特地上小百合搜了一下，身兼三个版主，难怪


*imagecmos*
2016年3月9日 15:58
