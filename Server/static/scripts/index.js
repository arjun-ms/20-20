let form = document.querySelector('#form')
let fileupload = document.querySelector('#fileUpload')
let res = document.querySelector('#result')

const uploadFile = (file) => {
  const formData = new FormData()
  console.log(file)
  formData.append('myFile', file)
  res.textContent = 'Uploading and Processing...'

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      let text = "My best guess is :  "+ data.toUpperCase()
      res.textContent = text
    })
    .catch(error => {
      console.error(error)
    })
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  uploadFile(fileupload.files[0])
})


function dropHandler(ev) {
  console.log('File dropped');
  ev.preventDefault();
  if (ev.dataTransfer.items.length > 1) {
    alert("Please upload only one file at a time");
    return
  }
  if (ev.dataTransfer.items && ev.dataTransfer.items.length == 1) {
    if (ev.dataTransfer.items[0].kind === 'file') {
      uploadFile(ev.dataTransfer.items[0].getAsFile())
    }
  }
  else {
    console.log('Insert a Valid File')
  }
}

function dragOverHandler(ev) {
  console.log('File(s) in drop zone');
  ev.preventDefault();
}

$('#fileUpload').change(function() {
  var i = $(this).prev('label').clone();
  var file = $('#fileUpload')[0].files[0].name;
  $(this).prev('label').text(file);
});