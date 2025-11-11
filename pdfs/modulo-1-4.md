# Módulo 1.4: Pensamento Crítico com IA

**Nível 1: Fundamentos | Carga Horária: 12 horas**

---

## 📖 Visão Geral

LLMs não são infalíveis. Desenvolva ceticismo saudável para usar IA com responsabilidade. Aprenda a detectar alucinações (invenções), identificar vieses estruturais, avaliar qualidade com Framework CRAFT e usar detectores de IA criticamente.

---

## 🎯 Tópico 1: Alucinações - O Risco #1

### O que é Alucinação?

**Alucinação = Quando LLM inventa dados, referências ou fatos com confiança absoluta**

É o risco #1 de IA na educação (alunos podem aprender informações falsas).

### 3 Tipos de Alucinação:

#### 1. Alucinação Factual
Invenção de dados ou eventos

**Exemplo:**
```
Pergunta: "Qual livro Machado de Assis publicou em 1920?"
Alucinação: "Em 1920 publicou 'A Última Crônica'" ❌
Realidade: Machado morreu em 1908 ✅
```

#### 2. Alucinação de Referência
Citação de fontes inexistentes

**Exemplo:**
```
Output: "Segundo estudo de Silva et al. (2024) na revista Nature..."
Problema: Artigo não existe ❌
```

#### 3. Alucinação de Conceito
Confusão entre conceitos similares

**Exemplo:**
```
Pergunta: "Explique fotofosforilação"
Alucinação: [Mistura fotossíntese + fosforilação incorretamente]
```

### 5 Técnicas para Detectar Alucinações:

1. **Validação cruzada:** Pergunte para 2-3 LLMs diferentes. Respostas divergentes = sinal de alerta
2. **Peça fontes:** Sempre solicite referências. Se LLM hesita ou inventa, é alucinação
3. **Verifique datas:** Cheque se eventos/publicações são cronologicamente possíveis
4. **Busca manual:** Para informações críticas, confirme com Google Scholar/Wikipedia
5. **Ceticismo com especificidade:** Quanto mais específico (nomes, datas, números), maior risco

---

## ⚖️ Tópico 2: Vieses de LLMs

### O que é Viés?

**Viés = Tendência sistemática do LLM favorecendo certos grupos/perspectivas**

Não é "erro", mas reflexo dos dados de treinamento (majoritariamente inglês, ocidental, masculino).

### 5 Tipos de Viés em LLMs:

#### 1️⃣ Viés Cultural
**O que é:** Favorece cultura anglo-saxã
**Exemplo:** "successful CEO" → descreve homem branco

#### 2️⃣ Viés Temporal
**O que é:** Dados até 2023, não sabe eventos recentes
**Exemplo:** Não sabe eleições 2024, descobertas científicas recentes

#### 3️⃣ Viés Linguístico
**O que é:** Melhor em inglês, português tem mais erros
**Exemplo:** Alucinações são mais comuns em português

#### 4️⃣ Viés de Gênero
**O que é:** Assume profissões por gênero
**Exemplo:** "Enfermeiro" → assume mulher | "Engenheiro" → assume homem

#### 5️⃣ Viés de Consenso
**O que é:** Favorece visões majoritárias
**Exemplo:** Silencia perspectivas minoritárias

### Como Mitigar Vieses:

- ✅ **Prompt explícito:** "Considere perspectivas de diferentes culturas/gêneros"
- ✅ **Diversifique fontes:** Use múltiplos LLMs + busca humana
- ✅ **Educação crítica:** Ensine alunos a identificar vieses
- ✅ **Validação local:** Adapte outputs para contexto brasileiro

---

## 🔍 Tópico 3: Framework CRAFT

### O que é CRAFT?

Framework de 5 critérios para avaliar confiabilidade de outputs de IA antes de usar em aula.

### Os 5 Critérios (0-2 pontos cada):

#### C - Completeness (Completude)
**Pergunta:** A resposta cobre todos os aspectos necessários?
- ✅ Bom: Responde pergunta + contexto + exemplos
- ❌ Ruim: Resposta superficial

#### R - Relevance (Relevância)
**Pergunta:** O conteúdo é pertinente ao objetivo pedagógico?
- ✅ Bom: Foco no que foi pedido
- ❌ Ruim: Divaga em tópicos tangenciais

#### A - Accuracy (Precisão)
**Pergunta:** Informações são factuais e verificáveis?
- ✅ Bom: Fatos corretos + fontes
- ❌ Ruim: Alucinações ou erros conceituais

#### F - Fairness (Imparcialidade)
**Pergunta:** Evita vieses e representa múltiplas perspectivas?
- ✅ Bom: Visões diversas
- ❌ Ruim: Favorece um grupo/perspectiva

#### T - Tone (Tom)
**Pergunta:** Linguagem é apropriada para público-alvo?
- ✅ Bom: Adequado ao nível/idade
- ❌ Ruim: Muito técnico ou infantilizado

### Sistema de Pontuação:

- Atribua 0-2 pontos para cada critério
- Pontuação total: 0-10 pontos
- **8-10:** Pronto para usar ✅
- **5-7:** Requer edição 🟡
- **0-4:** Refazer ou descartar ❌

---

## 🤖 Tópico 4: Detectores de IA

### Ferramentas Principais (Nov 2025):

| Ferramenta | Custo | Precisão |
|------------|-------|----------|
| GPTZero | Gratuito | ~70% |
| Turnitin AI Detector | Pago | ~75% |
| Originality.AI | Pago | ~80% |
| ZeroGPT | Gratuito | ~65% |

### Problemas dos Detectores:

❌ **Falsos positivos:** 25-40% de textos humanos são marcados como IA

❌ **Viés contra não-nativos:** Alunos ESL (inglês como 2ª língua) são mais detectados

❌ **Fácil de enganar:** Parafrasear ou traduzir texto burla detector

❌ **Piora com edição:** Texto gerado por IA + editado por humano = indetectável

### Recomendação Pedagógica:

**❌ NÃO use detectores como prova punitiva**

**✅ USO CORRETO:**
- Detector acusa → Conversar com aluno (não punir automaticamente)
- Foco em processo: Avaliar rascunhos, diário de bordo, apresentação oral
- Redesenhar avaliações: Menos textos escritos, mais atividades presenciais

**❌ EVITAR:**
- Zero automático baseado em detector (pode ser injusto)

---

## 📦 Recursos do Módulo

### 📹 Videoaulas (3h)
- Alucinações explicadas (45 min)
- Vieses de LLMs (50 min)
- Framework CRAFT tutorial (40 min)
- Detectores de IA - Análise crítica (45 min)

### 📄 Leituras (4h)
- Pesquisa sobre alucinações (60 min)
- Vieses em IA - Paper UNESCO (60 min)
- Guia CRAFT completo (45 min)
- Detectores: Eficácia e ética (55 min)

### 💬 Práticas (4h)
- Caça a alucinações (60 min)
- Identificar vieses em outputs (45 min)
- Aplicar CRAFT em 10 textos (90 min)
- Testar 4 detectores (45 min)

### ✅ Avaliação (1h)
- Quiz de pensamento crítico (30 questões)
- Análise de caso: Texto com alucinações
- Proposta de política de IA na escola

---

**© 2025 SuperProfessores | Licença MIT**
