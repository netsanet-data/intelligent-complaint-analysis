def generate_answer(question, retrieved_chunks):

    answer = "Based on the retrieved customer complaints:\n\n"

    for _, row in retrieved_chunks.iterrows():
        answer += "- " + row["chunk"] + "\n\n"

    return answer