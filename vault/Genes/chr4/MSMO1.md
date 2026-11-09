---
symbol: "MSMO1"
type: "gene"
col: 588
ensembl_id: "ENSG00000052802"
name: "methylsterol monooxygenase 1"
location: "4q32.3"
module: 86
arm: "+"
pooled_cpm: 62.07
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 35
n_dd_up_clean: 28
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# MSMO1

*methylsterol monooxygenase 1* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 3.60× (z +19.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.295× (z -18.6, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCR]] (+0.93, fdr 7e-06), [[FDFT1]] (+0.90, fdr 7e-06), [[FDPS]] (+0.86, fdr 7e-06); moves opposite to [[ZC3H7B]] (-0.53, fdr 1e-05), [[ZNF518A]] (-0.51, fdr 2e-05), [[ERCC6L2]] (-0.51, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PCSK9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **3.60×** | +19.4 | 0e+00 | 45/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **3.39×** | +18.5 | 0e+00 | 45/47 (HOP62, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.51×** | +13.0 | 3e-36 | 45/46 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.95×** | +9.0 | 4e-17 | 44/48 (COLO 205, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +7.6 | 5e-12 | 41/47 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.11×** | +6.4 | 2e-08 | 28/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **1.48×** | +6.0 | 2e-07 | 37/47 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +5.8 | 5e-07 | 32/47 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +5.7 | 6e-07 | 31/47 (HOP62, A498, …) | top dose only | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.73×** | +5.7 | 8e-07 | 36/48 (A498, HOP62, …) | rises with dose | plate-row cell shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.74×** | +5.7 | 8e-07 | 32/42 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | **1.71×** | +5.5 | 2e-06 | 33/47 (A498, HOP62, …) | rises with dose | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +5.5 | 2e-06 | 32/47 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.67×** | +5.3 | 5e-06 | 30/47 (HOP62, SNU-423, …) | top dose only |  |
| [[Berbamine (drug)]] 0.5 µM |  | **1.62×** | +5.2 | 7e-06 | 30/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.62×** | +5.2 | 9e-06 | 30/47 (A498, HOP62, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.61×** | +5.1 | 1e-05 | 30/47 (A498, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 4 with an alert ⚠; shown: the 15 strongest. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.295×** | -18.6 | 0e+00 | 43/47 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.277×** | -13.3 | 8e-38 | 47/47 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.338×** | -11.7 | 4e-29 | 39/47 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.360×** | -11.0 | 7e-26 | 44/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.393×** | -10.0 | 1e-21 | 44/47 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.540×** | -6.6 | 3e-09 | 36/46 (RKO, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.551×** | -5.9 | 2e-07 | 32/46 (RKO, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Quinestrol (drug)]] 5 µM |  | **0.694×** | -5.6 | 2e-06 | 33/48 (KATO III, RKO, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.610×** | -5.3 | 6e-06 | 34/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.629×** | -4.8 | 9e-05 | 27/47 (HCT15, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.664×** | -4.4 | 5e-04 | 30/47 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -4.3 | 7e-04 | 28/47 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.676×** | -4.2 | 0.001 | 28/46 (COLO 205, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.002 | 22/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.684×** | -3.9 | 0.004 | 26/47 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 110 | 2 | 7 | [[Berbamine (drug)]] 5 µM 3.06× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.3) |
| [[BT-474 (line)]] | alt | 203 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 121 | 3 | 5 | [[Berbamine (drug)]] 5 µM 2.72× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.3) |
| [[HS-578T (line)]] | alt | 66.1 | 2 | 5 | [[Cepharanthine (drug)]] 5 µM 4.71× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 163 | 2 | 5 | [[Berbamine (drug)]] 5 µM 2.28× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.6) |
| [[PANC-1 (line)]] | alt | 68.7 | 2 | 5 | [[Berbamine (drug)]] 5 µM 2.42× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.3) |
| [[RKO (line)]] | wt | 107 | 1 | 6 | [[TAK-901 (drug)]] 5 µM 9.57× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.0625× (z -28.3) |
| [[HCT15 (line)]] | alt | 121 | 2 | 4 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.40× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.6) |
| [[LS 180 (line)]] | wt | 75.5 | 4 (1 ⚠) | 2 | [[Berbamine (drug)]] 5 µM 5.27× (z +15.4) | [[Harringtonine (drug)]] 5 µM 0.169× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 89.2 | 1 (1 ⚠) | 5 | [[Niclosamide (olamine) (drug)]] 5 µM 5.42× (z +10.3) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.0735× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 43.2 | 1 | 5 | [[Berbamine (drug)]] 5 µM 2.75× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.5) |
| [[A-427 (line)]] | wt | 40.1 | 1 (1 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 4.43× (z +10.2) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -14.8) |
| [[A498 (line)]] | wt | 60.3 | 2 | 3 | [[Berbamine (drug)]] 5 µM 4.40× (z +15.9) | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.6) |
| [[LoVo (line)]] | wt | 53.0 | 4 (1 ⚠) | 1 | [[Berbamine (drug)]] 5 µM 7.43× (z +20.0) | [[Harringtonine (drug)]] 0.5 µM 0.293× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 2 | 3 | [[Berbamine (drug)]] 5 µM 4.78× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.135× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 110 | 2 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 5.92× (z +9.7) ⚠ toxic · without an alert: [[Berbamine (drug)]] 5 µM 3.17× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.8) |
| [[A-172 (line)]] | wt | 22.7 | 3 (1 ⚠) | 1 | [[Berbamine (drug)]] 5 µM 2.74× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -8.8) |
| [[COLO 205 (line)]] | alt | 64.9 | 4 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.73× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 43.3 | 3 (1 ⚠) | 1 | [[Cepharanthine (drug)]] 5 µM 7.78× (z +19.1) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.8) |
| [[Hs 766T (line)]] | wt | 40.3 | 2 | 2 | [[Berbamine (drug)]] 5 µM 3.56× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.3) |
| [[HT-29 (line)]] | alt | 67.1 | 2 | 2 | [[Berbamine (drug)]] 5 µM 4.40× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 2 | 2 | [[Cepharanthine (drug)]] 5 µM 5.10× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.0) |
| [[J82 (line)]] | alt | 50.6 | 3 (1 ⚠) | 1 | [[Cepharanthine (drug)]] 5 µM 3.26× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.0) |
| [[SNU-1 (line)]] | wt | 70.1 | 3 | 1 | [[Cepharanthine (drug)]] 5 µM 5.01× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 64.7 | 2 | 1 | [[Berbamine (drug)]] 5 µM 5.00× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.7) |
| [[C-33 A (line)]] | alt | 45.0 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 6.06× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 63.2 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.62× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 34.1 | 2 | 1 | [[Berbamine (drug)]] 5 µM 2.97× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 67.1 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 4.34× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 29.5 | 2 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.96× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 34.4 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.54× (z +11.8) ⚠ toxic · without an alert: [[Berbamine (drug)]] 5 µM 3.87× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.02× (z +10.1) ⚠ toxic · without an alert: [[Berbamine (drug)]] 5 µM 3.34× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 35.2 | 2 | 1 | [[Berbamine (drug)]] 5 µM 4.95× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.3) |
| [[A549 (line)]] | wt | 20.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 7.71× (z +16.5) | — |
| [[C32 (line)]] | wt | 47.7 | 2 | 0 | [[Berbamine (drug)]] 5 µM 6.17× (z +9.8) | — |
| [[H4 (line)]] | wt | 33.8 | 2 | 0 | [[Berbamine (drug)]] 5 µM 5.84× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 72.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.0) |
| [[SHP-77 (line)]] | alt | 66.6 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 11.6× (z +13.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.5) |
| [[SNU-423 (line)]] | alt | 28.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 6.12× (z +14.6) | — |
| [[SW48 (line)]] | wt | 76.1 | 1 | 1 | [[Berbamine (drug)]] 5 µM 2.96× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.198× (z -8.6) |
| [[SW480 (line)]] | alt | 32.6 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.65× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCR]] | +0.93 | +0.91 / +0.90 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 902 |
| [[FDFT1]] | +0.90 | +0.90 / +0.86 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 991 |
| [[FDPS]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 787 |
| [[DHCR7]] | +0.84 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 925 |
| [[MVD]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 752 |
| [[SCD]] | +0.80 | +0.82 / +0.80 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 613 |
| [[CYP51A1]] | +0.80 | +0.85 / +0.77 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 996 |
| [[ERG28]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 | STRING 994 |
| [[SQLE]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 992 |
| [[ACSS2]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | STRING 421 |
| [[HMGCS1]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 964 |
| [[HSD17B7P2]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.51 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD18A]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.49 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[MAPK1IP1L]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.48 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ITPA]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ZC3HC1]] | -0.48 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[FNTA]] | -0.47 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[LARP7]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RPL7L1]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK9]] | B | PCSK9 activity raises MSMO1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without PCSK9 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[MTOR]] | B | MTOR activity raises MSMO1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 7.8% of all compounds | 0.062 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ELOVL5]] | B | ELOVL5 activity lowers MSMO1's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 1.91× higher at baseline in the lines without ELOVL5 | 0.072 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |
| [[IDI1]] | C | IDI1's natural level strengthens MSMO1's drug response | IDI1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.44; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.905). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -49.2); signed map (-52.9, 32.4). **Vector** length 164, 59.4% of its response variance represented; |z| ≥ 3 in 1,758 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol homeostasis* (hallmark, mean cos +0.72 to 24); *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.73 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.73 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +12.7 | +18.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +11.0 | +19.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.9 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +7.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +6.3 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.1 | +2.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +5.8 | +5.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -13.3 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -13.0 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.9 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.4 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -9.2 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.8 | -6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.6 | -5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -4.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.3 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | methylsterol monooxygenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:165,327,667-165,343,164 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DESP4, ERG25; previously SC4MOL |
| Gene groups (HGNC) | Fatty acid hydroxylase domain containing |
| Reactome | 5 pathways, smallest: Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15800](https://www.uniprot.org/uniprotkb/Q15800) (Methylsterol monooxygenase 1):

> Catalyzes the three-step monooxygenation required for the demethylation of 4,4-dimethyl and 4alpha-methylsterols, which can be subsequently metabolized to cholesterol. Also involved in drug metabolism, as it can metabolize eldecalcitol (ED-71 or 1alpha,25-dihydroxy-2beta-(3-hydroxypropoxy)-cholecalciferol), a second-generation vitamin D analog, into 1alpha,2beta,25-trihydroxy vitamin D3; this reaction occurs via enzymatic hydroxylation and spontaneous O-dehydroxypropylation.

**Summary**, from NCBI Gene [6307](https://www.ncbi.nlm.nih.gov/gene/6307):

> Sterol-C4-mehtyl oxidase-like protein was isolated based on its similarity to the yeast ERG25 protein. It contains a set of putative metal binding motifs with similarity to that seen in a family of membrane desaturases-hydroxylases. The protein is localized to the endoplasmic reticulum membrane and is believed to function in cholesterol biosynthesis. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10545) · Entrez [6307](https://www.ncbi.nlm.nih.gov/gene/6307) · UniProt [Q15800](https://www.uniprot.org/uniprotkb/Q15800) · Ensembl [ENSG00000052802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052802)

## Data

Gene col 588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 588); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 588]; `tensor/DDL_lfc|DDL_z.npy` [588]; `embed/gene_vectors.npy` [588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 588 or target_col == 588). Every well: [[MSMO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSMO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
