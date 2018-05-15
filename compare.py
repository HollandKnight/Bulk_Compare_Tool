
# coding: utf-8

# # Bulk Comparison Generator

# #### *Install libraries*

# In[1]:


#get_ipython().system('pip install PyPDF2')
#get_ipython().system('pip install nbconvert')
#get_ipython().system('pip install textract')


# #### *Import Modules*

# In[3]:


from diff_match_patch import diff_match_patch
import codecs
import ipywidgets as widgets
from IPython.display import display, HTML
import os



# #### *Iterate through all files in designated folder.*

# In[4]:


dmp = diff_match_patch() #create instance of diff class
cwd = os.getcwd() #returns current directory
path = cwd + '/' + 'test/' #create folder named 'test' in current directory
diff = ''

with codecs.open(path + 'base.txt', 'r', encoding='utf-8', errors='ignore') as myfile:      #load base file
        old_text=myfile.read().replace('\n', '')                                            #read base file into string
        diff = 'base document' + '<p></p>' + old_text                                       #generate styled html of base text
for filename in os.listdir(path):                                                           #iterate through every file in the test folder
    print(filename)                                                                         #print file being compared to base
    with codecs.open(path + filename, 'r', encoding='utf-8', errors='ignore') as myfile:    #load new file
        new_text=myfile.read().replace('\n', '')                                            #read new file into string
    d = dmp.diff_main(old_text, new_text)                                                   #compare new file against the base file
    diff = diff + '<p></p>' + filename + '<p></p>' + dmp.diff_prettyHtml(d);                #style as more readable html
    Html_file= open("compare_file.html","w")                                                #create and open target file to write readable html
    Html_file.write(diff)                                                                   #write output to file 'compare_file.html'
    Html_file.close()                                                                       #close file


# In[5]:


with open('compare_file.html', 'r') as myfile:                                              #open html file 
    display_text=myfile.read()                                                              #read file
    display(HTML(display_text))                                                             #display file
 
