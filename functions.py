import os
import platform
import datetime
import cv2
import PyPDF2 as pdf
import socket

#pip install easyimap {for Email}
def length_string(s):
    """this function which gives the length of the given string
    arg s: string type
    """
    l = 0
    if type(s) == str:
        for i in s:
            l+=1
    else:
        print('it is not a string')
    return l


def index_of_elements(arg):
    """this function gives you the index of each element
    arg: any primitive data type"""
    if type(arg) == int:
        print('index object does not have a index')
    elif type(arg) == list or type(arg) == tuple or type(arg) == dict or type(arg) == str:
        j = 0
        for i in arg:
            print(i,'index:',j)
            j+=1


def dict_list(arg):
    """ This function converts dictionary into list and it unwraps the nested dictionaries also.
    :param arg: dictionary
    :return l: list of all elements
    """
    l = []
    if type(arg) == dict:
        for i in arg.values():
            if type(i) == dict:
                l1 = dict_list(i)
                l = l+l1
            else:
                l.append(i)
    else:
        print('input is not a dictionary')
    return l


def concatanationoflists(*args):
    """
    this function takes any number of lists and concatnates them into single list
    :param *args: input is multiple lists
    :return l: concatanated list of all the input lists
    """
    l = []
    for i in args:
        if type(i) == list:
            l = l+i
        else:
            print(i,'is not a list')
    return l


def indexes(arg,listarg):
    """
    this function searches the given element in the given list and returns index of all occurances
    :param arg: element for which index need to search
    :param listarg: list in which the element need to be search
    :return I: list of indexes where the element exists in the list
    """
    I = []
    index = 0
    for i in listarg:
        if i == arg:
            I.append(index)
        index+=1
    return I


def filesindir(path):
    """
    :param path: it is string contains the path of the directory
    :return : it is list which contains the files of the given path
    """
    return os.listdir(path)


def getsysinfo():
    """
    psutil library can be used to get RAM details
    :return:
    """
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info["machine"] = platform.machine()
        info['architecure'] = platform.architecture()
        #inf0['freeos'] = platform.freedesktop_os_release()
        info['processor'] = platform.processor()
        info['Node'] = platform.node()
        info['others'] = platform.win32_edition()
        info1 = platform.uname()
        return info, info1
    except Exception as e:
        print(e)


f=open('sysinfo.txt','w')
info ,info1= getsysinfo()
for i in info:
    f.write(str(i))
    f.write(':')
    f.write(str(info[i]))
    f.write('\r')
f.writelines(info1)
f.close()

#subprocess library also can be used
print(datetime.date.today())
print(datetime.datetime.utcnow())


def showimg(imagepath):
    """
    :param imagepath: takes the image path in string format and displays the image
    :return:
    """
    img1 = cv2.imread(imagepath)
    cv2.imshow('image',img1)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

showimg('14419.jpg')

def fun12(src_path, dst_path):
    """
    This function will1 move a file from one directory to another directory
    """
    import shutil
    shutil.move(src_path, dst_path )


#src_path=input ("Please enter the source directory path")
#dst_path=input ("please enter the destination directory path")

def shutdown():
    os.system('shutdown /s /t 1')
        # or
    #shut = 'shutdown /s'
    #return shut
#shutdown()

def pdfread(pdfpath):
    """
    This furctior will reed a complete pdtf file
    """
    f = open(pdfpath,'rb')
    f_read=pdf.PdfFileReader(f)
    f_page = f_read.getpage()
    print(f_page.extractText())
    f.clsoe()

def openwordfile(path):
    """

    :param path: takes the word file path in string format
    :return:
    """
    f=open(path,'r')
    print(f.read())

def wordfile_filter(dir):
    a=os.walk(dir)
    l=[]
    dir_list=list(a)
    import re
    pattern = re.compile(r"\.doc$")
    for l in dir_list:
        if type(l) == tuple:
            for dirct in l:
                if type(dirct)==list:
                    for file in dirct:
                        matches = pattern.finditer(file)
                        for match in matches:
                            l.append(file)
                            #above function get the wordfiles from deep inside directories in given path also
    #use os.listdir() so it will give list of all files and folders in given directory and then filter .doc and .docx files
    return l, dir_list
    """
    def wordfilefilter(dir = os.getcwd()):
        os.chdir(dir)
        files = os.listdir()
        
        for i in files:
            if i.endswith('.doc','.docx'):
                print(os.path.join(i)
                    or 
            file_details = os.path.splitext(i)
            if file_deatils[1] = '.doc' or file_details[1] = '.docx'
                print(i)
    """
def getip():
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    return ip
print(getip())


def appendpdf(*args):
    """

    :param *args: paths of mutliple pdf files in string format
    :return:
    """
    finalpdf = open('finaldoc'+str(datetime.datetime.now()),+'.pdf','wb')
    f_writer = pdf.PdfFileWriter()
    for i in args:
        f = open(i,'rb')
        fread = pdf.PdfFileReader(f)
        for page_no in range(fread.numPages):
            fpages = fread.getPage(page_no)
            f_writer.addPage(fpages)
        f.close()
    f_writer.write(finalpdf)
    finalpdf.close()
            #or
    from PyPDF2 import PdfFileMerger
    for pdf in args:
        merger.append(open(pdf,'rb'))
    with open('output_file.pdf','wb') as fileout:
        merger.write(fileout)

def playvideo(path):
    video = cv2.VideoCapture(path)

    while(video.isOpened()):
        ret,frame = video.read()
        if ret == True:
            cv2.imshow('Video',frame)
            if cv2.waitKey(24) & 0xFF == ord(x):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
        # or
    #from os import startfile
    #startfile(path)



