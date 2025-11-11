# Módulo 2A.2: Avaliação Formativa Assistida por IA

**Nível 2A: Pedagógico | Carga Horária: 12 horas**

---

## 📖 Visão Geral

Transforme avaliação de punitiva para formativa usando IA. Aprenda a dar feedback personalizado em escala, criar rubricas adaptativas e detectar gaps de aprendizagem com análise automática.

### Objetivos:
- Gerar feedback personalizado para 30+ alunos em 1h (vs 6h manual)
- Criar rubricas analíticas com IA alinhadas a objetivos
- Implementar avaliação diagnóstica, formativa e somativa com IA
- Analisar padrões de erro em turmas com dashboards automatizados

---

## 📊 Tipos de Avaliação com IA

### 1. Diagnóstica (Pré-curso)
**Objetivo:** Identificar conhecimento prévio
**IA:** Gerador de testes adaptativos

**Prompt Claude:**
```
Crie teste diagnóstico de 15 questões sobre [TEMA]:
- 5 fáceis (conceitos básicos)
- 5 médias (aplicação)
- 5 difíceis (análise)

Para cada questão:
- Enunciado claro
- 4 alternativas
- Feedback para cada alternativa (por que está certa/errada)
- Conceito testado

Formato: JSON estruturado para quiz adaptativo
```

### 2. Formativa (Durante)
**Objetivo:** Monitorar progresso e ajustar ensino
**IA:** Feedback automatizado

**Caso Real - Correção de Redações:**
- Sem IA: 3 min/redação × 30 alunos = 90 min
- Com IA: 30 min total (revisar outputs da IA)
- **Economia: 67%**

### 3. Somativa (Final)
**Objetivo:** Certificar aprendizagem
**IA:** Análise de consistência e vieses

---

## 🎯 Rubricas Analíticas com IA

### Estrutura de Rubrica:
- **Critérios:** O que será avaliado
- **Níveis:** Insuficiente, Básico, Proficiente, Avançado
- **Descritores:** O que caracteriza cada nível

### Gerador de Rubricas:

**Prompt ChatGPT:**
```
Crie rubrica analítica para avaliar [TAREFA]:

Critérios (4-6):
[Listar critérios essenciais]

Para cada critério, defina 4 níveis:
1. Insuficiente (0-25%): [Descritor específico]
2. Básico (26-50%): [Descritor específico]
3. Proficiente (51-75%): [Descritor específico]
4. Avançado (76-100%): [Descritor específico]

Formato: Tabela markdown
Público: [NÍVEL]
```

---

## 💬 Feedback Personalizado em Escala

### Problema:
Professores gastam 6h/semana dando feedback. 80% é repetitivo.

### Solução IA:
**Feedback Generator** - Personaliza mensagens baseado em padrões

**Prompt Multi-LLM:**
```
# Etapa 1: Claude analisa todos os trabalhos
Analise estas 30 redações e identifique:
1. Erros mais comuns (top 5)
2. Pontos fortes recorrentes (top 3)
3. Perfis de alunos (por padrão de erro)

# Etapa 2: ChatGPT gera feedbacks personalizados
Para cada aluno, crie feedback que:
- Menciona 2 pontos fortes específicos
- Sugere 2 melhorias prioritárias
- Conecta com erro comum identificado
- Tom: Encorajador, construtivo, específico
- Extensão: 100-150 palavras

# Etapa 3: Professor revisa e ajusta
```

**Resultado:** Feedback personalizado em 1h (vs 6h manual)

---

## 📦 Recursos do Módulo

### 📹 Videoaulas (3h)
- Avaliação formativa vs somativa (40 min)
- Criação de rubricas (45 min)
- Feedback em escala (50 min)
- Análise de padrões (45 min)

### 💬 Práticas (7h)
- Criar rubrica para sua disciplina (2h)
- Corrigir 10 trabalhos com IA (3h)
- Implementar ciclo de feedback (2h)

### ✅ Avaliação (2h)
- Entregar rubrica + 10 feedbacks
- Análise de impacto

---

**© 2025 SuperProfessores | Licença MIT**
