import os
import settings


def change_docker_file(service_path: str, parent_image: str) -> None:
    docker_file = os.path.join(service_path, settings.DOCKERFILE)
    dev_docker_file = os.path.join(service_path, settings.DEV_DOCKERFILE)

    for file in [dev_docker_file, docker_file]:
        if not os.path.exists(file):
            continue

        with open(file, "r") as f:
            lines = f.readlines()

        with open(file, "w") as f:
            for line in lines:
                if line.startswith("FROM"):
                    f.write(f"FROM {parent_image}\n")
                else:
                    f.write(line)


def extract_versions(path: str) -> dict:
    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "=" in line:
            image, version = line.strip().split("=")
        else:
            continue
        if image == settings.MINI_VERSION:
            mini = version
        elif image == settings.COMMON_VERSION:
            common = version
        elif image == settings.EXEC_ENV_VERSION:
            exec_env = version
        elif image == settings.TORCH_CPU_VERSION:
            torch_cpu = version
        else:
            continue
        print(f"{image}={version}")
    return mini, common, exec_env, torch_cpu


if __name__ == "__main__":
    print("The versions of the versions file are used. Currently:")
    if os.path.exists(settings.VERSIONS_FILE):
        mini, common, exec_env, torch_cpu = extract_versions("versions")
    elif os.path.exists(os.path.join("..", settings.VERSIONS_FILE)):
        mini, common, exec_env, torch_cpu = extract_versions("../versions")
    else:
        print("No versions file found.")
    input("Press enter to continue. Or press ctrl+c to abort.")

    print("Select a registry:")
    while True:
        registry = input("[k] for kernai, [o] for onetask")
        if registry == "k":
            registry = settings.DOCKERHUB_REGISTRY
        elif registry == "o":
            registry = settings.ONETASK_REGISTRY
            break
        print("Please select a valid option.")

    for service, path in settings.MINI_PATHS:
        change_docker_file(path, settings.MINI_PARENT_IMAGE.format(version=mini))
    for service, path in settings.COMMON_PATHS:
        change_docker_file(path, settings.COMMON_PARENT_IMAGE.format(version=common))
    for service, path in settings.EXEC_ENV_PATHS:
        change_docker_file(
            path, settings.EXEC_ENV_PARENT_IMAGE.format(version=exec_env)
        )
    for service, path in settings.TORCH_CPU_PATHS:
        change_docker_file(
            path, settings.TORCH_CPU_PARENT_IMAGE.format(version=torch_cpu)
        )
