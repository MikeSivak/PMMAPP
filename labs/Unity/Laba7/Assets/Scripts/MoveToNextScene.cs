using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MoveToNextScene : MonoBehaviour
{
    public string sceneName;
    public AudioClip clip;
    void OnTriggerEnter(Collider other)
    {
       
            SceneManager.LoadScene(sceneName);
        // GetComponent<AudioSource>().PlayOneShot(clip);

    }

}
