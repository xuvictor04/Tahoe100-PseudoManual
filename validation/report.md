# Validation report

Written by `tahoemap validate` (tahoemap/validate.py) on 2026-11-09 11:07. 15,076 genes are in the vector space (64 dimensions); the nodal map has 235 modules. `cos` is the signed cosine of two genes' unit vectors: the correlation of their denoised responses over every (drug-dose, cell line) context (+1 = always move together, -1 = always opposite). AUROC = probability that a pair of genes from the set has a higher cosine than a random pair of genes in the space (0.5 = no better than random, 1 = every set pair beats every random pair). 'p (random sets)' = share of 200 random gene sets of the same size that score at least as high.

## 1. Do known programmes hang together in the vector space?

Curated control sets (tahoemap/data/control_sets.json; literature, not Tahoe), ranked by AUROC on cos. 19 of 19 sets have >= 2 genes in the space; 19 reach AUROC >= 0.6 and 19 have p <= 0.05 against random sets. 'top module' = the module holding most of the set's genes, its share of the set, and its share of all genes (the chance level). Every drug-dose keeps its ranked place; ⚠ and its flags in plain words mark one with an artifact flag (technically untrustworthy ones included), and when the 5 strongest hold such drug-doses, the 5 strongest without an alert follow in their ranked place too. For a cell-cycle shift the share of the set's mean change that the shift would explain is given (the tables stage's rule; a shift that does not explain the change is named without ⚠).

| set | genes in space / listed | mean cos | AUROC cos | AUROC abs(cos) | p (random sets) | top module (share; all genes) | drug-doses raising it most (mean z) |
|---|---|---|---|---|---|---|---|
| INTERFERON | 25/25 | 0.84 | 1.00 | 1.00 | <= 0.005 | 32 (92%; all genes 0.9%) | Harringtonine 0.5 uM (+6.2, cell-cycle shift, explains ~0% of this change); Cobimetinib 5 uM (+5.4); Binimetinib 5 uM (+3.6); Trametinib (DMSO_TF solvate) 5 uM (+3.5); venetoclax 0.05 uM (+3.5) |
| DREAM_G2M_DOWN | 30/30 | 0.81 | 1.00 | 1.00 | <= 0.005 | 22 (93%; all genes 1.2%) | Homoharringtonine 5 uM (+10.8, ⚠ cell-cycle shift, explains ~100% of this change); Docetaxel 0.05 uM (+6.6, ⚠ transcription drop, cell-cycle shift, explains ~97% of this change); Harringtonine 5 uM (+6.4, ⚠ cell-cycle shift, explains ~100% of this change); Darinaparsin 5 uM (+5.5, ⚠ cell-cycle shift, explains ~88% of this change); Ouabain (Octahydrate) 5 uM (+5.4, ⚠ cell-cycle shift, explains ~100% of this change); Docetaxel 5 uM (+3.5); Mebendazole 5 uM (+3.1); Vinblastine (sulfate) 0.05 uM (+2.9); Peretinoin 0.5 uM (+2.7); Peretinoin 0.05 uM (+2.6) |
| CHOLESTEROL_SYNTHESIS | 23/23 | 0.61 | 0.99 | 0.98 | <= 0.005 | 86 (96%; all genes 0.3%) | Cepharanthine 5 uM (+14.0); Berbamine 5 uM (+13.4); Panobinostat 5 uM (+6.6, cell-cycle shift, explains ~9% of this change); Niclosamide (olamine) 5 uM (+6.4, ⚠ toxic, cell-cycle shift, explains ~7% of this change); Panobinostat 0.5 uM (+5.9, cell-cycle shift, explains ~9% of this change); Entrectinib 5 uM (+5.5) |
| E2F_G1S | 24/24 | 0.62 | 0.98 | 0.97 | <= 0.005 | 6 (96%; all genes 1.6%) | Dinaciclib 0.5 uM (+11.0, ⚠ toxic, transcription drop, cell-cycle shift, explains ~84% of this change); Dinaciclib 5 uM (+9.7, ⚠ toxic, transcription drop, cell-cycle shift, explains ~84% of this change); Panobinostat 5 uM (+8.2, ⚠ cell-cycle shift, explains ~100% of this change); Dinaciclib 0.05 uM (+7.8, ⚠ toxic, transcription drop, cell-cycle shift, explains ~77% of this change); Panobinostat 0.5 uM (+7.2, ⚠ cell-cycle shift, explains ~100% of this change); Mitoxantrone (dihydrochloride) 5 uM (+2.9); Belumosudil 5 uM (+2.5); Retinoic acid 0.05 uM (+2.4); Ixazomib citrate 0.5 uM (+2.1); Raltitrexed 0.5 uM (+2.1) |
| NFKB | 15/15 | 0.50 | 0.98 | 0.96 | <= 0.005 | 14 (80%; all genes 1.4%) | Homoharringtonine 5 uM (+32.6, cell-cycle shift, explains ~14% of this change); Harringtonine 5 uM (+21.9, cell-cycle shift, explains ~12% of this change); Homoharringtonine 0.5 uM (+14.7, cell-cycle shift, explains ~10% of this change); TAK-901 5 uM (+12.5, cell-cycle shift, explains ~7% of this change); Harringtonine 0.5 uM (+10.9, cell-cycle shift, explains ~9% of this change) |
| MAPK_OUTPUT | 18/18 | 0.55 | 0.97 | 0.95 | <= 0.005 | 92 (44%; all genes 0.3%) | Harringtonine 5 uM (+6.4, ⚠ cell-cycle shift, explains ~37% of this change); Homoharringtonine 5 uM (+5.5, ⚠ cell-cycle shift, explains ~68% of this change); TAK-901 5 uM (+4.7, cell-cycle shift, explains ~18% of this change); Harringtonine 0.5 uM (+3.2, ⚠ cell-cycle shift, explains ~29% of this change); Tucidinostat 5 uM (+3.0); PH-797804 5 uM (+2.5); Tucidinostat 0.5 uM (+2.1, cell-cycle shift, explains ~0% of this change); Filgotinib 5 uM (+1.8) |
| HEAT_SHOCK | 14/15 | 0.47 | 0.97 | 0.95 | <= 0.005 | 60 (93%; all genes 0.5%) | Auranofin 5 uM (+26.6); Ixazomib citrate 5 uM (+22.8, cell-cycle shift, explains ~0% of this change); Ixazomib citrate 0.5 uM (+20.5); Bortezomib 0.05 uM (+18.7, cell-cycle shift, explains ~0% of this change); Bortezomib 5 uM (+12.0, ⚠ toxic, cell-cycle shift, explains ~0% of this change); Bortezomib 0.5 uM (+10.6) |
| HYPOXIA | 16/16 | 0.46 | 0.96 | 0.93 | <= 0.005 | 99 (44%; all genes 0.3%) | TAK-901 5 uM (+3.8, cell-cycle shift, explains ~11% of this change); PF-06260933 5 uM (+3.8); Dimethyl fumarate 5 uM (+2.9); Fumaric acid 5 uM (+2.4); Pravastatin (sodium) 5 uM (+2.3) |
| PROTEASOME | 31/31 | 0.45 | 0.96 | 0.92 | <= 0.005 | 72 (35%; all genes 0.5%) | Ixazomib citrate 5 uM (+15.5, cell-cycle shift, explains ~0% of this change); Ixazomib citrate 0.5 uM (+15.4); Bortezomib 0.05 uM (+12.6, cell-cycle shift, explains ~0% of this change); Dinaciclib 0.5 uM (+8.1, ⚠ toxic, transcription drop, cell-cycle shift, explains ~51% of this change); Auranofin 5 uM (+7.9); Bortezomib 0.5 uM (+5.5) |
| ISR_ATF4 | 22/22 | 0.52 | 0.95 | 0.90 | <= 0.005 | 63 (73%; all genes 0.5%) | Artesunate 5 uM (+8.4, cell-cycle shift, explains ~3% of this change); Neratinib (maleate) 0.5 uM (+7.8, cell-cycle shift, explains ~4% of this change); Auranofin 5 uM (+7.7); c-Kit-IN-1 0.05 uM (+7.4, ⚠ unreliable plate only); Neratinib (maleate) 5 uM (+6.3); 5-Azacytidine 5 uM (+6.1) |
| UPR_ER | 18/18 | 0.53 | 0.94 | 0.93 | <= 0.005 | 42 (61%; all genes 0.7%) | Auranofin 5 uM (+5.1); Panobinostat 0.5 uM (+4.1, ⚠ cell-cycle shift, explains ~26% of this change); Dinaciclib 0.5 uM (+3.4, ⚠ toxic, transcription drop, cell-cycle shift, explains ~44% of this change); Idarubicin (hydrochloride) 5 uM (+3.3, ⚠ cell-cycle shift, explains ~16% of this change); Panobinostat 5 uM (+3.0, ⚠ cell-cycle shift, explains ~41% of this change); Lipoic acid 5 uM (+2.4); Fluvoxamine (maleate) 0.5 uM (+2.2); PH-797804 5 uM (+2.1); Tofacitinib 0.5 uM (+1.9) |
| SREBP1_LIPOGENESIS | 10/10 | 0.44 | 0.94 | 0.89 | <= 0.005 | 86 (60%; all genes 0.3%) | Cepharanthine 5 uM (+11.0); Berbamine 5 uM (+9.5); Idarubicin (hydrochloride) 5 uM (+8.0, cell-cycle shift, explains ~6% of this change); Dinaciclib 0.5 uM (+7.7, ⚠ toxic, transcription drop, cell-cycle shift, explains ~12% of this change); Dinaciclib 5 uM (+7.0, ⚠ toxic, transcription drop, cell-cycle shift, explains ~12% of this change); Entrectinib 5 uM (+5.2); (S)-Crizotinib 5 uM (+4.5) |
| IMMEDIATE_EARLY | 20/20 | 0.42 | 0.93 | 0.87 | <= 0.005 | 109 (45%; all genes 0.3%) | Homoharringtonine 5 uM (+18.3, ⚠ cell-cycle shift, explains ~29% of this change); Harringtonine 5 uM (+11.9, ⚠ cell-cycle shift, explains ~27% of this change); Homoharringtonine 0.5 uM (+7.4, cell-cycle shift, explains ~25% of this change); Harringtonine 0.5 uM (+5.3, cell-cycle shift, explains ~24% of this change); Dinaciclib 0.05 uM (+5.0, ⚠ toxic, transcription drop, cell-cycle shift, explains ~28% of this change); Tucidinostat 5 uM (+4.2); Panobinostat 5 uM (+2.9, cell-cycle shift, explains ~23% of this change); Tucidinostat 0.5 uM (+2.8, cell-cycle shift, explains ~0% of this change) |
| RIBOSOME_BIOGENESIS | 23/23 | 0.42 | 0.91 | 0.86 | <= 0.005 | 5 (26%; all genes 1.6%) | Homoharringtonine 0.5 uM (+8.9, cell-cycle shift, explains ~7% of this change); c-Kit-IN-1 0.05 uM (+8.0, ⚠ unreliable plate only); Dinaciclib 0.5 uM (+7.5, ⚠ toxic, transcription drop, cell-cycle shift, explains ~63% of this change); Harringtonine 0.5 uM (+7.1, cell-cycle shift, explains ~16% of this change); Panobinostat 5 uM (+6.6, ⚠ cell-cycle shift, explains ~62% of this change); PH-797804 5 uM (+6.4); TAK-901 5 uM (+6.1, cell-cycle shift, explains ~22% of this change); Ixazomib citrate 5 uM (+5.3, cell-cycle shift, explains ~0% of this change) |
| GLUCOCORTICOID | 8/9 | 0.36 | 0.89 | 0.83 | <= 0.005 | 98 (25%; all genes 0.3%) | Budesonide 0.05 uM (+9.8); Clobetasol propionate 0.05 uM (+9.7); Budesonide 0.5 uM (+9.6); Betamethasone dipropionate 5 uM (+9.4); Betamethasone dipropionate 0.5 uM (+9.3) |
| P53_TARGETS_UP | 42/42 | 0.36 | 0.88 | 0.82 | <= 0.005 | 62 (62%; all genes 0.5%) | Homoharringtonine 5 uM (+8.6, cell-cycle shift, explains ~0% of this change); Idarubicin (hydrochloride) 5 uM (+6.8, cell-cycle shift, explains ~11% of this change); Topotecan (hydrochloride) 5 uM (+5.8, ⚠ toxic, cell-cycle shift, explains ~11% of this change); Homoharringtonine 0.5 uM (+5.8, cell-cycle shift, explains ~0% of this change); Selinexor 5 uM (+4.5, cell-cycle shift, explains ~0% of this change); Idarubicin (hydrochloride) 0.5 uM (+4.4, cell-cycle shift, explains ~6% of this change) |
| NRF2 | 20/21 | 0.30 | 0.85 | 0.76 | <= 0.005 | 117 (40%; all genes 0.3%) | Auranofin 5 uM (+13.0); Dinaciclib 0.5 uM (+8.8, ⚠ toxic, transcription drop, cell-cycle shift, explains ~13% of this change); Ixazomib citrate 0.5 uM (+7.5); Dinaciclib 5 uM (+7.2, ⚠ toxic, transcription drop, cell-cycle shift, explains ~13% of this change); Bortezomib 0.05 uM (+7.1, cell-cycle shift, explains ~0% of this change); Ixazomib citrate 5 uM (+7.1, cell-cycle shift, explains ~0% of this change); Homoharringtonine 0.5 uM (+5.0, cell-cycle shift, explains ~21% of this change) |
| METALLOTHIONEIN | 8/9 | 0.47 | 0.84 | 0.85 | <= 0.005 | 113 (62%; all genes 0.3%) | Homoharringtonine 5 uM (+8.7, ⚠ cell-cycle shift, explains ~53% of this change); Chlorhexidine (diacetate) 5 uM (+6.9); Homoharringtonine 0.5 uM (+4.9, ⚠ cell-cycle shift, explains ~32% of this change); Dinaciclib 0.5 uM (+4.0, ⚠ toxic, transcription drop, cell-cycle shift, explains ~35% of this change); Tucidinostat 5 uM (+3.8); Budesonide 0.05 uM (+3.5); Clobetasol propionate 0.05 uM (+3.3); Panobinostat 0.5 uM (+3.3, cell-cycle shift, explains ~15% of this change) |
| AHR | 5/6 | 0.23 | 0.82 | 0.68 | <= 0.005 | 17 (20%; all genes 1.3%) | Dinaciclib 0.5 uM (+5.6, ⚠ toxic, transcription drop, cell-cycle shift, explains ~23% of this change); Homoharringtonine 5 uM (+4.7, ⚠ cell-cycle shift, explains ~77% of this change); Gemcitabine 0.05 uM (+4.7); Dinaciclib 5 uM (+4.3, ⚠ toxic, transcription drop, cell-cycle shift, explains ~25% of this change); AZD-7648 5 uM (+4.3); Idarubicin (hydrochloride) 5 uM (+4.0, cell-cycle shift, explains ~6% of this change); Menadione 5 uM (+3.9); Gemcitabine 5 uM (+3.7) |

**MSigDB Hallmark** (50 sets with >= 5 genes in the space): median AUROC on cos 0.56, 12 sets (24%) at >= 0.6, 47 with p <= 0.05 against random sets.

| set | genes in space / listed | mean cos | AUROC cos | AUROC abs(cos) | p (random sets) | top module (share; all genes) | drug-doses raising it most (mean z) |
|---|---|---|---|---|---|---|---|
| HALLMARK_INTERFERON_ALPHA_RESPONSE | 92/97 | 0.50 | 0.94 | 0.91 | <= 0.005 | 32 (61%; all genes 0.9%) | Harringtonine 0.5 uM (+4.4, cell-cycle shift, explains ~1% of this change); Cobimetinib 5 uM (+4.1); Binimetinib 5 uM (+3.1); Trametinib (DMSO_TF solvate) 5 uM (+3.1); Trametinib 0.5 uM (+3.0) |
| HALLMARK_MYC_TARGETS_V2 | 58/58 | 0.28 | 0.81 | 0.73 | <= 0.005 | 5 (22%; all genes 1.6%) | Dinaciclib 0.5 uM (+6.2, ⚠ toxic, transcription drop, cell-cycle shift, explains ~55% of this change); Dinaciclib 0.05 uM (+5.8, ⚠ toxic, transcription drop, cell-cycle shift, explains ~38% of this change); c-Kit-IN-1 0.05 uM (+5.3, ⚠ unreliable plate only); Dinaciclib 5 uM (+5.2, ⚠ toxic, transcription drop, cell-cycle shift, explains ~55% of this change); Topotecan (hydrochloride) 5 uM (+4.6, ⚠ toxic, cell-cycle shift, explains ~17% of this change); Ixazomib citrate 5 uM (+4.3, cell-cycle shift, explains ~0% of this change); Homoharringtonine 0.5 uM (+4.2, cell-cycle shift, explains ~12% of this change); Harringtonine 0.5 uM (+4.2, cell-cycle shift, explains ~20% of this change); PH-797804 5 uM (+4.2); Auranofin 5 uM (+3.3) |
| HALLMARK_TNFA_SIGNALING_VIA_NFKB | 188/200 | 0.21 | 0.77 | 0.67 | <= 0.005 | 14 (23%; all genes 1.4%) | Homoharringtonine 5 uM (+14.6, cell-cycle shift, explains ~25% of this change); Harringtonine 5 uM (+10.4, cell-cycle shift, explains ~19% of this change); Homoharringtonine 0.5 uM (+7.4, cell-cycle shift, explains ~17% of this change); TAK-901 5 uM (+5.9, cell-cycle shift, explains ~12% of this change); Harringtonine 0.5 uM (+5.7, cell-cycle shift, explains ~13% of this change) |
| HALLMARK_INTERFERON_GAMMA_RESPONSE | 169/200 | 0.27 | 0.77 | 0.70 | <= 0.005 | 32 (36%; all genes 0.9%) | Harringtonine 0.5 uM (+3.6, cell-cycle shift, explains ~4% of this change); Cobimetinib 5 uM (+2.8); Harringtonine 5 uM (+2.5, ⚠ cell-cycle shift, explains ~15% of this change); Homoharringtonine 0.5 uM (+2.4, ⚠ cell-cycle shift, explains ~12% of this change); Binimetinib 5 uM (+2.2); Trametinib (DMSO_TF solvate) 5 uM (+2.1); Trametinib 0.5 uM (+2.0) |
| HALLMARK_E2F_TARGETS | 200/200 | 0.26 | 0.76 | 0.71 | <= 0.005 | 6 (32%; all genes 1.6%) | Dinaciclib 0.5 uM (+7.4, ⚠ toxic, transcription drop, cell-cycle shift, explains ~75% of this change); Dinaciclib 5 uM (+6.6, ⚠ toxic, transcription drop, cell-cycle shift, explains ~71% of this change); Dinaciclib 0.05 uM (+5.2, ⚠ toxic, transcription drop, cell-cycle shift, explains ~64% of this change); Niclosamide (olamine) 5 uM (+3.8, ⚠ toxic, cell-cycle shift, explains ~70% of this change); Ouabain (Octahydrate) 5 uM (+3.8, ⚠ cell-cycle shift, explains ~100% of this change); Retinoic acid 0.05 uM (+1.6); Mebendazole 5 uM (+1.4); Berbamine 0.05 uM (+1.3); Raltitrexed 0.5 uM (+1.3); Diammonium Glycyrrhizinate 0.05 uM (+1.3) |
| HALLMARK_G2M_CHECKPOINT | 198/200 | 0.19 | 0.69 | 0.63 | <= 0.005 | 22 (30%; all genes 1.2%) | Ouabain (Octahydrate) 5 uM (+5.7, ⚠ cell-cycle shift, explains ~72% of this change); Homoharringtonine 5 uM (+5.5, ⚠ cell-cycle shift, explains ~100% of this change); Digitoxin 5 uM (+4.9, ⚠ toxic, transcription drop, cell-cycle shift, explains ~72% of this change); Digitoxin 0.5 uM (+4.0, ⚠ cell-cycle shift, explains ~71% of this change); Ouabain (Octahydrate) 0.5 uM (+4.0, ⚠ cell-cycle shift, explains ~68% of this change); PH-797804 5 uM (+2.7); Mebendazole 5 uM (+1.2); Retinoic acid 0.05 uM (+1.2); Berbamine 0.05 uM (+1.1); Docetaxel 5 uM (+1.0) |
| HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION | 183/200 | 0.12 | 0.66 | 0.57 | <= 0.005 | 13 (16%; all genes 1.4%) | Dinaciclib 0.5 uM (+8.6, ⚠ toxic, transcription drop, cell-cycle shift, explains ~10% of this change); Dinaciclib 5 uM (+7.5, ⚠ toxic, transcription drop, cell-cycle shift, explains ~9% of this change); Dinaciclib 0.05 uM (+6.1, ⚠ toxic, transcription drop, cell-cycle shift, explains ~7% of this change); Tucidinostat 5 uM (+4.4); Tucidinostat 0.5 uM (+3.0, cell-cycle shift, explains ~0% of this change); 9-ING-41 0.5 uM (+1.3); Carbamazepine 5 uM (+1.2); Flutamide 5 uM (+1.2) |
| HALLMARK_INFLAMMATORY_RESPONSE | 139/200 | 0.11 | 0.64 | 0.55 | <= 0.005 | 14 (16%; all genes 1.4%) | Homoharringtonine 5 uM (+6.1, cell-cycle shift, explains ~23% of this change); Harringtonine 5 uM (+4.3, cell-cycle shift, explains ~18% of this change); Tucidinostat 5 uM (+4.2); Tucidinostat 0.5 uM (+3.1, cell-cycle shift, explains ~0% of this change); Homoharringtonine 0.5 uM (+2.7, cell-cycle shift, explains ~18% of this change) |
| HALLMARK_HYPOXIA | 182/200 | 0.11 | 0.63 | 0.55 | <= 0.005 | 99 (9.3%; all genes 0.3%) | Tucidinostat 5 uM (+2.6); TAK-901 5 uM (+2.1, cell-cycle shift, explains ~16% of this change); Tucidinostat 0.5 uM (+2.0, ⚠ cell-cycle shift, explains ~9% of this change); PF-06260933 5 uM (+1.6); Dimethyl fumarate 5 uM (+1.3); Fumaric acid 5 uM (+1.0) |
| HALLMARK_CHOLESTEROL_HOMEOSTASIS | 69/74 | 0.13 | 0.63 | 0.56 | <= 0.005 | 86 (35%; all genes 0.3%) | Cepharanthine 5 uM (+5.4); Berbamine 5 uM (+5.2); Dinaciclib 0.5 uM (+3.1, ⚠ toxic, transcription drop, cell-cycle shift, explains ~15% of this change); Niclosamide (olamine) 5 uM (+3.1, ⚠ toxic, cell-cycle shift, explains ~12% of this change); Entrectinib 5 uM (+2.6); Adagrasib 5 uM (+2.2); Almonertinib (mesylate) 5 uM (+2.1) |
| HALLMARK_MYC_TARGETS_V1 | 200/200 | 0.11 | 0.63 | 0.61 | <= 0.005 | 4 (10%; all genes 1.6%) | Dinaciclib 0.5 uM (+10.2, ⚠ toxic, transcription drop, cell-cycle shift, explains ~40% of this change); Dinaciclib 5 uM (+8.8, ⚠ toxic, transcription drop, cell-cycle shift, explains ~40% of this change); Dinaciclib 0.05 uM (+7.1, ⚠ toxic, transcription drop, cell-cycle shift, explains ~35% of this change); Niclosamide (olamine) 5 uM (+4.9, ⚠ toxic, cell-cycle shift, explains ~42% of this change); Ixazomib citrate 5 uM (+4.4, cell-cycle shift, explains ~0% of this change); Ixazomib citrate 0.5 uM (+4.2); Auranofin 5 uM (+3.8); PH-797804 5 uM (+3.2); Abemaciclib 5 uM (+2.3) |
| HALLMARK_ANGIOGENESIS | 29/36 | 0.09 | 0.61 | 0.54 | <= 0.005 | 66 (17%; all genes 0.5%) | Dinaciclib 0.5 uM (+6.9, ⚠ toxic, transcription drop, cell-cycle shift, explains ~10% of this change); Dinaciclib 5 uM (+5.9, ⚠ toxic, transcription drop, cell-cycle shift, explains ~9% of this change); Dinaciclib 0.05 uM (+4.7, ⚠ toxic, transcription drop, cell-cycle shift, explains ~7% of this change); Tucidinostat 5 uM (+3.5); Digitoxin 5 uM (+2.2, ⚠ toxic, transcription drop, cell-cycle shift, explains ~31% of this change); Idarubicin (hydrochloride) 5 uM (+2.2, cell-cycle shift, explains ~0% of this change); Tucidinostat 0.5 uM (+2.1, cell-cycle shift, explains ~0% of this change); Epirubicin (hydrochloride) 5 uM (+1.8, cell-cycle shift, explains ~4% of this change); Mitoxantrone (dihydrochloride) 5 uM (+1.2) |

**Reactome** (2024 sets with >= 5 genes in the space): median AUROC on cos 0.56, 673 sets (33%) at >= 0.6.

## 2. Opposite programmes: apart in the vector space, together on the nodal map

Pairs of programmes expected to move in opposite directions under the same drugs. In the signed vector space they should be anti-aligned (mean cross-set cosine < 0, most cross pairs negative); the nodal map is built on |cos|, so it should put them in the same module (on opposite arms) and close together, while the signed map keeps them apart. Map distances are centroid distances divided by the map's spread (sqrt(var x + var y)); mixing = how often a gene's 5 nearest map neighbours (among both sets) come from the other set, relative to chance (1 = as mixed as chance, 0 = never). t-SNE keeps neighbourhoods, not long distances, so 'apart on the signed map' is read from the mixing (at most 0.25); how far apart two separate islands land varies from machine to machine. 'AUROC anti' = P(cross pair cos < random pair cos).

| pair | genes a / b | mean cross cos | cross pairs < 0 | AUROC anti | cross pairs in same module | of those, opposite arms | nodal map: distance / mixing | signed map: distance / mixing |
|---|---|---|---|---|---|---|---|---|
| P53_TARGETS_UP / DREAM_G2M_DOWN | 42 / 30 | -0.15 | 89% | 0.77 | 0% (random 0.8%) | - | 2.15 / 0.03 | 2.06 / 0.02 |
| ISR_ATF4 / RIBOSOME_BIOGENESIS | 22 / 23 | -0.00 | 51% | 0.51 | 0% (random 0.8%) | - | 1.86 / 0.12 | 1.49 / 0.17 |

- P53_TARGETS_UP / DREAM_G2M_DOWN: the two sets move in opposite directions (mean cross-set cosine -0.15; 89% of the cross pairs are negative). 0% of the cross pairs share a module of the nodal map (two random genes: 0.8%). Neighbourhood mixing (1 = as mixed as chance, 0 = none): 0.03 on the nodal map vs 0.02 on the signed map; centroid distance 2.15 vs 2.06 map spreads - opposite in the vector space, but the nodal map does not bring them together.
- ISR_ATF4 / RIBOSOME_BIOGENESIS: NOT opposite in this data (mean cross-set cosine -0.00; 51% of cross pairs negative). 0% of the cross pairs share a module of the nodal map (two random genes: 0.8%). Neighbourhood mixing (1 = as mixed as chance, 0 = none): 0.12 on the nodal map vs 0.17 on the signed map; centroid distance 1.86 vs 1.49 map spreads - with no opposite relation in the data, the map test does not apply.

## 3. Drug check: do drugs with the same mechanism get similar vectors?

Cosine of drug vectors (each drug's best trustworthy dose) for pairs sharing moa_fine vs pairs with different moa_fine ('unclear' / 'unknown' left out; salt forms of one compound never paired). 33 of the drugs tested get the vector of a dose with an artifact flag (marked ⚠ in drug_moa.csv; embed/drugs.parquet alert says which), 5 of them because they have no trustworthy dose (every dose flagged unreliable plate only, position not correctable or wells disagree); they are tested like the others.

| drugs | n | classes | same-moa pairs | other pairs | mean cos same | mean cos other | AUROC |
|---|---|---|---|---|---|---|---|
| all drugs with a known moa_fine | 180 | 25 | 885 | 15214 | +0.08 | +0.01 | 0.55 |
| active drugs only (best dose >= 10 significant genes) | 149 | 25 | 577 | 10438 | +0.11 | +0.02 | 0.58 |

Mechanism classes with >= 2 drugs (best first; full table in drug_moa.csv):

| moa_fine | drugs | mean cos within | mean cos to others | AUROC |
|---|---|---|---|---|
| MEK inhibitor | Binimetinib, Cobimetinib, TAK-733, Trametinib ⚠, Trametinib (DMSO_TF solvate) | +0.51 | +0.01 | 0.79 |
| Glucocorticoid receptor agonist | Betamethasone dipropionate, Budesonide, Dexamethasone, Methylprednisolone succinate, Triamcinolone | +0.37 | -0.01 | 0.75 |
| Androgen receptor antagonist | Apalutamide, Bicalutamide, Darolutamide, Flutamide | +0.34 | +0.06 | 0.72 |
| Sonic inhibitor | Glasdegib ⚠, Sonidegib, Vismodegib | +0.17 | +0.04 | 0.70 |
| HDAC inhibitor | Belinostat ⚠, Carbamazepine, Panobinostat ⚠, Tucidinostat | +0.26 | +0.01 | 0.69 |
| GSK3 inhibitor | 9-ING-41, AZD2858 ⚠, CP21R7, LY2090314 | +0.16 | +0.05 | 0.62 |
| MTOR inhibitor | AZD-8055, Everolimus, LY-2584702 (tosylate salt) ⚠, Rapamycin, Sapanisertib, Temsirolimus, Torkinib ⚠ | +0.19 | +0.04 | 0.62 |
| DNA methyltransferase inhibitor | 5-Azacytidine, Decitabine, Procainamide (hydrochloride), γ-Oryzanol | +0.13 | +0.03 | 0.59 |
| Other MAPK inhibitor | BI-78D3, Bentamapimod, ERK5-IN-2, LJI308, MK-8353, NG25 ⚠, OTS514, PF-06260933, PH-797804, Ralimetinib dimesylate, Temuterkib | +0.09 | -0.00 | 0.59 |
| Proteasome inhibitor | Bortezomib ⚠, Ixazomib, Ixazomib citrate ⚠ | +0.29 | +0.02 | 0.58 |
| Multi-TK inhibitor | Cabozantinib (S-malate), Crizotinib (hydrochloride), Pexidartinib (hydrochloride), Ponatinib, Regorafenib, Sulfatinib, Sunitinib ⚠, Vandetanib, c-Kit-IN-1, crizotinib | +0.12 | +0.01 | 0.57 |
| DNA synthesis/repair inhibitor | 5-Fluorouracil, AZD-7648, Altretamine, Amsacrine, Bendamustine, Busulfan, Clofarabine, Cytarabine ⚠, Cytarabine (hydrochloride) ⚠, Doxorubicin (hydrochloride) ⚠, Epirubicin (hydrochloride) ⚠, Gemcitabine | +0.07 | +0.01 | 0.56 |

## 4. Modules and their labels

Each module and each of its arms was tested against every set (hypergeometric, universe = the 15,076 genes in the space, Benjamini-Hochberg over all tests; module_enrichment.csv). 96 of 235 modules carry a set label (q < 0.05, >= 3 genes shared; the most significant set of <= 300 genes when there is one); the others are named by their top genes. The 20 largest:

| module | genes | +/- | label | from (arm) | q | top + arm | top - arm |
|---|---|---|---|---|---|---|---|
| 1 | 298 | 246/52 | rRNA processing | reactome (+) | 9.4e-15 | MAK16, UTP15, LTV1, BYSL, COA7 | PHF1, MXD1, GNAS, FBXO33, PNPLA8 |
| 2 | 248 | 240/8 | genes: SBF1, ZDHHC8, KLHL17, MEIS2, PARP8 | top genes | - | SBF1, ZDHHC8, KLHL17, SH3GLB2, INTS11 | MEIS2, PARP8, FNDC3A, RBM7, CGAS |
| 3 | 246 | 172/74 | mRNA 3'-end processing | reactome (-) | 1.1e-08 | MPG, COMMD6, LIN7B, LCMT1, CIAO2B | HNRNPK, YWHAE, EWSR1, EIF4G2, SRSF1 |
| 4 | 245 | 183/62 | MYC targets v1 | hallmark (+) | 6.4e-11 | MRPS27, POLR1A, NAA15, TMEM33, CCT2 | RSRP1, AAMDC, TESK2, ZFYVE1, SIRT2 |
| 5 | 244 | 206/38 | MYC targets v2 | hallmark (+) | 1.1e-09 | WDR4, PUS1, TWNK, ALG8, MRTO4 | PJA2, MPC2, PPDPF, SKAP2, DDAH2 |
| 6 | 236 | 231/5 | E2F targets | hallmark (+) | 8.5e-66 | EXO1, WDR76, CDC45, MYBL2, DTL | ATP6V1G1, CPEB4, TMEM150A, RNF10, ARHGAP5 |
| 7 | 235 | 224/11 | Dengue Virus-Host Interactions | reactome (+) | 0.038 | CBLL1, SMG8, ZNF629, MOCS3, GTF3C4 | PTMA, SEPTIN2, AP3S1, ATP1B3, TMSB4X |
| 8 | 228 | 228/0 | Dectin-2 family | reactome (all) | 0.002 | SLC44A4, BCL2L15, POF1B, ST14, TRIM31 | - |
| 9 | 222 | 222/0 | Neuronal System | reactome (all) | 0.009 | CDH12, RALYL, CDH10, KCNH7, NCAM2 | - |
| 10 | 217 | 205/12 | genes: PCNX4-DT, TMEM202-AS1, LINC00240, L2HGDH, FAM118A | top genes | - | PCNX4-DT, TMEM202-AS1, LINC00240, DPH6-DT, MAD2L1-DT | L2HGDH, FAM118A, CCDC134, KLHL8, CLTCL1 |
| 11 | 217 | 183/34 | Mitochondrial translation elongation | reactome (+) | 0.033 | RPP38, MRFAP1L1, C1orf131, RPP25L, ARL14EP | TMED4, TECR, NUTF2, LAPTM4A, RCN2 |
| 12 | 215 | 195/20 | mRNA Splicing - Major Pathway | reactome (+) | 1.1e-06 | CCDC174, RBMX2, RP9, PHAX, C18orf21 | SMG1P3, BCAP31, PTDSS1, EIF4EBP2, MAPK9 |
| 13 | 213 | 213/0 | epithelial mesenchymal transition | hallmark (all) | 8.0e-19 | APCDD1L, INSYN2B, NAV1, SYNDIG1, ITGA11 | - |
| 14 | 212 | 212/0 | TNF-alpha signaling via NF-kB | hallmark (all) | 2.6e-36 | TNFAIP2, BCL3, CX3CL1, SLC2A6, NINJ1 | - |
| 15 | 210 | 190/20 | genes: ZNF460-AS1, ZNF213-AS1, SEC24B-AS1, ALAS1, LMCD1 | top genes | - | ZNF460-AS1, ZNF213-AS1, SEC24B-AS1, VPS13B-DT, SPESP1 | ALAS1, LMCD1, DHRS2, POLR2E, DPF1 |
| 16 | 206 | 181/25 | genes: ZNF268, CSTF2T, ZNF260, GNRH1, MFN1 | top genes | - | ZNF268, CSTF2T, ZNF260, RTL6, ZNF780A | GNRH1, MFN1, PIGN, SMG1P5, SRD5A1 |
| 17 | 202 | 171/31 | Intraflagellar transport | reactome (all) | 0.002 | MRPS31P4, BBS5, TRAPPC11, PRPF39, METTL14 | MIATNB, HCG18, DDX5, PDK1-AS1, ANKMY1 |
| 18 | 197 | 190/7 | Nucleotide biosynthesis | reactome (+) | 0.010 | ADCY3, UCK2, MDN1, ADAT2, LETM1 | TOX4, PDPK1, DYNLRB1, CFAP20, ATG12 |
| 19 | 196 | 196/0 | Neuronal System | reactome (all) | 2.1e-05 | LINC01035, COL4A6, GLP2R, LINC03000, NCKAP5-AS2 | - |
| 20 | 191 | 99/92 | Cap-dependent Translation Initiation | reactome (+) | 1.8e-08 | RPSA, TXNDC5, DHFR, HNRNPA3, RPN1 | CROCCP2-1, NKAP, ZNF503, ZMYM5, INAFM1 |

## 5. Novel gene relations

2,815 pairs (one row per pair) are reproduced in both halves of the compounds (fdr <= 0.05, |cos| >= 0.5) and have no shared HGNC gene group, no shared Hallmark / Reactome pathway and no STRING link, and are not the same locus or a read-through pair; 14 of them carry an alert (⚠: a gene of the pair is in the vector space only through drug-doses that carry an alert, so the relation may reflect what those drug-doses did to the cells). Top 25 by |cos| (novel_edges.csv has all):

| gene a (module arm) | gene b (module arm) | cos | cos half1 / half2 | fdr | names |
|---|---|---|---|---|---|
| SYT4 (9+) | ASCL1 (9+) | +0.97 | +0.98 / +0.93 | 6.5e-06 | synaptotagmin 4 / achaete-scute family bHLH transcription  |
| SRRM4 (9+) | RIT2 (9+) | +0.97 | +0.91 / +0.96 | 6.5e-06 | serine/arginine repetitive matrix 4 / Ras like without CAAX 2 |
| PDXDC1 (56+) | PDXDC2P (56+) | +0.96 | +0.95 / +0.95 | 6.5e-06 | pyridoxal dependent decarboxylase domain / pyridoxal dependent decarboxylase domain |
| HSP90AB3P (60+) | HSP90AB2P (60+) | +0.95 | +0.94 / +0.90 | 6.5e-06 | heat shock protein 90 alpha family class / heat shock protein 90 alpha family class |
| SRRM4 (9+) | LRFN2 (9+) | +0.95 | +0.91 / +0.92 | 6.5e-06 | serine/arginine repetitive matrix 4 / leucine rich repeat and fibronectin type |
| ASCL1 (9+) | SRRM4 (9+) | +0.95 | +0.89 / +0.93 | 6.5e-06 | achaete-scute family bHLH transcription  / serine/arginine repetitive matrix 4 |
| RIT2 (9+) | LRFN2 (9+) | +0.95 | +0.96 / +0.91 | 6.5e-06 | Ras like without CAAX 2 / leucine rich repeat and fibronectin type |
| FNDC7 (38+) | TRIM72 (38+) | +0.94 | +0.93 / +0.92 | 6.5e-06 | fibronectin type III domain containing 7 / tripartite motif containing 72 |
| SYT4 (9+) | LRFN2 (9+) | +0.94 | +0.96 / +0.86 | 6.5e-06 | synaptotagmin 4 / leucine rich repeat and fibronectin type |
| TYR (87+) | LHFPL3-AS1 (87+) | +0.94 | +0.95 / +0.82 | 6.5e-06 | tyrosinase / LHFPL3 antisense RNA 1 |
| ASCL1 (9+) | LRFN2 (9+) | +0.93 | +0.94 / +0.87 | 6.5e-06 | achaete-scute family bHLH transcription  / leucine rich repeat and fibronectin type |
| WDR76 (6+) | MYBL2 (6+) | +0.93 | +0.92 / +0.92 | 6.5e-06 | WD repeat domain 76 / MYB proto-oncogene like 2 |
| FANCB (6+) | BLM (6+) | +0.93 | +0.93 / +0.88 | 6.5e-06 | FA complementation group B / BLM RecQ like helicase |
| IFIT5 (32+) | DTX3L (32+) | +0.92 | +0.88 / +0.93 | 6.5e-06 | interferon induced protein with tetratri / deltex E3 ubiquitin ligase 3L |
| INCENP (22+) | ARHGAP11A (22+) | +0.92 | +0.89 / +0.93 | 6.5e-06 | inner centromere protein / Rho GTPase activating protein 11A |
| POLQ (6+) | CENPK (6+) | +0.92 | +0.91 / +0.92 | 6.5e-06 | DNA polymerase theta / centromere protein K |
| CENPK (6+) | FANCB (6+) | +0.92 | +0.93 / +0.89 | 6.5e-06 | centromere protein K / FA complementation group B |
| MCM10 (6+) | WDR76 (6+) | +0.91 | +0.92 / +0.89 | 6.5e-06 | minichromosome maintenance 10 replicatio / WD repeat domain 76 |
| CIT (67+) | PBK (67+) | +0.91 | +0.89 / +0.91 | 6.5e-06 | citron rho-interacting serine/threonine  / PDZ binding kinase |
| A2M (87+) | LHFPL3-AS1 (87+) | +0.91 | +0.89 / +0.90 | 6.5e-06 | alpha-2-macroglobulin / LHFPL3 antisense RNA 1 |
| WDR76 (6+) | FANCA (6+) | +0.91 | +0.91 / +0.89 | 6.5e-06 | WD repeat domain 76 / FA complementation group A |
| IFI35 (32+) | SLC15A3 (32+) | +0.91 | +0.81 / +0.92 | 6.5e-06 | interferon induced protein 35 / solute carrier family 15 member 3 |
| MCM10 (6+) | FAM111B (6+) | +0.91 | +0.88 / +0.94 | 6.5e-06 | minichromosome maintenance 10 replicatio / FAM111 trypsin like peptidase B |
| SLC15A3 (32+) | TRIM22 (32+) | +0.91 | +0.87 / +0.91 | 6.5e-06 | solute carrier family 15 member 3 / tripartite motif containing 22 |
| CHL1 (19+) | SCARA5 (19+) | +0.91 | +0.84 / +0.91 | 6.5e-06 | cell adhesion molecule L1 like / scavenger receptor class A member 5 |

## 6. Novel module members (guilt by association)

Genes on a module arm enriched for a set (q < 0.01; sets of <= 300 genes in the space, >= 3 of them on the arm) that the set does not list, with mean cosine >= 0.5 to the arm's listed members: 2,145 genes (7,884 gene-set rows in novel_members.csv, <= 5 most significant sets per gene); 43 of these genes carry an alert (⚠: in the vector space only through drug-doses that carry an alert). Top 25 genes, and 6 more without an alert that the 25 strongest pushed below the cut, each with the arm's most significant set that does not list it ('sets already listing the gene' = Hallmark / Reactome sets naming it at all; 0 = no pathway annotation):

| gene | name | module arm | set | listed members in arm | mean cos to them | half1 / half2 | sets already listing the gene |
|---|---|---|---|---|---|---|---|
| RPS10 | ribosomal protein S10 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.93 | 0.89 / 0.93 | 52 |
| RPS25 | ribosomal protein S25 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.93 | 0.87 / 0.94 | 51 |
| RPS13 ⚠ | ribosomal protein S13 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.93 | 0.88 / 0.94 | 51 |
| RPS21 | ribosomal protein S21 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.91 | 0.85 / 0.93 | 51 |
| RPS29 | ribosomal protein S29 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.91 | 0.86 / 0.93 | 51 |
| RPS16 ⚠ | ribosomal protein S16 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.91 | 0.86 / 0.92 | 51 |
| RPS11 | ribosomal protein S11 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.91 | 0.87 / 0.91 | 51 |
| RPS23 | ribosomal protein S23 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.91 | 0.85 / 0.93 | 53 |
| RPL32 | ribosomal protein L32 | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.91 | 0.86 / 0.91 | 37 |
| RPL28 | ribosomal protein L28 | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.90 | 0.85 / 0.91 | 37 |
| RPLP2 | ribosomal protein lateral stalk subunit P2 | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.90 | 0.84 / 0.91 | 37 |
| CMPK2 | cytidine/uridine monophosphate kinase 2 | 32+ | interferon | 23/139 | 0.89 | 0.84 / 0.91 | 3 |
| RPL36A | ribosomal protein L36a | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.89 | 0.84 / 0.90 | 37 |
| RPL38 | ribosomal protein L38 | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.89 | 0.83 / 0.90 | 37 |
| RPL7A | ribosomal protein L7a | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.88 | 0.80 / 0.90 | 37 |
| RPS8 | ribosomal protein S8 | 43+ | Ribosome Quality Control (RQC) complex extracts and degrades | 34/97 | 0.88 | 0.85 / 0.88 | 51 |
| RPL8 ⚠ | ribosomal protein L8 | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.88 | 0.81 / 0.89 | 39 |
| RPS15 ⚠ | ribosomal protein S15 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.88 | 0.81 / 0.89 | 51 |
| RPS17 ⚠ | ribosomal protein S17 | 43+ | Ribosome Quality Control (RQC) complex extracts and degrades | 34/97 | 0.87 | 0.82 / 0.88 | 51 |
| IFI35 | interferon induced protein 35 | 32+ | interferon | 23/139 | 0.87 | 0.80 / 0.89 | 5 |
| USP18 | ubiquitin specific peptidase 18 | 32+ | interferon | 23/139 | 0.87 | 0.82 / 0.88 | 32 |
| RPS14 | ribosomal protein S14 | 43+ | Ribosome Quality Control (RQC) complex extracts and degrades | 34/97 | 0.87 | 0.83 / 0.86 | 53 |
| RPS3 ⚠ | ribosomal protein S3 | 43+ | Ribosome Quality Control (RQC) complex extracts and degrades | 34/97 | 0.86 | 0.82 / 0.87 | 52 |
| RPS12 | ribosomal protein S12 | 43+ | Ribosome Quality Control (RQC) complex extracts and degrades | 34/97 | 0.86 | 0.80 / 0.87 | 52 |
| RPS24 | ribosomal protein S24 | 131+ | Ribosome Quality Control (RQC) complex extracts and degrades | 8/36 | 0.86 | 0.79 / 0.87 | 51 |
| RPL15 | ribosomal protein L15 | 131+ | SARS-CoV-2 modulates host translation machinery | 12/36 | 0.86 | 0.78 / 0.90 | 37 |
| PARP14 | poly(ADP-ribose) polymerase family member 14 | 32+ | interferon | 23/139 | 0.86 | 0.80 / 0.90 | 14 |
| HERC6 | HECT and RLD domain containing E3 ubiquitin p | 32+ | interferon | 23/139 | 0.85 | 0.82 / 0.87 | 5 |
| RPS27 | ribosomal protein S27 | 43+ | Ribosome Quality Control (RQC) complex extracts and degrades | 34/97 | 0.85 | 0.82 / 0.85 | 68 |
| IFI44 | interferon induced protein 44 | 32+ | Interferon alpha/beta signaling | 27/139 | 0.85 | 0.79 / 0.88 | 5 |
| EPSTI1 | epithelial stromal interaction 1 | 32+ | interferon | 23/139 | 0.85 | 0.75 / 0.88 | 6 |

## 8. Direction: which gene probably acts on which

From the direction stage (direction/; its README.md documents the columns; docs/direction.md explains the method): arrows SOURCE → TARGET from recorded mutations, natural knockouts (lines that do not express a gene), compounds that target a gene, and genes' natural levels across the lines, each with a p, a Benjamini-Hochberg q, a grade and its alerts. A probable direction, from the screen's cell lines - not proof of direct regulation. A → B → C looks like A → C, and another alteration carried by the same lines can be the real cause; there is one time point (~24 h), and drugs act on proteins, not on mRNA.

102,590 edges (98,577 rows once edges that are one test for several sources are merged): grade A 25, B 56,441, C 46,124; 102,590 with an alert (⚠). Grades: A: strong: a recorded mutation, at least 5 lines on each side compared within organs, significant over the whole table, no other recorded alteration concentrated on either side, and not resting on a correction (any alert it carries is a note to read); B: worth taking seriously - read its alerts: a mutation result with alerts (another alteration on either side, compared across organs, ...) or only 3-4 lines on a side, a natural knockout with at least 5 lines lacking the gene, or compounds that target the gene; C: a glimpse, a lead to check, not a finding: a gene's natural level, a result significant only within its own group, a comparison the tissue can explain (tissue-confounded), or a natural knockout with few lines.

**Positive controls** (known biology that has to come back):

- TP53 (TP53 loss of function (33 lines) vs not recorded (17)) -> p53 targets (response): 22 of the 39 p53 target genes present recovered with the right sign (2 with the wrong sign); median rank 50 of 16,352 genes. Recovered (rank among all genes, grade; ⚠ = the arrow carries an alert): FDXR (rank 1, A ⚠), BAX (rank 2, A ⚠), ACER2 (rank 3, A ⚠), ZMAT3 (rank 4, A ⚠), DDB2 (rank 7, A ⚠), RRM2B (rank 10, A ⚠), CDKN1A (rank 11, A ⚠), SESN1 (rank 15, A ⚠), TRIAP1 (rank 17, A ⚠), ZNF79 (rank 22, B ⚠), PHLDA3 (rank 23, B ⚠), GDF15 (rank 25, B ⚠), MDM2 (rank 28, C ⚠), FAS (rank 32, C ⚠), TP53I3 (rank 37, C ⚠), RPS27L (rank 40, C ⚠), BBC3 (rank 50, C ⚠), ASCC3 (rank 52, C ⚠), BTG2 (rank 54, C ⚠), AEN (rank 69, C ⚠), TIGAR (rank 86, C ⚠), XPC (rank 95, C ⚠). Not recovered (rank): EDA2R (12), CCNG1 (18), POLH (27), SPATA18 (70), PPM1D (147), PLK3 (156), DRAM1 (158), TP53INP1 (163), GADD45A (171), TNFRSF10D (641), TNFRSF10B (929), SUSD6 (2002), SERPINB5 (2671), KITLG (8120), APAF1 (11512), and 2 more.
- TP53 (TP53 loss of function (33 lines) vs not recorded (17)) -> cells under DNA-damaging drugs (sensitivity): 0 edges among 42 DNA-damaging drug-doses, 0 with the expected sign (sign -1: TP53 activity makes the cells more sensitive)
- KEAP1 -> NRF2 targets (baseline): not assessable (KEAP1 is not recorded as altered in >= 3 lines)

**Edges per kind against the controls.** 'Expected false' = the edges a table without any real effect would hold: random pseudo-genotype groups (line sets drawn at random, tested exactly like the recorded groups, counted at the real table's cut) and, for the level kinds, the same tests with every gene's level permuted over its lines.

| evidence | edges | A / B / C | expected false | control |
|---|---|---|---|---|
| recorded mutation -> a gene's drug response (over the whole table) | 43 | 17/13/13 | 12.80 (up to 20.74) | random pseudo-genotype groups |
| recorded mutation -> a gene's drug response (within its group only) | 93 | 0/0/93 | 4.27 (up to 9.76) | random pseudo-genotype groups |
| recorded mutation -> a gene's baseline level (over the whole table) | 10 | 8/2/0 | 0.00 (up to 3.20) | random pseudo-genotype groups |
| recorded mutation -> a gene's baseline level (within its group only) | 9 | 0/0/9 | 13.87 (up to 22.05) | random pseudo-genotype groups |
| recorded mutation -> cells under a drug-dose (over the whole table) | 0 | 0/0/0 | 0.00 (up to 3.20) | random pseudo-genotype groups |
| recorded mutation -> cells under a drug-dose (within its group only) | 1 | 0/0/1 | 1.07 (up to 5.06) | random pseudo-genotype groups |
| not expressed (natural knockout) -> a partner's drug response | 2176 | 0/2026/150 | - | no random control (each edge's alerts say what to doubt) |
| not expressed (natural knockout) -> a partner's baseline level | 80506 | 0/38332/42174 | - | no random control (each edge's alerts say what to doubt) |
| not expressed (natural knockout) -> cells under a drug-dose | 6005 | 0/4194/1811 | - | no random control (each edge's alerts say what to doubt) |
| compounds that target a gene -> a gene's level | 11874 | 0/11874/0 | - | no random control (each edge's alerts say what to doubt) |
| natural level -> a partner's drug response (over the whole table) | 1359 | 0/0/1359 | 102.00 (up to 120.24) | the same tests with every level permuted |
| natural level -> cells under a drug-dose (over the whole table) | 0 | 0/0/0 | 0.00 (up to 3.00) | the same tests with every level permuted |
| natural level -> cells under a drug-dose (within its drug-dose only) | 514 | 0/0/514 | 37.00 (up to 48.68) | the same tests with every level permuted |

'Up to' is the 95% upper bound of that estimate: the controls are a small sample (no false arrow from 60 random groups still allows about 3 per 60 groups), and the natural-level controls are one shuffle each. The estimate can be low when the real groups overlap other alterations, tissue programmes or each other, which random groups do not.

⚠ The controls expect at least half of these edges to be false: recorded mutation -> a gene's baseline level (within its group only) (9 edges, 13.87 expected false); recorded mutation -> cells under a drug-dose (within its group only) (1 edge, 1.07 expected false). Read them as leads.

Random pseudo-groups (60 groups): edges per group over the whole table, pseudo vs real: response 0.2 vs 0.6719; baseline 0.0 vs 0.1719; sensitivity 0.0 vs 0.0.

## Caveats

- Correlation is not mechanism: two genes with a high cosine respond alike to these drugs in these lines; that may be co-regulation, a shared upstream stress, or a shared cell-state change.
- One time point (24 h): early and late responses are not separated; direct and indirect targets look the same.
- Cancer cell lines only (50 lines): relations driven by mutated pathways or lost checkpoints (e.g. TP53) may not hold in normal cells, and tissue-specific programmes are under-represented.
- Relations strong in only one of the two random halves of the compounds ('one half' in relations; the halves are a hash split of compound names) are not replicated and carry no error estimate; they are never called novel here.
- Neighbouring genes (same locus, <= 50 kb) and read-through pairs (the 5' gene's transcription running into the 3' gene) correlate without regulation: they are excluded from 'novel'.
- 'Not known' means no shared HGNC gene group, Hallmark / Reactome pathway or STRING link (score >= 400) in the cached reference files; the literature may still describe the relation.
- Gene-set AUROCs are against random gene pairs of the space; sets of genes that respond rarely in Tahoe-100M (few genes in the space) are weak tests, whatever their biology.
- Nothing is left out of a list for a flag: an item with a reason for doubt keeps its ranked place and carries ⚠ with the reason. Genes in the vector space only through drug-doses that carry an alert (79 genes; embed/genes.parquet evidence_flagged_only) are part of every test. Only the fit of the vector space leaves out the technically untrustworthy drug-doses (unreliable plate only, position not correctable, wells disagree; embed/info.json lists them).

## Files

control_sets.csv (every tested set), opposite_pairs.csv, module_enrichment.csv, module_labels.csv, drug_moa.csv, novel_edges.csv, novel_members.csv, metrics.json; README.md documents the columns.
