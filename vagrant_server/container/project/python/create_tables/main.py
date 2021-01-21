from code.main import create
from code.main import scraping
from code.code.in_data import all_in
from code.main import insertmain
from code.main import testdata


if __name__=='__main__':
    print("start")
    create.create_pdb()
    scraping.main()
    # insertmain.insert_data(item_list)
    # item_list = testdata.testdata()
    # dictio = scraping.main()
    # print(dictio)
    
