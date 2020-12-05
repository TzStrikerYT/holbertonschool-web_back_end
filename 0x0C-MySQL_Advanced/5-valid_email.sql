-- creates a trigger that resets the attribute valid_email only WHEN the email has been changed
delimiter //
CREATE trigger reset_valid 
before update ON users
for each row 
BEGIN 
    if NEW.email <> OLD.email 
    THEN SET NEW.valid_email = 0;
    end if;
END // 
delimiter ;