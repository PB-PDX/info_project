document.getElementById("userSubscribe").addEventListener("click", userSubscribe1);
const user_id = JSON.parse(document.getElementById('user_id').textContent);
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';




const buttons = document.querySelectorAll('button');
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function (event) {
     let snipId = event.target.id

     axios({
        method: 'get',
        url: "frapi/"+(user_id),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => console.log(response))
        
   
     axios({
        method: 'patch',
        url: "frapi/"+(user_id),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        data: {
            feeds: snipId
        },
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => console.log(response))
     
  })
}

function userSubscribe1() {
    axios({
        method: 'patch',
        url: "frapi/"+(user_id),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        data: {
            feeds: 'FederalRegister'
        },
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => console.log(response))}







