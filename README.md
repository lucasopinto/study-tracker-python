# ✅ Study Tracker (Python)

🇧🇷 [Português](#-português) | 🇺🇸 [English](#-english)

---

## 🇧🇷 Português

### O que o projeto faz
Gerenciador de tarefas de estudo no terminal. Permite adicionar tarefas, listar com status (✅ concluída / ❌ pendente) e data de criação, marcar tarefas como concluídas e ver estatísticas de progresso. As tarefas ficam salvas em um arquivo JSON, então nada se perde ao fechar o programa.

### Tecnologias
- Python 3
- Bibliotecas padrão: `json`, `os`, `datetime`

### Como executar
```bash
git clone https://github.com/lucasopinto/study-tracker-python.git
cd study-tracker-python
python study_tracker.py
```
O arquivo `tarefas.json` é criado automaticamente. Não é preciso instalar dependências.

### O que aprendi
- Persistir dados em arquivo JSON (`json.load` / `json.dump`)
- Verificar se arquivos existem com `os.path.exists`
- Formatar datas com `datetime.strftime`
- Validar entradas do usuário com `try/except ValueError`
- Calcular estatísticas simples (total, concluídas e percentual)

---

## 🇺🇸 English

### What it does
A terminal study task manager. Add tasks, list them with status (✅ done / ❌ pending) and creation date, mark tasks as done and view progress statistics. Tasks are saved to a JSON file, so nothing is lost when the program closes.

### Tech stack
- Python 3
- Standard library: `json`, `os`, `datetime`

### How to run
```bash
git clone https://github.com/lucasopinto/study-tracker-python.git
cd study-tracker-python
python study_tracker.py
```
`tarefas.json` is created automatically. No dependencies required.

### What I learned
- Persisting data to JSON files
- Checking file existence with `os.path.exists`
- Formatting dates with `datetime.strftime`
- Validating user input with `try/except ValueError`
- Computing simple statistics (total, completed, percentage)
