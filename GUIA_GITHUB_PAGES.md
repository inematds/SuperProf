# 📘 Guia de Publicação no GitHub Pages

## SuperProfessores - Como publicar este projeto

---

## 🎯 Objetivo

Publicar o projeto SuperProfessores no GitHub Pages em: `https://inematds.github.io/SuperProf`

---

## 📋 Pré-requisitos

- Conta GitHub: `inematds`
- Email: `inematds@gmail.com`
- Git instalado localmente
- Acesso ao repositório: `https://github.com/inematds/SuperProf`

---

## 🚀 Passo a Passo

### 1. Inicializar Repositório Git Local

```bash
# Navegue até a pasta do projeto
cd /home/nmaldaner/projetos/superprofessores

# Inicialize o repositório git
git init

# Configure seu nome e email
git config user.name "inematds"
git config user.email "inematds@gmail.com"
```

### 2. Preparar Arquivos para Commit

```bash
# Adicione todos os arquivos (exceto node_modules)
git add .

# Verifique o status
git status
```

### 3. Criar `.gitignore`

Crie um arquivo `.gitignore` para evitar commitar arquivos desnecessários:

```bash
# Criar .gitignore
cat > .gitignore << 'EOF'
# Node
node_modules/
package-lock.json

# BMad (apenas local)
.bmad-core/
.claude/

# Sistema
.DS_Store
Thumbs.db

# Temporários
*.tmp
*.log
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo
EOF
```

### 4. Fazer o Primeiro Commit

```bash
# Adicione o .gitignore
git add .gitignore

# Remova arquivos que não devem ser commitados
git rm -r --cached node_modules
git rm -r --cached .bmad-core
git rm -r --cached .claude

# Adicione apenas os arquivos importantes
git add README.md
git add doc/
git add package.json
git add GUIA_GITHUB_PAGES.md

# Faça o commit
git commit -m "Initial commit: SuperProfessores v3.0 - Modelo Híbrido"
```

### 5. Criar Repositório no GitHub

**Opção A: Via Interface Web**

1. Acesse: https://github.com/new
2. Nome do repositório: `SuperProf`
3. Descrição: "SuperProfessores: Transformando educadores em arquitetos do futuro da aprendizagem"
4. Público
5. **NÃO** inicialize com README (já temos um)
6. Clique em "Create repository"

**Opção B: Via GitHub CLI** (se instalado)

```bash
gh repo create SuperProf --public --description "SuperProfessores: Programa de formação em IA para educadores"
```

### 6. Conectar Repositório Local ao GitHub

```bash
# Adicione o remote
git remote add origin https://github.com/inematds/SuperProf.git

# Verifique
git remote -v
```

### 7. Push para GitHub

```bash
# Renomeie a branch para main (se necessário)
git branch -M main

# Faça o push
git push -u origin main
```

### 8. Configurar GitHub Pages

**Via Interface Web:**

1. Acesse: https://github.com/inematds/SuperProf/settings/pages
2. Em "Source", selecione: **Deploy from a branch**
3. Em "Branch", selecione: **main** e **/ (root)**
4. Clique em **Save**

**Aguarde 1-2 minutos e seu site estará em:**
`https://inematds.github.io/SuperProf`

### 9. (Opcional) Configurar Tema Jekyll

Para melhorar a aparência, você pode adicionar um tema Jekyll.

Crie um arquivo `_config.yml` na raiz:

```bash
cat > _config.yml << 'EOF'
# Site settings
title: SuperProfessores
description: Transformando educadores em arquitetos do futuro da aprendizagem
baseurl: "/SuperProf"
url: "https://inematds.github.io"

# Theme
theme: jekyll-theme-cayman
# Ou outro tema: minima, slate, architect, etc.

# Markdown
markdown: kramdown

# Plugins
plugins:
  - jekyll-feed
  - jekyll-seo-tag

# Exclude files
exclude:
  - node_modules/
  - .bmad-core/
  - .claude/
  - package.json
  - package-lock.json
  - GUIA_GITHUB_PAGES.md
EOF
```

Depois, commit e push:

```bash
git add _config.yml
git commit -m "Add Jekyll theme configuration"
git push
```

### 10. Verificar Deploy

1. Acesse: https://github.com/inematds/SuperProf/actions
2. Veja o status do deploy (deve ter um check verde ✅)
3. Acesse seu site: https://inematds.github.io/SuperProf

---

## 📁 Estrutura de Arquivos Recomendada

```
SuperProf/
├── README.md                          # Página inicial
├── _config.yml                        # Configuração Jekyll
├── .gitignore                         # Arquivos ignorados
├── package.json                       # Dependências (apenas referência)
├── GUIA_GITHUB_PAGES.md              # Este guia
├── doc/
│   ├── superprofessores_modelo_hibrido_2025.md    # Proposta completa
│   ├── comparacao_trilhas.md                       # Comparação Trilha A vs B
│   ├── sumario_executivo_visual.md                # Sumário executivo
│   └── proposta_curso_ia_final/                   # Proposta original
│       ├── README_expandido.md
│       ├── sumario_executivo_expandido.md
│       ├── proposta_curso_final_expandida.md
│       ├── proposta_curso_expandida.md
│       ├── analise_documento.md
│       ├── pesquisa_frameworks_cursos.md
│       └── pesquisa_conteudos_avancados.md
└── (outros arquivos...)
```

---

## 🎨 Customizações Avançadas (Opcional)

### Adicionar Google Analytics

No `_config.yml`:

```yaml
google_analytics: G-XXXXXXXXXX
```

### Adicionar Logo

Coloque uma imagem `logo.png` na raiz e adicione no `_config.yml`:

```yaml
logo: /logo.png
```

### Criar Página de FAQ

Crie `faq.md`:

```markdown
---
layout: default
title: FAQ
---

# Perguntas Frequentes

...
```

### Criar Página de Contato

Crie `contato.md`:

```markdown
---
layout: default
title: Contato
---

# Entre em Contato

...
```

---

## 🔧 Comandos Úteis

### Atualizar o Site

```bash
# Após fazer mudanças nos arquivos
git add .
git commit -m "Descrição da atualização"
git push
```

### Ver Status do Git

```bash
git status
```

### Ver Histórico

```bash
git log --oneline
```

### Criar Nova Branch

```bash
git checkout -b nova-feature
```

### Voltar para Main

```bash
git checkout main
```

---

## 🐛 Troubleshooting

### Problema: Site não aparece

**Solução:**
1. Verifique se o GitHub Pages está ativado em Settings
2. Aguarde 1-2 minutos após o push
3. Force refresh: Ctrl+F5 (Windows) ou Cmd+Shift+R (Mac)

### Problema: Página 404

**Solução:**
1. Verifique se o arquivo existe no repositório
2. Verifique se o `baseurl` no `_config.yml` está correto
3. Links devem ser: `/SuperProf/doc/arquivo.md` ou relativos

### Problema: Formatação quebrada

**Solução:**
1. Verifique se o Markdown está correto
2. Teste localmente com: `bundle exec jekyll serve`
3. Veja o log de build em Actions

### Problema: Imagens não aparecem

**Solução:**
1. Caminhos devem ser relativos: `![](../imagem.png)`
2. Ou absolutos: `![](https://github.com/.../imagem.png)`
3. Ou com baseurl: `![]({{ site.baseurl }}/imagem.png)`

---

## 📊 Monitoramento

### Ver Tráfego do Site

1. Acesse: https://github.com/inematds/SuperProf/graphs/traffic
2. Veja visitantes únicos, views, clones

### Ver Quem Deu Star

1. Acesse: https://github.com/inematds/SuperProf/stargazers

### Ver Forks

1. Acesse: https://github.com/inematds/SuperProf/network/members

---

## 🚀 Próximos Passos

### Depois de Publicar:

1. ✅ Compartilhe o link nas redes sociais
2. ✅ Adicione ao LinkedIn
3. ✅ Compartilhe com educadores
4. ✅ Submeta para comunidades (Reddit, HN, etc.)
5. ✅ Crie issues para melhorias
6. ✅ Aceite contribuições via PR

### Melhorias Futuras:

- [ ] Adicionar vídeo de apresentação
- [ ] Criar página de inscrição (Google Forms)
- [ ] Adicionar depoimentos de educadores
- [ ] Criar blog com artigos sobre IA na educação
- [ ] Adicionar seção de recursos (prompts, templates)

---

## 📞 Ajuda

Se tiver problemas:

1. Consulte a [documentação do GitHub Pages](https://docs.github.com/pages)
2. Abra uma [issue no GitHub](https://github.com/inematds/SuperProf/issues)
3. Envie email: inematds@gmail.com

---

## 📚 Recursos Adicionais

- [Documentação Jekyll](https://jekyllrb.com/docs/)
- [Temas Jekyll](https://jekyllthemes.io/)
- [GitHub Pages Docs](https://docs.github.com/pages)
- [Markdown Guide](https://www.markdownguide.org/)

---

<div align="center">

**Boa sorte com a publicação! 🚀**

Se este guia foi útil, considere deixar uma ⭐ no repositório!

</div>
