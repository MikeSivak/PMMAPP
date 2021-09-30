using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class last : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject prefab;

    // Instantiate the prefab somewhere between -10.0 and 10.0 on the x-z plane 
    void Start()
    {
        Vector3 position = new Vector3(Random.Range(100.0f, 170.0f), 0, Random.Range(-30.0f, 29.0f));
        Instantiate(prefab, position, Quaternion.identity);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
