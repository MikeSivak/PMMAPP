
using UnityEngine;
using UnityEngine.SceneManagement;

public class DieSpace : MonoBehaviour
{
    public GameObject respawn;
    public GameObject player;
    void Update()
    {
        DeathLevel();
    }
    void DeathLevel()
    {
        if(player.transform.position.y < -12)
        {
            //SceneManager.LoadScene("SampleScene");
            //player.transform.position = respawn.transform.position;
            player.transform.position = new Vector3(respawn.transform.position.x, respawn.transform.position.y, 0);

        }

    }
}
