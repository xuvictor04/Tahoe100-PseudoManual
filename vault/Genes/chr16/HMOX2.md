---
symbol: "HMOX2"
type: "gene"
col: 2364
ensembl_id: "ENSG00000103415"
name: "heme oxygenase 2"
location: "16p13.3"
module: 77
arm: "+"
pooled_cpm: 26.71
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 4
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# HMOX2

*heme oxygenase 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.61× (z +18.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.746× (z -5.4, q 4e-05, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM120B]] (+0.69, fdr 1e-05), [[TRIM35]] (+0.69, fdr 7e-06), [[MPP3]] (+0.69, fdr 1e-05); moves opposite to [[STAG2]] (-0.70, fdr 7e-06), [[HMGN2]] (-0.68, fdr 1e-05), [[BAZ2B]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +18.2 | 0e+00 | 46/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.59×** | +18.1 | 0e+00 | 47/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +15.8 | 0e+00 | 46/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +10.8 | 3e-25 | 39/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +9.9 | 7e-21 | 30/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +9.4 | 4e-19 | 37/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.60×** | +8.6 | 5e-16 | 34/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +8.2 | 1e-14 | 29/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +7.8 | 4e-13 | 31/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +7.5 | 4e-12 | 30/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +7.0 | 2e-10 | 29/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.4 | 5e-09 | 19/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +5.8 | 2e-07 | 26/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 2e-07 | 26/47 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.36×** | +5.8 | 3e-07 | 22/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 1e-06 | 23/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.5 | 2e-06 | 21/48 (A-172, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.4 | 2e-06 | 21/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +5.1 | 8e-06 | 20/47 (NCI-H1573, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.746×** | -5.4 | 4e-05 | 19/47 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.796×** | -4.2 | 0.008 | 18/47 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.823×** | -3.7 | 0.038 | 15/47 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.850× | -3.6 | 0.038 | 11/48 (HOP62, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.873× | -3.6 | 0.038 | 10/48 (A549, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.834× | -3.5 | 0.038 | 14/48 (NCI-H1573, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.705×** | -3.5 | 0.038 | 13/46 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.038 | 10/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.843× | -3.4 | 0.038 | 12/48 (AsPC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.15 | 6/48 (HEC-1-A, RPMI-7951, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.5 | 6 | 0 | [[Belinostat (drug)]] 5 µM 2.73× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 4 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.02× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +12.0) | — |
| [[SW480 (line)]] | alt | 30.5 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[J82 (line)]] | alt | 32.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.70× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 38.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.6) | — |
| [[A-172 (line)]] | wt | 35.7 | 1 | 1 | [[Belinostat (drug)]] 5 µM 2.86× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 39.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.64× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 24.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 21.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +8.7) | — |
| [[A549 (line)]] | wt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.134× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 4.13× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.7) | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.5) |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | +0.69 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TRIM35]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MPP3]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.66 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[IMPDH1]] | +0.66 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MON1A]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SLC27A4]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.62 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[GFOD2]] | +0.62 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PAQR5]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[WASF3]] | +0.62 | +0.51 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG2]] | -0.70 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[HMGN2]] | -0.68 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.66 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[KANSL1L]] | -0.61 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[MED12]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[AHI1-DT]] | -0.60 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[TIA1]] | -0.60 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ATRX]] | -0.60 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CASC9]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[HNRNPH2]] | -0.59 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[EIF1B-AS1]] | -0.59 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DCAF8]] | -0.59 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity raises HMOX2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without ABCA3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[BICDL1]] | B | BICDL1 activity raises HMOX2's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without BICDL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[PPP2R2C]] | B | PPP2R2C activity raises HMOX2's level | lines that do not express PPP2R2C (18) vs lines expressing it (32) | 1.12× lower at baseline in the lines without PPP2R2C | 0.092 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, CACNG6, JAKMIP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises HMOX2's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-2.1, 0.4); signed map (-43.8, -3.4). **Vector** length 87.0, 19.0% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +18.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.4 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +5.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.9 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | heme oxygenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,474,690-4,510,347 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HO-2 |
| Gene groups (HGNC) | Heme oxygenase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 14 pathways, smallest: Heme degradation; Metabolism of porphyrins; Cytoprotection by HMOX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P30519](https://www.uniprot.org/uniprotkb/P30519) (Heme oxygenase 2):

> [Heme oxygenase 2]: Catalyzes the oxidative cleavage of heme at the alpha-methene bridge carbon, released as carbon monoxide (CO), to generate biliverdin IXalpha, while releasing the central heme iron chelate as ferrous iron.; [Heme oxygenase 2 soluble form]: Catalyzes the oxidative cleavage of heme at the alpha-methene bridge carbon, released as carbon monoxide (CO), to generate biliverdin IXalpha, while releasing the central heme iron chelate as ferrous iron.

**Summary**, from NCBI Gene [3163](https://www.ncbi.nlm.nih.gov/gene/3163):

> Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenase-2. HMOX1 and HMOX2 belong to the heme oxygenase family. Several alternatively spliced transcript …

**Accessions** — [HGNC:5014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5014) · Entrez [3163](https://www.ncbi.nlm.nih.gov/gene/3163) · UniProt [P30519](https://www.uniprot.org/uniprotkb/P30519) · Ensembl [ENSG00000103415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103415)

## Data

Gene col 2364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2364); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2364]; `tensor/DDL_lfc|DDL_z.npy` [2364]; `embed/gene_vectors.npy` [2364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2364 or target_col == 2364). Every well: [[HMOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
