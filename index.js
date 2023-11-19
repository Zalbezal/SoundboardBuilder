function play_sound(clicked_id) {
    var audio = new Audio(clicked_id + ".wav"); 
    audio.play();
  }