export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a String');
    if (typeof length !== 'number') throw TypeError('Length must be a Number');
    if (students.constructor !== Array && students.every((element) => typeof element === 'string')) throw TypeError('students must be an Array of Strings');

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a String');

    this._name = newName;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('Length must be a Number');

    this._length = newLength;
  }

  set students(newStudents) {
    if (newStudents.constructor !== Array && newStudents.every((element) => typeof element === 'string')) throw TypeError('students must be an Array of Strings');

    this._students = newStudents;
  }
}
