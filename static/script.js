function calculerScore(){

let q1 = document.querySelector('input[name="q1"]:checked');
let q2 = document.querySelector('input[name="q2"]:checked');
let q3 = document.querySelector('input[name="q3"]:checked');

if(!q1 || !q2 || !q3){
alert("Répondez à toutes les questions");
return;
}

let score = 
parseInt(q1.value) +
parseInt(q2.value) +
parseInt(q3.value);

let niveau = "";

if(score <=3) niveau="Niveau 1 - Débutant";
else if(score <=6) niveau="Niveau 2 - Intermédiaire";
else niveau="Niveau 3 - Avancé";

document.getElementById("resultat").innerHTML =
"Score : " + score + " / Niveau : " + niveau;

}
