class GraphContextBuilder:

    @staticmethod
    def build(graph_data: dict) -> str:

        context = []

        context.append(
            f"Company: {graph_data['company']}"
        )

        # -----------------------------
        # Products
        # -----------------------------
        if graph_data["products"]:

            context.append("\nProducts:")

            for product in graph_data["products"]:

                context.append(f"- {product}")

        # -----------------------------
        # Risks
        # -----------------------------
        if graph_data["risks"]:

            context.append("\nRisks:")

            for risk in graph_data["risks"]:

                context.append(f"- {risk}")

        # -----------------------------
        # Technologies
        # -----------------------------
        if graph_data["technologies"]:

            context.append("\nTechnologies:")

            for tech in graph_data["technologies"]:

                context.append(f"- {tech}")

        # -----------------------------
        # Business Segments
        # -----------------------------
        if graph_data["segments"]:

            context.append("\nBusiness Segments:")

            for segment in graph_data["segments"]:

                context.append(f"- {segment}")

        # -----------------------------
        # Countries
        # -----------------------------
        if graph_data["countries"]:

            context.append("\nCountries:")

            for country in graph_data["countries"]:

                context.append(f"- {country}")

        # -----------------------------
        # Competitors
        # -----------------------------
        if graph_data["competitors"]:

            context.append("\nCompetitors:")

            for competitor in graph_data["competitors"]:

                context.append(f"- {competitor}")

        return "\n".join(context)