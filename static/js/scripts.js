// Animações e interatividade

document.addEventListener('DOMContentLoaded', function() {
    // Adicionar efeito de loading aos botões de formulário
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.classList.add('loading');
            this.disabled = true;
            
            // Remover loading após 3 segundos (fallback)
            setTimeout(() => {
                this.classList.remove('loading');
                this.disabled = false;
            }, 3000);
        });
    });

    // Animação suave para os cards
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease-out';
        cardObserver.observe(card);
    });

    // Validação de formulários
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let hasError = false;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.style.borderColor = '#e74c3c';
                    field.style.boxShadow = '0 0 0 0.2rem rgba(231, 76, 60, 0.25)';
                    hasError = true;
                } else {
                    field.style.borderColor = '#27ae60';
                    field.style.boxShadow = '0 0 0 0.2rem rgba(39, 174, 96, 0.25)';
                }
            });

            if (hasError) {
                e.preventDefault();
                showNotification('Por favor, preencha todos os campos obrigatórios.', 'error');
            }
        });
    });

    // Função para mostrar notificações
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type === 'error' ? 'danger' : type} notification`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            min-width: 300px;
            animation: slideInRight 0.3s ease-out;
        `;
        notification.innerHTML = `
            <strong>${type === 'error' ? 'Erro!' : 'Sucesso!'}</strong> ${message}
            <button type="button" class="btn-close float-end" onclick="this.parentElement.remove()"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Remover automaticamente após 5 segundos
        setTimeout(() => {
            if (notification.parentElement) {
                notification.style.animation = 'slideOutRight 0.3s ease-out';
                setTimeout(() => notification.remove(), 300);
            }
        }, 5000);
    }

    // Máscara para CEP
    const cepInputs = document.querySelectorAll('input[name="cep"]');
    cepInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length >= 5) {
                value = value.replace(/^(\d{5})(\d{3})$/, '$1-$2');
            }
            e.target.value = value;
        });
    });

    // Máscara para placa de veículo
    const placaInputs = document.querySelectorAll('input[name="idplaca"]');
    placaInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/[^a-zA-Z0-9]/g, '').toUpperCase();
            if (value.length >= 4) {
                value = value.replace(/^([A-Z]{3})(\d{4})$/, '$1-$2');
            }
            e.target.value = value;
        });
    });

    // Tooltip para ícones
    const icons = document.querySelectorAll('.bi');
    icons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });
        
        icon.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Adiciona fundo ao navbar quando rolar a página
    const navbar = document.querySelector('.transparent-navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});

// CSS para animações das notificações
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .notification {
        border-left: 4px solid;
        backdrop-filter: blur(10px);
    }
`;
document.head.appendChild(style);