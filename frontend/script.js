const API_URL = "http://127.0.0.1:5000/tarefas";

const lista = document.getElementById("lista-tarefas");
const input = document.getElementById("input-tarefa");
const botao = document.getElementById("btn-adicionar");

carregarTarefas();

function criarElementoTarefa(tarefa) {
    const li = document.createElement("li");

    if (tarefa.concluida) {
        li.classList.add("concluida");
    }

    li.innerHTML = `
        ${tarefa.nome}
        <div>
            <button onclick="concluirTarefa(${tarefa.id})">✔</button>
            <button class="remover" onclick="removerTarefa(${tarefa.id})">✘</button>
        </div>
    `;

    lista.appendChild(li);
}

async function carregarTarefas() {
    try {

        const resposta = await fetch(API_URL);
        const tarefas = await resposta.json();

        lista.innerHTML = "";

        tarefas.forEach(tarefa => {
            criarElementoTarefa(tarefa);
        });

    } catch (erro) {
        console.error("Erro ao carregar tarefas:", erro)
    }
}

async function adicionarTarefa() {
    try {
        const nome = input.value;

        if (!nome.trim()) return;

        const resposta = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ nome })
        });

        if (!resposta.ok) {
            alert("Erro ao adicionar tarefa");
            return;
        }

        input.value = "";
        input.focus();
        carregarTarefas();

    } catch (erro) {
        console.error("Erro ao adicionar tarefa", erro);
    }
}

botao.addEventListener("click", adicionarTarefa);

async function concluirTarefa(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "PUT"
    });

    carregarTarefas();

}

async function removerTarefa(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });

    carregarTarefas();

}

input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        adicionarTarefa();
    }
});