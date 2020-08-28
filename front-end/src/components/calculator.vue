<template>
  <section>
    <div class="calculator">
      <div class="display">{{current || '0'}}</div>
      <div @click="clear" class="btn">C</div>
      <div @click="sign" class="btn">+/-</div>
      <div @click="percent" class="btn">%</div>
      <div @click="divide" class="btn operator">÷</div>
      <div @click="append('7')" class="btn">7</div>
      <div @click="append('8')" class="btn">8</div>
      <div @click="append('9')" class="btn">9</div>
      <div @click="times" class="btn operator">x</div>
      <div @click="append('4')" class="btn">4</div>
      <div @click="append('5')" class="btn">5</div>
      <div @click="append('6')" class="btn">6</div>
      <div @click="minus" class="btn operator">-</div>
      <div @click="append('1')" class="btn">1</div>
      <div @click="append('2')" class="btn">2</div>
      <div @click="append('3')" class="btn">3</div>
      <div @click="add" class="btn operator">+</div>
      <download-csv class="btn btn-default" :data="historyData" name="results.csv">Download</download-csv>
      <div @click="append('0')" class="btn">0</div>
      <div @click="dot" class="btn">.</div>
      <div @click="equal" class="btn operator">=</div>
    </div>
  </section>
</template>

<script>
import operatorApi from "../services/operatorApi";

export default {
  data() {
    return {
      previous: null,
      current: "",
      operator: null,
      operatorClicked: false,
      historyData: [],
    };
  },
  methods: {
    clear() {
      this.current = "";
    },
    sign() {
      this.current =
        this.current.charAt(0) === "-"
          ? this.current.slice(1)
          : "-" + `${this.current}`;
    },
    append(number) {
      if (this.operatorClicked) {
        this.current = "";
        this.operatorClicked = false;
      }
      if (this.current == "0") {
        this.current = `${number}`;
      } else {
        this.current = `${this.current}${number}`;
      }
    },
    dot() {
      if (this.current.indexOf(".") === -1) {
        this.append(".");
      }
    },
    setPrevious() {
      this.previous = this.current;
      this.operatorClicked = true;
    },
    divide() {
      this.setPrevious();
      this.operator = "/";
    },
    times() {
      this.setPrevious();
      this.operator = "x";
    },
    minus() {
      this.setPrevious();
      this.operator = "-";
    },
    add() {
      this.setPrevious();
      this.operator = "+";
    },
    async percent() {
      this.operator = "%";
      const payload = {
        op1: this.current,
        op2: 100,
        operator: this.operator,
      };
      const result = await operatorApi.calculate(payload);
      this.current = result.toString();

      payload["result"] = this.current;
      this.historyData.push(payload);

      this.previous = null;
      this.operator = null;
    },
    async equal() {
      const payload = {
        op1: this.previous,
        op2: this.current,
        operator: this.operator,
      };
      const result = await operatorApi.calculate(payload);
      if (result != null) {
        this.current = result.toString();
      } else {
        this.current = "Undefined";
      }

      payload["result"] = this.current;
      this.historyData.push(payload);

      this.previous = null;
      this.operator = null;
    },
  },
};
</script>

<style scoped>
.calculator {
  margin: 130px auto;
  width: 400px;
  height: 545px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(50px, auto);
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
  border-radius: 10px;

}
.display {
  font-size: 48px;
  padding: 25px 10px 0px 0px;
  height: 85px;
  grid-column: 1 / 5;
  background-color: #333;
  color: white;
  text-align: right;
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
  border-radius: 5px;

}

.btn {
  text-align: center;
  margin: 1px;
  font-size: 18px;
  padding: 30px 0;
  background-color: #e8e8e8;
  border-radius: 5px;

}
.operator {
  background-color: #ff8d00ed;
  color: white;
  font-size: 18px;
  font-weight: 700;
}
</style>