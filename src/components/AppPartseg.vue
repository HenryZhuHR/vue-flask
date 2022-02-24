<template>
  <div class="app-container">
    <div class="button-list">
      <button @click="selectLocalImage">部分整体演示</button>
    </div>
    <div class="display-container">
      <div class="img-container">
        <img :src="img_url" alt="None" />
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
      img_url: "",
    };
  },
  methods: {
    selectLocalImage() {
      var this_vue = this;
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
          axios
            .post(this_vue.url_partSeg, {
              image: dataURL,
            })
            .then(function (response) {
              console.log(response);
              this_vue.img_url = response.data.image;
              // console.log(this_vue.img_url);
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
  width: 100%;
  height: 2rem;
  color: blue; /* font */
}
</style>