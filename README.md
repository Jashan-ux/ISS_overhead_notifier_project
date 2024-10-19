# ISS_overhead_notifier_project
This project tracks the International Space Station (ISS) and notifies the user via email when the ISS is overhead during nighttime. The code integrates several elements, including geolocation, time-based conditions, and automated email. notifications.
It uses API to request the exact location of ISS.
This is not independent , it import sunrise_set.py ,to implement the function whether its night or day.
also I Used standard mail transfer protocol (smtp) which send email notification from my one email to my another email, if ISS is overhead.
I imported time module to call sleep function to sleep 60 sec while true, which make it run 24hrs , if my pc is on.

I used my geolocation in sunrise_set module , you can update your own.
