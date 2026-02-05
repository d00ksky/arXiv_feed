from arxiv_client import fetch_papers

def main():
    papers = fetch_papers("machine learning")
    print(len(papers))

if __name__ == "__main__":
    main()
