from app.services.recommendation_service import (
    generate_recommendations
)


def main():

    print("\nFIRST CALL")
    result = generate_recommendations(101)
    print(result)

    print("\nSECOND CALL")
    result = generate_recommendations(101)
    print(result)


if __name__ == "__main__":
    main()