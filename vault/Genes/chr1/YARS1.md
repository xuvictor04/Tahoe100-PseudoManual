---
symbol: "YARS1"
type: "gene"
col: 5587
ensembl_id: "ENSG00000134684"
name: "tyrosyl-tRNA synthetase 1"
location: "1p35.1"
module: 133
arm: "+"
pooled_cpm: 120.38
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 11
n_dd_up_clean: 34
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# YARS1

*tyrosyl-tRNA synthetase 1* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.85× (z +13.3, q 2e-37, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 1.54× (z +13.1, q 6e-37, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.824× (z -5.9, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AARS1]] (+0.88, fdr 7e-06), [[MARS1]] (+0.88, fdr 7e-06), [[IARS1]] (+0.87, fdr 7e-06).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +13.3 | 2e-37 | 45/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM |  | **1.54×** | +13.1 | 6e-37 | 43/48 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.76×** | +12.2 | 7e-32 | 44/48 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +10.6 | 3e-24 | 31/49 (HS-578T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +10.6 | 5e-24 | 34/44 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.41×** | +10.5 | 8e-24 | 36/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +9.7 | 2e-20 | 38/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +9.7 | 2e-20 | 42/47 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.52×** | +9.1 | 9e-18 | 43/48 (C32, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +8.1 | 2e-14 | 35/48 (HOP62, C-33 A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.08×** | +7.7 | 5e-13 | 44/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.43×** | +7.7 | 5e-13 | 38/48 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.28×** | +7.5 | 2e-12 | 34/49 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.99×** | +7.3 | 2e-11 | 42/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +7.1 | 3e-11 | 32/49 (Hs 766T, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.39×** | +7.1 | 4e-11 | 32/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +6.9 | 2e-10 | 32/49 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 1e-09 | 35/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.82×** | +6.3 | 7e-09 | 39/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -5.9 | 2e-06 | 25/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -5.1 | 1e-04 | 23/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.779×** | -5.0 | 1e-04 | 23/47 (LoVo, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.854× | -4.8 | 2e-04 | 20/48 (J82, LS 180, …) | top dose only | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.810×** | -4.5 | 6e-04 | 25/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.811×** | -4.5 | 6e-04 | 22/48 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.815×** | -4.4 | 9e-04 | 23/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.816×** | -4.4 | 1e-03 | 24/48 (RKO, KATO III, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.819×** | -4.3 | 0.001 | 26/49 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.879× | -3.9 | 0.005 | 10/48 (KATO III, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.836× | -3.8 | 0.007 | 20/49 (SW480, HT-29, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.845× | -3.4 | 0.030 | 14/48 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.030 | 13/48 (HS-578T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.729×** | -3.3 | 0.033 | 16/49 (HS-578T, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.033 | 10/47 (HS-578T, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.860× | -3.2 | 0.044 | 16/48 (RKO, SW48, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.818×** | -3.1 | 0.068 | 15/48 (HS-578T, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 249 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -27.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -20.7) |
| [[LoVo (line)]] | wt | 166 | 1 | 7 (3 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 1.88× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -13.7) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.414× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 87.0 | 7 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.03× (z +12.1) ⚠ unreliable plate only · without an alert: [[Neratinib (maleate) (drug)]] 5 µM 2.03× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 143 | 6 (3 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.30× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 220 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -15.4) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.455× (z -11.9) |
| [[KATO III (line)]] | alt | 172 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.424× (z -11.1) |
| [[A-427 (line)]] | wt | 140 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.380× (z -11.5) |
| [[A498 (line)]] | wt | 112 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.85× (z +8.8) | — |
| [[C32 (line)]] | wt | 61.4 | 4 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.68× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 4 (3 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.26× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 89.9 | 4 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.28× (z +9.5) ⚠ unreliable plate only · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.71× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 108 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.46× (z +12.0) ⚠ toxic | — |
| [[HEC-1-A (line)]] | alt | 92.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 2.14× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 165 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.6) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.478× (z -9.6) |
| [[SW480 (line)]] | alt | 164 | 2 (1 ⚠) | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.63× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -11.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A549 (line)]] | wt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 58.5 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.69× (z +9.6) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 1.81× (z +8.5) | — |
| [[J82 (line)]] | alt | 106 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.02× (z +9.0) ⚠ unreliable plate only | [[Selinexor (drug)]] 5 µM 0.582× (z -9.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H1573 (line)]] | alt | 69.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 124 | 2 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.26× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 150 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -13.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[Panc 03.27 (line)]] | alt | 47.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +9.2) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[RKO (line)]] | wt | 210 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.74× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.603× (z -8.6) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SNU-1 (line)]] | wt | 171 | 2 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.29× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 94.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.4) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[SW48 (line)]] | wt | 209 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.96× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.9) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 68.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.4) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[AsPC-1 (line)]] | alt | 54.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.24× (z +9.2) ⚠ unreliable plate only | — |
| [[C-33 A (line)]] | alt | 105 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 2.60× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 162 | 1 | 0 | [[Artesunate (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 76.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 82.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +9.3) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +10.5) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 80.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.113× (z -8.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AARS1]] | +0.88 | +0.84 / +0.92 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 996 |
| [[MARS1]] | +0.88 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 999 |
| [[IARS1]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 966 |
| [[PSAT1]] | +0.85 | +0.84 / +0.85 | both halves | 7e-06 | STRING 498 |
| [[TARS1]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 911 |
| [[PCK2]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[NARS1]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 966 |
| [[XPOT]] | +0.81 | +0.74 / +0.87 | both halves | 7e-06 | STRING 745 |
| [[CARS1]] | +0.81 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 898 |
| [[ASNS]] | +0.81 | +0.82 / +0.83 | both halves | 7e-06 | STRING 665 |
| [[PHGDH]] | +0.79 | +0.80 / +0.81 | both halves | 7e-06 | STRING 500 |
| [[SLC6A9]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises YARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without ASNSP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ANK2]] | B | ANK2 activity raises YARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without ANK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[ULBP1]] | B | ULBP1 activity raises YARS1's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ULBP1 | 0.054 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ASNSP1]] | B | ASNSP1 activity weakens YARS1's drug response | lines that do not express ASNSP1 (35) vs lines expressing it (14) | the lines without ASNSP1 respond 1.63× as strongly (z diff -1.33); strongest at Dinaciclib 0.5 µM: 1.66x vs 1.30x (z diff -2.2) | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; target measured in part of the lines; artifact flags |
| [[PSAT1]] | B | PSAT1 activity raises YARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without PSAT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[CHAC1]] | B | CHAC1 activity raises YARS1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without CHAC1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.859). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.8, 47.3); signed map (-13.5, 23.6). **Vector** length 156, 56.1% of its response variance represented; |z| ≥ 3 in 1,656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +13.2 | +13.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +10.6 | +13.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +9.3 | +10.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +9.0 | +7.7 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.7 | +12.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.4 | +8.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +7.9 | +7.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +7.9 | +9.1 |
| fall | [[Harringtonine (drug)]] 0.05 µM |  | -6.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -4.1 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | tyrosyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,775,237-32,818,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YTS, YRS, tyrRS; previously YARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P54577](https://www.uniprot.org/uniprotkb/P54577) (Tyrosine--tRNA ligase, cytoplasmic):

> Tyrosine--tRNA ligase that catalyzes the attachment of tyrosine to tRNA(Tyr) in a two-step reaction: tyrosine is first activated by ATP to form Tyr-AMP and then transferred to the acceptor end of tRNA(Tyr) (Probable). Also acts as a positive regulator of poly-ADP-ribosylation in the nucleus, independently of its tyrosine--tRNA ligase activity. Activity is switched upon resveratrol-binding: resveratrol strongly inhibits the tyrosine--tRNA ligase activity and promotes relocalization to the …

**Summary**, from NCBI Gene [8565](https://www.ncbi.nlm.nih.gov/gene/8565):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observed for the human tyrosyl-tRNA synthetase, after it is split into two parts, an N-terminal fragment …

**Accessions** — [HGNC:12840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12840) · Entrez [8565](https://www.ncbi.nlm.nih.gov/gene/8565) · UniProt [P54577](https://www.uniprot.org/uniprotkb/P54577) · Ensembl [ENSG00000134684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134684)

## Data

Gene col 5587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5587); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5587]; `tensor/DDL_lfc|DDL_z.npy` [5587]; `embed/gene_vectors.npy` [5587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5587 or target_col == 5587). Every well: [[YARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
