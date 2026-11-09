---
symbol: "INAFM2"
type: "gene"
col: 15185
ensembl_id: "ENSG00000259330"
name: "InaF motif containing 2"
location: "15q15.1"
module: 11
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# INAFM2

*InaF motif containing 2* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +11.5, q 1e-27, up in 24 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.596× (z -4.7, q 0.001, down in 13 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (C32 0.0605×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (C32 0.0890×); [[DT-061 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0832×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENDOG]] (+0.58, fdr 7e-06), [[TLCD3A]] (+0.57, fdr 4e-05), [[PDE12]] (+0.54, fdr 3e-05); moves opposite to [[CALCOCO2]] (-0.55, fdr 1e-05), [[RTN3]] (-0.53, fdr 2e-05), [[TTC1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[APLN]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DPY30]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +11.5 | 1e-27 | 24/31 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.93×** | +5.8 | 3e-06 | 1/4 (PANC-1) | all doses, flat | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.6 | 5e-06 | 15/42 (NCI-H2030, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.3 | 1e-05 | 5/14 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.76×** | +4.8 | 2e-04 | 3/7 (NCI-H1792, HOP62, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.66×** | +4.6 | 4e-04 | 7/18 (MIA PaCa-2, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +4.5 | 6e-04 | 11/33 (Panc 03.27, CFPAC-1, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.63×** | +4.3 | 0.001 | 11/26 (SW480, A498, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.51×** | +3.7 | 0.012 | 5/18 (SW480, C32, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.4 | 0.035 | 4/15 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +3.4 | 0.035 | 8/37 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.096 | 4/31 (SK-MEL-2, BT-474, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15185.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (C32 0.0605×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (C32 0.0890×); [[DT-061 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0832×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -4.7 | 0.001 | 13/41 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.651×** | -3.7 | 0.058 | 12/36 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.663×** | -3.6 | 0.058 | 10/32 (SW 900, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Bergenin (drug)]] 5 µM |  | 0.782× | -3.2 | 0.20 | 8/41 (Hs 766T, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 6.97 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0605× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 4.47 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0832× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 3.07 | 0 | 1 | — | [[Adagrasib (drug)]] 5 µM 0.0710× (z -8.5) |
| [[A-172 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENDOG]] | +0.58 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TLCD3A]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PDE12]] | +0.54 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SERPINB6]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[ZNF672]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[DDX24]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[C8orf58]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[GRPEL1]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MGAT2]] | +0.50 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[FURIN]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[RUNDC1]] | +0.50 | +0.37 / +0.50 | both halves | 7e-05 |  |
| [[CCNJ]] | +0.50 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCOCO2]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RTN3]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TTC1]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[MALAT1]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[STX7]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CYB5R4]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ZNF235]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TOM1L1]] | -0.47 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[TALAM1]] | -0.47 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[NBDY]] | -0.46 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[PRKCI]] | -0.44 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[DYNC2LI1]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLN]] | B | APLN activity raises INAFM2's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without APLN | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CDA]] | B | CDA activity lowers INAFM2's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without CDA | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[PSMB5]] | B | PSMB5 activity raises INAFM2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers INAFM2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY30]] | C | INAFM2 activity lowers DPY30's level | lines that do not express INAFM2 (4) vs lines expressing it (46) | 1.48× higher at baseline in the lines without INAFM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EXO5; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.242). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (19.9, -10.7); signed map (16.5, -11.8). **Vector** length 44.9, 5.43% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.5 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.1 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +1.1 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.0 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | InaF motif containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,323,692-40,326,715 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OGU1; previously LINC00984 |
| Matched by | ensembl_id |

UniProt [P0DMQ5](https://www.uniprot.org/uniprotkb/P0DMQ5) carries no function annotation.

**Summary**, from NCBI Gene [100505573](https://www.ncbi.nlm.nih.gov/gene/100505573):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:35165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35165) · Entrez [100505573](https://www.ncbi.nlm.nih.gov/gene/100505573) · UniProt [P0DMQ5](https://www.uniprot.org/uniprotkb/P0DMQ5) · Ensembl [ENSG00000259330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259330)

## Data

Gene col 15185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15185); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15185]; `tensor/DDL_lfc|DDL_z.npy` [15185]; `embed/gene_vectors.npy` [15185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15185 or target_col == 15185). Every well: [[INAFM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INAFM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
