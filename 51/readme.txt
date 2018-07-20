https://console.firebase.google.com/u/0/project/fiftyone-a1bf4/overview

curl -X PUT -d '{ "alanisawesome": { "name": "Alan Turing", "birthday": "June 23, 1912" } }' 'https://docs-examples.firebaseio.com/rest/quickstart/users.json'


Min databas:
https://fiftyone-a1bf4.firebaseio.com/


Läsa
curl 'https://samplechat.firebaseio-demo.com/users/jack/name.json'

Skriva över all data
curl -X PUT -d '{ "first": "Jack", "last": "Sparrow" }' 'https://samplechat.firebaseio-demo.com/users/jack/name.json'

Lägga till entry:
curl -X POST -d '{"user_id" : "jack", "text" : "Ahoy!"}' 'https://samplechat.firebaseio-demo.com/message_list.json'


Jag vill göra:
curl -X POST -d '{"date": "2018-07-07 07:54:12", "note": "text"}' 'https://fiftyone-a1bf4.firebaseio.com/notes.json'


{ "notes": [{"date": "2018-07-07 07:54:12", "note": "text"}]}
