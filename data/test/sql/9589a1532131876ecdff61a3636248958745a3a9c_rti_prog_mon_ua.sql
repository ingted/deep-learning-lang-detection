DROP TRIGGER IF EXISTS `c_rti_prog_mon_ua` //
CREATE definer=`dbadmin`@`localhost` trigger `c_rti_prog_mon_ua` AFTER UPDATE ON `c_rti_prog_mon`
  FOR EACH ROW


BEGIN

    INSERT INTO c_rti_prog_mon_au 
        
    SET     prog_mon_id = OLD.prog_mon_id
            ,moniker = IF(NEW.moniker != OLD.moniker, OLD.moniker, NULL)
            ,sort_order = IF(NEW.sort_order != OLD.sort_order, OLD.sort_order, NULL)
            ,action_code = 'u'
            ,audit_user_id = NEW.last_user_id
            ,client_id = IF(NEW.client_id != OLD.client_id, OLD.client_id, NULL)
            ,create_user_id = NEW.create_user_id
            ,last_user_id = IF(NEW.last_user_id != OLD.last_user_id, OLD.last_user_id, NULL)
            ,create_timestamp = IF(NEW.create_timestamp != OLD.create_timestamp, OLD.create_timestamp, NULL)
            ,last_edit_timestamp = IF(NEW.last_edit_timestamp != OLD.last_edit_timestamp, OLD.last_edit_timestamp, NULL)
    ;

END;
//
