from fpdf import FPDF

project       = input("Descreva o Projeto: ")
expectedHours = input("Digita a quantidade de horas previstas: ")
priceHour     = input("Digite o valor da hora cobrada: ")
term          = input("Digite o prazo estimado: ")
amount        =  int(expectedHours) * int(priceHour)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, project)
pdf.text(115, 160, expectedHours)
pdf.text(115, 175, priceHour)
pdf.text(115, 190, term)
pdf.text(115, 205, str(amount))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")

