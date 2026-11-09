---
symbol: "RMC1"
type: "gene"
col: 6524
ensembl_id: "ENSG00000141452"
name: "regulator of MON1-CCZ1"
location: "18q11.2"
module: 189
arm: "+"
pooled_cpm: 22.67
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# RMC1

*regulator of MON1-CCZ1* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.59× (z +29.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.920× (z -6.8, q 4e-09, down in 7 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 0.5 µM: 0.821× (z -4.6, q 0.001, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (RKO 0.260×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.254×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID5A]] (+0.64, fdr 4e-05), [[DLGAP4]] (+0.62, fdr 2e-05), [[CHP1]] (+0.61, fdr 2e-05); moves opposite to [[YARS2]] (-0.59, fdr 2e-04), [[PHC2-AS1]] (-0.57, fdr 1e-04), [[PNISR-AS1]] (-0.57, fdr 5e-04).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC16A14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.59×** | +29.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.48×** | +29.1 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.16×** | +26.9 | 0e+00 | 46/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +18.2 | 0e+00 | 43/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +10.3 | 7e-23 | 30/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +10.2 | 1e-22 | 27/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.5 | 2e-19 | 27/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +8.7 | 2e-16 | 31/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.0 | 2e-10 | 26/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +5.7 | 7e-07 | 15/48 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.5 | 2e-06 | 10/33 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +5.3 | 5e-06 | 20/46 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +5.0 | 3e-05 | 11/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 5e-05 | 17/47 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 1e-04 | 15/47 (CFPAC-1, LS 180, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 1e-04 | 19/47 (LS 180, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +4.4 | 3e-04 | 14/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (RKO 0.260×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.254×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -6.8 | 4e-09 | 7/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.821×** | -4.6 | 0.001 | 13/47 (AsPC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.903× | -3.4 | 0.12 | 13/48 (A-427, CFPAC-1, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.9) | — |
| [[LoVo (line)]] | wt | 24.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 18.4 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +14.3) | — |
| [[SW480 (line)]] | alt | 24.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +15.7) | — |
| [[A-427 (line)]] | wt | 32.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[A549 (line)]] | wt | 16.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.80× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 46.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.98× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 13.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +9.7) | — |
| [[J82 (line)]] | alt | 26.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.67× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 23.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.06× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +12.0) | — |
| [[RKO (line)]] | wt | 27.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.40× (z +9.6) | [[Simotinib (drug)]] 5 µM 0.260× (z -10.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 24.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 21.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 19.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.19× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 25.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.56× (z +9.7) | — |
| [[KATO III (line)]] | alt | 18.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 17.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.87× (z +8.8) | — |
| [[A498 (line)]] | wt | 40.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.2) | — |
| [[C32 (line)]] | wt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 17.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.22× (z +8.6) | — |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID5A]] | +0.64 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[DLGAP4]] | +0.62 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CHP1]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MFSD12]] | +0.59 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[GNAI2]] | +0.59 | +0.27 / +0.33 | both halves | 3e-04 |  |
| [[PI4K2A]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[TNK2]] | +0.56 | +0.24 / +0.42 | both halves | 5e-04 |  |
| [[FAM89B]] | +0.56 | +0.46 / +0.26 | both halves | 4e-04 |  |
| [[PITPNM1]] | +0.56 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[KCTD21]] | +0.56 | +0.42 / +0.32 | both halves | 2e-04 |  |
| [[SPAG9]] | +0.55 | +0.35 / +0.32 | both halves | 2e-04 |  |
| [[DNAAF3]] | +0.55 | +0.33 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[PCYT2]] | +0.55 | +0.47 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.59 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[PHC2-AS1]] | -0.57 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.57 | -0.34 / -0.24 | both halves | 5e-04 |  |
| [[SNX5]] | -0.56 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[MTREX]] | -0.55 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[SDHAF4]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SLC16A9]] | -0.55 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[PDHX]] | -0.54 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[LATS1]] | -0.53 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[TYSND1]] | -0.53 | -0.17 / -0.38 | ⚠ not reproduced | 0.001 |  |
| [[ANAPC1]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.52 | -0.23 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.52 | -0.23 / -0.29 | both halves | 5e-04 |  |
| [[TIAL1]] | -0.52 | -0.30 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A14]] | B | SLC16A14 activity lowers RMC1's level | lines that do not express SLC16A14 (16) vs lines expressing it (34) | 1.13× higher at baseline in the lines without SLC16A14 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, ARHGEF16, NEBL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, -1.6); signed map (-20.0, 25.4). **Vector** length 71.1, 12.7% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +29.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +26.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +29.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | regulator of MON1-CCZ1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,503,496-23,531,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIC1, HsT2591; previously C18orf8, WDR98 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DM3](https://www.uniprot.org/uniprotkb/Q96DM3) (Regulator of MON1-CCZ1 complex):

> Component of the CCZ1-MON1 RAB7A guanine exchange factor (GEF). Acts as a positive regulator of CCZ1-MON1A/B function necessary for endosomal/autophagic flux and efficient RAB7A localization.

**Summary**, from NCBI Gene [29919](https://www.ncbi.nlm.nih.gov/gene/29919):

> This gene encodes a colon cancer associated protein. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:24326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24326) · Entrez [29919](https://www.ncbi.nlm.nih.gov/gene/29919) · UniProt [Q96DM3](https://www.uniprot.org/uniprotkb/Q96DM3) · Ensembl [ENSG00000141452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141452)

## Data

Gene col 6524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6524); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6524]; `tensor/DDL_lfc|DDL_z.npy` [6524]; `embed/gene_vectors.npy` [6524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6524 or target_col == 6524). Every well: [[RMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
