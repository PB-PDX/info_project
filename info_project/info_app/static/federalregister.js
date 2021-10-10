document.getElementById("userSubscribe").addEventListener("click", userSubscribe1);
const user_id = JSON.parse(document.getElementById('user_id').textContent);
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

function userSubscribe1() {
    axios({
        method: 'patch',
        url: 'frapi/1',
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        data: {
            feeds: 'axios'
        },
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => console.log(response))}


