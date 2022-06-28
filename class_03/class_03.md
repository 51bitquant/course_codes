# 第三课: python环境的安装和创建虚拟环境

## 安装软件: 
1. Anaconda, 下载地址: https://www.anaconda.com/products/individual
   
2. PyCharm, 下载地址: https://www.jetbrains.com/pycharm/download/


##  python解析器和虚拟环境
1. Python是一门解释性的语言，需要解析器去帮把写好的代码运行起来，这就是python的运行环境。
      
2. 一个电脑可以运行很多个环境，类似微信的多开的功能，每个解析器的内容完全隔离开。


## conda创建虚拟环境:
在终端termial, window在cmd命令行中输入 
> conda create -n your_interpreter_name python=3.9 # 
 
例如创建名为study的解析器 
> conda create -n study python=3.9

## conda激活安装环境
> conda activate study 

## 查看环境列表
> conda env list 


## 删除环境
> conda deactivate # 先激活自己当前的环境

> conda remove -n <你的环境名称>

> conda remove -n study --all 
  

# Pycharm 配置环境
PyCharm需要能把代码跑起来，需要配置解析环境。 Window系统设置解析器: 
```
file --> setting  --> project --> interpreter --> 找你的环境解析器

```
    
MacOS系统设置解析器: 
```
Pycharm --> Preferences ---> project ---> interpreter --> 找到你的环境环境解析器

```
