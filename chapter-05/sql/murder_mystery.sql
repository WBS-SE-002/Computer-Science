SELECT * from crime_scene_report WHERE date = 20180115 AND city ILIKE 'sql city' AND type='murder';
SELECT * from person WHERE address_street_name = 'Northwestern Dr' ORDER BY address_number DESC LIMIT 1;
SELECT * from person WHERE name ILIKE 'Annabel%' AND address_street_name = 'Franklin Ave';
SELECT * from interview WHERE person_id = 14887 or person_id = 16371;

SELECT * from get_fit_now_check_in 
join get_fit_now_member on membership_id = id
join person on person_id = person.id
join drivers_license on license_id = drivers_license.id
WHERE membership_id LIKE '48Z%' AND plate_number ILIKE '%H42W%' AND check_in_date = 20180109;

--SELECT * from get_fit_now_member
--join person on person_id = person.id
--join drivers_license on license_id = drivers_license.id
--WHERE get_fit_now_member.id LIKE '48Z%' AND plate_number ILIKE '%H42W%';

--SELECT * from get_fit_now_check_in
--join get_fit_now_member on membership_id = id
--WHERE check_in_date = 20180109 and membership_id ILIKE '48Z%' 

INSERT into solution VALUES(1, 'Jeremy Bowers');

SELECT transcript from interview
join person on person_id = id
WHERE id = 67318;

SELECT * from drivers_license
join person on drivers_license.id = person.license_id
join facebook_event_checkin on person.id = facebook_event_checkin.person_id
WHERE height BETWEEN 65 and 67
and hair_color = 'red'
and gender = 'female'
and car_make = 'Tesla';

INSERT INTO solution VALUES(1, 'Miranda Priestly');
