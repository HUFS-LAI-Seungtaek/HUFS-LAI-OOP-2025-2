if __name__ == "__main__":
    try:
        from . import train_test_split, label_distribution
        tr, te = train_test_split([1,2,3,4,5],0.4,seed=42)
        print(tr,te)            #[4, 2, 3] [5, 1]
        print(label_distribution(["cat","dog","cat"])) #{'cat': 2, 'dog': 1}
        print("dsops demo OK") 
    except Exception as e:
        print("Implement textops first:", e)
