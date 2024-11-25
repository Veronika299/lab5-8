let checkList = document.getElementById('list1');
let checkList2 = document.getElementById('list2');
let checkList3 = document.getElementById('list3');
let checkList4 = document.getElementById('list4');
checkList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (checkList.classList.contains('visible'))
        checkList.classList.remove('visible');
    else
        checkList.classList.add('visible');
}

checkList2.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (checkList2.classList.contains('visible'))
        checkList2.classList.remove('visible');
    else
        checkList2.classList.add('visible');
}

checkList3.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (checkList3.classList.contains('visible'))
        checkList3.classList.remove('visible');
    else
        checkList3.classList.add('visible');
}

checkList4.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (checkList4.classList.contains('visible'))
        checkList4.classList.remove('visible');
    else
        checkList4.classList.add('visible');
}
