const button = document.getElementById("header-button");
const email = document.querySelector(".support-email");
const footer = document.querySelector(".footer");
const inputName = document.getElementById("inputName");
const outputName = document.getElementById("outputName");
const radioGender = document.querySelectorAll('input[type="radio"]');
const outputGender = document.getElementById("outputGender");
const inputNameError = document.querySelector(".inputNameError")
const inputBarError = document.querySelector(".input.error");
const inputGrayError = document.querySelector(".myform-name-gray");
const inputDate = document.getElementById("inputDate");
const outputDate = document.getElementById("outputDate");
const outputImage = document.getElementById("outputImage");
const inputFile = document.getElementById("inputFile");
const myformAvatar = document.querySelector(".myform-avatar");
const outputImageBlock = document.querySelector(".outputImageBlock");
const previewPhoto = document.querySelector(".preview-photo");
const outputImagePreview = document.getElementById("outputImagePreview");
const buttonContinue = document.querySelector(".bttn.continue");
const continueUrl = document.querySelector(".continue-url");
const form = document.getElementById('myform');
function updateResized() {
  if (window.innerWidth <= 768) {
    button.textContent = "Выйти";
    button.style.width = "64px";
    button.style.height = "36px";
    email.style.fontSize = "22px";
    footer.style.paddingLeft = "20px";
  }
  else{
    button.textContent = "Выйти из аккаунта";
    button.style.width = "173px";
    button.style.height = "40px";
    email.style.fontSize = "40px";
    footer.style.paddingLeft = "200px";
  }
}
updateResized();
window.addEventListener("resize", updateResized);

inputName.addEventListener('input', function(){
  const inputValue = inputName.value;
  const regex = /^[a-zA-Zа-яА-Я\s]+$/;
  if (!regex.test(inputValue)) {
    inputNameError.textContent = 'Неверный формат имени';
    inputBarError.style.border = '2px solid red';
    inputGrayError.style.color = 'red';
    inputGrayError.style.paddingBottom = '8px';
  }
  else{
    inputBarError.style.border = 'none';
    inputGrayError.style.color = 'rgb(93, 91, 102)';
    inputNameError.textContent = '';
  }
  outputName.textContent = inputName.value;

});

radioGender.forEach(function(radioOption){
  radioOption.addEventListener('change', function(){
    const label = document.querySelector(`label[for="${this.id}"]`);
    const labelText = label.textContent;
    outputGender.textContent = labelText;
  });
});

inputDate.addEventListener('input', function(){
  const birthDate = new Date(inputDate.value);
  const currentDate = new Date();
  const ageInMilliseconds = currentDate - birthDate;
  const ageInYears = Math.floor(ageInMilliseconds / (365 * 24 * 60 * 60 * 1000));
  outputDate.textContent = `${ageInYears} лет`;
});


inputFile.addEventListener('change', function(){
  console.log('ok');
  const file = inputFile.files[0];
  const reader = new FileReader();
  reader.onload = function(event) {
    const imageUrl = event.target.result;
    outputImage.src = imageUrl;
    outputImagePreview.src = imageUrl;
  };
  reader.readAsDataURL(file);
  myformAvatar.style.display = "none";
  outputImageBlock.style.display = "block";
  previewPhoto.style.border = "none";
  buttonContinue.style.opacity = "1";
  continueUrl.href = "/src2-obrazovaniye/index.html";
});

