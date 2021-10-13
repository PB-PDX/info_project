document.getElementById("userSubscribe").addEventListener("click", userSubscribe1);
const user_id = JSON.parse(document.getElementById('user_id').textContent);

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';




        



const buttons = document.querySelectorAll('.buttons');
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function (event) {    
        let snipId = event.target.name
        let subs = []
    async function fetchSubs() {
        const response = await fetch("subscribers/"+(snipId));  
        const subs = await response.json();
        return subs
    }
      
    fetchSubs().then(subs => {
        let x = subs.subscriber.values();
        sub = ""
        for (let letter of x){
            sub += letter
            
        }
        console.log(subs)
        return subs
      });    
     
    let x = fetchSubs()
    console.log(x, ' ssss')

    let zeta = []
    zeta.push(subs[0])
    zeta.push(user_id)
    console.log(zeta +' zeta')

    axios({
        method: 'patch',
        url: "subscribers/"+(snipId),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        data: {
            subscriber: [user_id]
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
        url: "subscribers/" + (user_id),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        data: {
            subscriber: [user_id]
        },
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => console.log(response))
}







