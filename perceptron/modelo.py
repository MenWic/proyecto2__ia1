import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.errors = []

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def train(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        self.errors = [] # Lista para guardar errores por época (para la gráfica)
        self.accuracies = []  # Lista para guardar accuracy por época (para la gráfica)

        for _ in range(self.epochs):
            total_error = 0
            predictions_epoch = []
            for xi, target in zip(X, y):
                z = np.dot(xi, self.weights) + self.bias
                output = self.sigmoid(z)
                error = target - output
                self.weights += self.learning_rate * error * xi
                self.bias += self.learning_rate * error
                total_error += error ** 2
                predictions_epoch.append(1 if output >= 0.5 else 0)
            mse = total_error / n_samples
            self.errors.append(mse)
            acc = np.mean(np.array(predictions_epoch) == y)
            self.accuracies.append(acc)

        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        self.errors = []

        for _ in range(self.epochs):
            total_error = 0
            for xi, target in zip(X, y):
                z = np.dot(xi, self.weights) + self.bias
                output = self.sigmoid(z)
                error = target - output
                self.weights += self.learning_rate * error * xi
                self.bias += self.learning_rate * error
                total_error += error ** 2
            mse = total_error / n_samples
            self.errors.append(mse)

    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        output = self.sigmoid(z)
        return np.where(output >= 0.5, 1, 0)

    def evaluate(self, X, y):
        predictions = self.predict(X)
        accuracy = np.mean(predictions == y)
        return accuracy

    def plot_decision_boundary(self, ax, X):
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                             np.linspace(y_min, y_max, 100))
        grid = np.c_[xx.ravel(), yy.ravel()]
        probs = self.predict(grid).reshape(xx.shape)
        ax.contourf(xx, yy, probs, alpha=0.2, cmap='bwr')
