from core.metrics import count_chapters, count_modules, read_builds


def collect_metrics(root, project_path, project):
    builds = read_builds(project_path)
    return {
        "project": project.name,
        "version": project.version,
        "kernel": "Online",
        "builder": "Pronto",
        "modules": count_modules(root),
        "chapters": count_chapters(project_path),
        "last_build": builds[0]["timestamp"] if builds else None,
        "module_names": [],
    }