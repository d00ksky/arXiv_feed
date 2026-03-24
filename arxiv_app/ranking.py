from arxiv_app.models import Paper

def select_discovery_papers(papers: list[Paper], limit: int = 5) -> list[Paper]:
    # ''' •	preferuj nowsze papers
	#  •	ogranicz liczbę wyników
	#  •	zwróć mały sensowny zestaw'''
    # return sorted(papers, key=lambda paper: paper.year, reverse=True)[:limit]
    return papers[:limit]