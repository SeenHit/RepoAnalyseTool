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
支持对单个仓，比如linux-kernel下面也能够进行检索工作     <br/>
支持 search commit xxx  [IGNORE xxx]     // 不在某些仓中搜寻对应的commit        <br/>
支持 search commit xxx  [repo   xxx]     // 支持在某些仓中搜索对应的commit      <br/>
支持 search all author                   // 列出所有的开发者邮箱                <br/>
支持 search all author repo xxx          // 列出在xxx 仓库开发的所有开发者名单  <br/>
