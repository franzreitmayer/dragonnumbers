import numpy
import pdfkit



class Generator:
    def __init__(self):
        pass
    def generate_numbers():
        first = numpy.empty(5)
        last  = numpy.empty(5)
        first.fill(0.9/5)
        last.fill(0.1/5);
        probs = numpy.concatenate((first, last))
        choices = numpy.arange(1,11, dtype=int) 

        ran = numpy.random.choice(choices,p = probs)
        li = [ ran ]
        sum = ran
        for x in range(5):
            ran = numpy.random.choice(choices,p = probs)
            sum = sum + ran
            if sum > 10:
                break
            else:
                li.append(ran)
        return li

def main():
    generator = Generator
    html_string = "<center><h1>Drachenaufgaben</h1></center>"
    for i in range(1, 20):
        li = generator.generate_numbers()
        if len(li) <= 1:
            continue
        html_string += "<p><table border='1'>"
        for i in range(len(li)):
            html_string += "<tr><td>St&auml;rke Drache " + str(i+1) + "</td><td>" + str(li[i]) + "</td></tr>" 
        html_string += "<tr><td>Gesamt</td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr></table>"
    pdfkit.from_string(html_string, "dragon.pdf")
    

if __name__ == '__main__':
    main()