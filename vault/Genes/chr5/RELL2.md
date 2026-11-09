---
symbol: "RELL2"
type: "gene"
col: 8974
ensembl_id: "ENSG00000164620"
name: "RELT like 2"
location: "5q31.3"
module: 184
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# RELL2

*RELT like 2* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.60× (z +23.5, q 0e+00, up in 30 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0725×); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0546×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB6]] (+0.61, fdr 1e-05), [[FAM219A]] (+0.60, fdr 3e-05), [[KCTD5]] (+0.59, fdr 3e-05); moves opposite to [[GUSBP2-1]] (-0.63, fdr 4e-05), [[PRPF4B]] (-0.62, fdr 3e-05), [[NHLRC3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.60×** | +23.5 | 0e+00 | 30/31 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.30×** | +14.1 | 2e-42 | 34/35 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.64×** | +13.2 | 1e-37 | 28/42 (HEC-1-A, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.51×** | +12.1 | 2e-31 | 36/43 (HOP62, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.42×** | +11.9 | 2e-30 | 33/39 (LoVo, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +11.4 | 4e-28 | 22/26 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.38×** | +11.3 | 1e-27 | 29/33 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.11×** | +10.9 | 6e-26 | 32/40 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.62×** | +8.9 | 3e-17 | 0/2 | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.52×** | +8.9 | 3e-17 | 28/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.42×** | +8.5 | 8e-16 | 23/39 (SW1417, HEC-1-A, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.07×** | +7.0 | 1e-10 | 14/29 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +6.9 | 2e-10 | 18/39 (HEC-1-A, HT-29, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.02×** | +6.8 | 6e-10 | 18/40 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.08×** | +6.5 | 3e-09 | 1/4 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +6.2 | 2e-08 | 16/36 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +5.5 | 1e-06 | 13/39 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.5 | 1e-06 | 11/42 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.001 | 9/41 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.002 | 6/36 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0725×); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0546×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 5 µM |  | 0.691× | -3.5 | 0.15 | 6/33 (HOP62, A-172, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.701× | -3.5 | 0.15 | 6/43 (A-172, A549, …) | rises with dose | position effect removed |
| [[Rifaximin (drug)]] 0.5 µM |  | 0.715× | -3.3 | 0.17 | 7/40 (C32, H4, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.792× | -3.2 | 0.17 | 9/41 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Busulfan (drug)]] 5 µM |  | 0.796× | -3.2 | 0.17 | 7/39 (AN3 CA, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.1) | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM 0.0546× (z -8.7) |
| [[HOP62 (line)]] | alt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 1.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 8.30 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0725× (z -10.1) |
| [[SW480 (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB6]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[FAM219A]] | +0.60 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[KCTD5]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[NIT1]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TUBA4A]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ORMDL2]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[P4HA2]] | +0.56 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[ATG9A]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[HOMER1]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RBPMS2]] | +0.54 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PTRH1]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PSMD8]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP2-1]] | -0.63 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[PRPF4B]] | -0.62 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[NHLRC3]] | -0.61 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MRPS31P4]] | -0.53 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ALDH7A1]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[SREK1]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.50 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[NDUFA5]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[PUM2]] | -0.50 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[ZZZ3]] | -0.49 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[EHMT2]] | -0.49 | -0.46 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RELL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-19.6, -3.7); signed map (-40.3, 30.8). **Vector** length 52.3, 7.29% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +23.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +13.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +0.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.4 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | RELT like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,636,950-141,641,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90583; previously C5orf16 |
| Gene groups (HGNC) | RELT family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC24](https://www.uniprot.org/uniprotkb/Q8NC24) (RELT-like protein 2):

> Induces activation of MAPK14/p38 cascade, when overexpressed. Induces apoptosis, when overexpressed.

**Summary**, from NCBI Gene [285613](https://www.ncbi.nlm.nih.gov/gene/285613):

> Predicted to enable collagen binding activity. Involved in positive regulation of p38MAPK cascade. Predicted to be located in basement membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26902) · Entrez [285613](https://www.ncbi.nlm.nih.gov/gene/285613) · UniProt [Q8NC24](https://www.uniprot.org/uniprotkb/Q8NC24) · Ensembl [ENSG00000164620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164620)

## Data

Gene col 8974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8974); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8974]; `tensor/DDL_lfc|DDL_z.npy` [8974]; `embed/gene_vectors.npy` [8974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8974 or target_col == 8974). Every well: [[RELL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
