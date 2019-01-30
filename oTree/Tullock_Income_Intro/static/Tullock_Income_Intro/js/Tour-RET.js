
//this initiates the tooltip mouseover to explain the counters
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
//

$(function () {
  $('[data-toggle="popover"]').popover()
})



(function(){

    var tour = new Tour({
        storage : false,
        debug: false
    });

    tour.addSteps([
     {
        element: "#time-out_mock-up",
        placement: "left",
        backdrop: true,
        title: "The Timeout",
        content: "This timer indicates the time left in this round to either solve sequences or stay in the \"switch mode\"." +
        " In this example the timer is static so as to not force a timeout. However, during the task it will" +
        " begin counting down from the moment the screen is displayed."
      },
     {
            element: "#step_1",
            placement: "left",
            backdrop: true,
            title: "The Timer",
            content: "This timer indicates how long you have spent counting the \"a\"s of the current sequence. " +
            "Once you submit a correct answer, the timer will restart."
     },
     {
        element: "#number_strings",
        placement: "left",
        backdrop: true,
        title: "Number of Sequences Solved",
        content: "This counter indicates how many sequences you have solved in the present round."
      },
     {
        element: "#time_last",
        placement: "bottom",
        backdrop: true,
        title: "Seconds needed to solve the previous sequence",
        content: "This timer indicates how many seconds you needed to solve the <strong> previous </strong> sequence."
        },
      {
        element: "#switch_modal",
        placement: "right",
        title: "Switch Button",
        content: "<p> By clicking this button you enter the \"switch mode\". You will need to confirm first. Once " +
        "you go in the \"switch mode\" you cannot go back to the letter counting task! </p>" +
        "<hr>" +
        "<p> <strong> Now try entering a correct answer in the input field and see how the counters change!</strong></p>"
      }
    ]);

    $("#start-tour").click(function() {
    tour.start();
    });


}());