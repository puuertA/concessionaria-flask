// Scripts globais para o Sistema de Vendas

// Formatar valores monetários
function formatarMoeda(valor) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(valor);
}

// Formatar data para padrão brasileiro
function formatarData(data) {
    if (!data) return '';
    const [ano, mes, dia] = data.split('-');
    return `${dia}/${mes}/${ano}`;
}

// Validar formulários com classe 'needs-validation'
(function() {
    'use strict';

    document.addEventListener('DOMContentLoaded', function() {
        const forms = document.querySelectorAll('.needs-validation');

        Array.from(forms).forEach(function(form) {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    });
})();

// Máscara para campos de moeda
document.addEventListener('DOMContentLoaded', function() {
    const monetaryInputs = document.querySelectorAll('.monetary');

    monetaryInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            value = (value / 100).toFixed(2);
            e.target.value = value;
        });
    });
});

// Confirmar exclusão
function confirmarExclusao(mensagem, url) {
    if (confirm(mensagem)) {
        window.location.href = url;
    }
    return false;
}