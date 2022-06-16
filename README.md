# 使用方法
## RepoAnalyseTool.py 使用方法
python3 RepoAnalyseTool.py repo update  (数据更新) <br/>
python3 RepoAnalyseTool.py listall repo  <br/>
python3 RepoAnalyseTool.py search repo xxx  <br/>
python3 RepoAnalyseTool.py search commit xxx  <br/>
python3 RepoAnalyseTool.py show repo [repoName]  <br/>
python3 RepoAnalyseTool.py show commit [commitid]  <br/>

## cpplintSearchAll.py 使用方法
使用的前提： <br/>
pip3 install cpplint  <br/>

使用的办法：  <br/>
进入到你要扫描的代码路径，然后执行如下脚本即可  <br/>
python3 cpplintSearchAll.py   <br/>

**结果查询，在当前路径下面会有一个nohup.out文件，该文件为扫描的结果** <br/>


# TODO
支持对单个仓，比如linux-kernel下面也能够进行检索工作
