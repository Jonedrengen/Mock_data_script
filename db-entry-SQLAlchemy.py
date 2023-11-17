from database import get_all_Persons

def main():                         
    result = get_all_Persons()
    print(result[:10])

if __name__ == main():
    main()