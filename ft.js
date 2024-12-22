const btn = document.getElementById("send");
const checkidbutton = document.getElementById("check");
const checkaccbtn = document.getElementById("checkaccbtn");
const delbtn = document.getElementById("delbtn");

btn.addEventListener("click", () => {
  const nome = document.querySelector('input[name="nome"]').value;
  const idade = document.querySelector('input[name="idade"]').value;
  const snh = document.querySelector('input[name="snh"]').value;
  const lvl = document.querySelector('input[name="lvl"]').value;

  if (!(nome && idade)) {
    alert("Nome e idade são obrigatórios!");
    return;
  }

  fetch("http://localhost:3000/user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nome: nome,
      idade: idade,
      senha: snh,
      level: lvl,
    }),
  })
    .then((response) => response.text())
    .then((data) => {
      alert(data);
    })
    .catch((error) => {
      console.error("Erro ao enviar dados:", error);
    });
});

checkidbutton.addEventListener("click", () => {
  const checkname = document.querySelector('input[name="checkid"]').value;
  const res = document.getElementById("res");
  fetch("http://localhost:3000/user")
    .then((resp) => {
      return resp.json();
    })
    .then((data) => {
      if (data[checkname]) {
        res.innerHTML = "result: the id exists";
      } else {
        res.innerHTML = "result: the id do not exists";
      }
    });
});

checkaccbtn.addEventListener("click", () => {
  const checkname = document.querySelector('input[name="checkname"]').value;
  const checksnh = document.querySelector('input[name="checksnh"]').value;
  const checkidade = document.querySelector('input[name="checkidade"]').value;
  const h3 = document.querySelector("h3");
  fetch("http://localhost:3000/user")
    .then((resp) => {
      return resp.json();
    })
    .then((data) => {
      if (
        data[checkname]["senha"] == checksnh ||
        data[checkname]["idade"] == checkidade
      ) {
        h3.innerHTML = "level: " + data[checkname].level;
      } else {
        alert("usuario ou senha errados!");
      }
    });
});

delbtn.addEventListener("click", () => {
  const delname = document.querySelector('input[name="delid"]').value;
  const confirmacao = confirm("Deseja realmente remover o item?");
  if (confirmacao) {
    fetch("http://localhost:3000/remove/" + delname, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((resp) => resp.text())
      .then((data) => {
        alert(data); // Exibe a resposta do servidor
      });
  } else {
    alert("sucessfuly canceled");
  }
});
