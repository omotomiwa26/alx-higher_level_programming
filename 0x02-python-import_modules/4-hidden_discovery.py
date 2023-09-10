#!/usr/bin/python3
import importlib.util
if __name__ == "__main__":
    def hidden_discovery():
        spec = importlib.util.spec_from_file_location(
            "hidden_4", "hidden_4.pyc")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        module_names = dir(module)
        filtered_names = sorted(
             name for name in module_names if not name.startswitch('__')
        )

        for name in filtered_names:
            print(name)
