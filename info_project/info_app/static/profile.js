axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
let ul = document.getElementById("submittedtasks");


popSnips()










function popSnips() {
    axios({
        method: 'get',
        url: "profilesniplist/",
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => {
        const subSnip = document.getElementById("submittedtasks")
        for (i = 0; i < response.data.length; i++) {
            const a = document.createElement("a");
            const h5 = document.createElement("h5");
            const div = document.createElement("div");
            h5.innerHTML =
                "<div></h5>" +
                response.data[i].title +
                "</h5></div>";
            a.href = response.data[i].link
            a.className = "list-group-item list-group-item-action"
            div.className = "d-flex w-100 justify-content-between"
            div.appendChild(h5)
            a.appendChild(div)
            subSnip.appendChild(a);
        }
    })
}