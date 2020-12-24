export default function updateStudentGradeByCity(studentsArray, city, newGds) {
  return studentsArray.filter((item) => item.location === city).map((student) => {
    const gitem = newGds.filter((item) => item.studentId === student.id).map((pos) => pos.grade)[0];
    const grade = gitem || 'N/A';
    return { ...student, grade };
  });
}
