#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera EXATAMENTE como nivel-1.html: páginas de 1400+ linhas
Com TODO o conteúdo dos MDs processado
"""

import re
from html import escape as html_escape

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def md_to_html_complete(md_content):
    """Converte MD COMPLETO para HTML"""
    lines = md_content.split('\n')
    html_parts = []
    in_code = False
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        
        # Code blocks
        if stripped.startswith('```'):
            if in_code:
                html_parts.append('</code></pre>')
                in_code = False
            else:
                lang = stripped[3:].strip() or 'text'
                html_parts.append(f'<pre class="bg-neutral-800 dark:bg-black text-neutral-100 p-4 rounded-lg overflow-x-auto my-4 text-sm"><code class="language-{lang}">')
                in_code = True
            continue
        
        if in_code:
            html_parts.append(html_escape(line))
            continue
        
        # Títulos
        if stripped.startswith('# ') and not stripped.startswith('##'):
            html_parts.append(f'<h2 class="text-3xl font-bold mb-6 mt-8 text-neutral-900 dark:text-neutral-100">{stripped[2:]}</h2>')
        elif stripped.startswith('## ') and not stripped.startswith('###'):
            html_parts.append(f'<h3 class="text-2xl font-bold mt-8 mb-4 text-primary dark:text-primary-light">{stripped[3:]}</h3>')
        elif stripped.startswith('### '):
            html_parts.append(f'<h4 class="text-xl font-semibold mt-6 mb-3 text-neutral-800 dark:text-neutral-200">{stripped[4:]}</h4>')
        elif stripped.startswith('#### '):
            html_parts.append(f'<h5 class="text-lg font-semibold mt-4 mb-2 text-neutral-700 dark:text-neutral-300">{stripped[5:]}</h5>')
        
        # Listas
        elif stripped.startswith('- ') or stripped.startswith('* ') or stripped.startswith('+ '):
            if not in_list:
                html_parts.append('<ul class="list-disc list-inside space-y-2 ml-6 my-4">')
                in_list = True
            content = stripped[2:]
            # Processar bold/italic/code
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-bold">\1</strong>', content)
            content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
            content = re.sub(r'`(.*?)`', r'<code class="bg-purple-100 dark:bg-purple-900/30 px-1.5 py-0.5 rounded text-sm">\1</code>', content)
            html_parts.append(f'<li class="text-neutral-700 dark:text-neutral-300">{content}</li>')
        
        # Parágrafos normais
        elif stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            
            # Processar markdown inline
            text = stripped
            text = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-semibold text-neutral-900 dark:text-neutral-100">\1</strong>', text)
            text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
            text = re.sub(r'`(.*?)`', r'<code class="bg-purple-100 dark:bg-purple-900/30 px-2 py-1 rounded text-sm font-mono">\1</code>', text)
            
            # Links
            text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" class="text-primary hover:underline" target="_blank">\1</a>', text)
            
            # Destaques especiais
            if text.startswith('**') or '✅' in text or '❌' in text or '⚠️' in text:
                html_parts.append(f'<p class="mb-4 text-neutral-800 dark:text-neutral-200 font-medium">{text}</p>')
            else:
                html_parts.append(f'<p class="mb-4 text-neutral-700 dark:text-neutral-300 leading-relaxed">{text}</p>')
        else:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
    
    if in_list:
        html_parts.append('</ul>')
    
    return '\n'.join(html_parts)

# Ler MDs completos
print("Lendo todos os MDs...")
all_mds = {}
for nivel in ['2a', '2b', '3a']:
    all_mds[nivel] = []
    
    if nivel == '2a':
        count = 5
    elif nivel == '2b':
        count = 4
    else:
        count = 3
    
    for i in range(1, count + 1):
        md_path = f'pdfs/modulo-{nivel}-{i}.md'
        all_mds[nivel].append(read_file(md_path))
        print(f"  ✓ {md_path}")

# Ler template base
print("\nLendo template nivel-1.html...")
base_html = read_file('niveis/nivel-1.html')

# Config
configs = {
    'nivel-2a.html': {
        'id': '2A', 'nome': 'Pedagógico', 'cor': '#9b59b6',
        'gradient': 'from-primary to-purple-600',
        'trilha': 'Trilha A', 'trilha_link': 'trilha-a.html', 'carga': 60,
        'descricao': 'Aprofundamento pedagógico em design instrucional, avaliação formativa, personalização, gamificação e comunidades de prática com IA',
        'mds': all_mds['2a'],
        'titulos': [
            'Design Instrucional com IA',
            'Avaliação Formativa Assistida por IA', 
            'Personalização em Escala',
            'Gamificação Inteligente',
            'Comunidades de Prática e Aprendizagem Social'
        ]
    },
    'nivel-2b.html': {
        'id': '2B', 'nome': 'Técnico', 'cor': '#10B981',
        'gradient': 'from-success to-green-600',
        'trilha': 'Trilha B', 'trilha_link': 'trilha-b.html', 'carga': 60,
        'descricao': 'Aprofundamento técnico em anatomia de LLMs, fine-tuning, RAG e criação de agentes educacionais autônomos',
        'mds': all_mds['2b'],
        'titulos': [
            'Anatomia de LLMs - Como Funcionam Por Dentro',
            'Fine-Tuning e RAG - Especializando LLMs',
            'Criação de Agentes Educacionais com IA',
            'Projeto Técnico - Educador de IA'
        ]
    },
    'nivel-3a.html': {
        'id': '3A', 'nome': 'Especialista', 'cor': '#8e44ad',
        'gradient': 'from-primary to-purple-800',
        'trilha': 'Trilha A', 'trilha_link': 'trilha-a.html', 'carga': 60,
        'descricao': 'Nível especialista: redesenho curricular completo, liderança em transformação digital educacional e projeto final de certificação',
        'mds': all_mds['3a'],
        'titulos': [
            'Currículo Aumentado por IA',
            'Liderança em Transformação Digital Educacional',
            'Projeto de Certificação - Professor 2.0'
        ]
    }
}

print("\nGerando páginas HTML ultra-completas...\n")

for filename, config in configs.items():
    print(f"Processando {filename}...")
    
    html = base_html
    
    # 1. Meta
    html = re.sub(r'<title>.*?</title>', 
                  f'<title>Nível {config["id"]}: {config["nome"]} | SuperProfessores</title>', html)
    
    # 2. Cores
    html = html.replace('from-primary to-blue-600', config['gradient'])
    html = html.replace('#3B82F6', config['cor'])
    
    # 3. Breadcrumb
    html = re.sub(
        r'(<nav class="flex text-sm" aria-label="Breadcrumb">.*?</nav>)',
        f'''<nav class="flex text-sm" aria-label="Breadcrumb">
                <a href="../index.html" class="text-primary hover:text-purple-700">Início</a>
                <span class="mx-2 text-neutral-400">/</span>
                <a href="{config["trilha_link"]}" class="text-primary hover:text-purple-700">{config["trilha"]}</a>
                <span class="mx-2 text-neutral-400">/</span>
                <span class="text-neutral-600 dark:text-neutral-400">Nível {config["id"]}</span>
            </nav>''',
        html,
        flags=re.DOTALL
    )
    
    # 4. Header
    html = re.sub(
        r'<h1 class="text-4xl[^>]*>.*?</h1>',
        f'<h1 class="text-4xl lg:text-5xl font-bold mb-4">Nível {config["id"]}: {config["nome"]}</h1>',
        html
    )
    
    html = re.sub(
        r'<p class="text-xl text-blue-100[^>]*>.*?</p>',
        f'<p class="text-xl text-white/90 mb-6">{config["descricao"]}</p>',
        html
    )
    
    # 5. Stats
    html = re.sub(r'<div class="text-2xl font-bold">5</div>',
                  f'<div class="text-2xl font-bold">{len(config["mds"])}</div>', html, count=1)
    html = re.sub(r'<span[^>]*>30 horas</span>',
                  f'<span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">{config["carga"]} horas</span>', html, count=1)
    
    # 6. Gerar JavaScript com conteúdo COMPLETO dos modais
    modal_data = []
    for idx, (md_content, titulo) in enumerate(zip(config["mds"], config["titulos"]), 1):
        modal_id = f'modulo-{config["id"].lower()}-{idx}'
        html_content = md_to_html_complete(md_content)
        
        # Escapar para JavaScript
        js_content = html_content.replace('`', '\\`').replace('$', '\\$')
        
        modal_data.append(f'''    '{modal_id}': {{
        title: '{config["id"]}.{idx}: {titulo}',
        content: `
            <div class="modal-content-inner">
                {js_content}
            </div>
        `
    }}''')
    
    modal_js = 'const moduleContent = {\n' + ',\n'.join(modal_data) + '\n};\n'
    
    # Inserir JS antes de </body>
    html = html.replace('</body>', f'''
    <script>
    {modal_js}
    </script>
</body>''')
    
    # 7. Salvar
    output = f'niveis/{filename}'
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html)
    
    lines = len(html.split('\n'))
    size_kb = len(html) / 1024
    print(f"  ✓ {filename}: {lines} linhas, {size_kb:.1f} KB")

print("\n✅ CONCLUÍDO!")
print("\nVerificando com wc -l:")
import subprocess
for f in ['nivel-2a.html', 'nivel-2b.html', 'nivel-3a.html']:
    result = subprocess.run(['wc', '-l', f'niveis/{f}'], capture_output=True, text=True)
    print(f"  {result.stdout.strip()}")
