update res_company set active=false where name='My Company';
update res_users set company_id=(select id from res_company where name='Victorikus');