import sys
import importlib


def check_env():
    # 1. Check if Virtual Environment (venv) is active
    # venv active hone par sys.prefix aur sys.base_prefix alag hote hain
    is_venv = sys.prefix != sys.base_prefix

    print("="*50)
    print("🛠️  SYSTEM AUDIT: VIRTUAL ENVIRONMENT & LIBRARIES")
    print("="*50)

    if is_venv:
        print(f"✅ VENV STATUS: Active (Path: {sys.prefix})")
    else:
        print("❌ VENV STATUS: NOT ACTIVE! (Base Python use ho raha hai)")
        print("💡 Tip: Run on Linux/Mac ' source /.venv/bin/activate' .")

    print("-" * 50)

    # 2. Check Libraries from your requirements.txt
    libraries = {
        "bs4": "beautifulsoup4",
        "mysql.connector": "mysql-connector-python",
        "numpy": "numpy",
        "pandas": "pandas",
        "requests": "requests"
    }

    missing_libs = []

    print("📦 LIBRARY STATUS:")
    for lib in libraries:
        try:
            importlib.import_module(lib)
            print(f"✅ {lib: <15} : Installed")
        except ImportError:
            print(f"❌ {lib: <15} : MISSING")
            missing_libs.append(lib) # type: ignore

    print("-" * 50)

    # Final Verdict
    if is_venv and not missing_libs:
        print("🚀 VERDICT: System Ready! Start coding.")
    else:
        print("⚠️  VERDICT: Setup incomplete. Some libraries are missing.")
    print("="*50)


if __name__ == "__main__":
    check_env()

print("\n")
