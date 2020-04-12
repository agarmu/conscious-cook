function foodParser() {
  let resp = "not a recipe";
  if ((location.hostname == "www.allrecipes.com" || location.hostname == "allrecipes.com") && !location.search.includes("recipeType")) {
    location.replace(location.href + "/print/?recipeType=Recipe");
    console.log(location.href + "/print/?recipeType=Recipe");
  }
  let foods = [];
  let foodids = [];
  const bod = document.querySelectorAll( 'body *' );
  
  for (var i = 0; i < bod.length; i++) {
    stringed = "" + bod[i].innerHTML;
    if (stringed.toLowerCase().indexOf("ingredients") != -1) {
      try { 
        if (bod[i].nextElementSibling.nodeName == "UL") {
          bod[i].nextElementSibling.setAttribute("id", "consciouscook1");
          bod[i].nextElementSibling.nextElementSibling.setAttribute("id", "consciouscook2");
        }
      }
      catch(err) {
        console.log(err)
      }
    }
  }
  try {
    let cc1 = document.getElementById("consciouscook1").getElementsByTagName("li");
    for (var x = 0; x < cc1.length; x++) {
      foods.push(cc1[x].innerHTML.trim());
      foodids.push("c1c" + x);
      cc1[x].setAttribute("id", "c1c" + x);
    }
    
    let cc2 = document.getElementById("consciouscook2").getElementsByTagName("li");
    for (var x = 0; x < cc2.length; x++) {
      foods.push(cc2[x].innerHTML.trim());
      foodids.push("c2c" + x);
      cc2[x].setAttribute("id", "c2c" + x);
    }
    
    setTimeout(function() {
      document.getElementsByClassName("recipe-print__title")[0].scrollIntoView(true)
    }, 500);

    let data = {};
    for (var x = 0; x < foods.length; x++) {
      data[foods[x]] = foodids[x];
    }
    console.log(data);

    let test = {"1 lb beef": "c1c0", "1 ounce of celery": "c1c2"}; // test is a fake version of data to send in development

    (async () => {
      const rawResponse = await fetch('https://antigluon.pythonanywhere.com/api/recipe_info', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // write data here instead of test once backend is working
      });
      const content = await rawResponse.json();
    
      jamesthing(content);
    })();

  }
  catch(err) {
    console.log(err)
  }
}


window.onload = foodParser;

function jamesthing(data) {
  console.log(data);
  let total_carbon = 0;
  let ingredient_total = 0;
  let total_calories = 0;
  let total_cost = 0;
  for( x in Object.keys(data)) {
    let food = Object.keys(data)[x];
    let carbon = data[Object.keys(data)[x]]["per_unit"]["carbon"] * data[Object.keys(data)[x]]["n_units"];
    total_carbon += carbon;
    let id = data[Object.keys(data)[x]]["element_id"];
    let calories = data[Object.keys(data)[x]]["per_unit"]["calories"] * data[Object.keys(data)[x]]["n_units"];
    total_calories += calories;
    let cost = data[Object.keys(data)[x]]["per_unit"]["cost"] * data[Object.keys(data)[x]]["n_units"];
    total_cost += cost;
    let subs = data[Object.keys(data)[x]]["substitutions"];
    let rating = data[Object.keys(data)[x]]["carbon_rating"];
    ingredient_total++;
    displayData(id, food, rating, calories, cost, subs, carbon);
  }
  let average_carbon = total_carbon / total_calories;
  alert(average_carbon)
  title = document.getElementsByClassName("recipe-print__title")[0].innerHTML;
  let color = "black";
  if (average_carbon > 0.0 && average_carbon <= 0.17) {
    color = "green";
    document.getElementsByClassName("recipe-print__title")[0].innerHTML = title + " - Earth-Friendly Choice!";
  } else if (average_carbon > 0.17 && average_carbon <= 0.5) {
    color = "#fcca03";
    document.getElementsByClassName("recipe-print__title")[0].innerHTML = title + " - Fairly Small Carbon Footprint";
  } else if (average_carbon > 0.5 && average_carbon <= 1.7) {
    color = "orange";
    document.getElementsByClassName("recipe-print__title")[0].innerHTML = title + " - Maybe find something greener?";
  } else if (average_carbon > 1.7) {
    color = "red";
    document.getElementsByClassName("recipe-print__title")[0].innerHTML = title + " - Consider the planet!";
  }
  document.getElementsByClassName("recipe-print__title")[0].style.color = color;

  // make the actual recipe title (the 'recipe-print__title' class) a hover over effect as well, listing its 
  // total_cost, total_calories, average_carbon
}

function displayData(id, food, carbon, calories, cost, substitutions, totalco2){
  let selected = document.getElementById(id);
  let color = "black";
  if (carbon > 0.0 && carbon <= 0.17) {
    color = "green";
  } else if (carbon > 0.17 && carbon <= 0.5) {
    color = "#fcca03";
  } else if (carbon > 0.5 && carbon <= 1.7) {
    color = "orange";
  } else if (carbon > 1.7) {
    color = "red";
  }
  selected.style.color = color;

  // need to somehow make a hoverover effect for the provided id so onmouseover it will show a little box with the name
  // of the food, carbon percentage, calories, cost, and provide a possible substitution
}