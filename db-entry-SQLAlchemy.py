from database import get_all_Persons, get_all_Sample, get_all_S_aureus, get_all_COVID19, get_all_Batch, get_all_Legionella, get_all_S_epidermidis, get_all_SequencedSample

def main():                         
    result = get_all_S_epidermidis()
    print(result[:10])

if __name__ == main():
    main()