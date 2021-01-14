const calculateNumber = require('./0-calcul')
const assert = require('assert');

describe('calculateNumber', () => {
    it('checks outut', () => {
        assert.equal(calculateNumber(1.5, 2.1), 4);
        assert.equal(calculateNumber(0, 0.0), 0)
    })
})

