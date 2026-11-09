---
symbol: "AKT1S1"
type: "gene"
col: 12911
ensembl_id: "ENSG00000204673"
name: "AKT1 substrate 1"
location: "19q13.33"
module: 173
arm: "+"
pooled_cpm: 15.87
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# AKT1S1

*AKT1 substrate 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.65× (z +21.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.403× (z -10.9, q 4e-25, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGPS1]] (+0.79, fdr 7e-06), [[CCDC90B-AS1]] (+0.78, fdr 2e-05), [[FBXL19-AS1]] (+0.78, fdr 7e-06); moves opposite to [[SDHAF3]] (-0.72, fdr 1e-05), [[ATG4C]] (-0.71, fdr 1e-05), [[POGLUT2]] (-0.70, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFATC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.65×** | +21.9 | 0e+00 | 45/47 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.53×** | +15.1 | 0e+00 | 38/39 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +13.4 | 2e-38 | 28/29 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.88×** | +12.7 | 1e-34 | 45/47 (SW480, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +11.2 | 6e-27 | 41/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +10.4 | 2e-23 | 27/35 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +9.5 | 2e-19 | 39/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.5 | 1e-15 | 34/45 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.04×** | +8.2 | 2e-14 | 31/46 (NCI-H1792, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.1 | 2e-14 | 37/46 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +6.9 | 2e-10 | 29/47 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +5.6 | 8e-07 | 30/47 (SW480, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 6e-06 | 23/47 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.9 | 4e-05 | 27/47 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.48×** | +4.7 | 9e-05 | 24/44 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 6e-04 | 25/47 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 19/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.006 | 17/48 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.029 | 12/44 (C-33 A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.038 | 16/47 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.058 | 4/47 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.403×** | -10.9 | 4e-25 | 43/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -9.9 | 1e-20 | 43/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.443×** | -9.8 | 2e-20 | 42/47 (HT-29, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.478×** | -8.9 | 8e-17 | 38/47 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.617×** | -8.3 | 2e-14 | 36/48 (LS 180, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.439×** | -5.2 | 2e-05 | 29/48 (HT-29, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -4.5 | 4e-04 | 24/44 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -4.3 | 0.001 | 23/47 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.044 | 13/48 (SW 1271, SHP-77, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.768×** | -3.2 | 0.077 | 10/47 (SW480, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 24.3 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +18.3) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -9.6) |
| [[HT-29 (line)]] | alt | 48.2 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -10.1) |
| [[PANC-1 (line)]] | alt | 22.4 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.334× (z -9.3) |
| [[A498 (line)]] | wt | 20.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.5) | — |
| [[SW480 (line)]] | alt | 13.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.64× (z +9.7) | — |
| [[A549 (line)]] | wt | 15.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +11.3) | — |
| [[LoVo (line)]] | wt | 11.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 14.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +10.5) | [[Belinostat (drug)]] 5 µM 0.195× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 31.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +15.7) | [[Belinostat (drug)]] 5 µM 0.237× (z -8.6) |
| [[SW1417 (line)]] | alt | 21.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -9.0) |
| [[A-172 (line)]] | wt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +14.3) | — |
| [[C32 (line)]] | wt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 6.35 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.62× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.95× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 19.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +13.7) | — |
| [[J82 (line)]] | alt | 14.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +12.8) | — |
| [[KATO III (line)]] | alt | 19.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.282× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +16.0) | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +19.2) | — |
| [[SNU-423 (line)]] | alt | 15.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +14.5) | — |
| [[A-427 (line)]] | wt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 9.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +17.4) | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0931× (z -8.9) |
| [[Hs 766T (line)]] | wt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 8.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +13.7) | — |
| [[SNU-1 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGPS1]] | +0.79 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.78 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | +0.78 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PHF8]] | +0.76 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[NQO1-DT]] | +0.74 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[C11orf58]] | +0.74 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[BRPF3]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ARFGAP2]] | +0.73 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PTOV1-AS1]] | +0.73 | +0.70 / +0.57 | both halves | 8e-06 | ⚠ same locus (17.4 kb, same strand: neighbours can correlate without regulation) |
| [[MMADHC-DT]] | +0.73 | +0.74 / +0.34 | both halves | 1e-04 |  |
| [[ATXN1L]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R3F]] | +0.73 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | +0.73 | +0.71 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.72 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.71 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.70 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.69 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[WASF3]] | -0.68 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[TAF5L]] | -0.68 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[TMEM120B]] | -0.68 | -0.67 / -0.37 | both halves | 8e-05 |  |
| [[L2HGDH]] | -0.68 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.68 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[ARL6]] | -0.67 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[HACE1]] | -0.66 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[MMS19]] | -0.66 | -0.71 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC1]] | B | NFATC1 activity lowers AKT1S1's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without NFATC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AKT1S1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises AKT1S1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.9, 12.1); signed map (16.7, -22.2). **Vector** length 98.7, 24.8% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.3 | +21.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.7 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | -0.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.3 | -10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | AKT1 substrate 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,869,033-49,878,459 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRAS40, MGC2865, Lobe |
| Gene groups (HGNC) | MTOR complex 1 |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 12 pathways, smallest: AKT phosphorylates targets in the cytosol; mTORC1-mediated signalling; Constitutive Signaling by AKT1 E17K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B36](https://www.uniprot.org/uniprotkb/Q96B36) (Proline-rich AKT1 substrate 1):

> Negative regulator of the mechanistic target of rapamycin complex 1 (mTORC1), an evolutionarily conserved central nutrient sensor that stimulates anabolic reactions and macromolecule biosynthesis to promote cellular biomass generation and growth. In absence of insulin and nutrients, AKT1S1 associates with the mTORC1 complex and directly inhibits mTORC1 activity by blocking the MTOR substrate-recruitment site. In response to insulin and nutrients, AKT1S1 dissociates from mTORC1. Its activity is …

**Summary**, from NCBI Gene [84335](https://www.ncbi.nlm.nih.gov/gene/84335):

> AKT1S1 is a proline-rich substrate of AKT (MIM 164730) that binds 14-3-3 protein (see YWHAH, MIM 113508) when phosphorylated (Kovacina et al., 2003 [PubMed 12524439]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28426](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28426) · Entrez [84335](https://www.ncbi.nlm.nih.gov/gene/84335) · UniProt [Q96B36](https://www.uniprot.org/uniprotkb/Q96B36) · Ensembl [ENSG00000204673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204673)

## Data

Gene col 12911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12911); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12911]; `tensor/DDL_lfc|DDL_z.npy` [12911]; `embed/gene_vectors.npy` [12911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12911 or target_col == 12911). Every well: [[AKT1S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKT1S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
