export default function getStudentIdsSum(studentsArray) {
  const reducer = (accumulator, item) => accumulator + item.id;
  return studentsArray.reduce(reducer, 0);
}
