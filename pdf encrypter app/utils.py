from PyPDF2 import PdfReader,PdfWriter

def encrypter(input_path,outer_path,password):
    reader=PdfReader(input_path)
    writer=PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    
    with open(outer_path,'wb') as f:
        writer.write(f)
        
def decrypter(input_path,output_path,password):
    reader=PdfReader(input_path)
    if reader.is_encrypted:
        reader.decrypt(password)
        
    writer=PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
        
        
    with open(output_path,'wb') as f:
        
        writer.write(f)