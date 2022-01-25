select title from items where item_code IN(SELECT item_code from ranking where sub_category='패션의류');

select max(items.dis_price) from items inner join ranking on items.item_code = ranking.item_code where ranking.sub_category='패션의류';

select max(items.dis_price) from items where item_code in(select item_code from ranking where sub_category ='패션의류');

select main_category,count(*) from ranking where item_code in (select item_code from items where dis_price>100000);
