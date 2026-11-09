---
symbol: "ACTR3"
type: "gene"
col: 3620
ensembl_id: "ENSG00000115091"
name: "actin related protein 3"
location: "2q14.1"
module: 111
arm: "+"
pooled_cpm: 256.45
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# ACTR3

*actin related protein 3* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.60× (z +9.1, q 3e-17, up in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.23× (z +8.5, q 4e-15, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.398× (z -18.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.78, fdr 8e-06), [[CDC42]] (+0.76, fdr 7e-06), [[MYH9]] (+0.69, fdr 7e-06); moves opposite to [[TMEM258]] (-0.66, fdr 1e-05), [[RPL36AL]] (-0.64, fdr 3e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[TMEM101]] (-0.63, fdr 1e-05), [[FAM193B]] (-0.63, fdr 1e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +9.1 | 3e-17 | 31/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +9.0 | 9e-17 | 37/49 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +8.5 | 4e-15 | 43/49 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +7.8 | 1e-12 | 31/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.6 | 2e-06 | 0/50 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.4 | 7e-06 | 27/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.2 | 2e-05 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 33/48 (HEC-1-A, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 4e-04 | 26/48 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.1 | 0.12 | 16/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.13 | 4/48 (COLO 205, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -18.6 | 0e+00 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.426×** | -17.2 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -14.7 | 0e+00 | 48/48 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -14.3 | 4e-44 | 43/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -9.3 | 2e-18 | 44/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -8.7 | 2e-16 | 44/48 (J82, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -6.3 | 3e-08 | 30/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -6.2 | 4e-08 | 41/48 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.752×** | -5.7 | 9e-07 | 31/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.618×** | -5.1 | 2e-05 | 34/49 (HepG2/C3A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.844× | -4.8 | 7e-05 | 22/48 (SK-MEL-2, A549, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.781×** | -4.8 | 7e-05 | 32/48 (J82, HS-578T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.798×** | -4.6 | 2e-04 | 27/49 (HOP62, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -4.3 | 8e-04 | 27/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.828×** | -3.8 | 0.005 | 26/48 (NCI-H23, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.006 | 23/49 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.843× | -3.5 | 0.016 | 21/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.027 | 14/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.046 | 17/48 (hTERT-HPNE, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 231 | 10 (8 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.57× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.345× (z -15.5) |
| [[A498 (line)]] | wt | 356 | 6 (6 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +12.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -16.3) |
| [[PANC-1 (line)]] | alt | 296 | 5 (3 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.313× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 415 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -17.7) |
| [[HS-578T (line)]] | alt | 265 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.328× (z -15.3) |
| [[J82 (line)]] | alt | 309 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -17.8) |
| [[SNU-423 (line)]] | alt | 218 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.388× (z -11.6) |
| [[SW480 (line)]] | alt | 261 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.332× (z -18.2) |
| [[A549 (line)]] | wt | 312 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -22.0) |
| [[HEC-1-A (line)]] | alt | 371 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 252 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.350× (z -13.0) |
| [[BT-474 (line)]] | alt | 194 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -10.9) |
| [[HT-29 (line)]] | alt | 274 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.418× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 261 | 3 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 6.75× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.394× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 339 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.319× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 202 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 3.87× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.335× (z -13.5) |
| [[RKO (line)]] | wt | 263 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 3.90× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.386× (z -12.4) |
| [[A-172 (line)]] | wt | 227 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 392 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -17.2) |
| [[C32 (line)]] | wt | 241 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -13.3) |
| [[HOP62 (line)]] | alt | 272 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -11.5) |
| [[Hs 766T (line)]] | wt | 199 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.83× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.288× (z -15.1) |
| [[KATO III (line)]] | alt | 128 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.398× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 307 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 326 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 182 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.03× (z +9.0) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 355 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -12.9) |
| [[H4 (line)]] | wt | 246 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 217 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.411× (z -9.5) |
| [[LoVo (line)]] | wt | 152 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.524× (z -9.5) |
| [[LS 180 (line)]] | wt | 199 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 320 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -10.3) |
| [[COLO 205 (line)]] | alt | 205 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 278 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -11.5) |
| [[SW 900 (line)]] | alt | 314 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.419× (z -10.1) |
| [[SW1417 (line)]] | alt | 162 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.436× (z -11.0) |
| [[A-427 (line)]] | wt | 148 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.494× (z -9.9) |
| [[CHP-212 (line)]] | wt | 213 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -9.0) |
| [[SHP-77 (line)]] | alt | 163 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.529× (z -8.8) |
| [[AN3 CA (line)]] | alt | 175 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 153 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.78 | +0.58 / +0.83 | both halves | 8e-06 | STRING 826 |
| [[CDC42]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | pathway: EPH-Ephrin signaling; STRING 841 |
| [[MYH9]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | pathway: EPH-Ephrin signaling; STRING 812 |
| [[ARPC4]] | +0.69 | +0.53 / +0.75 | both halves | 1e-05 | same gene group; pathway: Clathrin-mediated endocytosis; STRING 999 |
| [[GNB1]] | +0.67 | +0.62 / +0.75 | both halves | 7e-06 | pathway: Leishmania infection |
| [[DBNL]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 | STRING 673 |
| [[YWHAZ]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 468 |
| [[GNG12]] | +0.65 | +0.50 / +0.74 | both halves | 1e-05 | pathway: Leishmania infection |
| [[ADAM9]] | +0.65 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[CAPZB]] | +0.64 | +0.62 / +0.75 | both halves | 7e-06 | STRING 774 |
| [[TPM1]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 | STRING 413 |
| [[MAPRE1]] | +0.64 | +0.39 / +0.68 | both halves | 5e-05 | pathway: RHO GTPase Effectors; STRING 681 |

## Genes that move opposite

*47 of its nearest partners move opposite, 14 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM258]] | -0.66 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.64 | -0.43 / -0.65 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM101]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[FAM193B]] | -0.63 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[COG7]] | -0.63 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.62 | -0.47 / -0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[TULP3]] | -0.60 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[LAMTOR5]] | -0.59 | -0.29 / -0.63 | both halves | 2e-04 |  |
| [[CAMLG]] | -0.59 | -0.25 / -0.72 | both halves | 4e-04 |  |
| [[MTRFR]] | -0.59 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SNHG7]] | -0.59 | -0.41 / -0.71 | both halves | 4e-05 |  |
| [[PIAS4]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[MAP2K7]] | -0.58 | -0.37 / -0.59 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -18.5); signed map (-8.6, 34.7). **Vector** length 119, 44.7% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Platelet activation, signaling and aggregation* (reactome, mean cos +0.58 to 11); *mitotic spindle* (hallmark, mean cos +0.54 to 9); *RHO GTPases activate PAKs* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.4 | +2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.1 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.9 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,890,063-113,962,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP3 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits; Actin related proteins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P61158](https://www.uniprot.org/uniprotkb/P61158) (Actin-related protein 3):

> ATP-binding component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. Seems to contact the pointed end of the daughter actin filament. In podocytes, required for the formation of lamellipodia downstream of AVIL and PLCE1 regulation. In addition to its role in the cytoplasmic …

**Summary**, from NCBI Gene [10096](https://www.ncbi.nlm.nih.gov/gene/10096):

> The specific function of this gene has not yet been determined; however, the protein it encodes is known to be a major constituent of the ARP2/3 complex. This complex is located at the cell surface and is essential to cell shape and motility through lamellipodial actin assembly and protrusion. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:170) · Entrez [10096](https://www.ncbi.nlm.nih.gov/gene/10096) · UniProt [P61158](https://www.uniprot.org/uniprotkb/P61158) · Ensembl [ENSG00000115091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115091)

## Data

Gene col 3620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3620); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3620]; `tensor/DDL_lfc|DDL_z.npy` [3620]; `embed/gene_vectors.npy` [3620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3620 or target_col == 3620). Every well: [[ACTR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
