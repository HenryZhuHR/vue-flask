<template>
  <div class="app-container">
    <!--  -->
    <div class="button-list">
      <button @click="selectLocalImage">部分整体关系</button>
    </div>

    <!--  -->
    <div class="display-container">
      <div class="img-container">
          <img id="part_seg" :src="img_base64" alt="None" /> 
      </div>
      <div class="img-container">
          <img id="part_seg" :src="img_base64" alt="None" /> 
      </div>
      <div class="img-container">
          <img id="part_seg" :src="img_base64" alt="None" /> 
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      url_partSeg: "http://127.0.0.1:5000/api/part_seg",
      img_base64: require("@/assets/images/default.jpg"),
    };
  },
  methods: {
    selectLocalImage() {
      var that = this;
      // virtual input
      var tempfileinput = document.createElement("input");
      tempfileinput.type = "file";
      tempfileinput.accept = "image/*";
      tempfileinput.click();

      // read input
      tempfileinput.onchange = function () {
        var file = tempfileinput.files[0];
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function (e) {
          var dataURL = e.target.result;

          // send request to server
          axios({
            method: "post",
            url: that.url_partSeg,
            data: {
              image: dataURL,
            },
          })
            .then(function (response) {
              console.log(response);
              that.img_base64 = response.data.image;
              // console.log(that.img_base64);
            })
            .catch(function (error) {
              console.log(error);
            });
        };
      };
    },
  },
};
</script>

<style>
.app-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.button-list {
  width: 20%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.display-container {
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>


<style>
/* Button style */
button {
  width: 60%;
  height: 3rem;
  font-size: 1rem;
}
</style>

<style>
/* Image */
/* img {
  width: 300px;
  height: 300px;
  object-fit: cover;
} */
.display-container{
  width: 80vw;
}
/* .img-container{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
} */
.img-container img{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>