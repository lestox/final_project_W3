<script>
  import Margin from "../../../components/atoms/Margin.svelte";
import NewUserForm from "../../../components/organisms/Forms/NewUserForm.svelte";

  export let data;
</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <NewUserForm data={data} employeePicture={data.users[0].profile_pic}/>
  </div>
</Margin>