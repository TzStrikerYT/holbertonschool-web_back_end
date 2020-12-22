const Car = require('./10-car.js');

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  static get [Symbol.species]() {
    return Car;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(this._brand, this._motor, this._color, this._range);
  }
}
