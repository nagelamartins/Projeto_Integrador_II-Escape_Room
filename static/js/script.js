function configurarConfirmacao(mensagem) {
    const formularioOpcoes = document.querySelector(".opcoes");

    formularioOpcoes.addEventListener("submit", function (evento) {
        const confirmou = confirm(mensagem);

        if (!confirmou) {
            evento.preventDefault();
        }
    });
}

function efeitoDigitacao(seletor, velocidade = 25) {
    const container = document.querySelector(seletor);

    container.style.minHeight = container.offsetHeight + "px";

    const paragrafos = container.querySelectorAll("p");

    const textosOriginais = [];
    paragrafos.forEach(function (p) {
        textosOriginais.push(p.textContent);
        p.textContent = "";
    });

    let paragrafoAtual = 0;
    let caractereAtual = 0;

    function digitarProximaLetra() {
        if (paragrafoAtual >= paragrafos.length) {
            return;
        }

        const textoDoParagrafo = textosOriginais[paragrafoAtual];

        if (caractereAtual < textoDoParagrafo.length) {
            paragrafos[paragrafoAtual].textContent += textoDoParagrafo[caractereAtual];
            caractereAtual++;
            setTimeout(digitarProximaLetra, velocidade);
        } else {
            paragrafoAtual++;
            caractereAtual = 0;
            setTimeout(digitarProximaLetra, velocidade * 6);
        }
    }

    digitarProximaLetra();
}