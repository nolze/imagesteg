<!DOCTYPE html>
<html>
<head lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>imgsteg</title>
<link rel="stylesheet" href="/static/bootstrap.min.css">
<style>
html, body {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
.container-fluid, .row {
  height: 100%;
}
#action {
  width: 100%;
}
#main {
  height:100%;
  padding: 10px;
}
#image-container {
  border: 1px solid #b0b0b0;
  max-width: 100%;
  height: 100%;
}
#image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
</style>
</head>
<body id="body">
<div class="container-fluid">
  <div class="row">
    <div class="col-3" style="padding: 10px;">
      <form>
      <select id="action" name="action" size="10">
      <option value="original">Original image</option>
      <option value="inversion">Color inversion</option>
<!-- 
      <option value="alpha-7">Alpha plane 7</option>
      <option value="alpha-6">Alpha plane 6</option>
      <option value="alpha-5">Alpha plane 5</option>
      <option value="alpha-4">Alpha plane 4</option>
      <option value="alpha-3">Alpha plane 3</option>
      <option value="alpha-2">Alpha plane 2</option>
      <option value="alpha-1">Alpha plane 1</option>
      <option value="alpha-0">Alpha plane 0</option>
 -->
      <option value="red-7">Red plane 7</option>
      <option value="red-6">Red plane 6</option>
      <option value="red-5">Red plane 5</option>
      <option value="red-4">Red plane 4</option>
      <option value="red-3">Red plane 3</option>
      <option value="red-2">Red plane 2</option>
      <option value="red-1">Red plane 1</option>
      <option value="red-0">Red plane 0</option>
      <option value="green-7">Green plane 7</option>
      <option value="green-6">Green plane 6</option>
      <option value="green-5">Green plane 5</option>
      <option value="green-4">Green plane 4</option>
      <option value="green-3">Green plane 3</option>
      <option value="green-2">Green plane 2</option>
      <option value="green-1">Green plane 1</option>
      <option value="green-0">Green plane 0</option>
      <option value="blue-7">Blue plane 7</option>
      <option value="blue-6">Blue plane 6</option>
      <option value="blue-5">Blue plane 5</option>
      <option value="blue-4">Blue plane 4</option>
      <option value="blue-3">Blue plane 3</option>
      <option value="blue-2">Blue plane 2</option>
      <option value="blue-1">Blue plane 1</option>
      <option value="blue-0">Blue plane 0</option>
<!--       <option value="alpha-full">Full alpha</option> -->
      <option value="red-full">Full red</option>
      <option value="green-full">Full green</option>
      <option value="blue-full">Full blue</option>
      <option value="random-1">Random color map 1</option>
      <option value="random-2">Random color map 2</option>
      <option value="random-3">Random color map 3</option>
      <option value="graybits">Gray bits</option>
      </select>
      </form>
    </div>
    <div id="main" class="col">
      <div id="image-container"><img id="image"></div>
    </div>
  </div>
</div>
<script>
function setImage(imgBlob) {
  document.getElementById("image").src = imgBlob
}

function getOriginalImage() {
  fetch("/api/original", {
    method: "POST",
  })
  .then(response => {
    return response.blob()
  })
  .then(blob => {
    let objectURL = URL.createObjectURL(blob)
    console.log(blob, objectURL)
    setImage(objectURL)
  })
}

document.addEventListener("DOMContentLoaded", getOriginalImage)

let options = document.getElementById("action").options
document.getElementById("action").addEventListener('change', function(ev) {
  let idx = this.selectedIndex
  let name = options[idx].value
  fetch("/api/" + name, {
    method: "POST",
  })
  .then(response => {
    return response.blob()
  })
  .then(blob => {
    let objectURL = URL.createObjectURL(blob)
    // console.log(blob, objectURL)
    setImage(objectURL)
  })
})
</script>
</body>
</html>
