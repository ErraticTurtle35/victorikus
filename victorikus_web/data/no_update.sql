update ir_model_data
set noupdate=true
where module='victorikus_web'
  and model='product.template';

update ir_model_data
set noupdate=true
where module='victorikus_web'
  and model='res.partner';

-- update ir_model_data
-- set noupdate=true
-- where module='victorikus_web'
--   and model='website.page'
--   and name='landing_page';

update ir_model_data
set noupdate=true
where module='victorikus_web'
  and model='res.users';