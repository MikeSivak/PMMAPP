using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Script2 : MonoBehaviour
{
    public float speed;
    void Update()
    {
        float posX = transform.position.x;
        float posY = transform.position.y;
        float posZ = transform.position.z;
        transform.position=new Vector3(posX+speed, posY, posZ);

    }
}
