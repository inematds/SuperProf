#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as 3 páginas HTML completas com conteúdo REAL dos MDs
"""

import re
from html import escape as html_escape

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def md_to_html_summary(md_content):
    """Converte MD para HTML simplificado (resumo para modal)"""
    lines = md_content.split('\n')
    html_parts = []
    in_code = False
    
    for line in lines[:200]:  # Primeiras 200 linhas (resumo)
        # Títulos
        if line.startswith('# '):
            html_parts.append(f'<h2 class="text-3xl font-bold mb-6 text-neutral-900 dark:text-neutral-100">{line[2:]}</h2>')
        elif line.startswith('## '):
            html_parts.append(f'<h3 class="text-2xl font-bold mt-6 mb-4 text-neutral-900 dark:text-neutral-100">{line[3:]}</h3>')
        elif line.startswith('### '):
            html_parts.append(f'<h4 class="text-xl font-semibold mt-4 mb-3 text-primary">{line[4:]}</h4>')
        
        # Code blocks
        elif line.startswith('```'):
            if in_code:
                html_parts.append('</code></pre>')
                in_code = False
            else:
                html_parts.append('<pre class="bg-neutral-800 dark:bg-black text-neutral-100 p-4 rounded-lg overflow-x-auto my-4"><code>')
                in_code = True
        elif in_code:
            html_parts.append(html_escape(line))
        
        # Listas
        elif line.startswith('- ') or line.startswith('* '):
            html_parts.append(f'<li class="ml-6">{line[2:]}</li>')
        
        # Negrito/Itálico
        elif line.strip():
            text = line
            text = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-bold text-primary">\1</strong>', text)
            text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
            text = re.sub(r'`(.*?)`', r'<code class="bg-purple-100 dark:bg-purple-900/30 px-2 py-1 rounded text-sm">\1</code>', text)
            html_parts.append(f'<p class="mb-4 text-neutral-700 dark:text-neutral-300">{text}</p>')
    
    return '\n'.join(html_parts)

def extract_topics(md_content):
    """Extrai tópicos do MD"""
    topics = []
    lines = md_content.split('\n')
    
    for i, line in enumerate(lines):
        if line.startswith('## ') and not line.startswith('###'):
            title = line[3:].strip()
            # Pegar próximo parágrafo como explicação
            explanation = ''
            for j in range(i+1, min(i+10, len(lines))):
                if lines[j].strip() and not lines[j].startswith('#'):
                    explanation = lines[j].strip()
                    break
            
            if title and not title.startswith('📖') and not title.startswith('📦'):
                topics.append({
                    'title': title.replace('*', '').replace(':', ''),
                    'explanation': explanation[:200]
                })
                if len(topics) >= 5:
                    break
    
    return topics

# Ler base template
base_html = read_file('niveis/nivel-1.html')

# Configurações para cada nível
configs = {
    'nivel-2a.html': {
        'id': '2A',
        'nome': 'Pedagógico',
        'cor': '#9b59b6',
        'cor_nome': 'primary',
        'gradient': 'from-primary to-purple-600',
        'trilha': 'Trilha A',
        'trilha_link': 'trilha-a.html',
        'carga': 60,
        'descricao': 'Aprofundamento pedagógico em design instrucional, avaliação formativa, personalização, gamificação e comunidades de prática com IA',
        'modulos': [f'modulo-2a-{i}.md' for i in range(1, 6)],
        'titulos': [
            'Design Instrucional com IA',
            'Avaliação Formativa Assistida por IA', 
            'Personalização em Escala',
            'Gamificação Inteligente',
            'Comunidades de Prática e Aprendizagem Social'
        ]
    },
    'nivel-2b.html': {
        'id': '2B',
        'nome': 'Técnico',
        'cor': '#10B981',
        'cor_nome': 'success',
        'gradient': 'from-success to-green-600',
        'trilha': 'Trilha B',
        'trilha_link': 'trilha-b.html',
        'carga': 60,
        'descricao': 'Aprofundamento técnico em anatomia de LLMs, fine-tuning, RAG e criação de agentes educacionais autônomos',
        'modulos': [f'modulo-2b-{i}.md' for i in range(1, 5)],
        'titulos': [
            'Anatomia de LLMs - Como Funcionam Por Dentro',
            'Fine-Tuning e RAG - Especializando LLMs',
            'Criação de Agentes Educacionais com IA',
            'Projeto Técnico - Educador de IA'
        ]
    },
    'nivel-3a.html': {
        'id': '3A',
        'nome': 'Especialista',
        'cor': '#8e44ad',
        'cor_nome': 'primary',
        'gradient': 'from-primary to-purple-800',
        'trilha': 'Trilha A',
        'trilha_link': 'trilha-a.html',
        'carga': 60,
        'descricao': 'Nível especialista: redesenho curricular completo, liderança em transformação digital educacional e projeto final de certificação',
        'modulos': [f'modulo-3a-{i}.md' for i in range(1, 4)],
        'titulos': [
            'Currículo Aumentado por IA',
            'Liderança em Transformação Digital Educacional',
            'Projeto de Certificação - Professor 2.0'
        ]
    }
}

print("Gerando páginas HTML completas...\n")

for filename, config in configs.items():
    print(f"Processando {filename}...")
    
    html = base_html
    
    # 1. Substituir metadados
    html = re.sub(r'<title>.*?</title>', 
                  f'<title>Nível {config["id"]}: {config["nome"]} | SuperProfessores</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{config["descricao"]}"', html)
    
    # 2. Substituir cores
    html = html.replace('from-primary to-blue-600', config['gradient'])
    html = html.replace('#3B82F6', config['cor'])
    
    # 3. Breadcrumb
    html = re.sub(
        r'(<nav class="flex text-sm" aria-label="Breadcrumb">).*?(</nav>)',
        f'''\\1
                <a href="../index.html" class="text-primary hover:text-purple-700">Início</a>
                <span class="mx-2 text-neutral-400">/</span>
                <a href="{config["trilha_link"]}" class="text-primary hover:text-purple-700">{config["trilha"]}</a>
                <span class="mx-2 text-neutral-400">/</span>
                <span class="text-neutral-600 dark:text-neutral-400">Nível {config["id"]}</span>
            \\2''',
        html,
        flags=re.DOTALL
    )
    
    # 4. Header
    html = re.sub(
        r'<h1 class="text-4xl.*?</h1>',
        f'<h1 class="text-4xl lg:text-5xl font-bold mb-4">Nível {config["id"]}: {config["nome"]}</h1>',
        html
    )
    
    html = re.sub(
        r'<p class="text-xl.*?para iniciantes</p>',
        f'<p class="text-xl text-white/90 mb-6">{config["descricao"]}</p>',
        html
    )
    
    html = re.sub(
        r'<span class="inline-block px-4 py-2 bg-white/20[^>]*>30 horas</span>',
        f'<span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">{config["carga"]} horas</span>',
        html
    )
    
    html = re.sub(
        r'<div class="text-2xl font-bold">5</div>',
        f'<div class="text-2xl font-bold">{len(config["modulos"])}</div>',
        html
    )
    
    # 5. Gerar módulos
    modulos_html_parts = []
    modal_contents = {}
    
    for idx, (md_file, titulo) in enumerate(zip(config['modulos'], config['titulos']), 1):
        md_content = read_file(f'pdfs/{md_file}')
        topics = extract_topics(md_content)
        modal_html = md_to_html_summary(md_content)
        modal_id = f'modulo-{config["id"].lower()}-{idx}'
        
        modal_contents[modal_id] = {
            'title': f'Módulo {config["id"]}.{idx}: {titulo}',
            'content': modal_html
        }
        
        # Gerar card do módulo
        topics_html = ''
        for i, topic in enumerate(topics[:5]):
            topics_html += f'''
                    <li class="topic-item" data-topic="{modal_id}-topic-{i}">
                        <button class="topic-button w-full text-left px-4 py-2 bg-neutral-50 dark:bg-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-600 rounded-lg transition-colors font-medium text-neutral-800 dark:text-neutral-200">
                            {topic['title']}
                        </button>
                        <div class="topic-explanation hidden ml-6 mt-2 p-4 bg-{config["cor_nome"]}-50 dark:bg-{config["cor_nome"]}-900/20 rounded-lg border-l-4 border-{config["cor_nome"]}">
                            <p class="text-sm text-neutral-700 dark:text-neutral-300">{topic['explanation']}</p>
                        </div>
                    </li>'''
        
        modulo_card = f'''
        <!-- Módulo {config["id"]}.{idx} -->
        <div class="chapter-card bg-white dark:bg-neutral-800 rounded-2xl shadow-lg p-8 mb-8 border-2 border-transparent hover:border-{config["cor_nome"]} transition-all">
            <div class="flex items-start justify-between mb-6">
                <div>
                    <span class="inline-block px-3 py-1 bg-{config["cor_nome"]}/10 text-{config["cor_nome"]} rounded-full text-sm font-semibold mb-3">12-20 horas</span>
                    <h2 class="text-3xl font-bold text-neutral-900 dark:text-neutral-100 mb-2">Módulo {config["id"]}.{idx}: {titulo}</h2>
                    <p class="text-neutral-600 dark:text-neutral-400">{topics[0]['explanation'] if topics else 'Módulo avançado'}</p>
                </div>
            </div>

            <div class="flex flex-wrap gap-3 mb-6">
                <button onclick="openModal('{modal_id}')" class="px-6 py-3 bg-{config["cor_nome"]} text-white rounded-lg font-semibold hover:opacity-90 transition-colors flex items-center gap-2">
                    <span>Ver em Modal</span>
                </button>
                <a href="../modulos/{md_file.replace('.md', '.html')}" class="px-6 py-3 bg-transparent border-2 border-{config["cor_nome"]} text-{config["cor_nome"]} rounded-lg font-semibold hover:bg-{config["cor_nome"]} hover:text-white transition-colors flex items-center gap-2">
                    <span>Abrir Página Completa</span>
                </a>
                <a href="../pdfs/{md_file}" download class="px-6 py-3 bg-transparent border-2 border-neutral-300 dark:border-neutral-600 text-neutral-700 dark:text-neutral-300 rounded-lg font-semibold hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors flex items-center gap-2">
                    <span>Download MD</span>
                </a>
            </div>

            <div class="mb-4">
                <h3 class="font-semibold text-neutral-900 dark:text-neutral-100 mb-3 text-lg">Tópicos-chave:</h3>
                <ul class="topics-list space-y-2">{topics_html}
                </ul>
            </div>
        </div>
        '''
        
        modulos_html_parts.append(modulo_card)
    
    # 6. Substituir módulos do nível 1 pelos novos
    # Encontrar seção de módulos
    main_start = html.find('<!-- Main Content -->')
    main_end = html.find('<!-- Modal Container -->')
    
    if main_start > 0 and main_end > 0:
        before = html[:main_start]
        after = html[main_end:]
        
        new_main = f'''<!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {"".join(modulos_html_parts)}
    </main>

    '''
        
        html = before + new_main + after
    
    # 7. Adicionar JavaScript com conteúdo dos modais
    modal_js = 'const moduleContent = {\n'
    for modal_id, content in modal_contents.items():
        modal_js += f'''    '{modal_id}': {{
        title: `{content["title"]}`,
        content: `{content["content"]}`
    }},\n'''
    modal_js += '};\n'
    
    # Inserir antes do </script> final
    html = html.replace(
        '// Modal content placeholder',
        modal_js
    )
    
    # Salvar
    output_path = f'niveis/{filename}'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Contar linhas
    lines = len(html.split('\n'))
    print(f"  ✓ {filename}: {lines} linhas")

print("\n✅ Concluído!")
