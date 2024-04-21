document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            // Define your calendar events here
            {
                title: 'Event 1',
                start: '2024-04-20'
            },
            {
                title: 'Event 2',
                start: '2024-04-25'
            }
            // Add more events as needed
        ]
    });

    calendar.render();
});
