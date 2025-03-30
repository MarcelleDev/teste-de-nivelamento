<template>
  <div class="container">
    <h1 class="title">Busca de Operadoras de Saúde</h1>
    
    <div class="search-container">
      <input
        type="text"
        v-model="termo"
        @input="buscarOperadoras"
        placeholder="Digite um termo..."
        class="search-box"
      />
      <svg class="search-icon" viewBox="0 0 24 24">
        <path fill="currentColor" d="M15.5 14h-.79l-.28-.27a6.471 6.471 0 0 0 1.48-5.34C15.33 5.01 12.31 2 8.83 2S2.33 5.01 2.33 8.5 5.35 15 8.83 15c1.61 0 3.09-.59 4.23-1.55l.27.28v.79l4.99 5L21 19l-5.5-5zM8.83 13c-2.49 0-4.5-2.01-4.5-4.5S6.34 4 8.83 4s4.5 2.01 4.5 4.5-2.01 4.5-4.5 4.5z"/>
      </svg>
    </div>

    <div v-if="operadoras.length === 0 && termo.length > 1" class="no-result">
      Nenhuma operadora encontrada.
    </div>

    <div v-else class="operadora-list">
      <div v-for="operadora in operadoras" :key="operadora.CNPJ" class="operadora-card">
        <h2>{{ operadora.Nome_Fantasia || operadora.Razao_Social }}</h2>
        <p><strong>Localização:</strong> {{ operadora.Cidade }}, {{ operadora.UF }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termo: "",
      operadoras: [],
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termo.length < 2) {
        this.operadoras = [];
        return;
      }
      try {
        const response = await axios.get(`http://localhost:8000/api/buscar?termo=${this.termo}`);
        this.operadoras = response.data.message ? [] : response.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
        this.operadoras = [];
      }
    },
  },
};
</script>

<style scoped>
/* Estilo geral */
.container {
  background: linear-gradient(to bottom, #4f9dd8, #3a7eb2); /* Azul gradiente */
  padding: 20px;
  border-radius: 10px;
  max-width: 600px;
  margin: auto;
  text-align: center;
  color: white;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

/* 🔍 Estilização da Barra de Pesquisa */
.search-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.search-box {
  width: 100%;
  padding: 12px 40px 12px 15px; /* Adiciona espaço para o ícone */
  border-radius: 25px;
  border: none;
  font-size: 16px;
  outline: none;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}

.search-box:focus {
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
}

/* Ícone de Lupa 🔍 */
.search-icon {
  position: absolute;
  right: 15px;
  width: 20px;
  height: 20px;
  color: #3a7eb2;
}

/* Mensagem de erro */
.no-result {
  margin-top: 10px;
  color: #ffeb3b;
  font-weight: bold;
}

/* Cartões */
.operadora-list {
  margin-top: 20px;
}

.operadora-card {
  background: white;
  color: #333;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 10px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.operadora-card:hover {
  transform: scale(1.03);
}
</style>
