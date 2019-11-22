# 导入 jieba
import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取

# 全模式
seg_list = jieba.cut("他来到上海交通大学", cut_all=True)
print("【全模式】：" + "/ ".join(seg_list))

# 精确模式
seg_list = jieba.cut("他来到上海交通大学", cut_all=False)
print("【精确模式】：" + "/ ".join(seg_list))

# 返回列表
seg_list = jieba.lcut("他来到上海交通大学", cut_all=True)
print("【返回列表】：{0}".format(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")
print("【搜索引擎模式】：" + "/ ".join(seg_list))

# 返回列表
seg_list = jieba.lcut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")
print("【返回列表】：{0}".format(seg_list))

