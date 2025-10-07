from flask import Flask, request, render_template, redirect, url_for # type: ignore
import api_client
import config

app = Flask(__name__)

# Rota principal: exibe o formulário e, no POST, chama o api_client.
@app.route("/", methods=["GET", "POST"])
def index():
    # Defaults
    sign = getattr(config, "DEFAULT_SIGN", "") or ""
    date = ""  # opcional: usamos no formulário, mas neste exemplo seu api_client já busca a data de hoje

    result = None

    if request.method == "POST":
        # pegar valores do formulário
        sign = (request.form.get("sign") or "").strip().lower()
        date = (request.form.get("date") or "").strip()

        if not sign:
            # redirecionar para GET com mensagem simples seria ideal; aqui só renderizamos sem chamar a API
            result = {"ok": False, "status_code": None, "error": "Informe um signo válido."}
        else:
            # Chama seu client. 
            # Passa timeout via config se definido
            timeout = getattr(config, "API_TIMEOUT", 10)
            result = api_client.get_daily_horoscope(sign=sign, timeout=timeout)

    return render_template("index.html", result=result, sign=sign, date=date)

if __name__ == "__main__":
    # modo de desenvolvimento: debug True
    app.run(debug=True, host="127.0.0.1", port=5000)