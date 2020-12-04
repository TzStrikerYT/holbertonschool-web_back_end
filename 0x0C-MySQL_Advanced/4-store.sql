 --creates a trigger that decreases the quantity of an item after adding a new order
create trigger decrase_quant
after insert on orders
for each row update items
set quantity = quantity - NEW.number
where NEW.item_name = name;