const calculateNumber = require('./0-calcul')
const assert = require('assert');

describe('calculateNumber', () => {
    it('checks ouput', () => {
        assert.equal(calculateNumber(1.5, 2.1), 4);
        assert.equal(calculateNumber(0, 0.0), 0)
    });
    it('Checks Negatives Numbers', ()=> {
        assert.equal(calculateNumber(-2, -2), -4);
        assert.equal(calculateNumber(-10, -5), -15)
    })
})

