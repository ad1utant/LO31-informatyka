const x = ['ala',2,'ola','julka',4];
let i = 0;
while(i<x.length){
    if(typeof(x[i]) == "number"){
        console.log(x[i])
    }
    i++;
}

i = 0

do{
    if(typeof(x[i]) == "number"){
        console.log(x[i])
    }
    i++;
}while(i<x.length)

i = 0

for(let i = 0; i<x.length;i++){
    if(typeof(x[i]) == "number"){
        console.log(x[i])
    }
}

i = 0

for(let element in x){
    if(typeof(x[element]) == "number"){
        console.log(x[element])
    }
}

i = 0

for(let element of x){
    if(typeof(element) == "number"){
        console.log(element)
    }
}

