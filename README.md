smith.py, a simple minimalistic Smith Chart plotter for Python.

Usage:

```python
  import smith
  smith=smith.smith()
  smith.markZ(20+30j)
  smith.drawZList([0, 50j, 1e6j, -50j, 0])
  smith.save('smithchart.pdf')
  ```
Results in

![smithchart.png](https://github.com/qnzy/smith.py/raw/master/smithchart.png)

Depends on matplotlib and numpy.
