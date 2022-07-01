from gtts import gTTS
import PyPDF2


def create_audio_section(page_start: int, page_end: int, chapter_name: str, pdf: str):
    """
    Processes text from desired pdf, outputs an mp3 file.

    Args:
        page_start (int): Page to start processing text.
        page_end (int): Page to stop processing text.
        chapter_name (str): name for the output file.
        pdf (str): Name of the pdf required for the processing.
    """
    
    # Open the pdf file
    pdf_file = open(pdf + ".pdf", 'rb')
    language = "en"
    # Create the pdf reader
    try:
        reader = PyPDF2.PdfFileReader(pdf_file)
    except FileNotFoundError:
        print("File not found!")
    
    # Empty list to populate with page strings
    pages_text = []
    # Loop through pages and add to list
    for page in range(page_start, page_end + 1):
        current_page = reader.getPage(page)
        pages_text.append(current_page.extractText())
    
    # Close file 
    pdf_file.close()
    # Join string
    final_string = " ".join(pages_text)
    # Create TTS object
    try:
        tts_object = gTTS(text=final_string, lang=language, slow=False)
        tts_object.save(f"{chapter_name}.mp3")
    except:
        print("Yeah.... Something really went wrong here...\n Probably internet issues.. Yeah definately internet issues..")
    
    
if __name__ == "__main__":
    print("Welcome to PDF to Text To Speech.\n\n**WARNING**\nPlease make sure you are connected to the internet.\n")
    form_completed = False
    
    while not form_completed:
        try:
            # Get user input for passing into create_audio_section:
            user_spec_start = int(input("Please enter the starting page: "))
            user_spec_end = int(input("Please enter the ending page: "))       
            user_pdf = input("Please enter pdf name: ")
            test_file = open(f"{user_pdf}.pdf", "rb")
            test_reader = PyPDF2.PdfFileReader(test_file)
            user_file_name = input("Please enter desired filename: ")
            form_completed = True            
        except ValueError:
            print("\n**Found not number! Please enter a number.**")
            print("Please start again.\n")
        except FileNotFoundError:
            print("\n**The file you specified does not exist.**")
            print("Please start again.\n")
        
    if form_completed:
        print("Please wait while your mp3 file is created.")
        create_audio_section(
            page_start=user_spec_start, 
            page_end=user_spec_end,
            pdf=user_pdf,
            chapter_name=user_file_name)
        print("File creation complete!")

