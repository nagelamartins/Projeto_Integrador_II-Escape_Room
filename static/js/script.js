function configurarConfirmacao(mensagem) {
    const formularioOpcoes = document.querySelector(".opcoes");

    formularioOpcoes.addEventListener("submit", function (evento) {
        const confirmou = confirm(mensagem);

        if (!confirmou) {
            evento.preventDefault();
        }
    });
}