---
symbol: "FPGS"
type: "gene"
col: 5929
ensembl_id: "ENSG00000136877"
name: "folylpolyglutamate synthase"
location: "9q34.11"
module: 2
arm: "+"
pooled_cpm: 25.4
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FPGS

*folylpolyglutamate synthase* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.41× (z +7.0, q 1e-09, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 3.69×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.716× (z -6.7, q 9e-09, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP3]] (+0.72, fdr 7e-06), [[ST6GALNAC6-1]] (+0.72, fdr 7e-06), [[ST6GALNAC6]] (+0.67, fdr 7e-06); moves opposite to [[COQ9]] (-0.56, fdr 1e-05), [[CASD1]] (-0.56, fdr 2e-05), [[COG4]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5929.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 3.69×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +7.0 | 1e-09 | 25/47 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.3 | 8e-08 | 23/43 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +5.4 | 1e-05 | 21/40 (RKO, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +4.3 | 0.003 | 16/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +4.1 | 0.004 | 19/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.0 | 0.006 | 14/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.013 | 18/48 (COLO 205, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.078 | 14/33 (Panc 03.27, NCI-H2347, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.094 | 14/47 (C-33 A, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.094 | 15/47 (LS 180, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.716×** | -6.7 | 9e-09 | 28/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -6.2 | 1e-07 | 25/48 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.771×** | -5.3 | 3e-05 | 23/47 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -5.0 | 1e-04 | 23/47 (hTERT-HPNE, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.797×** | -4.6 | 6e-04 | 22/47 (A498, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.864× | -4.1 | 0.003 | 17/47 (BT-474, KATO III, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.815×** | -3.9 | 0.006 | 19/47 (NCI-H23, BT-474, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.837× | -3.6 | 0.024 | 16/47 (NCI-H1573, SW 1271, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.723×** | -3.4 | 0.039 | 17/46 (SNU-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.3 | 0.049 | 18/48 (SNU-1, SW 1271, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -3.2 | 0.063 | 3/48 (MIA PaCa-2, SW 1088, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.896× | -3.1 | 0.089 | 6/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.854× | -3.0 | 0.100 | 17/47 (AN3 CA, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 56.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -16.8) ⚠ toxic; cell-cycle shift, explains ~72% of this change |
| [[LoVo (line)]] | wt | 27.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -9.0) |
| [[LS 180 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.295× (z -10.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0970× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ST6GALNAC6-1]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ST6GALNAC6]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[GPSM1]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ZNF771]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD11-OT1-1]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MON1A]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ZNF276]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ9]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[CASD1]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[COG4]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[AGA]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[CSTF1]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CTDSPL2]] | -0.52 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ATRAID]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[WBP11]] | -0.51 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[RAB14]] | -0.51 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[TET2]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DECR1]] | -0.51 | -0.52 / -0.46 | both halves | 2e-05 | STRING 621 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers FPGS's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (37.6, -21.7); signed map (-45.6, -2.8). **Vector** length 78.6, 14.5% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.6 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.9 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -6.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | folylpolyglutamate synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,794,597-127,814,327 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ligases |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05932](https://www.uniprot.org/uniprotkb/Q05932) (Folylpolyglutamate synthase, mitochondrial):

> Catalyzes conversion of folates to polyglutamate derivatives allowing concentration of folate compounds in the cell and the intracellular retention of these cofactors, which are important substrates for most of the folate-dependent enzymes that are involved in one-carbon transfer reactions involved in purine, pyrimidine and amino acid synthesis. Unsubstituted reduced folates are the preferred substrates. Metabolizes methotrexate (MTX) to polyglutamates.

**Summary**, from NCBI Gene [2356](https://www.ncbi.nlm.nih.gov/gene/2356):

> This gene encodes the folylpolyglutamate synthetase enzyme. This enzyme has a central role in establishing and maintaining both cytosolic and mitochondrial folylpolyglutamate concentrations and, therefore, is essential for folate homeostasis and the survival of proliferating cells. This enzyme catalyzes the ATP-dependent addition of glutamate moieties to folate and folate derivatives. Alternative splicing results in transcript variants encoding different isoforms. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:3824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3824) · Entrez [2356](https://www.ncbi.nlm.nih.gov/gene/2356) · UniProt [Q05932](https://www.uniprot.org/uniprotkb/Q05932) · Ensembl [ENSG00000136877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136877)

## Data

Gene col 5929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5929); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5929]; `tensor/DDL_lfc|DDL_z.npy` [5929]; `embed/gene_vectors.npy` [5929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5929 or target_col == 5929). Every well: [[FPGS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FPGS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
