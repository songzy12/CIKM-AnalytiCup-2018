## PowerShell

| **Ctrl+Home** | 删除光标最左端的所有字符 |
| ------------- | ------------------------ |
| **Esc**       | 清空当前命令行           |

## Jupyter Notebook

```
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

<https://blog.csdn.net/lawme/article/details/51034543>

- **Shift-Enter** : 运行本单元，选中下个单元
- **Ctrl-Enter** : 运行本单元
- **Alt-Enter** : 运行本单元，在其下插入新单元

- **Y** : 单元转入代码状态
- **M** :单元转入markdown状态
- **R** : 单元转入raw状态

- **A** : 在上方插入新单元
- **B** : 在下方插入新单元

- **X** : 剪切选中的单元
- **C** : 复制选中的单元
- **Shift-V** : 粘贴到上方单元
- **V** : 粘贴到下方单元

- **Z** : 恢复删除的最后一个单元
- **D,D** : 删除选中的单元
- **Shift-M** : 合并选中的单元