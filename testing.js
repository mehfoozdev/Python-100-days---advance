// function getDiscount(price:number):any{
//     let discount = "";
//     if (price>= 10000){
//         discount = '20%'
//     }
//     else if (price >= 5000){
//         discount = '10%'
//     }
//     else if(price >= 2500){
//         discount = '10%'
//     }
//     return discount
// }
// let priceBeforeDiscount = 5000;
// let discountPercentage = getDiscount(priceBeforeDiscount)
// let discountedPrice = priceBeforeDiscount - (priceBeforeDiscount * discountPercentage/100);
// console.log(priceBeforeDiscount, discountPercentage, discountedPrice);
function getDiscount(price) {
    var discount = 0; // Initialize discount as a numerical value
    if (price >= 10000) {
        discount = 20;
    }
    else if (price >= 5000) {
        discount = 10;
    }
    else if (price >= 2500) {
        discount = 5;
    }
    return discount; // Return numerical discount percentage
}
var priceBeforeDiscount = 5000;
var discountPercentage = getDiscount(priceBeforeDiscount);
var discountedPrice = priceBeforeDiscount - (priceBeforeDiscount * discountPercentage / 100);
console.log(priceBeforeDiscount, discountPercentage + '%', discountedPrice);
