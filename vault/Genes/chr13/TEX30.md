---
symbol: "TEX30"
type: "gene"
col: 7502
ensembl_id: "ENSG00000151287"
name: "testis expressed 30"
location: "13q33.1"
module: 71
arm: "+"
pooled_cpm: 9.27
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# TEX30

*testis expressed 30* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.13× (z +10.2, q 2e-21, up in 37 of 45 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.47× (z +4.9, q 5e-05, up in 15 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.566× (z -4.0, q 0.034, down in 18 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.261×; ⚠ cell-cycle shift, explains ~60% of this change); [[Malotilate (drug)]] 0.05 µM in 1 line (SNU-1 0.0631×); [[Cobimetinib (drug)]] 5 µM in 1 line (BT-474 0.0811×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0902×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASF1B]] (+0.63, fdr 1e-05), [[FEN1]] (+0.62, fdr 1e-05), [[C9orf40]] (+0.62, fdr 7e-06); moves opposite to [[CTSD]] (-0.52, fdr 2e-05), [[IFITM10]] (-0.49, fdr 5e-05), [[GSN]] (-0.48, fdr 6e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.13×** | +10.2 | 2e-21 | 37/45 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.07×** | +9.8 | 4e-20 | 33/45 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.96×** | +9.0 | 3e-17 | 32/45 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.91×** | +8.4 | 7e-15 | 24/37 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.55×** | +8.3 | 1e-14 | 26/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.82×** | +7.8 | 8e-13 | 7/17 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.63×** | +6.5 | 5e-09 | 26/45 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.64×** | +6.4 | 9e-09 | 25/41 (J82, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.59×** | +6.0 | 1e-07 | 15/40 (SW480, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.56×** | +6.0 | 1e-07 | 18/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.50×** | +5.5 | 2e-06 | 20/40 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 5e-05 | 15/38 (HT-29, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +4.9 | 5e-05 | 18/42 (SW480, J82, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.40×** | +4.6 | 2e-04 | 14/36 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.5 | 3e-04 | 10/46 (J82, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.013 | 12/43 (HOP62, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.021 | 13/44 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.1 | 0.046 | 9/46 (LoVo, SHP-77, …) | rises with dose |  |
| [[Capivasertib (drug)]] 5 µM |  | **1.52×** | +2.9 | 0.073 | 1/37 (Hs 766T) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.261×; ⚠ cell-cycle shift, explains ~60% of this change); [[Malotilate (drug)]] 0.05 µM in 1 line (SNU-1 0.0631×); [[Cobimetinib (drug)]] 5 µM in 1 line (BT-474 0.0811×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0902×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -4.0 | 0.034 | 18/43 (HS-578T, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -3.8 | 0.038 | 9/39 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.789× | -3.2 | 0.25 | 6/46 (SW 1271, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.9) ⚠ cell-cycle shift, explains ~60% of this change |
| [[BT-474 (line)]] | alt | 6.27 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0811× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 6.78 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0902× (z -8.5) |
| [[SNU-1 (line)]] | wt | 8.57 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0631× (z -8.9) |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASF1B]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[FEN1]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[C9orf40]] | +0.62 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CCNE2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[LRR1]] | +0.58 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[E2F1]] | +0.56 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[POLR2D]] | +0.56 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNF695]] | +0.56 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[E2F7]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PSMC3IP]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[GINS4]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSD]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[IFITM10]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[GSN]] | -0.48 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[ST13]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ALDH3B1]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[QPRT]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ERP29]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ARL6IP5]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FAM204A]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[DNAH7]] | -0.46 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[ATP6V1A]] | -0.46 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CSDE1]] | -0.45 | -0.35 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEX30's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[QPRT]] | B | QPRT activity raises TEX30's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without QPRT | 0.0998 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.1, -48.4); signed map (-42.0, -45.1). **Vector** length 59.3, 9.52% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.2 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +3.7 | +8.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +1.6 | +1.6 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:102,765,888-102,773,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C13orf27 |
| Matched by | ensembl_id |

UniProt [Q5JUR7](https://www.uniprot.org/uniprotkb/Q5JUR7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25188) · Entrez [93081](https://www.ncbi.nlm.nih.gov/gene/93081) · UniProt [Q5JUR7](https://www.uniprot.org/uniprotkb/Q5JUR7) · Ensembl [ENSG00000151287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151287)

## Data

Gene col 7502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7502); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7502]; `tensor/DDL_lfc|DDL_z.npy` [7502]; `embed/gene_vectors.npy` [7502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7502 or target_col == 7502). Every well: [[TEX30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
