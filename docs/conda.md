# conda使用实践


## conda导出yml文件
```
conda export > environment.yaml
conda env create -f environment.yaml
```
TODO: 可以尝试导出更加简洁,比如只有python包等