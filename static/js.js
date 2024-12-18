// Calcula o total1 e atualiza de a cordo com o preenchemento dos campos da coluna correspondente
function atualizarTotal1() {
    var dinheiro1 = parseFloat(document.querySelector('input[name="dinheiro1"]').value) || 0;
    var cartao_cred1 = parseFloat(document.querySelector('input[name="cartao_cred1"]').value) || 0;
    var cartao_deb1 = parseFloat(document.querySelector('input[name="cartao_deb1"]').value) || 0;
    var pix1 = parseFloat(document.querySelector('input[name="pix1"]').value) || 0;
    var cheque1 = parseFloat(document.querySelector('input[name="cheque1"]').value) || 0;
    var total1 = dinheiro1 + cartao_cred1 + cartao_deb1 + pix1 + cheque1;
    document.querySelector('input[name="total1"]').value = total1.toFixed(2);
}

// Calcula o total2 e atualiza de a cordo com o preenchemento dos campos da coluna correspondente
function atualizarTotal2() {
    var dinheiro2 = parseFloat(document.querySelector('input[name="dinheiro2"]').value) || 0;
    var cartao_cred2 = parseFloat(document.querySelector('input[name="cartao_cred2"]').value) || 0;
    var cartao_deb2 = parseFloat(document.querySelector('input[name="cartao_deb2"]').value) || 0;
    var pix2 = parseFloat(document.querySelector('input[name="pix2"]').value) || 0;
    var cheque2 = parseFloat(document.querySelector('input[name="cheque2"]').value) || 0;
    var total2 = dinheiro2 + cartao_cred2 + cartao_deb2 + pix2 + cheque2;
    document.querySelector('input[name="total2"]').value = total2.toFixed(2);
}

// Calcula o total3 e atualiza de a cordo com o preenchemento dos campos da coluna correspondente
function atualizarTotal3() {
    var dinheiro3 = parseFloat(document.querySelector('input[name="dinheiro3"]').value) || 0;
    var cartao_cred3 = parseFloat(document.querySelector('input[name="cartao_cred3"]').value) || 0;
    var cartao_deb3 = parseFloat(document.querySelector('input[name="cartao_deb3"]').value) || 0;
    var pix3 = parseFloat(document.querySelector('input[name="pix3"]').value) || 0;
    var cheque3 = parseFloat(document.querySelector('input[name="cheque3"]').value) || 0;
    var total3 = dinheiro3 + cartao_cred3 + cartao_deb3 + pix3 + cheque3;
    document.querySelector('input[name="total3"]').value = total3.toFixed(2);
}

// Calcula o total4 e atualiza de a cordo com o preenchemento dos campos da coluna correspondente
function atualizarTotal4() {
    var dinheiro4 = parseFloat(document.querySelector('input[name="dinheiro4"]').value) || 0;
    var cartao_cred4 = parseFloat(document.querySelector('input[name="cartao_cred4"]').value) || 0;
    var cartao_deb4 = parseFloat(document.querySelector('input[name="cartao_deb4"]').value) || 0;
    var pix4 = parseFloat(document.querySelector('input[name="pix4"]').value) || 0;
    var cheque4 = parseFloat(document.querySelector('input[name="cheque4"]').value) || 0;
    var total4 = dinheiro4 + cartao_cred4 + cartao_deb4 + pix4 + cheque4;
    document.querySelector('input[name="total4"]').value = total4.toFixed(2);
}

// Calcula o total em dinheiro e atualiza de a cordo com o preenchemento dos campos da linha correspondente
function atualizarTotalDinheiro() {
    var dinheiro1 = parseFloat(document.querySelector('input[name="dinheiro1"]').value) || 0;
    var dinheiro2 = parseFloat(document.querySelector('input[name="dinheiro2"]').value) || 0;
    var dinheiro3 = parseFloat(document.querySelector('input[name="dinheiro3"]').value) || 0;
    var dinheiro4 = parseFloat(document.querySelector('input[name="dinheiro4"]').value) || 0;
    var dinheiro_total = dinheiro1 + dinheiro2 + dinheiro3 + dinheiro4;
    document.querySelector('input[name="dinheiro_total"]').value = dinheiro_total.toFixed(2);
}

// Calcula o total em cartão de crédito e atualiza de a cordo com o preenchemento dos campos da linha correspondente
function atualizarTotalCartaoCred() {
    var cartao_cred1 = parseFloat(document.querySelector('input[name="cartao_cred1"]').value) || 0;
    var cartao_cred2 = parseFloat(document.querySelector('input[name="cartao_cred2"]').value) || 0;
    var cartao_cred3 = parseFloat(document.querySelector('input[name="cartao_cred3"]').value) || 0;
    var cartao_cred4 = parseFloat(document.querySelector('input[name="cartao_cred4"]').value) || 0;
    var cartao_cred_total = cartao_cred1 + cartao_cred2 + cartao_cred3 + cartao_cred4;
    document.querySelector('input[name="cartao_cred_total"]').value = cartao_cred_total.toFixed(2);
}

// Calcula o total em cartão de débito e atualiza de a cordo com o preenchemento dos campos da linha correspondente
function atualizarTotalCartaoDeb() {
    var cartao_deb1 = parseFloat(document.querySelector('input[name="cartao_deb1"]').value) || 0;
    var cartao_deb2 = parseFloat(document.querySelector('input[name="cartao_deb2"]').value) || 0;
    var cartao_deb3 = parseFloat(document.querySelector('input[name="cartao_deb3"]').value) || 0;
    var cartao_deb4 = parseFloat(document.querySelector('input[name="cartao_deb4"]').value) || 0;
    var cartao_deb_total = cartao_deb1 + cartao_deb2 + cartao_deb3 + cartao_deb4;
    document.querySelector('input[name="cartao_deb_total"]').value = cartao_deb_total.toFixed(2);
}

// Calcula o total em pix e atualiza de a cordo com o preenchemento dos campos da linha correspondente
function atualizarTotalPix() {
    var pix1 = parseFloat(document.querySelector('input[name="pix1"]').value) || 0;
    var pix2 = parseFloat(document.querySelector('input[name="pix2"]').value) || 0;
    var pix3 = parseFloat(document.querySelector('input[name="pix3"]').value) || 0;
    var pix4 = parseFloat(document.querySelector('input[name="pix4"]').value) || 0;
    var pix_total = pix1 + pix2 + pix3 + pix4;
    document.querySelector('input[name="pix_total"]').value = pix_total.toFixed(2);
}

// Calcula o total em cheque e atualiza de a cordo com o preenchemento dos campos da linha correspondente
function atualizarTotalCheque() {
    var cheque1 = parseFloat(document.querySelector('input[name="cheque1"]').value) || 0;
    var cheque2 = parseFloat(document.querySelector('input[name="cheque2"]').value) || 0;
    var cheque3 = parseFloat(document.querySelector('input[name="cheque3"]').value) || 0;
    var cheque4 = parseFloat(document.querySelector('input[name="cheque4"]').value) || 0;
    var cheque_total = cheque1 + cheque2 + cheque3 + cheque4;
    document.querySelector('input[name="cheque_total"]').value = cheque_total.toFixed(2);
}

// Calcula o total_total, ainda sem funcionar pq o ainda nao consegui fazer q a função calcule mesmo sem o input manual de valores
function atualizarTotalTotal() {
    var total1 = parseFloat(document.querySelector('input[name="total1"]').value) || 0;
    var total2 = parseFloat(document.querySelector('input[name="total2"]').value) || 0;
    var total3 = parseFloat(document.querySelector('input[name="total3"]').value) || 0;
    var total4 = parseFloat(document.querySelector('input[name="total4"]').value) || 0;
    var total_total = total1 + total2 + total3 + total4;
    document.querySelector('input[name="total_total"]').value = total_total.toFixed(2);
}

// Calcula o total de malotes e atualiza de a cordo com o preenchemento dos campos da linha correspondente
function atualizarTotalMalotes() {
    var malote1 = parseFloat(document.querySelector('input[name="malote1"]').value) || 0;
    var malote2 = parseFloat(document.querySelector('input[name="malote2"]').value) || 0;
    var malote3 = parseFloat(document.querySelector('input[name="malote3"]').value) || 0;
    var malote4 = parseFloat(document.querySelector('input[name="malote4"]').value) || 0;
    var malote_total = malote1 + malote2 + malote3 + malote4;
    document.querySelector('input[name="malote_total"]').value = malote_total.toFixed(2);
}

// Calcula o total de Sangria
function atualizarTotalSangria() {
    var sangria1 = parseFloat(document.querySelector('input[name="sangria1"]').value) || 0;
    var sangria2 = parseFloat(document.querySelector('input[name="sangria2"]').value) || 0;
    var sangria3 = parseFloat(document.querySelector('input[name="sangria3"]').value) || 0;
    var sangria4 = parseFloat(document.querySelector('input[name="sangria4"]').value) || 0;
    var sangria_total = sangria1 + sangria2 + sangria3 + sangria4;
    document.querySelector('input[name="sangria_total"]').value = sangria_total.toFixed(2);
}

// Calcular o Resultado de cada caixao e atualiza de acordo com o preenchemento dos campos da linha correspondente
function calcularResultado1() {
    var dinheiro1 = parseFloat(document.querySelector('input[name="dinheiro1"]').value) || 0;
    var malote1 = parseFloat(document.querySelector('input[name="malote1"]').value) || 0;
    var sangria1 = parseFloat(document.querySelector('input[name="sangria1"]').value) || 0;
    var resultado1 = malote1 - dinheiro1 + sangria1;
    document.querySelector('input[name="resultado1"]').value = resultado1.toFixed(2);
}

function calcularResultado2() {
    var dinheiro2 = parseFloat(document.querySelector('input[name="dinheiro2"]').value) || 0;
    var malote2 = parseFloat(document.querySelector('input[name="malote2"]').value) || 0;
    var sangria2 = parseFloat(document.querySelector('input[name="sangria2"]').value) || 0;
    var resultado2 = malote2 - dinheiro2 + sangria2;
    document.querySelector('input[name="resultado2"]').value = resultado2.toFixed(2);
}

function calcularResultado3() {
    var dinheiro3 = parseFloat(document.querySelector('input[name="dinheiro3"]').value) || 0;
    var malote3 = parseFloat(document.querySelector('input[name="malote3"]').value) || 0;
    var sangria3 = parseFloat(document.querySelector('input[name="sangria3"]').value) || 0;
    var resultado3 = malote3 - dinheiro3 + sangria3;
    document.querySelector('input[name="resultado3"]').value = resultado3.toFixed(2);
}

function calcularResultado4() {
    var dinheiro4 = parseFloat(document.querySelector('input[name="dinheiro4"]').value) || 0;
    var malote4 = parseFloat(document.querySelector('input[name="malote4"]').value) || 0;
    var sangria4 = parseFloat(document.querySelector('input[name="sangria4"]').value) || 0;
    var resultado4 = malote4 - dinheiro4 + sangria4;
    document.querySelector('input[name="resultado4"]').value = resultado4.toFixed(2);
}

function calcularResultadoTotal() {
    var resultado1 = parseFloat(document.querySelector('input[name="resultado1"]').value) || 0;
    var resultado2 = parseFloat(document.querySelector('input[name="resultado2"]').value) || 0;
    var resultado3 = parseFloat(document.querySelector('input[name="resultado3"]').value) || 0;
    var resultado4 = parseFloat(document.querySelector('input[name="resultado4"]').value) || 0;
    var resultado_total = resultado1 + resultado2 + resultado3 + resultado4;
    document.querySelector('input[name="resultado_total"]').value = resultado_total.toFixed(2);
}

// Calcula o ticket médio
function atualizarTicketMedio() {
    var total1 = parseFloat(document.querySelector('input[name="total1"]').value) || 0;
    var qtd_vendas = parseFloat(document.querySelector('input[name="qtd_vendas"]').value) || 0;
    var ticket_medio = total1 / qtd_vendas;
    document.querySelector('input[name="tkt_medio"]').value = ticket_medio.toFixed(2);
}

// Calcula total de serviços e atualiza de acordo com o preenchemento dos campos da linha correspondente
function atualizarTotalServicos() {
    var servicos1 = parseFloat(document.querySelector('input[name="servicos1"]').value) || 0;
    var servicos2 = parseFloat(document.querySelector('input[name="servicos2"]').value) || 0;
    var servicos3 = parseFloat(document.querySelector('input[name="servicos3"]').value) || 0;
    var servicos4 = parseFloat(document.querySelector('input[name="servicos4"]').value) || 0;
    var servicos_total = servicos1 + servicos2 + servicos3 + servicos4;
    document.querySelector('input[name="servicos_total"]').value = servicos_total.toFixed(2);
}

// Função para formatar o valor como moeda
function formatCurrency(input) {
    let value = input.value;
    value = value.replace(/\D/g, ""); // Remove caracteres não numéricos
    value = (value / 100).toFixed(2) + ""; // Adiciona duas casas decimais
    value = value.replace(".", ","); // Substitui ponto por vírgula
    value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."); // Adiciona pontos a cada milhar
    input.value = value;
}

/*
// Removida pois o usuario final tem como costume o uso da tecla enter
// Permite navegar entre os inputs usando a tecla enter

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const inputs = Array.from(form.querySelectorAll('input'));

    form.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            const index = inputs.indexOf(document.activeElement);
            if (index !== -1 && index + 1 < inputs.length) {
                inputs[index + 1].focus();
            }
        }
    });
});
*/

// Permite navegar entre os inputs usando tabindex como ordem de tabulação e o "enter" como gatilho
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const inputs = Array.from(form.querySelectorAll('input')).sort((a, b) => {
        return (a.getAttribute('tabindex') || 0) - (b.getAttribute('tabindex') || 0);
    });

    form.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            const index = inputs.indexOf(document.activeElement);
            if (index !== -1 && index + 1 < inputs.length) {
                inputs[index + 1].focus();
            }
        }
    });
});


function calcular() {
    atualizarTotal1();
    atualizarTotal2();
    atualizarTotal3();
    atualizarTotal4();
    atualizarTotalTotal();
    atualizarTotalDinheiro();
    atualizarTotalCartaoCred();
    atualizarTotalCartaoDeb();
    atualizarTotalPix();
    atualizarTotalCheque();
    atualizarTotalMalotes();
    atualizarTotalSangria();
    atualizarTotalServicos();
    calcularResultadoTotal();
    
}