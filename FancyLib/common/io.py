import os

def enumerate_files(dir_root: str, search_pattern: str, recursive: bool = False):
    dir_stack = []
    dir_stack.append(dir_root)
    while len(dir_stack) > 0:
        dir_path = dir_stack.pop()
        entities = os.listdir(dir_path)
        for entity in entities:
            entity_full_path = os.path.join(dir_path, entity)
            if os.path.isdir(entity_full_path):
                dir_stack.append(entity_full_path)
                continue
            if str(entity).lower().endswith('.py'):
                yield entity_full_path

def enumerate_subfiles_nonrecursive(dir_root: str, search_pattern: str):
    for entity in os.listdir(dir_root):
        entity_full_path = os.path.join(dir_root, entity)
        if os.path.isdir(entity_full_path):
            continue
        