from API import BaseApi

def main():

    api_caller = BaseApi.AmadeusAPI()
    while(1):
        query = input("Please provide a query or type stop to finish session:\n")
        if query.lower() == 'stop':
            exit(0)
        resp = api_caller.query(query)
        print(resp)


if __name__ == '__main__':
    main()

