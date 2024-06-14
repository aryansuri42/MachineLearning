{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Encoder Layer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class EncoderLayer(tf.keras.layers.Layer):\n",
    "\n",
    "    def __init__(self, d_model, dff, dropout_rate):\n",
    "\n",
    "        super().__init__()\n",
    "\n",
    "        self.attention = GlobalSelfAttention()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python3.10",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
