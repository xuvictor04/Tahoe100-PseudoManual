---
symbol: "AMY2B"
type: "gene"
col: 14221
ensembl_id: "ENSG00000240038"
name: "amylase alpha 2B"
location: "1p21.1"
module: 23
arm: "+"
pooled_cpm: 5.35
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# AMY2B

*amylase alpha 2B* — 1p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +11.1, q 6e-26, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.457× (z -6.9, q 3e-09, down in 25 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.355× (z -4.8, q 3e-04, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 0.0368×, NCI-H460 0.202×; ⚠ cell-cycle shift, explains ~40% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (RKO 0.0558×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.105×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (KATO III 0.0856×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0982×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRANCR]] (+0.75, fdr 1e-05), [[PPP1R3F]] (+0.74, fdr 1e-05), [[SPESP1]] (+0.72, fdr 1e-05); moves opposite to [[SH3PXD2B]] (-0.61, fdr 4e-04), [[CBR1]] (-0.60, fdr 1e-04), [[SLC25A11]] (-0.60, fdr 4e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +11.1 | 6e-26 | 34/39 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.1 | 3e-07 | 23/36 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.97×** | +5.9 | 5e-07 | 25/46 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +5.9 | 5e-07 | 6/10 (HEC-1-A, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +5.9 | 6e-07 | 22/41 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.3 | 8e-06 | 16/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.44×** | +4.4 | 7e-04 | 15/44 (SW480, LS 180, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +4.4 | 7e-04 | 14/40 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.020 | 9/44 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.18×** | +3.6 | 0.020 | 6/42 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.029 | 13/44 (LoVo, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.4 | 0.030 | 11/28 (HT-29, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.030 | 9/43 (C32, HEC-1-A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.063 | 5/47 (SW480, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.083 | 10/42 (LoVo, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14221.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 0.0368×, NCI-H460 0.202×; ⚠ cell-cycle shift, explains ~40% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (RKO 0.0558×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.105×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (KATO III 0.0856×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.457×** | -6.9 | 3e-09 | 25/38 (J82, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.474×** | -6.6 | 1e-08 | 25/45 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.484×** | -6.4 | 3e-08 | 26/47 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -4.8 | 3e-04 | 15/42 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.641×** | -3.8 | 0.018 | 19/30 (LoVo, HT-29, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.047 | 11/45 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -3.4 | 0.047 | 14/46 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.509× | -3.1 | 0.12 | 13/37 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.704× | -3.1 | 0.12 | 10/44 (Hs 766T, J82, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.693× | -3.1 | 0.13 | 10/42 (Hs 766T, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.105× (z -10.5) |
| [[KATO III (line)]] | alt | 6.55 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0368× (z -13.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0856× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 8.06 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.195× (z -8.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[LoVo (line)]] | wt | 4.08 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0887× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 7.92 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0982× (z -8.9) |
| [[RKO (line)]] | wt | 8.10 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0558× (z -11.4) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRANCR]] | +0.75 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R3F]] | +0.74 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.72 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.71 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[HEXIM2-AS1]] | +0.70 | +0.73 / +0.34 | both halves | 1e-04 |  |
| [[ATE1OSP]] | +0.70 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[ZNF213-AS1]] | +0.70 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LRRC37A3]] | +0.69 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[ENTPD3-AS1]] | +0.68 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[AHI1-DT]] | +0.68 | +0.68 / +0.38 | both halves | 7e-05 |  |
| [[PXDNL]] | +0.67 | +0.64 / +0.47 | both halves | 2e-05 | STRING 418 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.61 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[CBR1]] | -0.60 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SLC25A11]] | -0.60 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[THEM6]] | -0.59 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AMY2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02398]] | B | LINC02398 activity raises AMY2B's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without LINC02398 | 0.041 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[DENND5B-AS1]] | B | DENND5B-AS1 activity lowers AMY2B's level | lines that do not express DENND5B-AS1 (6) vs lines expressing it (44) | 1.81× higher at baseline in the lines without DENND5B-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: DBN1, DENND5B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.8, 18.1); signed map (26.7, -7.7). **Vector** length 61.3, 9.18% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | amylase alpha 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.1 — chr1:103,553,815-103,579,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AMY2 |
| Gene groups (HGNC) | Amylases alpha |
| Reactome | 2 pathways, smallest: Digestion; Digestion and absorption |
| Matched by | ensembl_id |

UniProt [P19961](https://www.uniprot.org/uniprotkb/P19961) carries no function annotation.

**Summary**, from NCBI Gene [280](https://www.ncbi.nlm.nih.gov/gene/280):

> Amylases are secreted proteins that hydrolyze 1,4-alpha-glucoside bonds in oligosaccharides and polysaccharides, and thus catalyze the first step in digestion of dietary starch and glycogen. The human genome has a cluster of several amylase genes that are expressed at high levels in either salivary gland or pancreas. This gene encodes an amylase isoenzyme produced by the pancreas. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:478) · Entrez [280](https://www.ncbi.nlm.nih.gov/gene/280) · UniProt [P19961](https://www.uniprot.org/uniprotkb/P19961) · Ensembl [ENSG00000240038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240038)

## Data

Gene col 14221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14221); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14221]; `tensor/DDL_lfc|DDL_z.npy` [14221]; `embed/gene_vectors.npy` [14221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14221 or target_col == 14221). Every well: [[AMY2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMY2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
