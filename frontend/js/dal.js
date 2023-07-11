const URL = 'http://127.0.0.1:8080/api/v1/women/'
const send = (url = URL) => axios.post(`${url}?test=3`, {info: 'НЕТТТТТ, Я ХОТЕЛ ШПЁХНУТЬ ЛЕРКУ АААА.'})
                            .then(response => console.log(response))