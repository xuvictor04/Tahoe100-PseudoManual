---
symbol: "ITPKB"
type: "gene"
col: 6800
ensembl_id: "ENSG00000143772"
name: "inositol-trisphosphate 3-kinase B"
location: "1q42.12"
module: 189
arm: "+"
pooled_cpm: 12.39
n_lines_expressing: 44
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# ITPKB

*inositol-trisphosphate 3-kinase B* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.43× (z +7.7, q 7e-12, up in 22 of 41 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.39× (z +5.0, q 2e-04, up in 13 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.271× (z -19.7, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.56, fdr 5e-05), [[KLHL42]] (+0.56, fdr 4e-04), [[ECHDC1]] (+0.54, fdr 4e-05); moves opposite to [[SPAG9]] (-0.63, fdr 8e-05), [[NBEAL1]] (-0.58, fdr 4e-05), [[DLGAP4]] (-0.56, fdr 7e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PGAP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.43×** | +7.7 | 7e-12 | 22/41 (NCI-H23, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +5.0 | 2e-04 | 13/41 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.27×** | +3.6 | 0.050 | 10/39 (COLO 205, RKO, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.085 | 6/41 (KATO III, HCT15, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.17× | +3.3 | 0.085 | 4/41 (SHP-77, BT-474, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.085 | 3/41 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.271×** | -19.7 | 0e+00 | 39/41 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.304×** | -17.9 | 0e+00 | 37/41 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.342×** | -16.2 | 0e+00 | 37/41 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.523×** | -9.7 | 3e-20 | 26/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.519×** | -9.5 | 3e-19 | 24/40 (RKO, SW48, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -8.1 | 4e-14 | 27/41 (LS 180, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.702×** | -7.5 | 5e-12 | 20/38 (SK-MEL-2, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -7.3 | 2e-11 | 21/36 (RPMI-7951, CHP-212, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.616×** | -7.3 | 2e-11 | 25/41 (NCI-H2030, A-427, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.627×** | -7.0 | 1e-10 | 21/35 (CHP-212, SW480, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -5.9 | 2e-07 | 20/40 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.492×** | -5.6 | 1e-06 | 17/38 (HCT15, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.705×** | -5.0 | 2e-05 | 17/36 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -5.0 | 2e-05 | 16/40 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.750×** | -4.3 | 6e-04 | 18/39 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.603×** | -4.0 | 0.002 | 12/41 (SW1417, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.010 | 13/39 (C32, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.016 | 8/41 (SW48, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.859× | -3.2 | 0.035 | 12/41 (SK-MEL-2, C32, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.044 | 5/41 (HOP62, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 30.5 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0688× (z -19.4) |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -14.6) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0590× (z -19.9) |
| [[CHP-212 (line)]] | wt | 96.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0472× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -11.1) |
| [[SW480 (line)]] | alt | 13.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -13.6) |
| [[C32 (line)]] | wt | 41.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0824× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -10.4) |
| [[SW48 (line)]] | wt | 21.5 | 0 | 3 (1 ⚠) | — | [[Arbutin (drug)]] 5 µM 0.119× (z -10.3) |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -10.6) |
| [[KATO III (line)]] | alt | 13.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.152× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 4.69 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +10.5) ⚠ cell-cycle shift, explains ~7% of this change | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.161× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -13.4) |
| [[RKO (line)]] | wt | 18.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.138× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.6) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.190× (z -8.5) |
| [[A-172 (line)]] | wt | 8.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.2) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A-427 (line)]] | wt | 6.91 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0784× (z -10.8) |
| [[A498 (line)]] | wt | 8.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.7) ⚠ cell-cycle shift, explains ~73% of this change |
| [[BT-474 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0268× (z -17.3) |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0927× (z -9.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 7.96 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0737× (z -14.0) |
| [[SNU-1 (line)]] | wt | 8.77 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0904× (z -8.5) |
| [[A549 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.56 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[KLHL42]] | +0.56 | +0.26 / +0.41 | both halves | 4e-04 |  |
| [[ECHDC1]] | +0.54 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[NNT]] | +0.54 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[TOR1A]] | +0.53 | +0.23 / +0.46 | both halves | 5e-04 |  |
| [[NSMAF]] | +0.51 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[PLCL2]] | +0.51 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[RCC2]] | +0.50 | +0.39 / +0.33 | both halves | 1e-04 |  |
| [[ZNF618]] | +0.49 | +0.41 / +0.34 | both halves | 1e-04 |  |
| [[SLC25A21]] | +0.49 | +0.09 / +0.43 | ⚠ not reproduced | 0.003 |  |
| [[PATZ1]] | +0.48 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[JADE2]] | +0.48 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[TRAF5]] | +0.48 | +0.30 / +0.52 | both halves | 2e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.63 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NBEAL1]] | -0.58 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[DLGAP4]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[MRTFA]] | -0.56 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TMOD1]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[PTPRH]] | -0.56 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SYP]] | -0.54 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[RHOB]] | -0.53 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[MFSD12]] | -0.53 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[USP15]] | -0.52 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[PC]] | -0.52 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[KLF2]] | -0.51 | -0.25 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity raises ITPKB's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without PGAP4 | 0.068 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction -0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.8, 9.9); signed map (25.2, -27.6). **Vector** length 76.5, 13.9% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +5.8 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.3 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -19.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -17.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -16.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -8.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | inositol-trisphosphate 3-kinase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:226,631,690-226,739,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IP3KB, IP3-3KB |
| Gene groups (HGNC) | Inositol-trisphosphate 3-kinase family |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P27987](https://www.uniprot.org/uniprotkb/P27987) (Inositol-trisphosphate 3-kinase B):

> Catalyzes the phosphorylation of 1D-myo-inositol 1,4,5-trisphosphate (InsP3) into 1D-myo-inositol 1,3,4,5-tetrakisphosphate and participates to the regulation of calcium homeostasis.

**Summary**, from NCBI Gene [3707](https://www.ncbi.nlm.nih.gov/gene/3707):

> The protein encoded by this protein regulates inositol phosphate metabolism by phosphorylation of second messenger inositol 1,4,5-trisphosphate to Ins(1,3,4,5)P4. The activity of this encoded protein is responsible for regulating the levels of a large number of inositol polyphosphates that are important in cellular signaling. Both calcium/calmodulin and protein phosphorylation mechanisms control its activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6179) · Entrez [3707](https://www.ncbi.nlm.nih.gov/gene/3707) · UniProt [P27987](https://www.uniprot.org/uniprotkb/P27987) · Ensembl [ENSG00000143772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143772)

## Data

Gene col 6800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6800); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6800]; `tensor/DDL_lfc|DDL_z.npy` [6800]; `embed/gene_vectors.npy` [6800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6800 or target_col == 6800). Every well: [[ITPKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
