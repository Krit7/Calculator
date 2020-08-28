import Api from './Api.js'

export default {
    calculate(payload) {
        return Api().post('/calculate', payload).then(
            res => {
                const result = res.data.result;
                return result;
            }
        ).catch(err => {
            console.log(err);
        })
    },

}