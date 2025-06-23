   // Menu mobile
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const menuLinks = document.getElementById('menuLinks');
        
        mobileMenuBtn.addEventListener('click', function() {
            menuLinks.classList.toggle('show');
        });
        
        // Fechar menu ao clicar em um link
        const navLinks = document.querySelectorAll('.menu-links a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuLinks.classList.remove('show');
            });
        });
        
        // Ajustar menu no scroll
        window.addEventListener('scroll', function() {
            const header = document.querySelector('.br-header');
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
            } else {
                header.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
            }
        });