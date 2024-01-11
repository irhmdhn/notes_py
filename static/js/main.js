ClassicEditor.create(document.querySelector("#input-content"), {
    removePlugins: ["Heading", "Link", "CKFinder"],
    toolbar: [
      "bold",
      "italic",
      "bulletedList",
      "numberedList",
    ],
  }).catch((error) => {
    console.log(error);
  });



  document.querySelector("#btn-list").addEventListener('click',function(){
    const list = document.querySelector("aside")
    if (this.classList.contains('ph-list')){
      this.classList.replace('ph-list','ph-x')
      list.classList.replace('translate-x-96','translate-x-0')
    } else{
      this.classList.replace('ph-x','ph-list')
      list.classList.replace('translate-x-0','translate-x-96')
    }
  })