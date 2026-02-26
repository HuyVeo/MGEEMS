

# Tải dataset
from datasets import load_dataset

dataset = load_dataset("gamino/wiki_medical_terms")
print(dataset)
print(dataset['train'][0])  # Xem mẫu đầu tiên

# Chuyển sang DataFrame pandas
df = dataset['train'].to_pandas()
df.to_csv("wiki_medical_terms.csv", index=False)  # Lưu ra CSV