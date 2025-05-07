import os
from pathlib import Path

def print_directory_tree(
    startpath,
    excluded_dirs=None,
    excluded_extensions=None,
    max_depth=None,
    current_depth=0,
    prefix=''
):
    """
    打印带深度控制的树状目录结构
    
    :param startpath: 起始路径
    :param excluded_dirs: 要排除的目录列表
    :param excluded_extensions: 要排除的文件扩展名列表
    :param max_depth: 最大显示深度（None表示不限制）
    :param current_depth: 当前递归深度（内部使用）
    :param prefix: 用于构建树状结构的前缀（内部使用）
    """
    if excluded_dirs is None:
        excluded_dirs = {'.git', '__pycache__', 'venv', 'env', 'node_modules', '.idea', '.vscode'}
    if excluded_extensions is None:
        excluded_extensions = {'.pyc', '.pyo', '.pyd', '.db', '.log', '.tmp'}
    
    try:
        entries = sorted(os.listdir(startpath))
    except PermissionError:
        return

    # 过滤排除项
    entries = [
        e for e in entries 
        if (e not in excluded_dirs) and 
        (not any(e.endswith(ext) for ext in excluded_extensions))
    ]

    for i, entry in enumerate(entries):
        path = os.path.join(startpath, entry)
        is_last = i == len(entries) - 1

        # 打印当前条目
        print(prefix + ('└── ' if is_last else '├── ') + entry)

        # 递归处理子目录
        if os.path.isdir(path):
            if max_depth is None or current_depth < max_depth:
                new_prefix = prefix + ('    ' if is_last else '│   ')
                print_directory_tree(
                    path,
                    excluded_dirs,
                    excluded_extensions,
                    max_depth,
                    current_depth + 1,
                    new_prefix
                )
            elif current_depth == max_depth:
                print(prefix + '    └── ...')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='生成项目目录树')
    parser.add_argument('--max-depth', type=int, default=None, help='最大显示深度')
    parser.add_argument('--root', type=str, default='.', help='项目根目录路径')
    args = parser.parse_args()

    project_root = Path(args.root).resolve()
    
    print("=" * 50)
    print(f"项目目录结构: {project_root} (深度限制: {'无' if args.max_depth is None else args.max_depth})")
    print("=" * 50)
    print_directory_tree(project_root, max_depth=args.max_depth)
    print("=" * 50)