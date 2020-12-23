export default function getStudentsByLocation(studentArray, city) {
  return studentArray.filter((item) => item.location === city);
}
