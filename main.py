from bs4 import BeautifulSoup
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_green(text):
    print(f'{bcolors.OKGREEN}{text}{bcolors.ENDC}')

def print_red(text):
    print(f'{bcolors.FAIL}{text}{bcolors.ENDC}')

def print_title(text):
    print(f'{bcolors.BOLD}{bcolors.WARNING}--{text}{bcolors.ENDC}')

def print_bold(text):
    print(f'{bcolors.BOLD}|   {text}   |{bcolors.ENDC}')




page_menu= 'https://online-sms.org/es'
result= requests.get(page_menu)
content=result.text
soup = BeautifulSoup(content, 'lxml')


def page_getter(page):
    result= requests.get(page)
    content= result.text
    soup= BeautifulSoup(content,'lxml')
    return soup


def search_numbers():
    number_list=[]
    block=soup.find('div', {"class":'row nbox'})
    number=block.find_all('a', {"class":"npn nol"})
    for x in number:
        number=x.get_text()[1:]
        number_list.append(number)
    return number_list #Devuelve todos los numeros que hay en la pagina




# print(search_numbers())

def reminders_search(cell_number,page_number):
    
    page_number_menu='https://online-sms.org/es/free-phone-number-{}?page={}'.format(cell_number,page_number)

    soup = page_getter(page_number_menu) #obtengo la pagina del numero que quiero
    
    #first_block= soup.find('table',{"class":"table table-condensed table-hover table-striped num-sms"})
    body= soup.find('tbody')

    message_blocks=body.find_all('tr')
    reminder_list=[]

    for message_block1 in message_blocks:
        results= message_block1.find_all('td')
        reminder_list.append(results[0].get_text())
    
    return reminder_list # Lista con los remitentes


def get_last_page(number):
    number_page='https://online-sms.org/es/free-phone-number-{}?page=1'.format(number)
    soup = page_getter(number_page)
    li = soup.find_all ("li", {"class":"page-item"})
    return (li[-2].get_text())


def all_numbers_page():
    for numero in search_numbers():
        print_title("Para el siguiente numero hemos encontrado los siguientes reminders:")
        print_red(numero)
        print("\n")
        one_number_only(numero)



def one_number_only(numero):
    hit_counter=0
    last_page=int(get_last_page(numero))
    for page_number in range (0,last_page+1):
        print_bold("Number of page: {}".format(page_number))
        for element in reminders_search(numero,page_number):
            if (element == "Twitter"):
                print_green(element)
                hit_counter+=1
            else:
                print(element)
    print_green("All hits: ".format(hit_counter))


one_number_only(33644624724)

        
    
    




