var price_amz;
var link_amz;
var iname_amz;
var price_snp;
var link_snp;
var iname_snp;
function fn()
{
    document.getElementById("img_amz").src = ("amazon.png");
    document.getElementById("img_amz").height = 16;
    document.getElementById("img_amz").width = 16;
    document.getElementById("price_amz").innerHTML = ("    Price of " + iname_amz + " is " + price_amz);
    document.getElementById("link_amz").innerHTML = "Check other variants";
    document.getElementById("link_amz").href = link_amz;
    document.getElementById("img_snp").src = ("snapdeal.png");
    document.getElementById("img_snp").height = 16;
    document.getElementById("img_snp").width = 16;
    document.getElementById("price_snpdl").innerHTML = (" Price of " + iname_snp + " is " + price_snp);
    document.getElementById("link_snpdl").innerHTML = "Check other variants";
    document.getElementById("link_snpdl").href = link_snp;

}
document.getElementById("btn").onclick = fn;

