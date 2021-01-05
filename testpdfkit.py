import pdfkit    


if __name__ == '__main__':
    pdfkit.from_string("<center><h1>Hello World!</h1><p>first test with pdfkit</p></center>", "out.pdf")

    