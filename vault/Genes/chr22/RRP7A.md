---
symbol: "RRP7A"
type: "gene"
col: 12113
ensembl_id: "ENSG00000189306"
name: "ribosomal RNA processing 7 homolog A"
location: "22q13.2"
module: 5
arm: "+"
pooled_cpm: 25.75
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RRP7A

*ribosomal RNA processing 7 homolog A* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.33× (z +10.6, q 1e-23, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.723× (z -4.0, q 0.021, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0951×; ⚠ cell-cycle shift, explains ~85% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.249×; ⚠ cell-cycle shift, would explain all of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0884×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7BP-1]] (+0.76, fdr 7e-06, ⚠ same locus), [[EIF6]] (+0.74, fdr 7e-06), [[METTL2B]] (+0.70, fdr 7e-06), [[NIP7]] (+0.69, fdr 7e-06); moves opposite to [[PRCP]] (-0.71, fdr 1e-05), [[TXNDC16]] (-0.64, fdr 2e-05), [[ARL6IP5]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +10.6 | 1e-23 | 43/47 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.16×** | +9.7 | 9e-20 | 41/48 (HS-578T, SHP-77, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +8.6 | 2e-15 | 36/44 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.87×** | +7.9 | 5e-13 | 39/48 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.75×** | +7.0 | 3e-10 | 33/48 (SHP-77, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +6.4 | 1e-08 | 36/48 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.60×** | +5.9 | 3e-07 | 28/44 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.60×** | +5.7 | 9e-07 | 21/36 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +5.6 | 2e-06 | 33/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.8 | 1e-04 | 27/47 (NCI-H460, A498, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +4.6 | 2e-04 | 26/48 (NCI-H1573, A498, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.4 | 4e-04 | 25/47 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.28×** | +4.3 | 6e-04 | 25/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +4.1 | 0.002 | 25/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.1 | 0.002 | 22/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.053 | 16/48 (SHP-77, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12113.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0951×; ⚠ cell-cycle shift, explains ~85% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.249×; ⚠ cell-cycle shift, would explain all of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0884×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.021 | 27/47 (A498, SNU-1, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.803×** | -4.0 | 0.021 | 19/48 (HS-578T, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.761× | -3.4 | 0.13 | 12/48 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.790× | -3.0 | 0.37 | 7/48 (HCT15, J82, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0951× (z -11.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0884× (z -9.1) |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[HEC-1-A (line)]] | alt | 33.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 45.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.37× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.60× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 81.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.55× (z +10.4) | — |
| [[SW480 (line)]] | alt | 29.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.69× (z +11.2) | — |
| [[A-172 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | ⚠ same locus (35.4 kb, same strand: neighbours can correlate without regulation) |
| [[EIF6]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 | same gene group |
| [[METTL2B]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[NIP7]] | +0.69 | +0.76 / +0.70 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 756 |
| [[TRMT10C]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 | pathway: rRNA processing |
| [[METTL2A]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 | same gene group; STRING 845 |
| [[ZNF562]] | +0.65 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PWP2]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 996 |
| [[TRMT61A]] | +0.64 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[RRP1]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 771 |
| [[TWNK]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 991 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRCP]] | -0.71 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.64 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ARL6IP5]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[GNAS]] | -0.63 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[PAIP2B]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KAT2B]] | -0.58 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SGCE]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[RCN2]] | -0.58 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[LNX2]] | -0.57 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[HOXA3]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity lowers RRP7A's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without HOXA3 | 0.058 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.5, -30.3); signed map (2.7, -45.6). **Vector** length 83.7, 19.6% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +4.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -2.7 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 7 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,508,344-42,519,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-96, Rrp7 |
| Gene groups (HGNC) | UTPc subcomplex; Ribosome biogenesis factors |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3A4](https://www.uniprot.org/uniprotkb/Q9Y3A4) (Ribosomal RNA-processing protein 7 homolog A):

> Nucleolar protein that is involved in ribosomal RNA (rRNA) processing. Also plays a role in primary cilia resorption, and cell cycle progression in neurogenesis and neocortex development. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA …

**Summary**, from NCBI Gene [27341](https://www.ncbi.nlm.nih.gov/gene/27341):

> Enables RNA binding activity. Involved in cilium disassembly; protein localization to nucleolus; and ribosome biogenesis. Located in centrosome; cilium; and nucleolus. Part of small-subunit processome. Implicated in primary autosomal recessive microcephaly 28. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24286) · Entrez [27341](https://www.ncbi.nlm.nih.gov/gene/27341) · UniProt [Q9Y3A4](https://www.uniprot.org/uniprotkb/Q9Y3A4) · Ensembl [ENSG00000189306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189306)

## Data

Gene col 12113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12113); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12113]; `tensor/DDL_lfc|DDL_z.npy` [12113]; `embed/gene_vectors.npy` [12113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12113 or target_col == 12113). Every well: [[RRP7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
