const calculateNumber = require('./0-calcul')
const assert = require('assert');

describe('calculateNumber', function () {
      it('test function with values', function () {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(3.7, 1), 5);
        assert.strictEqual(calculateNumber(1, 3.3), 4);
        assert.strictEqual(calculateNumber(3.3, 1), 4);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(3.7, 1.2), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6)
        assert.strictEqual(calculateNumber(3.7, 1.2), 5);
        assert.strictEqual(calculateNumber(1.2, 2.1), 3);
      });
  })