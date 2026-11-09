---
symbol: "TRIM47"
type: "gene"
col: 5329
ensembl_id: "ENSG00000132481"
name: "tripartite motif containing 47"
location: "17q25.1"
module: 11
arm: "+"
pooled_cpm: 6.67
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TRIM47

*tripartite motif containing 47* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.53× (z +15.7, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.251× (z -12.2, q 1e-31, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.72, fdr 7e-06), [[RPP25L]] (+0.71, fdr 7e-06), [[NAIF1]] (+0.68, fdr 7e-06); moves opposite to [[STRAP]] (-0.70, fdr 7e-06), [[BTAF1]] (-0.69, fdr 7e-06), [[TM9SF2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[DLX2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.53×** | +15.7 | 0e+00 | 31/34 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.93×** | +13.5 | 3e-39 | 37/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.73×** | +11.6 | 7e-29 | 29/34 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.91×** | +9.4 | 7e-19 | 39/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +5.6 | 2e-06 | 24/40 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.4 | 8e-06 | 12/30 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.4 | 0.001 | 16/32 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.48×** | +3.4 | 0.040 | 10/31 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.090 | 11/37 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.47× | +3.0 | 0.13 | 11/36 (A549, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.251×** | -12.2 | 1e-31 | 37/43 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.268×** | -11.7 | 5e-29 | 37/41 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.348×** | -9.4 | 2e-18 | 36/42 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -5.4 | 1e-05 | 25/43 (SK-MEL-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.662×** | -3.7 | 0.028 | 17/42 (KATO III, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 0.500× | -3.2 | 0.12 | 10/41 (SHP-77, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.507× | -3.2 | 0.13 | 12/37 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 9.88 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 10.3× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.0467× (z -13.4) |
| [[PANC-1 (line)]] | alt | 8.33 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +16.2) | — |
| [[A-172 (line)]] | wt | 26.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0880× (z -16.3) |
| [[SW480 (line)]] | alt | 6.79 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0934× (z -12.9) |
| [[A498 (line)]] | wt | 17.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.273× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 4.37 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.0713× (z -9.6) |
| [[HOP62 (line)]] | alt | 4.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 9.16 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.0499× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 4.52 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0795× (z -9.0) |
| [[A549 (line)]] | wt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 4.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 6.28 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0411× (z -10.0) |
| [[Hs 766T (line)]] | wt | 5.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.12 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 11.8× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 4.76 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0358× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.155× (z -9.2) |
| [[SHP-77 (line)]] | alt | 5.38 | 0 | 1 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0836× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 5.21 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0428× (z -10.5) |
| [[SNU-423 (line)]] | alt | 2.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +8.5) | — |
| [[A-427 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.68 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[C1orf131]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SDSL]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TMEM265]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.67 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[PBDC1]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.67 | +0.68 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.70 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[BTAF1]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TXNDC12]] | -0.65 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[EEF1AKMT2]] | -0.65 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[PDIA4]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.65 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[NUDT21]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[CA5B]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[ILRUN]] | -0.63 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TRIM47's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EDN1]] | B | EDN1 activity raises TRIM47's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.32× lower at baseline in the lines without EDN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX2]] | C | TRIM47 activity lowers DLX2's level | lines that do not express TRIM47 (4) vs lines expressing it (46) | 3.66× higher at baseline in the lines without TRIM47 | 0.073 | ⚠ few lines (4 vs 46); across organs; also absent: PERP, SOX13, ABCA5 |
| [[SHROOM1]] | C | TRIM47 activity raises SHROOM1's level | lines that do not express TRIM47 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without TRIM47 | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: PERP, SOX13, ABCA5 |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.4, 6.5); signed map (3.3, -19.6). **Vector** length 90.8, 21.4% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -9.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,874,164-75,878,581 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GOA, RNF100 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LD4](https://www.uniprot.org/uniprotkb/Q96LD4) (E3 ubiquitin-protein ligase TRIM47):

> E3 ubiquitin-protein ligase that mediates the ubiquitination and proteasomal degradation of CYLD. It also mediates the ubiquitination and proteasomal degradation of ADAM17.

**Summary**, from NCBI Gene [91107](https://www.ncbi.nlm.nih.gov/gene/91107):

> Enables ubiquitin protein ligase activity. Involved in protein ubiquitination. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19020) · Entrez [91107](https://www.ncbi.nlm.nih.gov/gene/91107) · UniProt [Q96LD4](https://www.uniprot.org/uniprotkb/Q96LD4) · Ensembl [ENSG00000132481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132481)

## Data

Gene col 5329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5329); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5329]; `tensor/DDL_lfc|DDL_z.npy` [5329]; `embed/gene_vectors.npy` [5329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5329 or target_col == 5329). Every well: [[TRIM47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
