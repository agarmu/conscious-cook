
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    document.getElementById('settings_text').innerHTML = `<h2 id="settings_text">Curret recipe: ${tabs[0].title}</h2>`
});

