---
symbol: "BCDIN3D"
type: "gene"
col: 11844
ensembl_id: "ENSG00000186666"
name: "BCDIN3 domain containing RNA methyltransferase"
location: "12q13.12"
module: 10
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# BCDIN3D

*BCDIN3 domain containing RNA methyltransferase* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +12.5, q 6e-33, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.608× (z -5.6, q 2e-05, down in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.122×, KATO III 0.191×; ⚠ toxic; transcription drop); [[Berbamine (dihydrochloride) (drug)]] 0.05 µM in 1 line (LS 180 0.0506×); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0897×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM26-AS1]] (+0.84, fdr 7e-06), [[FAM200A]] (+0.81, fdr 7e-06), [[ZNF181]] (+0.79, fdr 7e-06); moves opposite to [[IGSF8]] (-0.69, fdr 3e-05), [[CAMK2G]] (-0.68, fdr 5e-05), [[LPCAT4]] (-0.68, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +12.5 | 6e-33 | 27/38 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +11.3 | 4e-27 | 35/37 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +11.1 | 2e-26 | 26/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.48×** | +10.2 | 3e-22 | 33/44 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +9.6 | 7e-20 | 27/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +8.2 | 2e-14 | 9/19 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +7.7 | 1e-12 | 16/44 (LS 180, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.91×** | +7.3 | 3e-11 | 20/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.2 | 4e-08 | 13/30 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.9 | 2e-07 | 4/5 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.4 | 4e-06 | 2/4 (HOP62, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-05 | 11/45 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 8/44 (A498, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.6 | 2e-04 | 8/46 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.004 | 6/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.008 | 5/22 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.012 | 8/43 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.014 | 8/35 (NCI-H460, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11844.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.122×, KATO III 0.191×; ⚠ toxic; transcription drop); [[Berbamine (dihydrochloride) (drug)]] 0.05 µM in 1 line (LS 180 0.0506×); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.608×** | -5.6 | 2e-05 | 16/45 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -5.2 | 5e-05 | 14/32 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -4.1 | 0.008 | 9/48 (SHP-77, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -3.7 | 0.034 | 10/41 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.744× | -3.3 | 0.11 | 13/45 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Naproxen (drug)]] 5 µM |  | 0.754× | -3.0 | 0.24 | 8/38 (NCI-H2030, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 2.94 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +10.8) | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0897× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.90 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.36× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.122× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 3.83 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0506× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 4.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +8.6) | — |
| [[A-172 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26-AS1]] | +0.84 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.81 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[ZNF181]] | +0.79 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[ZNF407-AS1]] | +0.79 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.79 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.79 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[RAB30-DT]] | +0.79 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[TIGD6]] | +0.78 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[PPP3CB-AS1]] | +0.78 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[LIG4]] | +0.77 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[ZNF594]] | +0.77 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[BDNF-AS]] | +0.76 | +0.81 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | -0.69 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[CAMK2G]] | -0.68 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.68 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[L2HGDH]] | -0.67 | -0.60 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BCDIN3D's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises BCDIN3D's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.0, 13.6); signed map (12.3, -21.4). **Vector** length 56.2, 7.24% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | -0.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | BCDIN3 domain containing RNA methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,836,043-49,843,106 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 2 pathways, smallest: MicroRNA (miRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5W3](https://www.uniprot.org/uniprotkb/Q7Z5W3) (RNA 5'-monophosphate methyltransferase):

> O-methyltransferase that specifically monomethylates 5'-monophosphate of cytoplasmic histidyl tRNA (tRNA(His)), acting as a capping enzyme by protecting tRNA(His) from cleavage by DICER1. Also able, with less efficiently, to methylate the 5' monophosphate of a subset of pre-miRNAs, acting as a negative regulator of miRNA processing. The 5' monophosphate of pre-miRNAs is recognized by DICER1 and is required for pre-miRNAs processing: methylation at this position reduces the processing of …

**Summary**, from NCBI Gene [144233](https://www.ncbi.nlm.nih.gov/gene/144233):

> This gene encodes an RNA methyltransferase which belongs to the rossmann fold methyltransferase family, and serves as a 5'-methylphosphate capping enzyme that is specific for cytoplasmic histidyl tRNA. The encoded protein contains an S-adenosylmethionine binding domain and uses the methyl group donor, S-adenosylmethionine. This gene is overexpressed in breast cancer cells, and is related to the tumorigenic phenotype and poor prognosis of breast cancer. The encoded protein is thought to promote …

**Accessions** — [HGNC:27050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27050) · Entrez [144233](https://www.ncbi.nlm.nih.gov/gene/144233) · UniProt [Q7Z5W3](https://www.uniprot.org/uniprotkb/Q7Z5W3) · Ensembl [ENSG00000186666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186666)

## Data

Gene col 11844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11844); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11844]; `tensor/DDL_lfc|DDL_z.npy` [11844]; `embed/gene_vectors.npy` [11844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11844 or target_col == 11844). Every well: [[BCDIN3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCDIN3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
