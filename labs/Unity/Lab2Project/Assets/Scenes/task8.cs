using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class task8 : MonoBehaviour
{
    MeshRenderer render;
    //GameObject sphere, cubb;
    public Material material;
    //Start is called before the first frame update
    void Start()
    {
        render = gameObject.GetComponent<MeshRenderer>();
        //cubb = GameObject.CreatePrimitive(PrimitiveType.Cube);
        //sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
    }

    //Update is called once per frame
    void Update()
    {
        float minX = render.bounds.min.x;
        float maxX = render.bounds.max.x;
        float minZ = render.bounds.min.z;
        float maxZ = render.bounds.max.z;

        float newX = Random.Range(minX, maxX);
        float newZ = Random.Range(minZ, maxZ);
        float newY = gameObject.transform.position.y + 5;
        if (Input.GetKeyDown(KeyCode.Space))
        {
            GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
            cube.transform.position = new Vector3(newX, newY, newZ);

            material = cube.GetComponent<Renderer>().material;
            material.color = GetRandomColor();

            cube.AddComponent<Rigidbody>();
        }
        if (Input.GetMouseButtonDown(0))
        {
            GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            sphere.transform.position = new Vector3(newX, newY, newZ);

            material = sphere.GetComponent<Renderer>().material;
            material.color = GetRandomColor();

            sphere.AddComponent<Rigidbody>();
        }
    }
    Color GetRandomColor()
    {
        return new Color(Random.value, Random.value, Random.value);
    }
}
