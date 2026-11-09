---
symbol: "TAS2R4"
type: "gene"
col: 4804
ensembl_id: "ENSG00000127364"
name: "taste 2 receptor member 4"
location: "7q34"
module: 23
arm: "+"
pooled_cpm: 4.43
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TAS2R4

*taste 2 receptor member 4* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.50× (z +7.8, q 2e-12, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.462× (z -6.6, q 2e-08, down in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.311× (z -5.3, q 4e-05, down in 21 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0454×, BT-474 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0963×; ⚠ cell-cycle shift, explains ~52% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (RKO 0.0472×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0759×); [[Pemetrexed (drug)]] 0.05 µM in 1 line (BT-474 0.0804×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASS4]] (+0.82, fdr 7e-06), [[CHD1-DT]] (+0.82, fdr 1e-05), [[MGAM]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.50×** | +7.8 | 2e-12 | 32/44 (NCI-H23, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.2 | 1e-10 | 26/38 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +7.0 | 4e-10 | 24/38 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +6.4 | 2e-08 | 22/40 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +5.7 | 1e-06 | 22/41 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +5.6 | 2e-06 | 14/48 (SW480, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.9 | 1e-04 | 10/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.92×** | +4.8 | 1e-04 | 15/44 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.72×** | +4.6 | 2e-04 | 12/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.001 | 16/40 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.0 | 0.003 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 13/46 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 10/46 (SW1417, NCI-H2030, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.015 | 14/45 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.5 | 0.020 | 9/26 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4804.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0454×, BT-474 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0963×; ⚠ cell-cycle shift, explains ~52% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (RKO 0.0472×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0759×); [[Pemetrexed (drug)]] 0.05 µM in 1 line (BT-474 0.0804×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.462×** | -6.6 | 2e-08 | 30/46 (PANC-1, SW480, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -5.3 | 4e-05 | 21/44 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.571×** | -4.8 | 3e-04 | 18/36 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -4.5 | 0.001 | 18/45 (hTERT-HPNE, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.598×** | -4.4 | 0.001 | 19/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.630×** | -4.0 | 0.006 | 16/44 (H4, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.631×** | -4.0 | 0.006 | 17/44 (RKO, NCI-H1792, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.513× | -3.0 | 0.19 | 14/37 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.17 | 0 | 4 (1 ⚠) | — | [[Pemetrexed (drug)]] 0.05 µM 0.0804× (z -9.1) |
| [[PANC-1 (line)]] | alt | 3.37 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0454× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SW480 (line)]] | alt | 5.99 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0963× (z -12.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 5.17 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0752× (z -8.7) |
| [[HOP62 (line)]] | alt | 3.97 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0583× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 5.04 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0873× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0759× (z -9.3) |
| [[RKO (line)]] | wt | 8.16 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0472× (z -11.5) |
| [[A-172 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASS4]] | +0.82 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.82 | +0.83 / +0.54 | both halves | 1e-05 |  |
| [[MGAM]] | +0.81 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[CDKL3]] | +0.80 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.79 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[PRANCR]] | +0.79 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[KLRA1P]] | +0.79 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.78 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[ZFHX2-AS1]] | +0.77 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.77 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[MSH4]] | +0.77 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.76 | +0.72 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAS2R4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF382]] | B | ZNF382 activity raises TAS2R4's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.17× lower at baseline in the lines without ZNF382 | 0.077 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[HDAC6]] | B | HDAC6 activity raises TAS2R4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.3, 16.9); signed map (25.8, -7.6). **Vector** length 68.4, 10.5% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +4.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.3 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.1 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | taste 2 receptor member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,776,674-141,781,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | T2R4 |
| Gene groups (HGNC) | Taste 2 receptors |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 8 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYW5](https://www.uniprot.org/uniprotkb/Q9NYW5) (Taste receptor type 2 member 4):

> Gustducin-coupled receptor for denatonium and N(6)-propyl-2-thiouracil implicated in the perception of bitter compounds in the oral cavity and the gastrointestinal tract. Signals through PLCB2 and the calcium-regulated cation channel TRPM5. In airway epithelial cells, binding of denatonium increases the intracellular calcium ion concentration and stimulates ciliary beat frequency.

**Summary**, from NCBI Gene [50832](https://www.ncbi.nlm.nih.gov/gene/50832):

> This gene encodes a member of a family of candidate taste receptors that are members of the G protein-coupled receptor superfamily and that are specifically expressed by taste receptor cells of the tongue and palate epithelia. These apparently intronless genes encode a 7-transmembrane receptor protein, functioning as a bitter taste receptor. This gene is clustered with another 3 candidate taste receptor genes in chromosome 7 and is genetically linked to loci that influence bitter perception. …

**Accessions** — [HGNC:14911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14911) · Entrez [50832](https://www.ncbi.nlm.nih.gov/gene/50832) · UniProt [Q9NYW5](https://www.uniprot.org/uniprotkb/Q9NYW5) · Ensembl [ENSG00000127364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127364)

## Data

Gene col 4804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4804); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4804]; `tensor/DDL_lfc|DDL_z.npy` [4804]; `embed/gene_vectors.npy` [4804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4804 or target_col == 4804). Every well: [[TAS2R4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAS2R4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
