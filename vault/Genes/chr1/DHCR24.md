---
symbol: "DHCR24"
type: "gene"
col: 3765
ensembl_id: "ENSG00000116133"
name: "24-dehydrocholesterol reductase"
location: "1p32.3"
module: 86
arm: "+"
pooled_cpm: 30.44
n_lines_expressing: 46
n_dd_up: 37
n_dd_down: 21
n_dd_up_clean: 27
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# DHCR24

*24-dehydrocholesterol reductase* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.18× (z +14.3, q 6e-44, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.490× (z -13.2, q 4e-37, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHCR7]] (+0.80, fdr 7e-06), [[FASN]] (+0.70, fdr 7e-06), [[PCSK9]] (+0.69, fdr 7e-06); moves opposite to [[ZKSCAN1]] (-0.54, fdr 2e-05), [[CCDC174]] (-0.54, fdr 1e-05), [[APLF]] (-0.54, fdr 5e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SORT1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DPY19L1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.18×** | +14.3 | 6e-44 | 41/44 (NCI-H23, HS-578T, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.85×** | +13.1 | 5e-37 | 29/30 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.97×** | +12.5 | 1e-33 | 39/44 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.50×** | +12.0 | 7e-31 | 36/40 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.38×** | +11.3 | 1e-27 | 39/44 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.36×** | +11.2 | 3e-27 | 38/44 (LOX-IMVI, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.18×** | +10.2 | 2e-22 | 39/44 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.13×** | +9.1 | 5e-18 | 27/36 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.79×** | +7.3 | 1e-11 | 29/42 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.74×** | +7.2 | 3e-11 | 30/44 (HS-578T, C-33 A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +6.9 | 2e-10 | 32/44 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +6.2 | 2e-08 | 30/43 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | **1.62×** | +6.1 | 6e-08 | 30/44 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.62×** | +6.0 | 6e-08 | 26/44 (HOP62, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +5.9 | 1e-07 | 29/40 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.07×** | +5.0 | 2e-05 | 26/44 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.9 | 3e-05 | 23/44 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +4.9 | 3e-05 | 22/44 (HOP62, HS-578T, …) | rises with dose | plate-row cell shift |
| [[Berbamine (drug)]] 0.5 µM |  | **1.43×** | +4.6 | 1e-04 | 21/44 (LS 180, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.39×** | +4.2 | 9e-04 | 22/44 (HOP62, HS-578T, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.003 | 15/44 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 20/44 (HEC-1-A, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.004 | 14/44 (HepG2/C3A, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.490×** | -13.2 | 4e-37 | 36/44 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.373×** | -12.9 | 9e-36 | 39/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.573×** | -7.3 | 5e-11 | 33/44 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.677×** | -7.3 | 6e-11 | 33/44 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.598×** | -6.8 | 2e-09 | 32/44 (NCI-H2030, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -6.3 | 3e-08 | 29/44 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.639×** | -5.7 | 1e-06 | 27/44 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.668×** | -5.3 | 8e-06 | 25/44 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.712×** | -4.5 | 5e-04 | 20/44 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.728×** | -4.2 | 0.002 | 20/44 (PANC-1, J82, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.721×** | -4.1 | 0.002 | 24/44 (J82, KATO III, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.736×** | -4.0 | 0.003 | 20/43 (hTERT-HPNE, H4, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.820×** | -3.7 | 0.009 | 18/44 (A498, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.752×** | -3.5 | 0.016 | 18/44 (AN3 CA, CFPAC-1, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **0.605×** | -3.4 | 0.021 | 15/43 (SHP-77, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.609×** | -3.4 | 0.023 | 12/44 (HS-578T, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | 0.840× | -3.3 | 0.036 | 11/44 (HS-578T, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 29.7 | 9 | 2 | [[Clobetasol propionate (drug)]] 0.5 µM 4.53× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -10.6) |
| [[A498 (line)]] | wt | 72.4 | 3 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 2.66× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -13.8) |
| [[A-427 (line)]] | wt | 40.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.7) |
| [[HS-578T (line)]] | alt | 30.1 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.12× (z +11.5) | — |
| [[J82 (line)]] | alt | 49.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.9) |
| [[BT-474 (line)]] | alt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -20.5) |
| [[HT-29 (line)]] | alt | 62.4 | 1 | 2 | [[Cepharanthine (drug)]] 5 µM 2.17× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.3) |
| [[KATO III (line)]] | alt | 57.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 11.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 8.13× (z +9.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 33.8 | 1 | 2 | [[Cepharanthine (drug)]] 5 µM 2.23× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.8) |
| [[SNU-423 (line)]] | alt | 18.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.1× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 16.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.57× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 20.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.17× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.56× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 9.81 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 6.30× (z +11.4) | — |
| [[LoVo (line)]] | wt | 15.0 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.60× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.33× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 84.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.1) |
| [[SW480 (line)]] | alt | 26.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.5) |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.111× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -8.6) |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.4) |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.228× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -10.0) |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.9) |
| [[A549 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHCR7]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 996 |
| [[FASN]] | +0.70 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 635 |
| [[PCSK9]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[MSMO1]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 987 |
| [[HMGCR]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 829 |
| [[FDFT1]] | +0.67 | +0.71 / +0.57 | both halves | 8e-06 | pathway: Cholesterol biosynthesis; STRING 831 |
| [[ACSL3]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[FADS2]] | +0.65 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[ACACA]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 459 |
| [[FADS1]] | +0.63 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[ERG28]] | +0.61 | +0.67 / +0.46 | both halves | 3e-05 | STRING 594 |
| [[ELOVL5]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN1]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[CCDC174]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[APLF]] | -0.54 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[GATAD1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ZNF397]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZNF721]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[ZC3H6]] | -0.51 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[ARL14EP]] | -0.51 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[CCDC90B]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[BET1]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ATE1OSP]] | -0.51 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[TCEAL4]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORT1]] | B | SORT1 activity raises DHCR24's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without SORT1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L1]] | C | DHCR24 activity lowers DPY19L1's level | lines that do not express DHCR24 (4) vs lines expressing it (46) | 1.25× higher at baseline in the lines without DHCR24 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.6, -50.0); signed map (-51.8, 32.2). **Vector** length 138, 43.8% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol homeostasis* (hallmark, mean cos +0.56 to 24); *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.56 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.57 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +8.5 | +14.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +7.1 | +12.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +7.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +5.9 | +12.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.9 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.5 | -12.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.7 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -13.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | 24-dehydrocholesterol reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,849,627-54,887,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0018, seladin-1; previously DCE |
| Gene groups (HGNC) | Flavoproteins; AEBS complex subunits; Dehydrocholesterol reductases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ANDROGEN_RESPONSE, FATTY_ACID_METABOLISM, MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: Cholesterol biosynthesis from zymosterol (modified Kandutsch-Russell pathway); Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15392](https://www.uniprot.org/uniprotkb/Q15392) (Delta(24)-sterol reductase):

> Catalyzes the reduction of the delta-24 double bond of sterol intermediates during cholesterol biosynthesis. In addition to its cholesterol-synthesizing activity, can protect cells from oxidative stress by reducing caspase 3 activity during apoptosis induced by oxidative stress. Also protects against amyloid-beta peptide-induced apoptosis.

**Summary**, from NCBI Gene [1718](https://www.ncbi.nlm.nih.gov/gene/1718):

> This gene encodes a flavin adenine dinucleotide (FAD)-dependent oxidoreductase which catalyzes the reduction of the delta-24 double bond of sterol intermediates during cholesterol biosynthesis. The protein contains a leader sequence that directs it to the endoplasmic reticulum membrane. Missense mutations in this gene have been associated with desmosterolosis. Also, reduced expression of the gene occurs in the temporal cortex of Alzheimer disease patients and overexpression has been observed in …

**Accessions** — [HGNC:2859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2859) · Entrez [1718](https://www.ncbi.nlm.nih.gov/gene/1718) · UniProt [Q15392](https://www.uniprot.org/uniprotkb/Q15392) · Ensembl [ENSG00000116133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116133)

## Data

Gene col 3765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3765); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3765]; `tensor/DDL_lfc|DDL_z.npy` [3765]; `embed/gene_vectors.npy` [3765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3765 or target_col == 3765). Every well: [[DHCR24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHCR24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
