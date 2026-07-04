from backend.app.llm.llm_client import LLMClient


def main():

    llm = LLMClient()

    response = llm.generate(

        """
        Explain in simple words what an annual report is.
        Keep the answer under 100 words.
        """

    )

    print()

    print(response)


if __name__ == "__main__":
    main()