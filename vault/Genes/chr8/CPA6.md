---
symbol: "CPA6"
type: "gene"
col: 9062
ensembl_id: "ENSG00000165078"
name: "carboxypeptidase A6"
location: "8q13.2"
module: 81
arm: "+"
pooled_cpm: 5.87
n_lines_expressing: 36
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# CPA6

*carboxypeptidase A6* — 8q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.08× (z +18.5, q 0e+00, up in 7 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +15.4, q 0e+00, up in 14 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.605× (z -5.2, q 1e-04, down in 13 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.0419×, NCI-H460 0.130×, NCI-H1792 0.196×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 0.0446×, NCI-H460 0.153×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.112×, hTERT-HPNE 0.207×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.133×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.102×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCKR]] (+0.63, fdr 1e-05), [[NRIP3]] (+0.57, fdr 1e-05), [[SH2D2A]] (+0.56, fdr 3e-05); moves opposite to [[AGFG2]] (-0.45, fdr 2e-04), [[CCND3]] (-0.44, fdr 6e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00698]] → it (grade B ⚠); 4 go from it, the strongest it → [[AGPAT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.08×** | +18.5 | 0e+00 | 7/16 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +15.4 | 0e+00 | 14/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.66×** | +15.2 | 0e+00 | 2/6 (HS-578T, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +10.9 | 3e-25 | 4/10 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.68×** | +10.1 | 5e-22 | 19/29 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +9.6 | 7e-20 | 19/32 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.55×** | +9.1 | 9e-18 | 17/28 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.23×** | +8.2 | 1e-14 | 18/29 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.08×** | +7.5 | 4e-12 | 11/30 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.26×** | +6.3 | 1e-08 | 5/9 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.18×** | +5.7 | 6e-07 | 7/30 (NCI-H1792, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 5e-06 | 10/27 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.006 | 4/19 (LS 180, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.009 | 2/22 (AsPC-1, HOP62) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.7 | 0.010 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.027 | 0/21 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.028 | 1/25 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9062.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.0419×, NCI-H460 0.130×, NCI-H1792 0.196×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 0.0446×, NCI-H460 0.153×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.112×, hTERT-HPNE 0.207×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.133×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -5.2 | 1e-04 | 13/29 (hTERT-HPNE, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.785× | -3.5 | 0.12 | 7/30 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.720× | -3.4 | 0.13 | 9/28 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.18 | 8/30 (C32, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 165 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0419× (z -24.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -14.3) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.112× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 7.64 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 13.6× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0912× (z -8.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 22.4 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.31× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0645× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCKR]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SH2D2A]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[LINC00698]] | +0.54 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[RBFOX1]] | +0.54 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[GLI2]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SLCO1C1]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[DGKG]] | +0.50 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[DYNC1I1]] | +0.50 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.50 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[OAF]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGFG2]] | -0.45 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[CCND3]] | -0.44 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00698]] | B | LINC00698 activity raises CPA6's level | lines that do not express LINC00698 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without LINC00698 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253642, HEPH, SRRM4; maybe low, not absent |
| [[PDE3A]] | B | PDE3A activity raises CPA6's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without PDE3A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[OCIAD2]] | B | OCIAD2 activity lowers CPA6's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 2.47× higher at baseline in the lines without OCIAD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[LINC01684]] | B | LINC01684 activity raises CPA6's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without LINC01684 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent |
| [[EGF]] | B | EGF activity raises CPA6's level | lines that do not express EGF (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without EGF | 0.035 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[USP9Y]] | B | USP9Y activity raises CPA6's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without USP9Y | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1 |
| [[IL33]] | B | IL33 activity raises CPA6's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without IL33 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411 |
| [[PASD1]] | B | PASD1 activity raises CPA6's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.14× lower at baseline in the lines without PASD1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGPAT4]] | B | CPA6 activity raises AGPAT4's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without CPA6 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[MMP1]] | B | CPA6 activity raises MMP1's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without CPA6 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[PDE3A]] | B | CPA6 activity raises PDE3A's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 2.87× lower at baseline in the lines without CPA6 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[AGFG2]] | B | CPA6 activity lowers AGFG2's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 1.34× higher at baseline in the lines without CPA6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, -1.4); signed map (13.3, 54.2). **Vector** length 54.6, 9.64% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +18.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.2 — chr8:67,422,038-67,746,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPAH |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4T0](https://www.uniprot.org/uniprotkb/Q8N4T0) (Carboxypeptidase A6):

> May be involved in the proteolytic inactivation of enkephalins and neurotensin in some brain areas. May convert inactive angiotensin I into the biologically active angiotensin II. Releases a C-terminal amino acid, with preference for large hydrophobic C-terminal amino acids and shows only very weak activity toward small amino acids and histidine.

**Summary**, from NCBI Gene [57094](https://www.ncbi.nlm.nih.gov/gene/57094):

> The gene encodes a member of the peptidase M14 family of metallocarboxypeptidases. The encoded preproprotein is proteolytically processed to generate the mature enzyme, which catalyzes the release of large hydrophobic C-terminal amino acids. This enzyme has functions ranging from digestion of food to selective biosynthesis of neuroendocrine peptides. Mutations in this gene may be linked to epilepsy and febrile seizures, and a translocation t(6;8)(q26;q13) involving this gene has been associated …

**Accessions** — [HGNC:17245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17245) · Entrez [57094](https://www.ncbi.nlm.nih.gov/gene/57094) · UniProt [Q8N4T0](https://www.uniprot.org/uniprotkb/Q8N4T0) · Ensembl [ENSG00000165078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165078)

## Data

Gene col 9062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9062); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9062]; `tensor/DDL_lfc|DDL_z.npy` [9062]; `embed/gene_vectors.npy` [9062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9062 or target_col == 9062). Every well: [[CPA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
