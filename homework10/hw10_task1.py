import requests

from urllib.parse import urljoin

from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor


pages_urls = []
for page in range(1, 12):
    page_url = 'https://markets.businessinsider.com/index/components/s&p_500?p=' + str(page)
    pages_urls.append(page_url)


def get_company_list(p_url):  # processing one page out of 12
    response = requests.get(p_url)
    html_insider = BeautifulSoup(response.text, features="html.parser")
    h = html_insider.body
    body = h.find("tbody", class_="table__tbody")
    companies = []
    for row in body.findAll("tr"):
        company = {}
        for cell in row.findAll('td'):
            a = cell.find('a')
            if a:
                company['name'] = a.text
                company['link'] = cell.find(href=True).get('href')
                full_link = company['link']
                full_link = urljoin('https://markets.businessinsider.com/', full_link)
                response = requests.get(full_link)
                html_company = BeautifulSoup(response.text, features="html.parser")
                v = html_company.find('span', class_="price-section__current-value").text
                company['value'] = float(v.replace(',',''))
                items = html_company.findAll('div', class_="snapshot__data-item")
                for item in items:
                    f = item.find(class_='snapshot__header').text
                    if f == "P/E Ratio":
                        p_e_value = item.text.strip()[0:5]
                        company[f] = float(p_e_value.replace(',',''))
                    if f == "52 Week Low":
                        low = float(item.text[:20].strip().replace(',', ''))
                    if f == "52 Week High":
                        high = float(item.text[:20].strip().replace(',', ''))
                        company['potential_profit_%'] = round(((high - low) / low * 100), 2)
        if row.findAll('span', class_="colorGreen"):
            for cell in row.findAll('span', class_="colorGreen")[-1]:
                company['1_year'] = float(cell.text.replace('%',''))
        companies.append(company)
    res = [x for x in a for a in companies]
    print(res)
    return res


with ThreadPoolExecutor(max_workers=12) as pool:
    comps = list(pool.map(get_company_list, pages_urls))
    print(len(comps))

# sorted_by_price = sorted(comps, key=lambda k: k['value'], reverse=True)
# ten_most_expensive = sorted_by_price[10]  # ten companies with most expensive stocks???? is that right?
# sorted_by_P_E_Ratio = sorted(comps, key=lambda k: k['P/E Ratio'])
# ten_lowest_P_E_Ratio = sorted_by_P_E_Ratio[0:10]  # ten companies with lowest P/E Ratio
# sorted_by_growth = sorted(comps, key=lambda k: k['1_year'], reverse=true)
# ten_biggest_growth = sorted_by_growth[10]    # ten companies with biggest 1 year growth
# sorted_by_pot_profit = sorted(comps, key=lambda k: k['potential_profit_%'], reverse=True)
# ten_biggest_pt_profit = sorted_by_pot_profit[10]   # ten companies with biggest potential profit
#
# curr = requests.get('https://www.cbr-xml-daily.ru/daily_json.js') #  current usd values
# curr_usd = curr.json()['Valute']['USD']['Value']
#
# for one in ten_most_expensive:
#     one["value"] = one["value"] * curr_usd
#
# print(ten_most_expensive)
