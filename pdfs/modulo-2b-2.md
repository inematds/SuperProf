# Módulo 2B.2: Fine-Tuning e RAG - Especializando LLMs

**Nível 2B: Técnico | Carga Horária: 15 horas**

---

## 📖 Visão Geral

Aprenda a adaptar LLMs para necessidades educacionais específicas. Domine técnicas de fine-tuning (ajuste fino) e RAG (Retrieval-Augmented Generation) para criar assistentes especializados, bases de conhecimento personalizadas e sistemas de Q&A institucionais.

### Objetivos:
- Entender quando usar RAG vs Fine-Tuning
- Implementar sistema RAG do zero (Python básico)
- Criar embeddings de materiais educacionais
- Fazer fine-tuning de modelo open-source (opcional)
- Construir chatbot especializado em conteúdo próprio

---

## 🎯 RAG vs Fine-Tuning: Quando Usar Cada Um?

### Problema Comum:

**Cenário:** Universidade quer chatbot que responde sobre regulamentos internos

**Opção 1: Prompt Engineering** ❌
- Colar regulamento no prompt
- Limite: Contexto máximo (128k-200k tokens)
- Problema: Documento tem 500 páginas = 500k tokens

**Opção 2: Fine-Tuning** ⚠️
- Treinar modelo nos regulamentos
- Problema: Caro ($$$), lento, não atualiza fácil
- Risco: Modelo "memoriza" mas pode alucinar

**Opção 3: RAG** ✅
- Busca trechos relevantes + injeta no prompt
- Barato, rápido, atualizável, verificável
- **Solução ideal para 90% dos casos educacionais**

---

## 📊 Tabela Comparativa

| Critério | RAG | Fine-Tuning |
|----------|-----|-------------|
| **Custo** | $ (barato) | $$$ (caro) |
| **Tempo setup** | Horas | Dias/Semanas |
| **Atualização** | Imediata (add docs) | Requer re-treino |
| **Verificabilidade** | Alta (cita fonte) | Baixa (caixa-preta) |
| **Privacidade** | Boa (docs locais) | Depende (modelo onde?) |
| **Complexidade** | Baixa | Alta |
| **Casos de uso** | Q&A, busca, suporte | Estilo, formato, domínio |

### Regra Prática:

**Use RAG quando:**
✅ Precisa de fontes verificáveis
✅ Conteúdo muda frequentemente
✅ Base de conhecimento grande (>100k tokens)
✅ Budget limitado
✅ Quer controle sobre o que modelo "sabe"

**Use Fine-Tuning quando:**
✅ Precisa mudar comportamento/estilo do modelo
✅ Domínio muito específico (jargão técnico)
✅ Dados sensíveis (não podem ir para API externa)
✅ Tem expertise técnico + infraestrutura

**Use Ambos quando:**
✅ Fine-tune para estilo + RAG para conhecimento
✅ Exemplo: Modelo fine-tuned para falar como professor + RAG para conteúdo de cursos

---

## 🔍 RAG: Retrieval-Augmented Generation

### Como Funciona (5 Passos):

```
1. INDEXAÇÃO (Feito 1x, ou quando docs mudam)
   └─ Quebrar documentos em chunks (pedaços)
   └─ Gerar embeddings para cada chunk
   └─ Armazenar em vector database

2. QUERY (Cada pergunta do usuário)
   └─ Usuário faz pergunta
   └─ Gerar embedding da pergunta

3. RETRIEVAL
   └─ Buscar chunks mais similares (cosine similarity)
   └─ Retornar top 5-10 chunks

4. AUGMENTATION
   └─ Montar prompt: "Baseado nestes trechos: [chunks], responda: [pergunta]"

5. GENERATION
   └─ LLM gera resposta usando chunks como contexto
```

---

## 🛠️ Implementando RAG: Passo-a-Passo

### Setup Inicial (Python + Bibliotecas)

```bash
pip install openai langchain chromadb pypdf sentence-transformers
```

**Bibliotecas:**
- `openai`: Acesso a GPT-4/GPT-3.5
- `langchain`: Framework para LLM apps
- `chromadb`: Vector database (grátis, local)
- `pypdf`: Ler PDFs
- `sentence-transformers`: Gerar embeddings

---

### Passo 1: Preparar Documentos

**Exemplo:** 10 PDFs de apostilas de curso

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Carregar PDFs
docs = []
for pdf_file in ["aula1.pdf", "aula2.pdf", ...]:
    loader = PyPDFLoader(pdf_file)
    docs.extend(loader.load())

# Quebrar em chunks (1000 chars, overlap 200)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200  # Overlap garante contexto entre chunks
)
chunks = splitter.split_documents(docs)

print(f"Total de chunks: {len(chunks)}")
# Saída: Total de chunks: 487
```

**Por que chunk_size=1000?**
- Pequeno demais (100): Perde contexto
- Grande demais (5000): Retrieval impreciso
- 1000-1500: Sweet spot para maioria dos casos

---

### Passo 2: Gerar Embeddings e Armazenar

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Gerar embeddings (usando OpenAI ada-002)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Criar vector database
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./db_curso"  # Salva localmente
)
vectordb.persist()

print("Database criado!")
```

**Custo:** ~$0.0001 per 1k tokens
- 487 chunks × 1000 chars ≈ 487k tokens
- Custo: ~$0.05 (único)

**Alternativa Grátis:** Usar `HuggingFaceEmbeddings` ao invés de OpenAI

```python
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)
```

---

### Passo 3: Fazer Perguntas (Query)

```python
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Carregar database
vectordb = Chroma(
    persist_directory="./db_curso",
    embedding_function=embeddings
)

# Criar chain de Q&A
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(model="gpt-3.5-turbo"),
    retriever=vectordb.as_retriever(search_kwargs={"k": 5}),  # Top 5 chunks
    return_source_documents=True  # Retorna fontes
)

# Fazer pergunta
result = qa_chain("Qual a diferença entre RAG e Fine-Tuning?")

print("Resposta:", result['result'])
print("\nFontes:")
for doc in result['source_documents']:
    print(f"- {doc.metadata['source']} (página {doc.metadata['page']})")
```

**Output:**
```
Resposta: RAG (Retrieval-Augmented Generation) é uma técnica que busca
informações relevantes em uma base de dados e as injeta no contexto do prompt,
enquanto Fine-Tuning é o processo de retreinar um modelo em dados específicos...

Fontes:
- aula5.pdf (página 12)
- aula5.pdf (página 13)
- aula7.pdf (página 8)
```

---

## 🎨 Melhorando o RAG

### Problema 1: Retrieval Ruim (Chunks Irrelevantes)

**Sintoma:** LLM responde "Não encontrei informação sobre isso" mesmo tendo

**Causas:**
1. Embeddings ruins
2. Chunks muito grandes/pequenos
3. Pergunta mal formulada

**Soluções:**

**A) Query Expansion (Expandir Pergunta)**
```python
# Antes
query = "RAG"

# Depois
query_expanded = """
RAG, Retrieval-Augmented Generation, busca semântica,
recuperação de informação, embeddings
"""
```

**B) Hybrid Search (Keyword + Semantic)**
```python
# Combinar BM25 (keyword) + embeddings (semantic)
from langchain.retrievers import BM25Retriever, EnsembleRetriever

keyword_retriever = BM25Retriever.from_documents(chunks)
semantic_retriever = vectordb.as_retriever()

ensemble = EnsembleRetriever(
    retrievers=[keyword_retriever, semantic_retriever],
    weights=[0.4, 0.6]  # 40% keyword, 60% semantic
)
```

**C) Reranking**
```python
# Buscar top 20, rerankar para top 5
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, docs):
    pairs = [[query, doc.page_content] for doc in docs]
    scores = reranker.predict(pairs)
    return sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)[:5]
```

---

### Problema 2: Resposta Sem Contexto

**Sintoma:** Resposta correta, mas não cita fonte ou dá detalhes

**Solução:** Melhorar Prompt de Síntese

```python
from langchain.prompts import PromptTemplate

template = """
Você é um assistente educacional especializado.

Use APENAS os trechos abaixo para responder. Se não souber, diga "Não encontrei essa informação nos materiais".

Contexto:
{context}

Pergunta: {question}

Instruções:
1. Responda de forma clara e educativa
2. Cite a fonte ([Fonte: nome_arquivo, página X])
3. Se múltiplas fontes, liste todas
4. Use exemplos dos trechos quando possível

Resposta:
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)
```

---

### Problema 3: Custo e Latência

**Sintoma:** Cada query demora 3-5 segundos e custa $$

**Soluções:**

**A) Cache de Embeddings**
```python
import shelve

cache = shelve.open("embedding_cache")

def get_embedding_cached(text):
    if text in cache:
        return cache[text]
    else:
        emb = embeddings.embed_query(text)
        cache[text] = emb
        return emb
```

**B) Usar Modelo Menor para Retrieval**
```python
# Retrieval: HuggingFace (grátis, local)
# Generation: GPT-4 (pago, mas só 1x por query)

retriever_embeddings = HuggingFaceEmbeddings()  # Grátis
generation_llm = OpenAI(model="gpt-4")  # Qualidade
```

**C) Batch Queries**
```python
# Se processando múltiplas perguntas, fazer em batch
queries = ["Pergunta 1", "Pergunta 2", ...]
embeddings_batch = embeddings.embed_documents(queries)  # 1 API call
```

---

## 🔧 Fine-Tuning: Quando e Como

### O que é Fine-Tuning?

**Pré-treino:** Modelo aprende linguagem geral (Wikipedia, livros, web)
**Fine-tuning:** Modelo aprende tarefa/domínio específico (seus dados)

### Exemplo: GPT-3 → ChatGPT

```
GPT-3 (base): Completa texto
Input: "Professor é"
Output: "uma profissão importante que..." [neutro]

ChatGPT (fine-tuned): Conversa
Input: "Explique fotossíntese"
Output: "Claro! Fotossíntese é o processo..." [instrutivo]

Diferença: Fine-tuned com 10k+ exemplos de conversas instrutivas
```

---

### Quando Fine-Tuning Faz Sentido (Educação):

**Caso 1: Correção Automática com Estilo Específico**
```
Dados: 1000 redações + correções de professor específico
Objetivo: Modelo que corrige no estilo desse professor
Resultado: Feedback personalizado em escala
```

**Caso 2: Geração de Questões de Múltipla Escolha**
```
Dados: 5000 questões criadas por instituição
Objetivo: Gerar novas questões no mesmo formato/dificuldade
Resultado: Banco de questões infinito
```

**Caso 3: Chatbot de Suporte Institucional**
```
Dados: 2 anos de tickets de suporte + respostas
Objetivo: Automatizar 70% das perguntas comuns
Resultado: Suporte 24/7
```

---

### Processo de Fine-Tuning (OpenAI GPT-3.5)

**Passo 1: Preparar Dados (JSONL)**

```json
{"messages": [
  {"role": "system", "content": "Você é um corretor de redações do ENEM"},
  {"role": "user", "content": "Redação: [TEXTO]"},
  {"role": "assistant", "content": "Análise: [FEEDBACK DETALHADO]"}
]}
{"messages": [...]}
```

**Requisitos:**
- Mínimo: 10 exemplos (recomendado: 50-100)
- Formato: JSONL (1 exemplo por linha)
- Qualidade > Quantidade

**Passo 2: Upload e Treino**

```python
import openai

# Upload do arquivo
file = openai.File.create(
  file=open("treino.jsonl", "rb"),
  purpose='fine-tune'
)

# Iniciar fine-tune
job = openai.FineTuningJob.create(
  training_file=file.id,
  model="gpt-3.5-turbo"
)

# Acompanhar progresso
openai.FineTuningJob.retrieve(job.id)
```

**Tempo:** 10 min - 2h (depende do tamanho)
**Custo:** $0.008 / 1k tokens (8x mais barato que treino from scratch)

**Passo 3: Usar Modelo Fine-Tuned**

```python
completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo:org:modelo_redacao:abc123",  # Seu modelo
  messages=[
    {"role": "system", "content": "Você é um corretor de redações do ENEM"},
    {"role": "user", "content": "Redação: [NOVA REDAÇÃO]"}
  ]
)
```

---

## 🎓 Caso Prático: Chatbot de Curso

**Objetivo:** Criar assistente que responde dúvidas sobre seu curso

**Stack:**
- RAG para conteúdo (apostilas, slides)
- LangChain para orquestração
- Streamlit para interface
- ChromaDB para vector store

### Código Completo (Simplificado):

```python
import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Setup
embeddings = HuggingFaceEmbeddings()
vectordb = Chroma(persist_directory="./db", embedding_function=embeddings)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Chain
chain = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(),
    retriever=vectordb.as_retriever(),
    memory=memory
)

# Interface
st.title("🤖 Assistente do Curso")
user_input = st.text_input("Sua pergunta:")

if user_input:
    response = chain({"question": user_input})
    st.write(response['answer'])
```

**Deploy:** Streamlit Cloud (grátis) ou Vercel

---

## 🔒 Considerações de Privacidade

### LGPD e Dados Educacionais:

**Problema:** Enviar dados de alunos para OpenAI/Anthropic

**Soluções:**

**1. Anonimização**
```python
import re

def anonimizar(texto):
    # Remove nomes
    texto = re.sub(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', '[NOME]', texto)
    # Remove emails
    texto = re.sub(r'\S+@\S+', '[EMAIL]', texto)
    # Remove CPFs
    texto = re.sub(r'\d{3}\.\d{3}\.\d{3}-\d{2}', '[CPF]', texto)
    return texto
```

**2. Modelo Local (Open-Source)**
```python
from langchain.llms import HuggingFacePipeline

# Baixar LLaMA 3 (8B) - roda em GPU consumer
llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3-8B-Instruct",
    device=0,  # GPU
    task="text-generation"
)

# Tudo roda local, zero API externa
```

**3. Azure OpenAI (Enterprise)**
- Dados não são usados para treinar
- SLA de privacidade
- Compliance com LGPD/GDPR

---

## 📊 Benchmarking e Avaliação

### Como Avaliar se RAG Está Funcionando?

**Métricas:**

**1. Retrieval Precision@K**
```
Dos K chunks retornados, quantos são realmente relevantes?
Precision@5 = (Chunks relevantes retornados) / 5
```

**2. MRR (Mean Reciprocal Rank)**
```
Em que posição aparece o primeiro chunk relevante?
MRR = 1 / (posição do primeiro relevante)
```

**3. Answer Quality (Humano)**
```
Escala 1-5:
1. Incorreto
2. Parcialmente correto
3. Correto mas incompleto
4. Correto e completo
5. Excelente (+ fontes + exemplos)
```

### Conjunto de Teste:

Criar 20-50 perguntas com respostas esperadas:

```python
test_set = [
    {
        "question": "O que é RAG?",
        "expected_answer": "Retrieval-Augmented Generation...",
        "relevant_chunks": ["aula5.pdf:p12", "aula5.pdf:p13"]
    },
    # ... mais exemplos
]

# Avaliar automaticamente
for item in test_set:
    result = qa_chain(item['question'])
    # Comparar result com expected_answer
    # Verificar se relevant_chunks foram retornados
```

---

## 📦 Recursos do Módulo

### 📹 Videoaulas (4h)
- RAG: Conceitos e arquitetura (50 min)
- Implementação RAG do zero (90 min)
- Fine-tuning: Quando e como (60 min)
- Casos práticos e troubleshooting (40 min)

### 💬 Práticas (9h)
- Implementar RAG com seus documentos (4h)
- Melhorar retrieval (reranking, hybrid) (2h)
- Criar interface com Streamlit (2h)
- Avaliar e iterar (1h)

### ✅ Avaliação (2h)
- Projeto: Chatbot RAG funcional com ≥20 docs
- Demonstração: Responder 10 perguntas com fontes
- Documentação: Explicar escolhas técnicas

---

## 📚 Referências

- **Paper:** "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al, 2020)
- **Docs:** LangChain Documentation (python.langchain.com)
- **Curso:** DeepLearning.AI - Building Applications with Vector Databases
- **Blog:** Pinecone Learning Center (vector databases)

---

**© 2025 SuperProfessores | Licença MIT**
