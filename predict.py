def predict(xlist, ylist, epochs, pdict:float,optimizer,loss,fuzzifica=False):
    """author:Dong Xing
    python_version:>=python3.6
    Predict with keras and numpy.It do not use GPU.
    for example:from predict import predict;print(predict(xlist=[1,2,3,4],ylist=[2,4,6,8],epochs=10000,pdict=5.0,optimizer='sgd',loss='mean_squared_error'))
    """
    if fuzzifica:
        import keras
        from numpy import array
        m = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
        m.compile(optimizer=optimizer, loss=loss)
        xs = array(xlist, dtype=float)
        ys = array(ylist, dtype=float)
        m.fit(xs, ys, epochs=epochs)
        return round(m.predict([pdict]))
    else:
        import keras
        from numpy import array
        m = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
        m.compile(optimizer='sgd', loss='mean_squared_error')
        xs = array(xlist, dtype=float)
        ys = array(ylist, dtype=float)
        m.fit(xs, ys, epochs=epochs)
        return m.predict([pdict])

