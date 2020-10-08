import requests
import pandas as pd
import numpy as np

def main():


    company_name = list()
    purpose = list()

    for i in range(0, 50):

        resp = requests.get("http://3.95.249.159:8000/random_company")

        # Split the text from the title
        text_name = resp.text.split('Name:')
        text_purpose = resp.text.split('Purpose:')

        # Split the text from </li>
        text_name_2 = text_name[1].split('</li>')[0]
        text_purpose_2 = text_purpose[1].split('</li>')[0]

        company_name = np.append(text_name_2, company_name)
        purpose = np.append(text_purpose_2, purpose)

        print(text_name_2)
        print(text_purpose_2)

    d = {'Company name': company_name, 'Company purpose': purpose}
    df = pd.DataFrame(data=d)
    df.to_csv('Mydata.csv')

if __name__ == "__main__":
    main()
