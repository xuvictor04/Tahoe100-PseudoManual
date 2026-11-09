---
symbol: "BEND6"
type: "gene"
col: 7580
ensembl_id: "ENSG00000151917"
name: "BEN domain containing 6"
location: "6p12.1"
module: 10
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 36
n_dd_up: 40
n_dd_down: 2
n_dd_up_clean: 33
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# BEND6

*BEN domain containing 6* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +14.8, q 0e+00, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Cytarabine (drug)]] 5 µM: 0.664× (z -3.9, q 0.037, down in 7 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.274×, NCI-H23 0.0938×, A-427 0.206×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.307×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.277×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.309×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01013]] (+0.67, fdr 1e-05), [[MRAS]] (+0.65, fdr 7e-06), [[CNN3-DT]] (+0.61, fdr 1e-05); moves opposite to [[SMYD4]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); 8 go from it, the strongest it → [[CNN3-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +14.8 | 0e+00 | 22/30 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.12×** | +13.4 | 9e-39 | 9/12 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +12.7 | 1e-34 | 13/17 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.56×** | +11.6 | 6e-29 | 10/12 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.39×** | +8.6 | 8e-16 | 26/33 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.3 | 2e-11 | 17/32 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.5 | 3e-06 | 13/33 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.9 | 8e-05 | 8/31 (LoVo, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.81×** | +4.8 | 8e-05 | 8/31 (PANC-1, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.41×** | +4.8 | 8e-05 | 13/32 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +4.7 | 1e-04 | 11/31 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 2e-04 | 15/29 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.5 | 2e-04 | 5/23 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +4.5 | 2e-04 | 11/32 (C32, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 5e-04 | 14/31 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.55×** | +4.3 | 5e-04 | 9/32 (NCI-H460, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.2 | 9e-04 | 9/28 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.0 | 0.002 | 6/32 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.002 | 11/32 (LOX-IMVI, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7580.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.274×, NCI-H23 0.0938×, A-427 0.206×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.307×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.277×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.309×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.037 | 7/32 (C-33 A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -3.8 | 0.037 | 12/32 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.712× | -3.4 | 0.15 | 16/32 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.687× | -3.1 | 0.30 | 13/32 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 3.35 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +10.3) | [[Harringtonine (drug)]] 0.05 µM 0.0891× (z -9.1) |
| [[A-172 (line)]] | wt | 6.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +11.8) | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +11.5) | — |
| [[A549 (line)]] | wt | 1.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +8.5) | — |
| [[J82 (line)]] | alt | 4.65 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0578× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 7.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.48× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01013]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MRAS]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CNN3-DT]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[UNC5C]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ATP6V1E2]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[KATNAL2]] | +0.59 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[LINC01116]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ME1]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.56 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[HOXD3]] | +0.55 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[VLDLR-AS1]] | +0.55 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MXRA8]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD4]] | -0.47 | -0.50 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises BEND6's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without ASNSP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[MAP2K1]] | B | MAP2K1 activity lowers BEND6's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |
| [[PCDH18]] | B | PCDH18 activity raises BEND6's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without PCDH18 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[MXRA8]] | B | MXRA8 activity raises BEND6's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without MXRA8 | 0.098 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[HHIPL2]] | C | HHIPL2 activity raises BEND6's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.69× lower at baseline in the lines without HHIPL2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises BEND6's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 2.84× lower at baseline in the lines without DPY19L2 | 0.048 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNN3-DT]] | B | BEND6 activity raises CNN3-DT's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without BEND6 | 0.037 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[UCHL1]] | B | BEND6 activity raises UCHL1's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 5.35× lower at baseline in the lines without BEND6 | 0.069 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[CCDC3]] | B | BEND6 activity raises CCDC3's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without BEND6 | 0.091 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[EID3]] | B | BEND6 activity lowers EID3's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 1.37× higher at baseline in the lines without BEND6 | 0.098 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[NREP]] | C | BEND6 activity raises NREP's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 4.61× lower at baseline in the lines without BEND6 | 0.048 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ; co-absent with the target |
| [[BVES-AS1]] | C | BEND6 activity raises BVES-AS1's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 2.11× lower at baseline in the lines without BEND6 | 0.079 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ; co-absent with the target |
| [[DPY19L2]] | C | BEND6 activity raises DPY19L2's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 2.99× lower at baseline in the lines without BEND6 | 0.084 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ; co-absent with the target |
| [[SUSD5]] | C | BEND6 activity raises SUSD5's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 2.75× lower at baseline in the lines without BEND6 | 0.0998 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.4, 33.3); signed map (38.3, -0.2). **Vector** length 66.5, 14.9% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +14.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | BEN domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:56,955,107-57,027,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30162, bA203B9.1; previously C6orf65 |
| Gene groups (HGNC) | BEN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SZJ8](https://www.uniprot.org/uniprotkb/Q5SZJ8) (BEN domain-containing protein 6):

> Acts as a corepressor of recombining binding protein suppressor hairless (RBPJ) and inhibits Notch signaling in neural stem cells, thereby opposing their self-renewal and promoting neurogenesis.

**Summary**, from NCBI Gene [221336](https://www.ncbi.nlm.nih.gov/gene/221336):

> Enables transcription corepressor activity. Predicted to be involved in negative regulation of Notch signaling pathway and positive regulation of neuron differentiation. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20871) · Entrez [221336](https://www.ncbi.nlm.nih.gov/gene/221336) · UniProt [Q5SZJ8](https://www.uniprot.org/uniprotkb/Q5SZJ8) · Ensembl [ENSG00000151917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151917)

## Data

Gene col 7580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7580); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7580]; `tensor/DDL_lfc|DDL_z.npy` [7580]; `embed/gene_vectors.npy` [7580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7580 or target_col == 7580). Every well: [[BEND6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEND6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
