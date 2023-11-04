const button = document.getElementById("header-button");
const email = document.querySelector(".support-email");
const footer = document.querySelector(".footer");

const inputGrade = document.getElementById("inputGrade");
const inputFaculty = document.getElementById("inputFaculty");
const inputProgram = document.getElementById("inputProgram");
const inputErrors = document.querySelectorAll(".inputNameError");

const inputGradeGray = document.querySelector(".myform-grade p");
const inputFacultyGray = document.querySelector(".myform-faculty p");
const inputProgramGray = document.querySelector(".myform-program p");

const studyInfoSpans = document.querySelectorAll("#studyInfo span");
const radioElements = document.querySelectorAll('.select-radio');
const inputWork = document.querySelector('.input.work');
const outputWork = document.querySelector('.info-empty p');

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

  inputGrade.addEventListener('change', function(){
    if (inputGrade.value == ''){
        inputErrors[0].textContent = 'Обязательное поле';
        inputErrors[0].style.fontSize = '14px';
        inputGradeGray.style.color = 'red';
        inputGrade.style.border = '2px solid red';
    }
    else{
        inputErrors[0].textContent = '';
        inputGradeGray.style.color = '#5D5B66';
        inputGrade.style.border = 'none';
        studyInfoSpans[1].textContent = inputGrade.value;
    }
  });

  inputFaculty.addEventListener('change', function(){
    if (inputFaculty.value == ''){
        inputErrors[1].textContent = 'Обязательное поле';
        inputErrors[1].style.fontSize = '14px';
        inputFacultyGray.style.color = 'red';
        inputFaculty.style.border = '2px solid red';
    }
    else{
        inputErrors[1].textContent = '';
        inputFacultyGray.style.color = '#5D5B66';
        inputFaculty.style.border = 'none';
        studyInfoSpans[2].textContent = inputFaculty.value;
    }
  });

  inputProgram.addEventListener('change', function(){
    if (inputProgram.value == ''){
        inputErrors[2].textContent = 'Обязательное поле';
        inputErrors[2].style.fontSize = '14px';
        inputProgramGray.style.color = 'red';
        inputProgram.style.border = '2px solid red';
    }
    else{
        inputErrors[2].textContent = '';
        inputProgramGray.style.color = '#5D5B66';
        inputProgram.style.border = 'none';
        studyInfoSpans[3].textContent = inputProgram.value;
    }
  });

  radioElements.forEach(function(radio) {
    radio.addEventListener('change', function() {
      if (radio.checked) {
        studyInfoSpans[0].textContent = radio.value;
      }
    });
  });

  inputWork.addEventListener("change", function(){
    outputWork.textContent = inputWork.value;
  });