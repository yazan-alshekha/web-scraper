import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):

    """
     Counts how many 'citation needed' in the article.
     Arguments:
        url : {string} The url of the website to scrap from.
     Output:
        {integer} number of citation needed.
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    all=[]
    for i in results:
        try:
            all_p = i.find_all('span', string = lambda text: 'citation' in text.lower())
            if all_p :
                for j in range(len(all_p)): # If there is more than 1 citation needed in the same paragragh
                    all.append(all_p[j])
        except Exception as e:
            continue
    return len(all)





def get_citations_needed_report(url):

    """
     Will return a report indicating where each citation is needed, the report will contain 
     the paragragh(that needs citation) and the line before citation is needed.
     The report will be stored in citation.txt file.
     Arguments:
        url : {string} The url of the website to scrap from.
     Output:
        output : {string} Contains the report, it can also be found in citation.txt file.
    """
    # prepare url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    all_para  = []
    all_line = []

    # Find all paragraphs that contains a span which also contains 'citation needed'
    results_k = results.find_all('p')
    for i in results_k:
        try:
            all_p = i.find_all('span', string = lambda text: 'citation' in text.lower())
            if all_p:
                for j in range(len(all_p)):

                        # For the whole paragraph
                        all_para.append(i.text) 

                        # For the line
                        pos = i.text.index('citation') 
                        line = i.text[:pos-1].split(". ")
                        all_line.append(line[-1])

                        
        except Exception as e:
            continue
            
    # Construct the report
    output = ''
    for p in range(len(all_para)):
        output += f'-------------------------------------------------\n'
        output += f'Citation Number {p+1} \n'
        output += f'A Citation is needed for this paraghraph: \n'
        output += f'{all_para[p]} \n'
        output += f'After this line: \n'
        output += f'{all_line[p]} \n'

    # Store in a file
    f = open("citation.txt", "w")
    f.write(output)
    f.close()

    return output




if __name__ == "__main__":
    # URL = "https://en.wikipedia.org/wiki/Petra"
    # print(get_citations_needed_report(URL))
    # print(get_citations_needed_count(URL))