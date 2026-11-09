---
symbol: "NEK11"
type: "gene"
col: 3574
ensembl_id: "ENSG00000114670"
name: "NIMA related kinase 11"
location: "3q22.1"
module: 26
arm: "+"
pooled_cpm: 35.15
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# NEK11

*NIMA related kinase 11* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.12× (z +14.1, q 4e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.437× (z -8.2, q 9e-14, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.555× (z -5.9, q 7e-07, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKDD1B]] (+0.79, fdr 7e-06), [[CCDC90B-AS1]] (+0.78, fdr 1e-05), [[CCDC30]] (+0.78, fdr 7e-06); moves opposite to [[BRAT1]] (-0.64, fdr 5e-05), [[SDHAF3]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ADRA1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.12×** | +14.1 | 4e-42 | 46/48 (HT-29, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.8 | 2e-06 | 33/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.46×** | +5.3 | 2e-05 | 37/48 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.8 | 2e-04 | 26/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.005 | 26/48 (A-427, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.006 | 26/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.033 | 22/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.035 | 20/48 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.043 | 20/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.2 | 0.081 | 3/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.081 | 14/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.82×** | +3.1 | 0.092 | 20/47 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.093 | 21/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.11 | 14/48 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.437×** | -8.2 | 9e-14 | 39/48 (RKO, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.502×** | -6.9 | 2e-09 | 34/48 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.515×** | -6.6 | 8e-09 | 33/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.555×** | -5.9 | 7e-07 | 36/47 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.561×** | -5.7 | 1e-06 | 33/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.559×** | -5.6 | 3e-06 | 28/46 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.591×** | -5.2 | 1e-05 | 34/48 (NCI-H23, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -5.2 | 1e-05 | 33/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.369×** | -5.2 | 1e-05 | 33/48 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.626×** | -4.7 | 2e-04 | 28/48 (LoVo, CFPAC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.474×** | -3.9 | 0.005 | 25/47 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.678×** | -3.9 | 0.005 | 23/48 (H4, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.687×** | -3.6 | 0.014 | 27/48 (A549, SW 900, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.701×** | -3.5 | 0.016 | 20/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **0.702×** | -3.5 | 0.016 | 22/45 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.719×** | -3.3 | 0.036 | 21/48 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.043 | 20/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.729×** | -3.2 | 0.050 | 19/48 (SW 1271, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.737×** | -2.9 | 0.096 | 18/48 (HT-29, Hs 766T, …) | top dose only | plate-row cell shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.739×** | -2.9 | 0.100 | 19/48 (A549, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 45.5 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 41.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.132× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 60.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 72.2 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.02× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.223× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 46.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 19.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.84× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.141× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[LoVo (line)]] | wt | 31.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.83× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.324× (z -8.5) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 35.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.59× (z +9.2) | [[Digitoxin (drug)]] 0.05 µM 0.296× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 42.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[RKO (line)]] | wt | 23.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 10.5× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.167× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +9.4) | — |
| [[SW480 (line)]] | alt | 19.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.72× (z +16.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -8.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 28.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.1× (z +15.4) | — |
| [[A-427 (line)]] | wt | 45.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +10.3) | — |
| [[C32 (line)]] | wt | 14.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 23.4× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 65.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.88× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 61.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.48× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HT-29 (line)]] | alt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 25.0× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LS 180 (line)]] | wt | 17.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.24× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.29× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 53.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.03× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 29.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.99× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 21.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.83× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 9.46 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.34× (z +9.1) | — |
| [[SW48 (line)]] | wt | 27.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.9× (z +10.2) | — |
| [[A498 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKDD1B]] | +0.79 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.78 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[CCDC30]] | +0.78 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.78 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[MCPH1]] | +0.76 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CATSPERE]] | +0.76 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LINC00571]] | +0.76 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[YIPF7]] | +0.75 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ACYP2]] | +0.75 | +0.77 / +0.46 | both halves | 3e-05 |  |
| [[ZFHX2-AS1]] | +0.74 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[CELF6]] | +0.74 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | +0.73 | +0.70 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.64 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[SDHAF3]] | -0.64 | -0.57 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA1B]] | B | ADRA1B activity raises NEK11's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without ADRA1B | 0.063 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[JHY]] | B | JHY activity raises NEK11's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without JHY | 0.064 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[TTC6]] | B | TTC6 activity raises NEK11's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without TTC6 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NEK11's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C17orf67]] | C | C17orf67 activity raises NEK11's level | lines that do not express C17orf67 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without C17orf67 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP10, IQSEC2, MBOAT2; maybe low, not absent |
| [[IMPG2]] | C | IMPG2 activity raises NEK11's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without IMPG2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.5, 13.1); signed map (24.2, -4.3). **Vector** length 121, 37.3% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.6 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +6.2 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.2 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.1 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.7 | -8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.6 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.1 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.8 | -5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.9 | -2.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -3.0 | -1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:131,026,850-131,350,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23495 |
| Gene groups (HGNC) | NIMA related kinase family |
| Reactome | 5 pathways, smallest: Ubiquitin-Mediated Degradation of Phosphorylated Cdc25A; p53-Independent G1/S DNA Damage Checkpoint; G1/S DNA Damage Checkpoints |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG66](https://www.uniprot.org/uniprotkb/Q8NG66) (Serine/threonine-protein kinase Nek11):

> Protein kinase which plays an important role in the G2/M checkpoint response to DNA damage. Controls degradation of CDC25A by directly phosphorylating it on residues whose phosphorylation is required for BTRC-mediated polyubiquitination and degradation.

**Summary**, from NCBI Gene [79858](https://www.ncbi.nlm.nih.gov/gene/79858):

> This gene encodes a member of the never in mitosis gene A family of kinases. The encoded protein localizes to the nucleoli, and may function with NEK2A in the S-phase checkpoint. The encoded protein appears to play roles in DNA replication and response to genotoxic stress. Alternatively spliced transcript variants have been described.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:18593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18593) · Entrez [79858](https://www.ncbi.nlm.nih.gov/gene/79858) · UniProt [Q8NG66](https://www.uniprot.org/uniprotkb/Q8NG66) · Ensembl [ENSG00000114670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114670)

## Data

Gene col 3574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3574); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3574]; `tensor/DDL_lfc|DDL_z.npy` [3574]; `embed/gene_vectors.npy` [3574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3574 or target_col == 3574). Every well: [[NEK11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
