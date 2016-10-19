
function getSentence(id){
  return sentences[id].sentence;
}

function getWord(word_id, sentence_id){
  var sentence = getSentence(sentence_id);
  var word = sentence.split(" ")[word_id];
  return word;
}

//splitting a sentence for sub classification (for compound sentences)

function splitSentence(split_id){
  //1 split the sentence display
  var sentence_id = parseInt(split_id.split(".")[0]),
      word_id = parseInt(split_id.split(".")[1]);

  var sentence = getSentence(sentence_id-1).split(" ");
  console.log(sentence)
  //
  var sentence_part1 = sentence.slice(0,word_id).join(" "),
      sentence_part2 = sentence.slice(word_id+1,sentence.length).join(" ");

  var part1_html = "<div><h3>Subsentence Part 1</h3>" + sentence_part1 + "</div>";
  var part2_html = "<div><h3>Subsentence Part 2</h3>" + sentence_part2 + "</div>";

  $('#selected-sentence').append(part1_html);
  $('#selected-sentence').append(part2_html);

}


//adding a row to a table
function addTableRowRadio(selector,heading,radio_options){

  var row_html = "<td>" + heading + "</td>";
  $(selector).append(row_html);

  for (var i=0; i < radio_options.length; i++){
    row_html = "<td><input type='radio' id='" + radio_options[i].concat(classify_number.toString()) + "'></td>";
    $(selector).append(row_html);
  }

}

//add paradigm to form
function addClassification(selector){
  console.log("add classification");
  console.log(selector);
  classify_number += 1;
  var subselector = 'classification'.concat(classify_number.toString());
  console.log(subselector)
  var row_html = "<tr id='" + subselector + "'></tr>";
  console.log(row_html);
  $(selector).append(row_html);

  addTableRowRadio("#".concat(subselector),"Classification #".concat(classify_number.toString()), paradigms);
}


//refer to https://jsfiddle.net/lainglo/0bmqLgt2/1/
function SelectText(element) {
    var doc = document
        , text = doc.getElementById(element)
        , range, selection
    ;
    if (doc.body.createTextRange) {
        range = document.body.createTextRange();
        range.moveToElementText(text);
        range.select();
    } else if (window.getSelection) {
        selection = window.getSelection();
        range = document.createRange();
        range.selectNodeContents(text);
        selection.removeAllRanges();
        selection.addRange(range);
    }
}

function parse_paradigm(){
  var paradigmElements = _.filter($( "form input:radio" ),function(data){if (data.checked) { return data.value }});
  var paradigms = [];
  for (i=0; i < paradigmElements.length; i++){
    paradigms.push(paradigmElements[i].value);
  }
  return paradigms;
}

//knowledge_generation subclassification
function knowledge_gen(){
  //taken from http://stackoverflow.com/a/29064649/5411181
  var metatheory_elements = ['Ontology','Epistemology','Research object','Method','Theory of truth','Validity','Reliability','Training'];
  var list = '<h2>Knowledge Generation</h2> Which metatheoretical assumption applies? <ul><li>' + metatheory_elements.join('</li><li>') + '</li></ul>';
  $("#level2").html(list);
};

//agency subclassification
function agency(){
  //taken from http://stackoverflow.com/a/29064649/5411181
  var metatheory_elements = ['Organising question','Unit of Analysis','Prime empirical focus','Locus of agency','Level of Analysis','Ontology','Recommendations based on specific theoretical assumptions', 'Voice','Ethics','Hegemony','Axiology','Nature of research products','Control'];
  var list = '<h2>Agency</h2> Which metatheoretical assumption applies? <ul><li>' + metatheory_elements.join('</li><li>') + '</li></ul>';
  $("#level2").html(list);
};

//paradigm select
function paradigm_classify() {
  var paradigms = parse_paradigm();

  //classify between agency and knowledge generation
    var classifcation_tag = "Does this sentence fall under <u><a onclick='knowledge_gen()'>knowledge generation</a></u> or <u><a onclick='agency()'> agency</a></u> ?";
    $("#level1").html(classifcation_tag);
};
