//GLOBAL VAR DECLARATIONS
championData = {};
championDataLoaded = false;
champDict = {}//This is for efficency I guess

function toggleDropDown(id) {
    currentContainer = document.getElementById("container" + id)
    currentDetailBox = document.getElementById("detailsBlock" + id)
    currentDropDownImage = document.getElementById("dropDownImg" + id)
    if(parseInt(currentContainer.style.marginBottom) > 50){
        //pull
        currentContainer.style.marginBottom = 15;
        currentDetailBox.style.display = "None"
        currentDropDownImage.classList.toggle("flippedImg")
    }
    else {
        //drop
        currentContainer.style.marginBottom = currentContainer.clientHeight * 1.5 + 15;
        currentDetailBox.style.display = "Block"
        currentDropDownImage.classList.toggle("flippedImg")
    }
}
toggleDropDown(1);//comment out later

function selectDetailsTab(selected, id) {
    //deselect all
    for(var i = 1; i <= 3; i ++) {//<= number of tabs
        document.getElementById("detailsBlockTab-" + i + "-" + id).classList.remove("detailsBlockTabSelected")
    }
    document.getElementById("detailsBlockTab-" + selected + "-" + id).classList.add("detailsBlockTabSelected")

}

function changeProgressionMap(value) {
    var dotsArr = document.querySelectorAll('[id^="t-"]');
    for(var dot in dotsArr) {
        var temp = dotsArr[dot]
        if(temp.id == undefined) {
            continue;
        }
        if((temp.id.substr(2) / 1693719) * 100 > value) {
            temp.style.display = "None"
        }
        else {
            temp.style.display = "inline-block"
        }
    }
}

// function loadJSON(callback, filename) {   

//     var xobj = new XMLHttpRequest();
//     xobj.overrideMimeType("application/json");
//     xobj.open('GET', '/static/data_files/' + filename + '.json', true); // Replace 'my_data' with the path to your file
//     xobj.onreadystatechange = function () {
//         if (xobj.readyState == 4 && xobj.status == "200") {
//             // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
//             callback(xobj.responseText);
//         }
//     };
//     xobj.send(null);  
// }

// function getChampionName(championId) {
//     if(!championDataLoaded) {
//         return Error("champDataNotLoaded");
//     }

//     //first check shortlist to see if champ has been indexed
//     var returns = champDict[championId]
//     if(returns != undefined) {
//         return returns;
//     }
//     //if not, check full list
//     for(key in championData) {
//         if(championData[key]["id"] == championId) {
//             //add to shortlist
//             champDict[championId] = championData[key]["name"];
//             return championData[key]["name"];
//         }
//     }
// }

// loadJSON((res) => {
//     championData = JSON.parse(res).data
//     championDataLoaded = true;
// }, "champion_data")