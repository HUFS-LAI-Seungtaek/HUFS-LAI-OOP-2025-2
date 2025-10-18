from main import Metric, Accuracy, Precision, Recall

def run_tests():
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

    accuracy = Accuracy()
    precision = Precision(positive_class=1)
    recall = Recall(positive_class=1)

    assert isinstance(accuracy, Metric)
    assert isinstance(precision, Metric)
    assert isinstance(recall, Metric)

    assert abs(accuracy.compute(y_true, y_pred) - 0.75) < 0.01
    assert abs(precision.compute(y_true, y_pred) - 0.75) < 0.01
    assert abs(recall.compute(y_true, y_pred) - 0.75) < 0.01

    assert "Accuracy: 0.750" in accuracy.evaluate(y_true, y_pred)

    metrics = [accuracy, precision, recall]
    for metric in metrics:
        result = metric.evaluate(y_true, y_pred)
        assert ":" in result

    try:
        Metric("Test")
        assert False
    except TypeError:
        pass

    print("All Problem 6 tests passed.")

run_tests()
