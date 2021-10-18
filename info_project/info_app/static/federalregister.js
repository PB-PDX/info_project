const user_id = JSON.parse(document.getElementById('user_id').textContent);
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// This for loop listens to all the buttons on the page for a click 
// with the class of snipButton and then a variable is set to the buttons 
// 'name', which is the snippets pk. The user will then be stored on
// the respective snippet. This also allows for the toggle of Add Snippet and 
// Added. 

const snipButton = document.querySelectorAll('.snipButton');
for (let i = 0; i < snipButton.length; i++) {
    snipButton[i].addEventListener("click", function (event) {
        let classes = event.target.classList
        let result = classes.toggle("btn-success");
        let snipId = event.target.name
        if (result) {
            snipButton.textContent = `'btn-success' added; classList is now "${classes}".`;
            event.target.innerText = 'Added'

            // async function is going to wait to get data from a get request. The get request is 
            // needed on the front end to append the existing data to the new data, or
            // else the existing data will be overwritten.  
            async function getData() {
                try {
                    let res = await axios({
                        method: 'get',
                        url: "snipsubs/" + (snipId),
                        xstfCookieName: 'csrftoken',
                        xsrfHeaderName: 'X-CSRFToken',
                        headers: {
                            'X-CSRFToken': 'csrftoken',
                        }
                    })
                    if (res.status == 200) {
                        console.log(res.status)
                    }
                    return res.data.subscriber
                }
                catch (err) {
                    console.error(err);
                }
            }
            // calling the async get request and then merging all the data into one array
            // that can be pushed. 
            getData()
                .then(res => {
                    subscriberUpdate = []
                    subscriberUpdate.push(user_id)
                    for (i = 0; i < res.length; i++) {
                        subscriberUpdate.push(res[i])
                    }
                    // This axios patch request allows for the manipulation of one field only.    
                    axios({
                        method: 'patch',
                        url: "snipsubs/" + (snipId),
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
        }

        else {
            snipButton.textContent = `'btn-success' removed; classList is now "${classes}".`;
            event.target.innerText = 'Add Snippet'
            axios({
                method: 'get',
                url: "snipsubs/" + (snipId),
                xstfCookieName: 'csrftoken',
                xsrfHeaderName: 'X-CSRFToken',
                headers: {
                    'X-CSRFToken': 'csrftoken',
                }
            }).then(response => {
                let checkId = user_id
                let subs = response.data.subscriber
               if (subs.includes(checkId)==true){
                const index = subs.indexOf(user_id)
                if (index > -1) {
                    subs.splice(index, 1);
                
                  }
                  console.log('test')
               }
               
               
                
            })

        }

    })

}

// This will listen for the userSubscribe button. It will send a post request and if a 404 is returned then an update will be attempted.
const button1 = document.querySelectorAll('.userSubscribe');
for (let i = 0; i < button1.length; i++) {
    button1[i].addEventListener("click", function (event) {
        let currentFeed = event.target.name
        
        axios({
            method: 'POST',
            url: "create/subscriptions",
            xstfCookieName: 'csrftoken',
            xsrfHeaderName: 'X-CSRFToken',
            data: {
                "user_id": user_id,
                "subscriber": user_id,
                "AvailableFeeds": currentFeed
            },
            headers: {
                'X-CSRFToken': 'csrftoken',
            }
        }).then(response => {
            if (response.data == "user exists") {
                axios({
                    method: 'get',
                    url: "feedsubs/" + (user_id),
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                }).then(response => {
                    let subsUpdate = []
                    let subs = response.data.AvailableFeeds
                    let currentSub = currentFeed
                    subsUpdate.push(currentSub)
                    for (i = 0; i < subs.length; i++) {
                        subsUpdate.push(subs[i])
                    }
                   
                    axios({
                        method: 'patch',
                        url: "feedsubs/" + (user_id),
                        xstfCookieName: 'csrftoken',
                        xsrfHeaderName: 'X-CSRFToken',
                        data: {

                            "AvailableFeeds": subsUpdate
                        },
                        headers: {
                            'X-CSRFToken': 'csrftoken',
                        }
                    }).then(response => console.log(response))
                })
            }
        })

    })
}













