import os
from pathlib import Path

# Define root folder
ROOT_DIR = "neuron-sql"

# Define layout directories
DIRECTORIES = [
    "backend/app/api",
    "backend/app/application/services",
    "backend/app/application/dto",
    "backend/app/domain/models",
    "backend/app/domain/interfaces",
    "backend/app/infrastructure/database",
    "backend/app/infrastructure/llm",
    "backend/app/infrastructure/embeddings",
    "backend/app/infrastructure/vectorstore",
    "backend/app/infrastructure/logging",
    "backend/app/workflow",
    "backend/app/config",
    "backend/app/core",
    "backend/tests",
    "backend/docs",
    "backend/requirements",
]

# Define concrete implementation files
FILES = [
    "backend/app/main.py",
]


def generate_ddd_structure():
    root = Path(ROOT_DIR)

    # 1. Build out target folder hierarchy
    for rel_path in DIRECTORIES:
        dir_path = root / rel_path
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created: {dir_path}")

        # Auto-create intermediate python module files (__init__.py)
        if "backend/app" in rel_path or "backend/tests" in rel_path:
            # We walk up to make sure parent layer folders also get initialized
            current_dir = dir_path
            while current_dir != root / "backend":
                init_file = current_dir / "__init__.py"
                init_file.touch(exist_ok=True)
                current_dir = current_dir.parent

    # 2. Add base files
    for rel_file in FILES:
        file_path = root / rel_file
        file_path.touch(exist_ok=True)
        print(f"📄 Created: {file_path}")

    print("\n✅ Architecture setup complete! Codebase is ready for development.")


if __name__ == "__main__":
    generate_ddd_structure()
