export default function updateStudentGradeByCity(studentsArray, city, newGrades) {
    return studentsArray.filter(item => item.location === city).map(student => {
	const grades = newGrades.filter(item => item.studentId === student.id).map(pos => pos.grades)[0];
	const grade = grades || 'N/A';
	return { ...student, grade };
    });
}
