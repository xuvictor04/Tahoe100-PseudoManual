---
symbol: "GALC"
type: "gene"
col: 618
ensembl_id: "ENSG00000054983"
name: "galactosylceramidase"
location: "14q31.3"
module: 3
arm: "-"
pooled_cpm: 17.11
n_lines_expressing: 33
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# GALC

*galactosylceramidase* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.54× (z +22.1, q 0e+00, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.40× (z +8.5, q 2e-15, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.492× (z -12.9, q 3e-35, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5D2]] (+0.68, fdr 1e-05), [[EWSR1]] (+0.65, fdr 1e-04), [[ACADM]] (+0.64, fdr 2e-05); moves opposite to [[SDHAF1]] (-0.64, fdr 3e-05), [[MPG]] (-0.63, fdr 3e-05), [[NUDT22]] (-0.63, fdr 1e-04).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HYI]] → it (grade B ⚠); 3 go from it, the strongest it → [[PLIN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +22.1 | 0e+00 | 19/22 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +21.6 | 0e+00 | 25/28 (SW 900, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +14.2 | 9e-44 | 24/27 (SW 900, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +10.1 | 7e-22 | 7/31 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +8.5 | 2e-15 | 17/31 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +7.1 | 1e-10 | 7/17 (NCI-H2347, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.4 | 9e-04 | 9/24 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.6 | 0.025 | 9/28 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.059 | 7/30 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.067 | 5/30 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.093 | 1/30 (A-427) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.093 | 2/30 (LS 180, A-427) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.093 | 3/29 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.492×** | -12.9 | 3e-35 | 23/30 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.508×** | -12.3 | 2e-32 | 21/30 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.543×** | -11.1 | 2e-26 | 22/31 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.551×** | -10.8 | 3e-25 | 21/31 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -8.6 | 1e-15 | 23/31 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.417×** | -8.3 | 9e-15 | 16/29 (NCI-H23, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -8.2 | 3e-14 | 17/31 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.713×** | -6.2 | 5e-08 | 14/29 (HCT15, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.727×** | -5.8 | 4e-07 | 14/30 (BT-474, A-427, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.721×** | -5.7 | 5e-07 | 15/31 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.775×** | -4.5 | 4e-04 | 11/30 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -4.2 | 0.001 | 10/31 (NCI-H1792, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -3.9 | 0.004 | 13/31 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.816×** | -3.7 | 0.008 | 6/28 (SW1417, J82, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.890× | -3.0 | 0.093 | 6/31 (KATO III, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.099 | 3/30 (NCI-H1792, CHP-212, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 38.7 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +19.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.290× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 38.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.16× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.82× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 55.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +20.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 42.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.334× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 20.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.64× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 36.3 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.335× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 40.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.36× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 8.32 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0871× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 12.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.183× (z -8.9) |
| [[BT-474 (line)]] | alt | 8.18 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0292× (z -13.8) |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +10.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -9.2) |
| [[LS 180 (line)]] | wt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 10.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | +0.68 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.65 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[ACADM]] | +0.64 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MTERF2]] | +0.63 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[TAF9B]] | +0.63 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[FUBP1]] | +0.62 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[PDIA3P1]] | +0.62 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[VPS35L]] | +0.62 | +0.63 / +0.37 | both halves | 8e-05 |  |
| [[PMF1]] | +0.61 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[DDX3X]] | +0.61 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ZNF300]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CC2D2A]] | +0.61 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.64 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MPG]] | -0.63 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NUDT22]] | -0.63 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[TRAPPC4]] | -0.62 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[RASSF7]] | -0.61 | -0.26 / -0.62 | both halves | 4e-04 |  |
| [[C1orf35]] | -0.61 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[POP7]] | -0.61 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MRPL55]] | -0.60 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TRIM11]] | -0.60 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[TSEN54]] | -0.59 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[FBXO45]] | -0.59 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[MRPL41]] ⚠ | -0.58 | -0.32 / -0.54 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[C16orf91]] | -0.58 | -0.29 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYI]] | B | HYI activity raises GALC's level | lines that do not express HYI (9) vs lines expressing it (41) | 2.96× lower at baseline in the lines without HYI | 0.095 | ⚠ within organs, on part of the lines; also absent: HEIH |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN3]] | B | GALC activity raises PLIN3's level | lines that do not express GALC (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without GALC | 0.048 | ⚠ within organs, on part of the lines; also absent: HERC5, TNFRSF1B, ZNF354C |
| [[HYI]] | B | GALC activity raises HYI's level | lines that do not express GALC (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without GALC | 0.092 | ⚠ within organs, on part of the lines; also absent: HERC5, TNFRSF1B, ZNF354C |
| [[EFEMP1]] | C | GALC activity raises EFEMP1's level | lines that do not express GALC (17) vs lines expressing it (33) | 3.26× lower at baseline in the lines without GALC | 0.089 | ⚠ within organs, on part of the lines; also absent: HERC5, TNFRSF1B, ZNF354C; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.6, 3.9); signed map (16.4, -36.8). **Vector** length 70.5, 15.1% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.0 | +22.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.8 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.7 | +21.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -11.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | galactosylceramidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:87,837,820-87,993,665 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 4 pathways, smallest: Glycosphingolipid catabolism; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P54803](https://www.uniprot.org/uniprotkb/P54803) (Galactocerebrosidase):

> Lysosomal hydrolase that removes the terminal galactose from galactosylceramide, a major lipid of the myelin sheath, kidney, and epithelial cells of the small intestine and colon, and from related glycosphingolipids such as galactosylsphingosine. Present at very low abundance/specific activity in tissues relative to other lysosomal enzymes. Requires the lipid-binding activator protein Saposin-A (SapA, a cleavage product of PSAP) to access glycosphingolipid substrates embedded in lysosomal …

**Summary**, from NCBI Gene [2581](https://www.ncbi.nlm.nih.gov/gene/2581):

> This gene encodes a lysosomal protein which hydrolyzes the galactose ester bonds of galactosylceramide, galactosylsphingosine, lactosylceramide, and monogalactosyldiglyceride. Mutations in this gene have been associated with Krabbe disease, also known as globoid cell leukodystrophy. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4115) · Entrez [2581](https://www.ncbi.nlm.nih.gov/gene/2581) · UniProt [P54803](https://www.uniprot.org/uniprotkb/P54803) · Ensembl [ENSG00000054983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054983)

## Data

Gene col 618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 618); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 618]; `tensor/DDL_lfc|DDL_z.npy` [618]; `embed/gene_vectors.npy` [618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 618 or target_col == 618). Every well: [[GALC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
