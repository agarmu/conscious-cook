chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
     document.getElementById('settings_text').innerHTML =  `<h3 id="settings_text">Current Recipe: ${tabs[0].title}</h3>`
});
  /*
  let tooltip = document.querySelector('#tooltip');
  let paragraphs = document.getElementsByTagName('p');
  let selected = document.querySelector('#ClassName');
  
  
  
  function show() {
      tooltip.setAttribute('data-show', '');
    }
    
    function hide() {
      tooltip.removeAttribute('data-show');
    }
    
    const showEvents = ['mouseenter', 'focus'];
    const hideEvents = ['mouseleave', 'blur'];
    
    showEvents.forEach(event => {
      selected.addEventListener(event, show);
    });
    
    hideEvents.forEach(event => {
      selected.addEventListener(event, hide);
    });


    <button id="button" aria-describedby="tooltip">My button</button>
    <div id="tooltip" role="tooltip">My tooltip</div>*/
