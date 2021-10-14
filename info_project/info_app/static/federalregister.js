const user_id = JSON.parse(document.getElementById('user_id').textContent);
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// This for loop listens to all the buttons on the page for a click with the class of buttons and then a variable is set to the buttons 'name', which is the snippets pk. 
const buttons = document.querySelectorAll('.buttons');
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function (event) {
        let snipId = event.target.name
        async function getData() {
            try {
                let res = await axios({
                    method: 'get',
                    url: "subscribers/" + (snipId),
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                })
                if (res.status == 200) {
                    // console.log(res.status)
                }
                return res.data.subscriber
            }
            catch (err) {
                console.error(err);
            }
        }

        getData()
            .then(res => {
                subscriberUpdate = []
                subscriberUpdate.push(user_id)
                for (i=0; i<res.length; i++){
                    subscriberUpdate.push(res[i])
                }
                
                axios({
                    method: 'patch',
                    url: "subscribers/" + (snipId),
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    data: {
                        "subscriber": subscriberUpdate
                    },
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                }).then(response => console.log(response))
            })
    })
}

const button1 = document.querySelectorAll('.userSubscribe');
for (let i = 0; i < button1.length; i++) {
    button1[i].addEventListener("click", function (event) {
        async function getData() {
            try {
                let res = await axios({
                    method: 'get',
                    url: "usersubscriptions/" + (user_id),
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                })
                
                if (res.status == 200) {
                    // console.log(res.status)
                console.log(res.data.AvailableFeeds)
                return res.data.AvailableFeeds
                } 
            }
            catch (err) {
                console.error(err);
                
            }
            finally {

                    axios({
                        method: 'post',
                        url: "usersubscriptions/" + (user_id),
                        xstfCookieName: 'csrftoken',
                        xsrfHeaderName: 'X-CSRFToken',
                        data: {
                            user_id: user_id,
                            subscriber: user_id,
                            AvailableFeeds: "federal register"
                        },
                        headers: {
                            'X-CSRFToken': 'csrftoken',
                        }
                    }).then(response => {
                        return response
                    })
            }
            
        }

        getData()
            .then(res => {
                subscriberUpdate = []
                subscriberUpdate.push('federal register')
                for (i=0; i<res.length; i++){
                    subscriberUpdate.push(res[i])
                }
                console.log(subscriberUpdate)
                try {
                    axios({
                    method: 'patch',
                    url: "usersubscriptions/" + (user_id),
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    data: {
                        user_id: user_id,
                        AvailableFeeds: subscriberUpdate
                    },
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                }).then(response => console.log(response))
                }
                catch (err) {
                    console.log('test')
                }
                
            })
    })
}

















