//this initiates the tooltip mouseover to explain the counters
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
//

$(function () {
    $('[data-toggle="popover"]').popover()
})


(function () {

    var tour = new Tour({
        storage: false,
        debug: false
    });

    tour.addSteps([
        {
            element: "#step_1",
            placement: "left",
            backdrop: true,
            title: "The Timer",
            content: "This timer will show you how long you have spent counting the \"a\"s of the current sequence. " +
            "Once you submit a correct answer, the timer will restart."
        },
        {
            element: "#string",
            placement: "left",
            backdrop: true,
            title: "The Sequence",
            content: "This is the sequence of characters of which you have to count the number of \"a\"s."
        },
        {
        element: "#time_last",
        placement: "bottom",
        backdrop: true,
        title: "Seconds needed to solve the previous sequence",
        content: "This timer indicates how many seconds you needed to solve the <strong> previous </strong> sequence."
        },
        {
            element: "#player_guess",
            placement: "left",
            title: "The Input Field",
            backdropPadding: true,
            content: "Type here the number of \"a\"s in the sequence above and hit enter to submit."
        }
    ]);

    // Initialize the tour
    tour.init();

    // Start the tour
    tour.start();

}());