import argparse
from agent import PRDAgent
from utils import pretty_print

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="PRD文件路径")
    args = parser.parse_args()

    if not args.file:
        print("请提供PRD文件路径")
        return

    with open(args.file, "r", encoding="utf-8") as f:
        prd_text = f.read()

    agent = PRDAgent()
    result = agent.run(prd_text)

    print("\n===== 最终结果 =====\n")
    pretty_print(result)

if __name__ == "__main__":
    main()
