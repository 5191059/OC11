from cord.main import create
from cord.main import scraping
from cord.cord.in_data import all_in
from cord.main import insertmain
from cord.main import testdata


if __name__=='__main__':
    print("start")
    create.create_pdb()
    scraping.main()
    # insertmain.insert_data(item_list)
    # item_list = testdata.testdata()
    # dictio = scraping.main()
    # print(dictio)
    
