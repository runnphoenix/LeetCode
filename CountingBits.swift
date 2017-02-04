import Foundation

class Solution {
    
    func countBits(num:Int) -> [Int] {
    
        if num == 0 {
            return [0]
        }
        
        var resultArray = [Int]()
        let pivotArr = getPivotArray(Int(log2(Double(num))))
        for i in 0...num {
            resultArray.append(pivotArr[i])
        }
        return resultArray
    }

    func arrayInc(array:[Int]) -> [Int] {
        var appendArray = [Int]()
        for num in array {
            appendArray.append(num + 1)
        }
    
        return array + appendArray
    }

    func getPivotArray(times:Int) -> [Int] {
        var pivotArray:[Int] = [1]
        var appendedArray:[Int] = [1]
    
        for _ in 0...times {
            appendedArray = arrayInc(appendedArray)
            pivotArray += appendedArray
        }
    
        pivotArray.insert(0, atIndex: 0)
    
        return pivotArray
    }

}