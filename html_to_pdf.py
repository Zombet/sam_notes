from weasyprint import HTML

def html_to_pdf(input_html, output_pdf):
    try:
        # Convert HTML to PDF
        HTML(input_html).write_pdf(output_pdf)
        print(f"PDF saved as {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")

'''file_name = input('Enter name of the HTML file: ')
html_file = file_name + '.html'
output_pdf = file_name + '.pdf'''
html_to_pdf(r"C:\Users\sadiq\OneDrive\Desktop\samsung\rnsit_sam_py\day6\Certificate_Generator(White)\Certificate_Generator(White)\html_certificates\Ifrah Sadiq _ 1RN23CS088.html",r"C:\Users\sadiq\OneDrive\Desktop\Ifrah Sadiq _ 1RN23CS088.pdf")

