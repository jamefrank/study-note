# poetry结合conda使用方法

## conda创建环境
```
conda create -n my_project_env python=3.9
conda activate my_project_env
```

## conda环境中安装poetry
```
pip install poetry
```

## poetry关闭自身虚拟环境
```
poetry config virtualenvs.create false
```

## 在已有项目中初始化poetry
```
cd your_project
poetry init
```
Poetry 会通过交互式提示询问项目名称、版本、描述、作者、依赖等信息。完成后，会生成 pyproject.toml 文件。

## 管理包
Conda 和 Poetry 都尝试管理依赖，可能导致版本冲突。解决方法是优先使用 Conda 安装那些需要通过 Conda 管理的包（如 numpy、pandas 等），然后使用 Poetry 添加 Python 纯软件包。

```
poetry add  xxx
poetry remove xxx
conda install xxx
conda remove xxx
```