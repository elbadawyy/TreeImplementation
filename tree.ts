import {BinaryTreeNode} from './node'

export class BinaryTree {
    traversalArray:any[]=[]
    totalLeafs:any[]=[]
    root: BinaryTreeNode;

    constructor(root:BinaryTreeNode){
        this.root = root
    }
    isEmpty(){
        if(this.root == null){
            return 'Yes , This tree is empty'
        }else{
            return 'No , This tree contain values'
        }
    }

    getLeafs(treeNode:BinaryTreeNode){
        if(treeNode == null){
            this.getLeafs(this.root)  
        }
        if (treeNode == undefined) {
            return false
        }
        if(treeNode.isLeaf()){
            treeNode.isLeaf()
            console.log('leaf  >>>> ',treeNode.isLeaf())
            this.totalLeafs.push(treeNode.isLeaf())
        }else{
            if(treeNode.refLeft && !treeNode.refRight){
                this.getLeafs(treeNode.refLeft)
            }else if(!treeNode.refLeft && treeNode.refRight){
                this.getLeafs(treeNode.refRight)
            }else if(treeNode.refLeft && treeNode.refRight){
                this.getLeafs(treeNode.refLeft)
                this.getLeafs(treeNode.refRight)
            }
        }
    }

    onlyUnique(value, index, self) { 
        return self.indexOf(value) === index;
    }

    traversalInOrder(treeNode:BinaryTreeNode){
         if (treeNode == null) {
            this.traversalInOrder(this.root);
        }
        if (treeNode == undefined) {
            return false;
        }
        if( treeNode.refLeft && !treeNode.refRight ){
            this.traversalInOrder(treeNode.refLeft);
            this.traversalArray.push(treeNode.refLeft.value)
        }else if ( treeNode.refLeft && treeNode.refRight) {
            this.traversalInOrder(treeNode.refLeft);
            this.traversalInOrder(treeNode.refRight);
            this.traversalArray.push(treeNode.refLeft.value,treeNode.value,treeNode.refRight.value)
        }else if ( treeNode.refRight && !treeNode.refLeft  ){
            this.traversalInOrder(treeNode.refRight);
        }
        var unique = this.traversalArray.filter( this.onlyUnique );
        console.log('Traversal in order : ', unique)
    }
}