let col_btn = document.querySelectorAll(".btn-col");
let col_item = document.querySelectorAll(".collection-item");
let noProductsMsg = document.getElementById("no-products-js");

col_btn.forEach((btn,index)=>{
    btn.addEventListener("click",(e)=>{
        col_btn.forEach((col_bt,ind)=>{
            col_bt.classList.remove("btn");
        })
        e.target.classList.add("btn");
        let data_btn = btn.getAttribute("data-btn");
        let hasVisible = false;
        col_item.forEach((col,inde)=>{
            if(col.getAttribute("data-item")==data_btn || data_btn == "all"){
                col.classList.remove("hide")
                hasVisible = true;
            }else{
                col.classList.add("hide");
            }
        });
        noProductsMsg.style.display = hasVisible ? "none" : "block";
    });
});


// nav bar

let ul = document.querySelector("ul");
let burger_icon = document.querySelector(".burger_icon");

burger_icon.addEventListener("click",()=>{
    if(burger_icon.classList.contains("fa-bars")){
        burger_icon.classList.add("fa-xmark");
        burger_icon.classList.remove("fa-bars");
        ul.classList.add("active");
    }
    else{
        burger_icon.classList.remove("fa-xmark");
        burger_icon.classList.add("fa-bars");
        ul.classList.remove("active");
    }
})