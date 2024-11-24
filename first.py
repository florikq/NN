import fitz


def fill_pdf_form(input_pdf_path, output_pdf_path):
    """
    Fill PDF form fields with specified values while keeping fields interactive

    Args:
        input_pdf_path (str): Path to the input PDF file
        output_pdf_path (str): Path where to save the filled PDF
    """
    # Open the PDF
    doc = fitz.open(input_pdf_path)

    # Get the first page
    page = doc[0]

    # Get form fields
    widgets = page.widgets()

    # Find and fill the Surname field
    for widget in widgets:
        if widget.field_name == "Surname":
            widget.field_value = "Artem"
            widget.update()

    # Save the modified PDF
    doc.save(output_pdf_path)
    doc.close()


# Example usage
if __name__ == "__main__":
    fill_pdf_form('test.pdf', 'output_filled.pdf')