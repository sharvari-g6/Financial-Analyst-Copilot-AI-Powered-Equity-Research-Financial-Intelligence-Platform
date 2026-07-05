from backend.app.router.agent_router import AgentRouter


def main():

    router = AgentRouter()

    reports = router.route(

        company="Apple",

        query="Analyze Apple"

    )

    print("\n" + "=" * 80)
    print("REPORTS GENERATED")
    print("=" * 80)

    for report_name in reports:

        print(report_name)


if __name__ == "__main__":
    main()