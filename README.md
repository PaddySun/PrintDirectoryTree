# PrintDirectoryTree
打印树状文件结构

------



## 功能介绍

1. **深度控制**：

   - 通过`max_depth`参数限制显示层级
   - 达到最大深度时显示`...`表示还有未显示内容
   - 默认`None`表示不限制深度

2. **命令行参数支持**：

   ```bash
   python script.py --max-depth 2 --root ./myproject
   ```

3. **健壮的异常处理**：

   - 自动跳过无权限访问的目录

4. **优化显示效果**：

   - 使用集合(`set`)加速排除项检查
   - 深度限制时显示省略号提示

### 使用示例

1. 显示完整目录树：

   ```bash
   python dir_tree.py
   ```

2. 只显示2层深度：

   ```bash
   python dir_tree.py --max-depth 2
   ```

3. 指定其他项目路径：

   ```bash
   python dir_tree.py --root ../other_project --max-depth 1
   ```

### 典型输出（max_depth=2）

```
==================================================
项目目录结构: /projects/demo (深度限制: 2)
==================================================
demo
├── README.md
├── requirements.txt
├── src
│   ├── main.py
│   └── utils
│       └── ...
├── tests
│   └── test_main.py
└── data
    └── ...
==================================================
```
