<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";
  import Image from "../../atoms/Image.svelte";
  import Icon from "../../atoms/Icon.svelte";
  import AddIcon from "../../../assets/icons/AddIcon.svelte";

  import Account from "../../../assets/img/account.png";

  /**
   * @type {string}
  */
  export let selectValue = '';

  /**
   * @type {any}
  */
  export let employeePicture;

    /**
   * @type {any}
  */
  export let data;

</script>

<form class="form-newUser">
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase w-100 text-center'
  > 
    Nouvel utilisateur
  </Text>

  <div class='avatar-upload block-center'>
    <Image
      imageSrc={employeePicture ? employeePicture : Account }
      imageAlt="Employee picture"
      imageWidth=80
      border
    />
    <br>
    <InputForm type='file' id='avatar' name='avatar'> 
      Importer image
    </InputForm>
  </div>

  <InputForm id='lastname' name='lastname' widthForm='calc(50% - 5px)'> Nom </InputForm>
  <InputForm id='firstname' name='firstname' widthForm='calc(50% - 5px)'> Prénom </InputForm>
  <InputForm id='email' name='email' type='email'> Email </InputForm>
  <SelectForm nameSelect="domain" data={data.metadata.domain} labelName='domain' widthForm='calc(50% - 5px)' bind:selectValue={selectValue} > Domaine </SelectForm>
  <SelectForm nameSelect="role" data={data.metadata.role} labelName='role' widthForm='calc(50% - 5px)' bind:selectValue={selectValue}> Rôle </SelectForm>
  {#if selectValue == 'traducteur'}
    <CheckboxForm data={data.metadata.translations} catForm='langues-traducteur'> Langues de traduction </CheckboxForm>
  {/if}
  <Button marginTop='var(--spacing-2)'> Valider </Button>
</form>

<style>
  .form-newUser{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    row-gap: var(--spacing-3);
    column-gap: var(--spacing-2);
  }

  .avatar-upload{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .avatar-upload :global(.input-form){
    width: auto;
    text-align: center;
    margin-top: var(--spacing-1);
  }
</style>