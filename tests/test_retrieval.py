from rag.retrieval import rechercher_passages


def test_rechercher_passages_renvoie_des_resultats():
    question = "What does GDPR protect?" 

    passages, distances, sources = rechercher_passages(question, k=3)

    assert len(passages) > 0
    assert len(passages) <= 3
    assert len(passages) == len(distances) == len(sources)