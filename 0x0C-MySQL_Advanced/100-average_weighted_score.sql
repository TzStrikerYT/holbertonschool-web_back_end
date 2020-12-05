-- 
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser( user_id INT ) BEGIN DECLARE w_avg_score FLOAT;

SET w_avg_score = (
SELECT  SUM(score * weight) / SUM(weight)
FROM users AS U
JOIN corrections AS C
ON U.id=C.user_id
JOIN projects AS P
ON C.project_id=P.id
WHERE U.id=user_id); UPDATE users 

SET average_score = w_avg_score
WHERE id=user_id; 
END // 
DELIMITER ; 