export default function createInt8TypedArray(length, position, value) {
    if (position >= length) throw Error('Position outside range');
    const buff = new ArrayBuffer(length);
    const int8 = new Int8Array(buff);

    int8[position] = value;
    return int8;
}
