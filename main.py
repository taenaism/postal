from postcode import APIClient 
import sys

"""
pip install ./postal
py -m postal.main ?
py -m postal.main "CB3 0FA"
py -m postal.main "SW1W 0NY"
py -m postal.main "X"
py -m postal.main
"""
def main(input=None):
    try:
        if input is None:
            return 'no input'

        POSTCODE= input
        client = APIClient()

        if client.PostCodes.validate(POSTCODE) != True:
            print('PostCode is not valid')
            return 'invalid'

        result = client.PostCodes.getPostCode(POSTCODE)
        print(f'Country and region of {POSTCODE}:')
        print(result)
        print()

        nearest = client.PostCodes.nearest(POSTCODE)
        print('List of nearest postcodes with their country and region:')
        for x in nearest:
            print(f'Postcode:{x["postcode"]}')
            print(f'Country:{x["country"]}')
            print(f'Region:{x["region"]}')
            print()
        
        return True

    except Exception as ex:
            print((f"Encountered Error: {ex}"))
            raise ex

if __name__ == "__main__":
    if sys.argv.__len__() < 2:
        print('Please enter a postal code')
        exit()
    try:
        main(sys.argv[1])
    except Exception as e:
        pass
    
