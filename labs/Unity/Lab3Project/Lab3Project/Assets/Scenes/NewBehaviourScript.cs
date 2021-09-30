using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public int forceApplied;
    // Start is called before the first frame update

    void OnCollisionEnter(Collision myCollision)
    {
        myCollision.gameObject.GetComponent<Rigidbody>().AddForce(0, 0, forceApplied);
    }
}
