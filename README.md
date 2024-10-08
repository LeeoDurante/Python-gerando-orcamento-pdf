
# Projeto: Gerador de Orçamento

Este projeto permite a criação de orçamentos a partir de informações fornecidas pelo usuário, como descrição do projeto, horas previstas e valor cobrado por hora. O orçamento gerado é automaticamente convertido em um arquivo PDF.

## Funcionalidades

* O usuário insere as informações do projeto, como descrição, horas estimadas, valor por hora e prazo.
* O projeto calcula o valor total do orçamento com base nas horas previstas e no valor da hora.
* Um arquivo PDF é gerado com as informações do projeto e o valor final.

## Tecnologias Utilizadas

* **Python 3**
* **fpdf**: Biblioteca utilizada para a criação de PDFs.

## Pré-requisitos

Para executar este projeto, você precisará instalar a seguinte biblioteca:

```bash
pip install fpdf
