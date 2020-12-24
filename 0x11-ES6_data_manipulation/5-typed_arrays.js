export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw Error('Position outside range');
  const buff = new ArrayBuffer(length);
  const int8 = new DataView(buff, 0);
  int8.setInt8(position, value);
  return int8;
}
