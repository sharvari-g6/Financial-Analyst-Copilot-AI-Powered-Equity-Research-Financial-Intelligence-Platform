from backend.app.database.pinecone_db import PineconeDB


def main():

    db = PineconeDB()

    stats = db.get_index_stats()

    print("\nConnected to Pinecone Successfully!\n")

    print(stats)


if __name__ == "__main__":
    main()