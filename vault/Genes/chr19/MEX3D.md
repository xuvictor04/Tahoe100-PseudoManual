---
symbol: "MEX3D"
type: "gene"
col: 11198
ensembl_id: "ENSG00000181588"
name: "mex-3 RNA binding family member D"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 13.25
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MEX3D

*mex-3 RNA binding family member D* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.43× (z +9.0, q 1e-16, up in 23 of 25 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.56× (z +3.4, q 0.046, up in 21 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 7.68×, LoVo 6.73×, HOP62 5.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.599× (z -3.9, q 0.058, down in 29 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.125×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.285×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.71, fdr 1e-05), [[METRN]] (+0.64, fdr 4e-05), [[PIP5K1C]] (+0.64, fdr 1e-05); moves opposite to [[KICS2]] (-0.60, fdr 3e-05), [[CCT7]] (-0.58, fdr 1e-05), [[MCTS1]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RTF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 7.68×, LoVo 6.73×, HOP62 5.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.43×** | +9.0 | 1e-16 | 23/25 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.82×** | +7.9 | 8e-13 | 31/36 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.86×** | +4.4 | 0.002 | 23/32 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.71×** | +4.1 | 0.005 | 28/45 (NCI-H1792, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.005 | 22/40 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.73×** | +4.0 | 0.006 | 27/42 (SNU-423, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.64×** | +3.8 | 0.012 | 24/46 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.56×** | +3.4 | 0.046 | 17/46 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.046 | 21/44 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.2 | 0.076 | 20/44 (A498, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | 1.48× | +3.0 | 0.13 | 20/44 (SW480, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.125×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.285×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.599×** | -3.9 | 0.058 | 29/46 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.656× | -3.2 | 0.23 | 18/43 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.637× | -3.2 | 0.23 | 22/45 (RKO, C32, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.639× | -3.1 | 0.23 | 12/46 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.751× | -3.1 | 0.23 | 18/46 (SW 1271, MIA PaCa-2, …) | all doses, flat |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.649× | -3.0 | 0.23 | 14/45 (SW48, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -12.0) |
| [[PANC-1 (line)]] | alt | 11.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.68× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.71 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[METRN]] | +0.64 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[PIP5K1C]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SLC66A2]] | +0.64 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PSMD9]] | +0.63 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GIT1]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[NELFB]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MPND]] | +0.62 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[A1BG-AS1]] | +0.61 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ULK1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.61 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RAB40C]] | +0.61 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KICS2]] | -0.60 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CCT7]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MCTS1]] | -0.55 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[NEK9]] | -0.54 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[LIN7C]] | -0.54 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ZNF816]] | -0.53 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[PTGR2]] | -0.53 | -0.36 / -0.52 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises MEX3D's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without STARD9 | 0.063 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers MEX3D's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTF1]] | C | MEX3D's natural level weakens RTF1's drug response | MEX3D's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.03; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.1, -0.7); signed map (-26.8, 8.2). **Vector** length 68.9, 17.3% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.7 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.6 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.3 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mex-3 RNA binding family member D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,554,672-1,568,325 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tino, KIAA2031, OK/SW-cl.4, RNF193; previously RKHD1 |
| Gene groups (HGNC) | Ring finger proteins; Mex-3 RNA binding family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XN8](https://www.uniprot.org/uniprotkb/Q86XN8) (RNA-binding protein MEX3D):

> RNA binding protein, may be involved in post-transcriptional regulatory mechanisms.

**Summary**, from NCBI Gene [399664](https://www.ncbi.nlm.nih.gov/gene/399664):

> Enables mRNA 3'-UTR AU-rich region binding activity. Predicted to be involved in mRNA destabilization and mRNA localization resulting in post-transcriptional regulation of gene expression. Located in nucleus and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16734) · Entrez [399664](https://www.ncbi.nlm.nih.gov/gene/399664) · UniProt [Q86XN8](https://www.uniprot.org/uniprotkb/Q86XN8) · Ensembl [ENSG00000181588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181588)

## Data

Gene col 11198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11198); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11198]; `tensor/DDL_lfc|DDL_z.npy` [11198]; `embed/gene_vectors.npy` [11198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11198 or target_col == 11198). Every well: [[MEX3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEX3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
