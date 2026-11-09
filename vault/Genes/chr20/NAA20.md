---
symbol: "NAA20"
type: "gene"
col: 10381
ensembl_id: "ENSG00000173418"
name: "N-alpha-acetyltransferase 20, NatB catalytic subunit"
location: "20p11.23"
module: 33
arm: "+"
pooled_cpm: 48.66
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NAA20

*N-alpha-acetyltransferase 20, NatB catalytic subunit* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.26× (z +11.4, q 3e-27, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.698× (z -13.5, q 6e-39, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC123]] (+0.73, fdr 7e-06), [[ALG3]] (+0.71, fdr 7e-06), [[EARS2]] (+0.69, fdr 7e-06); moves opposite to [[PIM3]] (-0.54, fdr 1e-05), [[ABCA5]] (-0.54, fdr 2e-05), [[TRIM36]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +11.4 | 3e-27 | 41/49 (KATO III, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +10.4 | 5e-23 | 34/48 (HT-29, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +10.4 | 8e-23 | 31/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.6 | 3e-12 | 21/40 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +6.8 | 9e-10 | 28/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +6.7 | 2e-09 | 25/47 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.9 | 3e-07 | 26/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.24×** | +5.8 | 4e-07 | 25/49 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 6e-05 | 20/47 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.7 | 2e-04 | 18/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 3e-04 | 19/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 6/48 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.0 | 0.003 | 13/35 (HOP62, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.012 | 9/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.14× | +3.5 | 0.015 | 12/48 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.049 | 8/48 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.056 | 4/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.058 | 10/48 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.058 | 2/46 (HOP62, HCT15) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.698×** | -13.5 | 6e-39 | 35/48 (LoVo, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -9.2 | 1e-17 | 31/48 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.808×** | -5.7 | 3e-06 | 21/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.798×** | -5.1 | 6e-05 | 20/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.829×** | -4.8 | 2e-04 | 19/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -4.7 | 2e-04 | 13/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.0 | 0.005 | 20/49 (RKO, A-427, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.865× | -3.7 | 0.014 | 8/48 (SW 1088, AsPC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.5 | 0.029 | 17/48 (RKO, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.873× | -3.5 | 0.031 | 16/47 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.913× | -3.4 | 0.036 | 16/48 (LoVo, RKO, …) | top dose only |  |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.891× | -3.1 | 0.100 | 3/48 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.889× | -3.0 | 0.100 | 10/49 (LoVo, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.895× | -3.0 | 0.100 | 5/48 (LoVo, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.100 | 13/48 (A-172, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -17.0) |
| [[KATO III (line)]] | alt | 73.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.31× (z +10.8) | — |
| [[RKO (line)]] | wt | 71.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -9.9) ⚠ cell-cycle shift, explains ~1% of this change |
| [[A-172 (line)]] | wt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.4) |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.7) |
| [[HOP62 (line)]] | alt | 51.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.613× (z -8.8) |
| [[HT-29 (line)]] | alt | 42.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +11.6) | — |
| [[J82 (line)]] | alt | 41.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 55.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | — |
| [[PANC-1 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.95× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 56.3 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0804× (z -8.6) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC123]] | +0.73 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[ALG3]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[EARS2]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LSG1]] | +0.67 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TOMM70]] | +0.66 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[CTU1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.64 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[TIMM23]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[SAMM50]] | +0.63 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[HSF1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CNOT7]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[WDR3]] | +0.62 | +0.68 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TRIM36]] | -0.53 | -0.48 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NAA20's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.2, -30.7); signed map (-14.8, -56.2). **Vector** length 85.8, 17.8% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.9 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 20, NatB catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:20,017,310-20,033,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1002M8.1, NAT3; previously NAT5 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [P61599](https://www.uniprot.org/uniprotkb/P61599) (N-alpha-acetyltransferase 20):

> Catalytic subunit of the NatB complex which catalyzes acetylation of the N-terminal methionine residues of peptides beginning with Met-Asp, Met-Glu, Met-Asn and Met-Gln. Proteins with cell cycle functions are overrepresented in the pool of NatB substrates. Required for maintaining the structure and function of actomyosin fibers and for proper cellular migration.

**Summary**, from NCBI Gene [51126](https://www.ncbi.nlm.nih.gov/gene/51126):

> NAT5 is a component of N-acetyltransferase complex B (NatB). Human NatB performs cotranslational N(alpha)-terminal acetylation of methionine residues when they are followed by asparagine (Starheim et al., 2008 [PubMed 18570629]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:15908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15908) · Entrez [51126](https://www.ncbi.nlm.nih.gov/gene/51126) · UniProt [P61599](https://www.uniprot.org/uniprotkb/P61599) · Ensembl [ENSG00000173418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173418)

## Data

Gene col 10381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10381); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10381]; `tensor/DDL_lfc|DDL_z.npy` [10381]; `embed/gene_vectors.npy` [10381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10381 or target_col == 10381). Every well: [[NAA20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
