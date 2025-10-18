from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)

PASTA_PDFS = os.path.join(os.getcwd(), "static", "pdfs")

@app.route("/", methods=["GET", "POST"])
def index():
    pdf_path = None
    erro = None

    if request.method == "POST":
        numero_processo = request.form.get("numero_processo", "").strip()
        if numero_processo:
            numero_limpo = re.sub(r'\D', "", numero_processo)

            if not os.path.exists(PASTA_PDFS):
                erro = "A pasta de PDFs não existe. Por favor, crie 'static/pdfs' e adicione os arquivos."
            else:
                for arquivo in os.listdir(PASTA_PDFS):
                    nome_limpo = re.sub(r'\D', '', arquivo)
                    if numero_limpo in nome_limpo:
                        pdf_path = f"static/pdfs/{arquivo}"
                        break

                if not pdf_path and not erro:
                    erro = "PDF não encontrado para esse número de processo."

    return render_template("index.html", pdf_path=pdf_path, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
