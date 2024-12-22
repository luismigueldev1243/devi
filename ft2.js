const selbtn = document.getElementById("selbtn");
const lvlbtn = document.getElementById("lvlbtn");
selbtn.addEventListener("click", () => {
  const selacc = document.querySelector('input[name="selacc"]').value;
  const selsnh = document.querySelector('input[name="selsnh"]').value;

  let clicks = 0;
  fetch("http://localhost:3000/user")
    .then((resp) => {
      return resp.json();
    })
    .then((data) => {
      if (!data[selacc]) {
        alert("usuario não existe. crie um !");
      }
      if (data[selacc]["senha"] != selsnh) {
        alert("senha incorreta");
      }
      if (data[selacc]["senha"]) {
        lvlbtn.addEventListener("click", () => {
          clicks++;
          fetch("http://localhost:3000/changeuser", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              usersel: selacc,
              lvl: clicks,
            }),
          });
        });
      }
    });
});
