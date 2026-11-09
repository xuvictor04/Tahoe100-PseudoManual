---
symbol: "MCUB"
type: "gene"
col: 64
ensembl_id: "ENSG00000005059"
name: "mitochondrial calcium uniporter dominant negative subunit beta"
location: "4q25"
module: 95
arm: "-"
pooled_cpm: 40.54
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# MCUB

*mitochondrial calcium uniporter dominant negative subunit beta* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.08× (z +5.4, q 4e-05, up in 1 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.24× (z +4.3, q 0.004, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.369× (z -28.5, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5F]] (+0.60, fdr 3e-05), [[C1orf21]] (+0.60, fdr 3e-05), [[MAD2L2]] (+0.59, fdr 7e-05); moves opposite to [[HEXIM2-AS1]] (-0.56, fdr 7e-05), [[BDNF-AS]] (-0.55, fdr 2e-04), [[LINC00174]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR161]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 64.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.4 | 4e-05 | 1/45 (SW 1088) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 0.004 | 16/45 (HEC-1-A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 64.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.369×** | -28.5 | 0e+00 | 42/45 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -19.6 | 0e+00 | 42/45 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -19.3 | 0e+00 | 40/45 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -13.6 | 6e-40 | 36/45 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.517×** | -13.4 | 1e-38 | 34/45 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.691×** | -10.6 | 4e-24 | 35/45 (SW1417, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.594×** | -10.5 | 6e-24 | 37/45 (A-172, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.602×** | -10.3 | 8e-23 | 28/45 (J82, A-172, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -10.0 | 9e-22 | 35/46 (SW 900, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.641×** | -8.6 | 3e-16 | 27/44 (RPMI-7951, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -8.3 | 6e-15 | 27/45 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -7.3 | 2e-11 | 22/45 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -7.0 | 1e-10 | 30/45 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.722×** | -6.6 | 2e-09 | 25/45 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -6.1 | 3e-08 | 25/45 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.576×** | -5.8 | 2e-07 | 27/45 (CFPAC-1, C32, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.657×** | -4.4 | 3e-04 | 20/45 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 64. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 106 | 0 | 20 (4 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.192× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 55.7 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -14.4) |
| [[A-172 (line)]] | wt | 86.1 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -29.7) |
| [[HOP62 (line)]] | alt | 45.0 | 0 | 10 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -17.6) |
| [[J82 (line)]] | alt | 47.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -24.8) |
| [[A549 (line)]] | wt | 40.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 32.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 32.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -16.0) |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -14.1) |
| [[SNU-1 (line)]] | wt | 80.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.229× (z -10.8) |
| [[SNU-423 (line)]] | alt | 34.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.4) |
| [[SW 900 (line)]] | alt | 44.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -11.2) |
| [[A498 (line)]] | wt | 44.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -25.3) |
| [[Hs 766T (line)]] | wt | 56.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 61.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -27.8) |
| [[NCI-H2347 (line)]] | alt | 71.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.4) |
| [[Panc 03.27 (line)]] | alt | 51.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.9) |
| [[RKO (line)]] | wt | 74.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -17.4) |
| [[BT-474 (line)]] | alt | 52.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.7) |
| [[H4 (line)]] | wt | 63.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 46.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 3 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.254× (z -11.8) |
| [[PANC-1 (line)]] | alt | 23.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 47.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.6) |
| [[A-427 (line)]] | wt | 72.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -18.8) |
| [[KATO III (line)]] | alt | 26.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -9.6) |
| [[SW 1271 (line)]] | alt | 70.9 | 0 | 2 | — | [[Isocorydine (drug)]] 0.5 µM 0.0738× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.2) |
| [[LoVo (line)]] | wt | 38.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.400× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 50.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0861× (z -9.5) |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.6) |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.469× (z -9.0) |
| [[SW48 (line)]] | wt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.1) |
| [[AN3 CA (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 64), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5F]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[C1orf21]] | +0.60 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[MAD2L2]] | +0.59 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[MPZL1]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[FXYD5]] | +0.56 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SPTLC2]] | +0.56 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[KHDRBS3]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[WASF3]] | +0.55 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[POGLUT2]] | +0.55 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[LSM11]] | +0.55 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[AP3M2]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TSPAN13]] | +0.54 | +0.56 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXIM2-AS1]] | -0.56 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[BDNF-AS]] | -0.55 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[LINC00174]] | -0.54 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[CRADD]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[USP40]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GOPC]] | -0.54 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[N4BP2L2]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.53 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[HCG11]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NFE2L2]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.52 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[SLC38A4-AS1]] | -0.51 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR161]] | B | GPR161 activity raises MCUB's level | lines that do not express GPR161 (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without GPR161 | 0.042 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PPP2R3A, NKAIN1 |
| [[RGS10]] | C | RGS10 activity raises MCUB's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without RGS10 | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (3.4, 6.8); signed map (-41.4, 17.2). **Vector** length 105, 27.9% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.1 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -2.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.8 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -19.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -28.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -10.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial calcium uniporter dominant negative subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,560,209-109,688,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20647; previously CCDC109B |
| Gene groups (HGNC) | MCU complex subunits |
| Reactome | 3 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWR8](https://www.uniprot.org/uniprotkb/Q9NWR8) (Calcium uniporter regulatory subunit MCUb, mitochondrial):

> Negative regulator of the mitochondrial calcium uniporter (MCU), a channel that mediates calcium uptake into the mitochondrial matrix. MCUB is required to limit mitochondrial calcium overload during stress. Acts as a dominant-negative regulator that displaces MCU from the functional uniplex complex and thereby decreases the association of calcium sensors MICU1 and MICU2, preventing channel gating. Mitochondrial calcium homeostasis plays key roles in mitochondrial metabolism. Acts as an …

**Summary**, from NCBI Gene [55013](https://www.ncbi.nlm.nih.gov/gene/55013):

> Enables calcium channel inhibitor activity. Involved in negative regulation of calcium import into the mitochondrion. Located in mitochondrial inner membrane. Part of uniplex complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26076) · Entrez [55013](https://www.ncbi.nlm.nih.gov/gene/55013) · UniProt [Q9NWR8](https://www.uniprot.org/uniprotkb/Q9NWR8) · Ensembl [ENSG00000005059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005059)

## Data

Gene col 64: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 64); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 64, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 64]; `tensor/DDL_lfc|DDL_z.npy` [64]; `embed/gene_vectors.npy` [64]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 64 or target_col == 64). Every well: [[MCUB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCUB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
