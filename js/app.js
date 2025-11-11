/**
 * SuperProfessores - Main Application JavaScript
 * Implements dark mode toggle, mobile menu, and interactive features
 */

document.addEventListener('DOMContentLoaded', function() {
    // Remove preload class to enable CSS transitions
    setTimeout(() => {
        document.body.classList.remove('preload');
    }, 100);

    // ============================================
    // DARK MODE TOGGLE
    // ============================================

    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    // Function to update icon visibility based on current theme
    function updateThemeIcon(isDark) {
        if (isDark) {
            themeToggleLightIcon.classList.remove('hidden');
            themeToggleDarkIcon.classList.add('hidden');
        } else {
            themeToggleDarkIcon.classList.remove('hidden');
            themeToggleLightIcon.classList.add('hidden');
        }
    }

    // Check for saved theme preference or default to light
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme === 'dark') {
        html.classList.add('dark');
        updateThemeIcon(true);
    } else if (currentTheme === 'light') {
        html.classList.remove('dark');
        updateThemeIcon(false);
    } else {
        // Check system preference if no saved theme
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            html.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            updateThemeIcon(true);
        } else {
            html.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            updateThemeIcon(false);
        }
    }

    // Toggle theme on button click
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const isDark = html.classList.toggle('dark');
            const newTheme = isDark ? 'dark' : 'light';
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(isDark);
        });
    }

    // Listen for system theme changes
    if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
            if (!localStorage.getItem('theme')) {
                const isDark = e.matches;
                if (isDark) {
                    html.classList.add('dark');
                } else {
                    html.classList.remove('dark');
                }
                updateThemeIcon(isDark);
            }
        });
    }

    // ============================================
    // MOBILE MENU TOGGLE
    // ============================================

    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');

            // Update button icon (hamburger <-> X)
            const icon = mobileMenuBtn.querySelector('svg path');
            if (mobileMenu.classList.contains('hidden')) {
                icon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');
            } else {
                icon.setAttribute('d', 'M6 18L18 6M6 6l12 12');
            }
        });

        // Close mobile menu when clicking a link
        const mobileMenuLinks = mobileMenu.querySelectorAll('a');
        mobileMenuLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.add('hidden');
                const icon = mobileMenuBtn.querySelector('svg path');
                icon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');
            });
        });
    }

    // ============================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ============================================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Skip if it's just "#"
            if (href === '#') return;

            e.preventDefault();

            const target = document.querySelector(href);
            if (target) {
                // Calculate offset for sticky header (64px = h-16)
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============================================
    // STICKY HEADER SHADOW ON SCROLL
    // ============================================

    const nav = document.querySelector('nav');
    if (nav) {
        let lastScroll = 0;

        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 10) {
                nav.classList.add('shadow-md');
            } else {
                nav.classList.remove('shadow-md');
            }

            lastScroll = currentScroll;
        });
    }

    // ============================================
    // EXPANDABLE TOPICS SYSTEM (ATIA Compact Topics)
    // ============================================

    // Event delegation for topic buttons
    document.addEventListener('click', function(e) {
        const topicButton = e.target.closest('.topic-button');

        if (topicButton) {
            const topicItem = topicButton.closest('.topic-item');
            const explanation = topicItem ? topicItem.querySelector('.topic-explanation') : null;

            if (explanation) {
                const wasHidden = explanation.classList.contains('hidden');

                // Close all other topics in the same chapter (accordion behavior)
                const chapterCard = topicItem.closest('.chapter-card');
                if (chapterCard) {
                    chapterCard.querySelectorAll('.topic-explanation').forEach(exp => {
                        exp.classList.add('hidden');
                    });
                }

                // Toggle current topic
                if (wasHidden) {
                    explanation.classList.remove('hidden');
                } else {
                    explanation.classList.add('hidden');
                }
            }
        }
    });

    // ============================================
    // CARD HOVER ANIMATIONS
    // ============================================

    const trilhaCards = document.querySelectorAll('.trilha-card');
    trilhaCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // ============================================
    // INTERSECTION OBSERVER FOR FADE-IN ANIMATIONS
    // ============================================

    // Add fade-in-up class to sections for animation
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const fadeInObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible');
            }
        });
    }, observerOptions);

    // Observe all sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.classList.add('fade-in-up');
        fadeInObserver.observe(section);
    });

    // ============================================
    // EXTERNAL LINK HANDLING
    // ============================================

    // Add icon to external links
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
    externalLinks.forEach(link => {
        if (!link.querySelector('svg')) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });

    // ============================================
    // CONSOLE MESSAGE
    // ============================================

    console.log('%c🎓 SuperProfessores', 'font-size: 24px; font-weight: bold; color: #3B82F6;');
    console.log('%cTransformando educadores em arquitetos do futuro da aprendizagem', 'font-size: 14px; color: #666;');
    console.log('%c📖 GitHub: https://github.com/inematds/SuperProf', 'font-size: 12px; color: #10B981;');
});

// ============================================
// UTILITY FUNCTIONS
// ============================================

/**
 * Debounce function to limit rate of function calls
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Check if element is in viewport
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
