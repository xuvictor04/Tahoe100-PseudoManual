---
symbol: "TEN1"
type: "gene"
col: 15075
ensembl_id: "ENSG00000257949"
name: "TEN1 subunit of CST complex"
location: "17q25.1"
module: 51
arm: "+"
pooled_cpm: 9.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TEN1

*TEN1 subunit of CST complex* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +10.2, q 1e-21, up in 12 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.95× (z +5.3, q 1e-05, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.457× (z -12.0, q 2e-30, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF713]] (+0.65, fdr 7e-06), [[RBM4B]] (+0.61, fdr 7e-06), [[CLN3]] (+0.57, fdr 2e-05); moves opposite to [[TTC13]] (-0.53, fdr 2e-05), [[VANGL1]] (-0.49, fdr 2e-05), [[TBC1D4]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +10.2 | 1e-21 | 12/18 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +9.5 | 6e-19 | 20/34 (SW 900, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +9.5 | 6e-19 | 17/24 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.3 | 1e-05 | 17/46 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 7/47 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +4.0 | 0.005 | 16/46 (NCI-H460, A498, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.070 | 5/48 (PANC-1, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.070 | 6/40 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.091 | 6/47 (PANC-1, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.092 | 3/47 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.10 | 10/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.22× | +3.0 | 0.12 | 14/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.457×** | -12.0 | 2e-30 | 40/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.461×** | -11.9 | 5e-30 | 41/47 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.458×** | -11.5 | 2e-28 | 35/45 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.474×** | -11.4 | 4e-28 | 41/47 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.541×** | -9.4 | 5e-19 | 34/47 (NCI-H1792, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.568×** | -8.3 | 8e-15 | 28/44 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.730×** | -6.8 | 8e-10 | 25/44 (SW480, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.446×** | -6.5 | 7e-09 | 26/47 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -6.2 | 3e-08 | 19/48 (A-427, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -5.4 | 3e-06 | 20/48 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.728×** | -4.7 | 2e-04 | 10/46 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -4.6 | 2e-04 | 5/48 (HepG2/C3A, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -4.6 | 2e-04 | 16/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.744×** | -4.5 | 2e-04 | 14/44 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.757×** | -4.3 | 8e-04 | 15/42 (HCT15, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.023 | 11/47 (SNU-423, AN3 CA, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.801×** | -3.4 | 0.023 | 7/46 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +12.7) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -9.4) |
| [[RKO (line)]] | wt | 9.32 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.7) |
| [[SW480 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -9.4) |
| [[A-172 (line)]] | wt | 7.75 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -11.3) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[AsPC-1 (line)]] | alt | 7.04 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.134× (z -8.9) |
| [[H4 (line)]] | wt | 9.08 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0454× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.49 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.210× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 8.60 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0487× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 7.26 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0610× (z -12.7) |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.323× (z -8.6) |
| [[A498 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF713]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RBM4B]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CLN3]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SPATA24]] | +0.57 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[AP5Z1]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[NBDY]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TRMO]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[POMZP3]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[KPNA5]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[STK11IP]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[YJU2]] | +0.54 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[BORCS7]] | +0.53 | +0.34 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC13]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[VANGL1]] | -0.49 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TBC1D4]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[GSTCD]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ELOVL1]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[EIF5A]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TUBG1]] | -0.46 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[LSM4]] | -0.45 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TEN1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers TEN1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.8, 13.9); signed map (-12.5, -12.5). **Vector** length 63.9, 9.78% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +5.4 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | -1.0 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.5 | +0.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.1 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.0 | -4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | TEN1 subunit of CST complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,979,240-76,000,586 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39785; previously C17orf106 |
| Gene groups (HGNC) | CST complex |
| Reactome | 7 pathways, smallest: Telomere C-strand synthesis initiation; Polymerase switching on the C-strand of the telomere; Telomere C-strand (Lagging Strand) Synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WV5](https://www.uniprot.org/uniprotkb/Q86WV5) (CST complex subunit TEN1):

> Component of the CST complex proposed to act as a specialized replication factor promoting DNA replication under conditions of replication stress or natural replication barriers such as the telomere duplex. The CST complex binds single-stranded DNA with high affinity in a sequence-independent manner, while isolated subunits bind DNA with low affinity by themselves. Initially the CST complex has been proposed to protect telomeres from DNA degradation. However, the CST complex has been shown to …

**Summary**, from NCBI Gene [100134934](https://www.ncbi.nlm.nih.gov/gene/100134934):

> C17ORF106, or TEN1, appears to function in a telomere-associated complex with STN1 (OBFC1; MIM 613128) and CTC1 (C17ORF68; MIM 613129) (Miyake et al., 2009 [PubMed 19854130]).[supplied by OMIM, Nov 2009]

**Accessions** — [HGNC:37242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37242) · Entrez [100134934](https://www.ncbi.nlm.nih.gov/gene/100134934) · UniProt [Q86WV5](https://www.uniprot.org/uniprotkb/Q86WV5) · Ensembl [ENSG00000257949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257949)

## Data

Gene col 15075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15075); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15075]; `tensor/DDL_lfc|DDL_z.npy` [15075]; `embed/gene_vectors.npy` [15075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15075 or target_col == 15075). Every well: [[TEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
