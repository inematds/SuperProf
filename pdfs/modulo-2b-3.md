# Módulo 2B.3: Criação de Agentes Educacionais com IA

**Nível 2B: Técnico | Carga Horária: 15 horas**

---

## 📖 Visão Geral

Aprenda a criar agentes autônomos de IA capazes de executar tarefas complexas em educação. Domine frameworks como LangChain Agents, AutoGPT e CrewAI para construir tutores personalizados, geradores de conteúdo e assistentes de pesquisa que agem com mínima supervisão humana.

### Objetivos:
- Entender arquitetura de agentes (ReAct, Plan-and-Execute)
- Implementar agente com ferramentas customizadas
- Criar tutor socrático que faz perguntas ao invés de dar respostas
- Construir gerador de conteúdo multi-step (pesquisa + síntese + validação)
- Orquestrar múltiplos agentes (multi-agent systems)

---

## 🤖 O que são Agentes de IA?

### Definição:

**Agente = LLM + Ferramentas + Loop de Raciocínio**

**Diferença de Chatbot:**

**Chatbot:**
```
User: "Qual a capital da França?"
LLM: "A capital da França é Paris."
[1 turno, resposta direta]
```

**Agente:**
```
User: "Me dê informações atualizadas sobre Paris"

Agent (interno):
1. Thought: "Preciso buscar informações recentes"
2. Action: google_search("Paris novidades 2025")
3. Observation: [Resultados da busca]
4. Thought: "Preciso sintetizar em tópicos"
5. Action: None (raciocínio suficiente)
6. Final Answer: "Aqui estão 5 novidades sobre Paris..."

[Multi-step, usa ferramentas, raciocínio iterativo]
```

---

## 🧩 Arquitetura de Agentes

### Componente 1: Brain (LLM)

**Função:** Raciocínio e decisão

**Modelos Recomendados:**
- **GPT-4:** Melhor raciocínio, mais caro
- **GPT-3.5:** Bom custo-benefício
- **Claude 3:** Forte em reasoning chains
- **LLaMA 3 70B:** Open-source, mas requer infra

---

### Componente 2: Tools (Ferramentas)

**Função:** Ações que agente pode executar

**Exemplos Educacionais:**

```python
tools = [
    Tool(
        name="Buscar_Biblioteca",
        func=buscar_em_pdfs,
        description="Busca informação em materiais do curso"
    ),
    Tool(
        name="Gerar_Quiz",
        func=gerar_questoes,
        description="Cria questões de múltipla escolha sobre tópico"
    ),
    Tool(
        name="Avaliar_Resposta",
        func=corrigir_resposta,
        description="Avalia resposta do aluno (0-10)"
    ),
    Tool(
        name="Recomendar_Material",
        func=recomendar_recurso,
        description="Sugere material baseado em dificuldades"
    )
]
```

**Anatomia de uma Tool:**
- **Nome:** Identificador único
- **Função:** Código Python que executa
- **Descrição:** Como LLM entende quando usar (crítico!)

---

### Componente 3: Memory (Memória)

**Função:** Lembrar interações passadas

**Tipos:**

**Short-term (Conversa Atual):**
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context(
    {"input": "Olá"},
    {"output": "Olá! Como posso ajudar?"}
)
```

**Long-term (Entre Sessões):**
```python
from langchain.memory import VectorStoreRetrieverMemory

# Armazena em vector DB, busca por similaridade
memory = VectorStoreRetrieverMemory(retriever=vectordb.as_retriever())
```

---

### Componente 4: Agent Loop (Ciclo de Raciocínio)

**Framework: ReAct (Reasoning + Acting)**

```
Loop até responder:
1. REASON: "Que informação preciso?"
2. ACT: Usar ferramenta
3. OBSERVE: Ver resultado
4. [Repetir ou finalizar]
```

**Exemplo Real:**

```
User: "Crie quiz sobre fotossíntese para 8º ano"

Iteration 1:
├─ Thought: "Preciso saber o que alunos já aprenderam"
├─ Action: Buscar_Biblioteca(tópico="fotossíntese", série="8º ano")
└─ Observation: "Alunos já viram cloroplastos, mas não Calvin cycle"

Iteration 2:
├─ Thought: "Vou criar questões focadas no nível deles"
├─ Action: Gerar_Quiz(tópico="fotossíntese", nível="intermediário", n=5)
└─ Observation: [5 questões geradas]

Iteration 3:
├─ Thought: "Questões estão boas, posso responder"
├─ Action: None
└─ Final Answer: "Aqui está seu quiz: [QUESTÕES]"
```

---

## 🛠️ Implementação: Tutor Socrático

### Objetivo:

Criar agente que ensina fazendo perguntas (método socrático), não dando respostas diretas.

### Código (LangChain):

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

# Ferramentas
def avaliar_compreensao(resposta_aluno: str) -> str:
    """Avalia se aluno entendeu conceito baseado na resposta"""
    prompt = f"""
    Resposta do aluno: {resposta_aluno}

    Analise:
    1. Aluno demonstrou compreensão? (Sim/Parcial/Não)
    2. Conceitos corretos mencionados
    3. Misconceptions identificadas

    Formato: JSON
    """
    # [Chamar LLM para analisar]
    return resultado

def gerar_pergunta_socratica(topico: str, nivel_dificuldade: str) -> str:
    """Gera pergunta que leva aluno a descobrir resposta"""
    prompt = f"""
    Tópico: {topico}
    Nível: {nivel_dificuldade}

    Crie pergunta socrática que:
    - Não dá resposta direta
    - Faz aluno pensar e conectar conceitos
    - Usa analogias ou contra-exemplos

    Exemplo ruim: "O que é fotossíntese?"
    Exemplo bom: "Se plantas precisam de luz solar, como sobrevivem em florestas densas?"
    """
    # [Chamar LLM]
    return pergunta

tools = [
    Tool(
        name="Avaliar_Compreensao",
        func=avaliar_compreensao,
        description="Usa isto quando aluno responder uma pergunta. Retorna análise de compreensão."
    ),
    Tool(
        name="Gerar_Pergunta",
        func=gerar_pergunta_socratica,
        description="Usa isto para criar próxima pergunta baseada em tópico e nível."
    )
]

# System Prompt
system_prompt = """
Você é um tutor socrático de biologia.

Regras:
1. NUNCA dê respostas diretas
2. SEMPRE faça perguntas que levem aluno a descobrir
3. Use analogias e exemplos do cotidiano
4. Se aluno errar, faça pergunta mais simples
5. Se acertar, aprofunde com pergunta mais complexa
6. Seja encorajador e paciente

Ferramentas disponíveis: {tools}

Formato de resposta:
Thought: [Seu raciocínio]
Action: [Ferramenta a usar]
Action Input: [Input da ferramenta]
Observation: [Resultado da ferramenta]
... (repita Thought/Action/Observation até ter resposta)
Final Answer: [Sua pergunta para o aluno]
"""

# Inicializar agente
llm = OpenAI(temperature=0.7, model="gpt-4")
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="conversational-react-description",
    memory=memory,
    verbose=True,  # Ver raciocínio interno
    system_message=system_prompt
)

# Usar
response = agent.run("Quero entender fotossíntese")
print(response)
```

**Output Esperado:**
```
Thought: Aluno quer entender fotossíntese. Vou começar descobrindo conhecimento prévio.
Action: Gerar_Pergunta
Action Input: {"topico": "fotossíntese", "nivel_dificuldade": "iniciante"}
Observation: "Você já viu plantas em lugares diferentes (sombra vs sol). O que você nota de diferente nelas?"

Final Answer: Ótimo! Vamos explorar fotossíntese juntos. Para começar: você já percebeu que plantas crescem em lugares diferentes - algumas no sol, outras na sombra. O que você acha que muda em plantas que ficam em locais muito ensolarados comparado às que ficam na sombra?
```

---

## 🎓 Caso 2: Gerador de Conteúdo Multi-Step

### Objetivo:

Agente que cria aula completa:
1. Pesquisa tópico
2. Estrutura conteúdo
3. Gera materiais (slides, quiz, atividades)
4. Valida qualidade

### Arquitetura Plan-and-Execute:

```python
from langchain.agents import create_plan_and_execute_agent
from langchain.tools import Tool

# Fase 1: PLAN
plan_prompt = """
Tarefa: Criar aula de 50min sobre {topico} para {publico}

Crie plano com:
1. Objetivos de aprendizagem (3-5)
2. Estrutura da aula (tempo em minutos)
3. Materiais necessários
4. Forma de avaliação

Formato: Lista numerada de passos acionáveis
"""

# Fase 2: EXECUTE
# Agente executa cada passo do plano usando ferramentas

tools = [
    Tool(
        name="Pesquisar_Conteudo",
        func=pesquisar_web_e_pdfs,
        description="Busca informações atualizadas sobre tópico"
    ),
    Tool(
        name="Gerar_Slide",
        func=criar_slide_markdown,
        description="Cria slide em markdown com título, conteúdo, imagens"
    ),
    Tool(
        name="Gerar_Quiz",
        func=criar_questoes,
        description="Cria questões de múltipla escolha"
    ),
    Tool(
        name="Validar_Qualidade",
        func=revisar_conteudo,
        description="Verifica se conteúdo está adequado (Bloom, BNCC, etc)"
    )
]

agent = create_plan_and_execute_agent(
    llm=llm,
    tools=tools,
    verbose=True
)

# Executar
resultado = agent.run(
    "Crie aula sobre Inteligência Artificial para ensino médio (15-17 anos)"
)
```

**Output:**
```
Plan:
1. Pesquisar: conceitos de IA adequados para ensino médio
2. Estruturar: aula de 50min (5min intro, 20min conceitos, 15min prática, 10min avaliação)
3. Criar: 10 slides sobre IA (história, tipos, ética)
4. Gerar: 5 questões de múltipla escolha
5. Validar: checar alinhamento com BNCC
6. Empacotar: ZIP com slides + quiz + plano de aula

Executing Step 1...
[Agente usa ferramenta Pesquisar_Conteudo]
Found: "IA é campo da computação que simula inteligência humana..."

Executing Step 2...
[Agente raciocina sobre estrutura]
Structure: Intro (historia) → Tipos (supervised/unsupervised/RL) → Etica → Hands-on

...

Final Package:
├── aula_ia.md (10 slides)
├── quiz_ia.json (5 questões)
├── plano_aula.pdf
└── recursos_adicionais.txt
```

---

## 🤝 Multi-Agent Systems

### Conceito:

Múltiplos agentes especializados trabalhando juntos.

**Exemplo: Criação de Curso Completo**

```
Agente 1 - Pesquisador:
└─ Busca conteúdo, papers, exemplos

Agente 2 - Designer Instrucional:
└─ Estrutura curso seguindo ADDIE

Agente 3 - Criador de Conteúdo:
└─ Gera aulas, slides, atividades

Agente 4 - Avaliador:
└─ Cria quizzes, rubricas

Agente 5 - Revisor:
└─ Valida qualidade, corrige erros
```

### Implementação (CrewAI):

```python
from crewai import Agent, Task, Crew

# Definir agentes
pesquisador = Agent(
    role="Pesquisador Educacional",
    goal="Encontrar conteúdo de qualidade sobre {topico}",
    backstory="Você é PhD em Educação com 15 anos pesquisando métodos eficazes",
    tools=[google_search, arxiv_search, wikipedia],
    verbose=True
)

designer = Agent(
    role="Designer Instrucional",
    goal="Estruturar aprendizagem seguindo melhores práticas",
    backstory="Especialista em ADDIE, Bloom, Merrill",
    tools=[criar_estrutura, alinhar_bncc],
    verbose=True
)

criador = Agent(
    role="Criador de Conteúdo",
    goal="Gerar materiais envolventes e claros",
    backstory="Você é professor com 10 anos criando recursos didáticos",
    tools=[gerar_slide, gerar_atividade, gerar_video_script],
    verbose=True
)

revisor = Agent(
    role="Revisor de Qualidade",
    goal="Garantir excelência pedagógica",
    backstory="Coordenador pedagógico rigoroso com olho para detalhes",
    tools=[validar_conteudo, checar_acessibilidade],
    verbose=True
)

# Definir tarefas
task1 = Task(
    description="Pesquisar sobre {topico} e compilar 10 melhores recursos",
    agent=pesquisador
)

task2 = Task(
    description="Criar estrutura de curso de 12h baseado na pesquisa",
    agent=designer
)

task3 = Task(
    description="Gerar materiais para os 6 módulos do curso",
    agent=criador
)

task4 = Task(
    description="Revisar todos os materiais e sugerir melhorias",
    agent=revisor
)

# Criar crew (equipe)
crew = Crew(
    agents=[pesquisador, designer, criador, revisor],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

# Executar
resultado = crew.kickoff(inputs={"topico": "Pensamento Computacional para Ensino Fundamental"})

print(resultado)
```

**Output:**
```
[Pesquisador]: Encontrei 10 recursos sobre pensamento computacional...
[Designer]: Estruturei curso em 6 módulos: 1) Decomposição, 2) Padrões...
[Criador]: Gerados 6 conjuntos de materiais com 18 atividades...
[Revisor]: Validação completa. Sugestões: Módulo 3 muito denso, sugiro dividir...

Final Result:
✅ Curso de 12h estruturado
✅ 18 atividades hands-on
✅ 6 avaliações formativas
✅ Alinhado com BNCC (EF05MA05, EF67LP04...)
```

---

## ⚠️ Challenges e Limitações

### 1. Loops Infinitos

**Problema:** Agente fica preso em ciclo

```
Thought: Preciso de mais informação
Action: Buscar
Observation: [Resultados]
Thought: Preciso de mais informação
Action: Buscar
[LOOP INFINITO]
```

**Solução:**
```python
agent = initialize_agent(
    ...,
    max_iterations=10,  # Limitar iterações
    early_stopping_method="generate"  # Forçar resposta após max
)
```

---

### 2. Uso Excessivo de Ferramentas

**Problema:** Agente usa 10 ferramentas para tarefa simples (custo $$)

**Solução: Few-shot Examples**

```python
system_prompt = """
Você é um agente eficiente.

Bons exemplos:
User: "Qual a capital da França?"
Thought: Sei a resposta, não preciso de ferramentas
Action: None
Final Answer: "Paris"

User: "Pesquise últimas notícias sobre IA"
Thought: Preciso buscar informação atualizada
Action: google_search("IA novidades 2025")
[Usa ferramenta apropriadamente]
"""
```

---

### 3. Alucinação de Ferramentas

**Problema:** Agente inventa ferramentas que não existem

```
Action: Ferramenta_Magica(input="resolver tudo")
[ERRO: Ferramenta não existe]
```

**Solução: Descrições Claras**

```python
# Ruim
Tool(name="Search", description="Busca coisas")

# Bom
Tool(
    name="Buscar_Biblioteca_Curso",
    description="Busca informação APENAS nos PDFs do curso XYZ. Use quando aluno perguntar sobre conteúdo do curso. NÃO use para informações gerais da web."
)
```

---

## 📊 Avaliação de Agentes

### Métricas:

**1. Task Success Rate**
```
De 100 tarefas, quantas o agente completou corretamente?
Taxa de sucesso = 85/100 = 85%
```

**2. Average Steps to Completion**
```
Quantos passos (iterações) agente precisa em média?
Menos é melhor (eficiência)
```

**3. Tool Usage Efficiency**
```
Agente usa ferramenta certa na primeira tentativa?
Ou fica tentando várias até achar?
```

**4. Cost per Task**
```
Custo médio (tokens API) para completar tarefa
Importante para escala
```

### Teste A/B:

```python
# Agente A: GPT-3.5 (barato, rápido)
# Agente B: GPT-4 (caro, melhor raciocínio)

test_cases = [
    "Crie quiz sobre mitose para 9º ano",
    "Explique relatividade para ensino médio",
    ...  # 50 casos
]

for case in test_cases:
    result_a = agent_a.run(case)
    result_b = agent_b.run(case)

    # Avaliar qualidade (humano ou LLM)
    score_a = avaliar(result_a)
    score_b = avaliar(result_b)

    # Comparar custo
    cost_a = calcular_custo(result_a.tokens)
    cost_b = calcular_custo(result_b.tokens)

# Decidir: GPT-4 vale 10x o custo?
```

---

## 🎨 Casos de Uso Avançados

### 1. Assistente de Pesquisa Acadêmica

**Ferramentas:**
- Buscar ArXiv (papers científicos)
- Buscar Google Scholar
- Extrair informações de PDFs
- Sintetizar múltiplas fontes
- Gerar citações (APA/ABNT)

**Fluxo:**
```
User: "Pesquise sobre gamificação em educação STEM"

Agent:
1. Busca ArXiv + Scholar (últimos 3 anos)
2. Filtra top 10 papers mais citados
3. Lê abstracts
4. Sintetiza em 5 insights principais
5. Gera bibliografia formatada
```

---

### 2. Gerador de Trilhas Personalizadas

**Ferramentas:**
- Avaliar conhecimento prévio (quiz diagnóstico)
- Mapear currículo
- Recomendar recursos
- Gerar cronograma

**Fluxo:**
```
User: "Quero aprender Python para Data Science"

Agent:
1. Aplica quiz diagnóstico (10 questões)
2. Identifica: "Usuário sabe programação básica, mas zero estatística"
3. Cria trilha:
   - Semana 1-2: Pandas + NumPy
   - Semana 3-4: Estatística descritiva
   - Semana 5-6: Visualização (Matplotlib)
   - Semana 7-8: Machine Learning intro
4. Recomenda recursos específicos para cada semana
5. Gera cronograma adaptado a "3h/semana disponível"
```

---

### 3. Moderador de Fóruns Educacionais

**Ferramentas:**
- Detectar toxicidade
- Classificar tipo de pergunta
- Sugerir recursos relevantes
- Conectar alunos com dúvidas similares
- Notificar professor quando necessário

**Fluxo:**
```
Novo post: "Não entendo polinômios, socorro!"

Agent:
1. Classifica: "Pedido de ajuda em matemática"
2. Busca posts similares: "3 alunos com mesma dúvida esta semana"
3. Sugere: "Olá! Vi que 3 colegas têm dúvida similar. Que tal formarem grupo de estudo? Aqui está vídeo explicativo: [link]"
4. Notifica professor: "4 alunos com dificuldade em polinômios - considere aula de reforço"
```

---

## 📦 Recursos do Módulo

### 📹 Videoaulas (4h)
- Fundamentos de agentes (ReAct, Plan-Execute) (50 min)
- Implementando agente com LangChain (60 min)
- Multi-agent systems (60 min)
- Troubleshooting e otimização (50 min)

### 💬 Práticas (9h)
- Criar tutor socrático (3h)
- Implementar gerador de conteúdo multi-step (3h)
- Construir sistema multi-agente (3h)

### ✅ Avaliação (2h)
- Projeto: Agente funcional com ≥3 ferramentas customizadas
- Demonstração: Resolver 5 tarefas educacionais
- Análise: Comparar performance (GPT-3.5 vs GPT-4, single vs multi-agent)

---

## 📚 Referências

- **Paper:** "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al, 2022)
- **Docs:** LangChain Agents (python.langchain.com/docs/modules/agents)
- **Framework:** CrewAI (docs.crewai.com)
- **Curso:** DeepLearning.AI - Building AI Agents

---

**© 2025 SuperProfessores | Licença MIT**
