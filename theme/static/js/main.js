// add domain to zoho from cloudfare js 

// select domain 
var select_domain_list = []
function select_domain(event) {
    current_div = event.target;
    if (current_div.classList.contains('selected_domain')) {
        domain_name = current_div.innerText;
        select_domain_list.splice(select_domain_list.indexOf(domain_name), 1)
        current_div.classList.remove('selected_domain');
        current_div.classList.remove('text-white');
        current_div.classList.remove('bg-[#2B2358]');
    } else {
        domain_name = current_div.innerText;
        console.log(domain_name)
        select_domain_list.push(domain_name)
        current_div.classList.add('selected_domain');
        current_div.classList.add('text-white');
        current_div.classList.add('bg-[#2B2358]');
    }

    console.log(select_domain_list)
    document.getElementById('hidden_form').value = select_domain_list

}

// stop form form resubmitting 

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

// gery out button 

const targetElement = document.getElementById('domain_container');
console.log(targetElement)
const button = document.getElementById('run_automation');
console.log(button)

if (targetElement) {
    console.log('yes it exist')
    button.classList.add('disabled_button');
    button.innerHTML = 'Please Wait Until All Ongoing Taks Finishes';
    button.setAttribute('disabled', 'disabled');
}


// nav bar js 


function toggle_nav() {
    drop_down = document.getElementById('dropdownDivider');
    console.log(drop_down)

    if (drop_down.classList.contains('hidden')) {
        drop_down.classList.remove('hidden');
    }

    else {
        console.log('none')
        drop_down.classList.add('hidden');

    }
}


// validate input 

// function ValidateActInsert() {
//     var specialChars = /[^a-zA-Z0-9 ]/g;

//     username = document.getElementById('username')

//     console.log(username)

//     if (username.value.match(specialChars)) {
//         alert ("Only characters A-Z, a-z and 0-9 are allowed!")
//         username.focus();
//         return false;
//     }
//     return (true);
// }