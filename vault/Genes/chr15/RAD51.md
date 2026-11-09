---
symbol: "RAD51"
type: "gene"
col: 576
ensembl_id: "ENSG00000051180"
name: "RAD51 recombinase"
location: "15q15.1"
module: 6
arm: "+"
pooled_cpm: 15.21
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RAD51

*RAD51 recombinase* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.66× (z +7.0, q 1e-09, up in 10 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change. The strongest without an alert is [[Raltitrexed (drug)]] 0.5 µM: 1.27× (z +3.5, q 0.034, up in 10 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.442× (z -11.7, q 1e-28, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCA]] (+0.90, fdr 7e-06), [[CENPK]] (+0.89, fdr 7e-06), [[RAD54L]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **1.66×** | +7.0 | 1e-09 | 10/23 (HT-29, Hs 766T, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +4.9 | 2e-04 | 18/46 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.23×** | +4.2 | 0.005 | 13/47 (SW480, HT-29, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.22×** | +4.1 | 0.005 | 13/45 (PANC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.32×** | +4.0 | 0.008 | 16/44 (PANC-1, SW480, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.29×** | +3.7 | 0.019 | 13/45 (PANC-1, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.28×** | +3.6 | 0.024 | 13/45 (PANC-1, SW480, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.19× | +3.6 | 0.024 | 12/47 (SW480, LoVo, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.034 | 10/43 (HT-29, LoVo, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.042 | 10/44 (RPMI-7951, Hs 766T, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.057 | 9/46 (A-427, PANC-1, …) | top dose only | plate-row cell shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.24×** | +3.1 | 0.091 | 11/43 (SW480, LoVo, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.23× | +3.0 | 0.11 | 7/47 (A-427, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.442×** | -11.7 | 1e-28 | 30/44 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -9.3 | 3e-18 | 28/46 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.680×** | -7.9 | 6e-13 | 26/46 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.569×** | -7.8 | 6e-13 | 26/46 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.633×** | -6.5 | 6e-09 | 24/44 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.634×** | -6.5 | 6e-09 | 24/45 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.633×** | -6.2 | 3e-08 | 26/45 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -6.1 | 6e-08 | 27/47 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -6.0 | 1e-07 | 22/45 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -5.3 | 6e-06 | 23/46 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.772×** | -5.3 | 7e-06 | 19/47 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.702×** | -5.1 | 1e-05 | 23/46 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.703×** | -4.9 | 4e-05 | 17/44 (A-427, HEC-1-A, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.630×** | -4.8 | 7e-05 | 16/47 (KATO III, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.732×** | -4.5 | 2e-04 | 20/46 (HOP62, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.809×** | -3.7 | 0.007 | 13/46 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.835× | -3.7 | 0.007 | 11/46 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.008 | 11/44 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.013 | 16/44 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.020 | 15/46 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.793×** | -3.3 | 0.020 | 10/45 (A-427, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 38.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.2) |
| [[A-172 (line)]] | wt | 19.1 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.168× (z -10.7) |
| [[A498 (line)]] | wt | 28.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -15.1) |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 5 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.113× (z -10.3) |
| [[A-427 (line)]] | wt | 23.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.8) |
| [[PANC-1 (line)]] | alt | 17.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.05× (z +9.3) ⚠ cell-cycle shift, explains ~82% of this change | [[Bortezomib (drug)]] 5 µM 0.0587× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0495× (z -13.8) |
| [[C32 (line)]] | wt | 9.33 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0874× (z -9.7) |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0579× (z -8.5) |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0997× (z -9.6) |
| [[SW 900 (line)]] | alt | 5.50 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0736× (z -8.5) |
| [[SW480 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCA]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; STRING 936 |
| [[CENPK]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | STRING 448 |
| [[RAD54L]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | STRING 992 |
| [[EXO1]] | +0.89 | +0.87 / +0.86 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 997 |
| [[CHAF1A]] | +0.88 | +0.83 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[MELK]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 763 |
| [[BLM]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 998 |
| [[CDC45]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | STRING 927 |
| [[DTL]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | STRING 722 |
| [[RFC4]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 888 |
| [[WDHD1]] | +0.86 | +0.79 / +0.86 | both halves | 7e-06 | STRING 882 |
| [[POLQ]] | +0.86 | +0.81 / +0.87 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 822 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises RAD51's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without E2F8 | 0.036 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises RAD51's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without CDC25A | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises RAD51's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[PBK]] | C | PBK activity raises RAD51's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without PBK | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises RAD51's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without MYBL2 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.895). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.9, -46.4); signed map (-39.0, -43.1). **Vector** length 124, 33.4% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.67 to 65); *DNA strand elongation* (reactome, mean cos +0.71 to 28); *DNA Replication* (reactome, mean cos +0.71 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.0 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.5 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +3.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.6 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.3 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RAD51 recombinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,694,774-40,732,340 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsRad51, HsT16930, BRCC5, FANCR; previously RAD51A, RECA |
| Gene groups (HGNC) | FA complementation groups; RAD51 paralogs |
| Hallmark sets | DNA_REPAIR |
| Reactome | 25 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06609](https://www.uniprot.org/uniprotkb/Q06609) (DNA repair protein RAD51 homolog 1):

> Homologous DNA recombinase that catalyzes strand exchange, a key step in DNA repair through homologous recombination (HR). Binds to single-stranded DNA (ssDNA) in an ATP-dependent manner to form nucleoprotein filaments which are essential for the homology search and strand exchange. Catalyzes the recognition of homology and strand exchange between homologous DNA partners to form a joint molecule between a processed DNA break and the repair template. RAD51 targeting to ssDNA promotes removal of …

**Summary**, from NCBI Gene [5888](https://www.ncbi.nlm.nih.gov/gene/5888):

> The protein encoded by this gene is a member of the RAD51 protein family. RAD51 family members are highly similar to bacterial RecA and Saccharomyces cerevisiae Rad51, and are known to be involved in the homologous recombination and repair of DNA. This protein can interact with the ssDNA-binding protein RPA and RAD52, and it is thought to play roles in homologous pairing and strand transfer of DNA. This protein is also found to interact with BRCA1 and BRCA2, which may be important for the …

**Accessions** — [HGNC:9817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9817) · Entrez [5888](https://www.ncbi.nlm.nih.gov/gene/5888) · UniProt [Q06609](https://www.uniprot.org/uniprotkb/Q06609) · Ensembl [ENSG00000051180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051180)

## Data

Gene col 576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 576); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 576]; `tensor/DDL_lfc|DDL_z.npy` [576]; `embed/gene_vectors.npy` [576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 576 or target_col == 576). Every well: [[RAD51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
