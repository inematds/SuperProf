#!/usr/bin/env python3
"""
Script para gerar as páginas HTML completas dos níveis 2A, 2B e 3A
Mantém a estrutura rica do nivel-1.html com conteúdo extraído dos MDs
"""

def generate_nivel_2a():
    """Gera nivel-2a.html completo"""

    html_content = '''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nível 2A: Pedagógico | SuperProfessores</title>
    <meta name="description" content="Trilha A - Nível Pedagógico: 60 horas de especialização em pedagogia aumentada por IA">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#3B82F6',
                        'trilha-a': '#9b59b6',
                        'trilha-b': '#10B981',
                        fundamentos: '#3B82F6',
                        pedagogico: '#9b59b6',
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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { transition: background-color 200ms ease-in-out, border-color 200ms ease-in-out, color 200ms ease-in-out; }
        .preload * { transition: none !important; }
        .modal { display: none; position: fixed; z-index: 100; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.6); backdrop-filter: blur(4px); }
        .modal.active { display: flex; align-items: center; justify-content: center; }
        .modal-content { background-color: white; margin: auto; padding: 0; width: 90%; max-width: 1000px; max-height: 90vh; border-radius: 1rem; overflow: hidden; box-shadow: 0 20px 25px rgba(0,0,0,0.3); }
        .dark .modal-content { background-color: #1f2937; }
        .modal-header { padding: 1.5rem 2rem; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; }
        .dark .modal-header { border-bottom-color: #374151; }
        .modal-body { padding: 2rem; overflow-y: auto; max-height: calc(90vh - 80px); }
        .close-modal { color: #9ca3af; font-size: 2rem; font-weight: 700; cursor: pointer; line-height: 1; }
        .close-modal:hover { color: #ef4444; }
    </style>
</head>
<body class="preload bg-neutral-50 dark:bg-neutral-900 text-neutral-900 dark:text-neutral-100">

    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/90 dark:bg-neutral-800/90 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-700">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center">
                    <a href="../index.html" class="text-2xl font-bold bg-gradient-to-r from-primary to-trilha-a bg-clip-text text-transparent">
                        🎓 SuperProfessores
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
                <a href="../index.html" class="text-primary hover:text-blue-700">Início</a>
                <span class="mx-2 text-neutral-400">/</span>
                <a href="trilha-a.html" class="text-primary hover:text-blue-700">Trilha A</a>
                <span class="mx-2 text-neutral-400">/</span>
                <span class="text-neutral-600 dark:text-neutral-400">Nível 2A</span>
            </nav>
        </div>
    </div>

    <!-- Header Section -->
    <section class="bg-gradient-to-r from-pedagogico to-purple-700 py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white">
            <div class="flex items-center gap-4 mb-4">
                <a href="trilha-a.html" class="inline-flex items-center px-4 py-2 bg-white/20 rounded-full text-sm font-semibold hover:bg-white/30 transition-colors">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                    </svg>
                    Voltar para Trilha A
                </a>
                <span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">60 horas</span>
            </div>
            <h1 class="text-4xl lg:text-5xl font-bold mb-4">Nível 2A: Pedagógico</h1>
            <p class="text-xl text-purple-100 mb-6">Especializaç\u00e3o em pedagogia aumentada por IA - Design instrucional, avaliação formativa e personalização</p>
            <div class="grid md:grid-cols-3 gap-4 mt-8">
                <div class="bg-white/10 backdrop-blur p-4 rounded-lg">
                    <div class="text-2xl font-bold">5</div>
                    <div class="text-sm text-purple-100">Módulos</div>
                </div>
                <div class="bg-white/10 backdrop-blur p-4 rounded-lg">
                    <div class="text-2xl font-bold">100%</div>
                    <div class="text-sm text-purple-100">Prático</div>
                </div>
                <div class="bg-white/10 backdrop-blur p-4 rounded-lg">
                    <div class="text-2xl font-bold">Avançado</div>
                    <div class="text-sm text-purple-100">Nível pedagógico</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
'''

    # Continua no próximo Write devido ao tamanho
    with open("/home/nmaldaner/projetos/superprofessores/niveis/nivel-2a.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Parte 1 de nivel-2a.html criada")

if __name__ == "__main__":
    generate_nivel_2a()
    print("Scripts preparados")
