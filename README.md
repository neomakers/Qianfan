---
chatgpt_for_conda_env:https://chatgpt.com/c/673164ca-1f78-8009-93ec-ddf365b8db4f
---
# 环境配置
安装conda 
[ubuntu](https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh)下载anaconda。

```shell
bash ./Miniconda3-latest-Linux-x86_64.sh 
```

查看虚拟环境有那些环境
```shell
conda env list
```
进入环境产
```shell
conda activate base
```
求python的版本大于等于3.9

```shell
python --version
```
## 创建环境

打开新的终端
```shell
conda create -n vlm python=3.11
```
进入环境
```shell
conda activate vlm
```
# 千帆模型使用方法
其中详细[官方连接](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/clntwmv7t),具体安全认证来源于官网(用户需要 百度智能云[控制台 - 安全认证](https://console.bce.baidu.com/iam/#/iam/accesslist) 页面获取 Access Key 与 Secret Key，具体流程参见平台 [说明文档](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb))



目前千帆Python SDK 已发布到 PyPI ，用户可使用 pip 命令进行安装，Python需要 3.7.0 或更高的版本。

```shell
pip install 'qianfan[dataset_base]'
```

打开 VS Code。

按下 Ctrl + Shift + P，输入 Python: Select Interpreter。

在列表中选择您的虚拟环境 vlm，通常路径为,实例根据实际状况：

```shell
~/miniconda3/envs/vlm/bin/python
```



# 参考文献
https://github.com/baidubce/bce-qianfan-sdk
https://github.com/baidubce/bce-qianfan-sdk/blob/main/docs/configurable.md
[如何获取ASKK](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb)
[百度智能云](https://qianfan.cloud.baidu.com/appbuilder/)
[模型广场](https://console.bce.baidu.com/qianfan/modelcenter/model/buildIn/list)
[ERNIE-Speed-Pro-128K模型](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Bm0hnziyn)
[推理服务API——V1](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/illg7thxi)
[应用接入-appkey](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v1)
[Access-Key](https://console.bce.baidu.com/iam/#/iam/accesslist)
[模型资源赠送](https://console.bce.baidu.com/ai_apaas/resource)