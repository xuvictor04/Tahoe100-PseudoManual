---
symbol: "TMEM138"
type: "gene"
col: 7377
ensembl_id: "ENSG00000149483"
name: "transmembrane protein 138"
location: "11q12.2"
module: 5
arm: "+"
pooled_cpm: 8.6
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TMEM138

*transmembrane protein 138* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.17× (z +30.0, q 0e+00, up in 15 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.64× (z +8.0, q 1e-13, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Hesperidin (drug)]] 0.05 µM: 0.771× (z -3.8, q 0.036, down in 4 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP42]] (+0.73, fdr 7e-06), [[PEX26]] (+0.69, fdr 7e-06), [[SSU72]] (+0.66, fdr 3e-05); moves opposite to [[OCEL1]] (-0.61, fdr 1e-04), [[RASSF7]] (-0.59, fdr 3e-05), [[BTG1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.17×** | +30.0 | 0e+00 | 15/15 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.18×** | +28.8 | 0e+00 | 32/34 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.36×** | +21.5 | 0e+00 | 22/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +9.1 | 1e-17 | 21/38 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +8.0 | 1e-13 | 25/47 (SW480, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +7.8 | 9e-13 | 24/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.4 | 9e-12 | 24/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +7.4 | 9e-12 | 22/44 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.3 | 2e-11 | 24/47 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.8 | 8e-10 | 21/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +6.7 | 9e-10 | 17/44 (SW480, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 1e-07 | 19/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.41×** | +5.4 | 2e-06 | 21/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.40×** | +5.3 | 6e-06 | 16/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 7e-06 | 12/43 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.1 | 1e-05 | 13/47 (COLO 205, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +4.9 | 3e-05 | 11/42 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.8 | 5e-05 | 13/47 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 1e-04 | 12/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.6 | 1e-04 | 18/45 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.003 | 7/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.004 | 16/42 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.018 | 4/42 (RKO, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.028 | 6/47 (CFPAC-1, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hesperidin (drug)]] 0.05 µM |  | **0.771×** | -3.8 | 0.036 | 4/47 (BT-474, HS-578T, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.847× | -3.7 | 0.036 | 13/44 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.792×** | -3.7 | 0.036 | 13/45 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.794×** | -3.7 | 0.036 | 11/47 (SW1417, A498, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.807×** | -3.4 | 0.073 | 13/46 (NCI-H460, HCT15, …) | two highest doses |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.081 | 9/45 (NCI-H1792, HEC-1-A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.827× | -3.0 | 0.21 | 6/47 (AN3 CA, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.58 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.2× (z +10.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 12.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +12.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 13.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.9× (z +22.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 12.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.64× (z +17.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 4.80 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 15.0× (z +9.7) ⚠ toxic; transcription drop | [[Vandetanib (drug)]] 0.5 µM 0.0825× (z -8.9) |
| [[BT-474 (line)]] | alt | 11.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 6.88 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.4× (z +13.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 6.97 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.07× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.21× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 9.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.39× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 8.41 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 6.29 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0607× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 8.62 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.98× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 6.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.2× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 8.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.96× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 7.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.28× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 6.76 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.8× (z +11.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 5.37 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 44.6× (z +18.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 9.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 5.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.89× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 6.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +14.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 6.34 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.3× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP42]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PEX26]] | +0.69 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SSU72]] | +0.66 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[SENP3]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[COMT]] | +0.65 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SYMPK]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[EFTUD2]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[MCM3AP]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[WDR77]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SAE1]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCEL1]] | -0.61 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[RASSF7]] | -0.59 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[BTG1]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[RNASE4]] | -0.56 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[RIOK3]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[RNF181]] | -0.56 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[RPL18]] ⚠ | -0.55 | -0.24 / -0.62 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | -0.54 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[RYBP]] | -0.54 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[GTF2B]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FAM53C]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ING2]] | -0.54 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[SNHG7]] | -0.53 | -0.36 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.1, -30.6); signed map (-8.4, -42.3). **Vector** length 70.6, 11.3% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +28.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +30.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +21.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +9.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.1 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.6 | -3.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 138 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,361,964-61,377,890 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC196, JBTS16 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPI0](https://www.uniprot.org/uniprotkb/Q9NPI0) (Transmembrane protein 138):

> Required for ciliogenesis.

**Summary**, from NCBI Gene [51524](https://www.ncbi.nlm.nih.gov/gene/51524):

> This gene encodes a multi-pass transmembrane protein. Reduced expression of this gene in mouse fibroblasts causes short cilia and failure of ciliogenesis. Expression of this gene is tightly coordinated with expression of the neighboring gene TMEM216. Mutations in this gene are associated with the autosomal recessive neurodevelopmental disorder Joubert Syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:26944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26944) · Entrez [51524](https://www.ncbi.nlm.nih.gov/gene/51524) · UniProt [Q9NPI0](https://www.uniprot.org/uniprotkb/Q9NPI0) · Ensembl [ENSG00000149483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149483)

## Data

Gene col 7377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7377); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7377]; `tensor/DDL_lfc|DDL_z.npy` [7377]; `embed/gene_vectors.npy` [7377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7377 or target_col == 7377). Every well: [[TMEM138 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM138.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
