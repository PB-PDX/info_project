document.getElementById("userSubscribe").addEventListener("click", userSubscribe1);
const user_id = JSON.parse(document.getElementById('user_id').textContent);


function userSubscribe1() {
    let data = new FormData();
    
    data.append("title", document.getElementById('title').value)  
    data.append("note", document.getElementById('note').value)
    data.append("csrfmiddlewaretoken", '{{csrf_token}}') 
    
    axios.post('create_note/', data) 
     .then(res => alert("Form Submitted")) 
     .catch(errors => console.log(errors)) }


    