function operation() {
    var ans=document.getElementById("answer");
    if (document.getElementById("add").checked) {
        ans.value= calculate('add');
    }
    if (document.getElementById("subtract").checked) {
        ans.value= calculate('subtract');
    }
    if (document.getElementById("multiply").checked) {
        ans.value= calculate('multiply');
    }
    if (document.getElementById("divide").checked) {
        ans.value= calculate('divide');
    }
    }
    function calculate(action){
            var num1 = parseInt(document.getElementById("num1").value);
            var num2 = parseInt(document.getElementById("num2").value);
            var result;
            switch(action){
                case 'add':
                    result= num1+num2;
                    break;
                case 'subtract':
                    result= num1-num2;
                     break;
                case 'multiply':
                    result= num1*num2;
                     break;
                case 'divide':
            if(num2!=0){
                 result= num1/num2;
                }
                else{
                alert("Divide by zero error");
                }
                    break;
            }
            return result;
        }		
    