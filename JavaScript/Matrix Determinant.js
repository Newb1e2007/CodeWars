function determinant(m) {
  if (m.length == 0) return 0;
  if (m.length == 1) return m[0][0];
  if (m.length == 2) return m[0][0] * m[1][1] - m[0][1] * m[1][0];
  if (m.length > 2) {
    return m.reduce((prev, curr, i, arr) => {
      let miniArr = arr.slice(0, i).concat(arr.slice(i + 1)).map(item => item.slice(1));
      return prev + (i % 2 == 0 ? 1 : -1 ) * curr[0] * determinant(miniArr);
    }, 0);
  }
};


# ----------------------------------

// I "completed" this Kata well over
// a year ago by "cheating" the test
// cases a little bit (which I now
// deeply regret) so let's settle the
// record by submitting a legitimate
// solution
// I did NOT refer to other's solutions
// before coming up with this solution

const determinant = m => m.length === 1 ? m[0][0] : m[0].reduce((s, n, i) => s + (i % 2 === 0 ? 1 : -1) * n * determinant(m.slice(1).map(r => r.filter((_, j) => j !== i))), 0);
