---
symbol: "EGFEM1P"
type: "gene"
col: 13034
ensembl_id: "ENSG00000206120"
name: "EGF like and EMI domain containing 1, pseudogene"
location: "3q26.2"
module: 9
arm: "+"
pooled_cpm: 9.92
n_lines_expressing: 30
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# EGFEM1P

*EGF like and EMI domain containing 1, pseudogene* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.10× (z +22.2, q 0e+00, up in 18 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW480 0.102×); [[Simotinib (drug)]] 5 µM in 1 line (HOP62 0.0817×; ⚠ toxic); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.197×; ⚠ cell-cycle shift, explains ~84% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMD]] (+0.72, fdr 7e-06), [[PIEZO2]] (+0.65, fdr 7e-06), [[PCDH11X]] (+0.65, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[KCNIP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.10×** | +22.2 | 0e+00 | 18/24 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.89×** | +21.3 | 0e+00 | 20/24 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.55×** | +14.7 | 0e+00 | 23/27 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.13×** | +12.7 | 1e-34 | 11/21 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.84×** | +11.6 | 7e-29 | 20/26 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.95×** | +11.5 | 8e-29 | 8/15 (CFPAC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +11.2 | 5e-27 | 19/24 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +9.4 | 4e-19 | 17/26 (HOP62, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +9.2 | 2e-18 | 21/26 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.80×** | +9.2 | 2e-18 | 19/27 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.28×** | +9.1 | 3e-18 | 23/27 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.25×** | +9.0 | 1e-17 | 23/27 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.32×** | +8.6 | 3e-16 | 7/17 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.17×** | +8.3 | 5e-15 | 11/23 (NCI-H460, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.08×** | +7.8 | 2e-13 | 17/25 (NCI-H460, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +4.6 | 1e-04 | 12/26 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.001 | 12/26 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.002 | 10/26 (C32, SK-MEL-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.007 | 7/25 (NCI-H1792, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.86×** | +3.6 | 0.008 | 5/25 (HOP62, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.052 | 2/26 (hTERT-HPNE, HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13034.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW480 0.102×); [[Simotinib (drug)]] 5 µM in 1 line (HOP62 0.0817×; ⚠ toxic); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.197×; ⚠ cell-cycle shift, explains ~84% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentagastrin (drug)]] 5 µM |  | 0.819× | -3.2 | 0.36 | 1/28 (BT-474) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.822× | -3.2 | 0.36 | 4/27 (AN3 CA, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.599× | -3.0 | 0.36 | 12/25 (hTERT-HPNE, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.65 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 5.56 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +16.6) | [[Simotinib (drug)]] 5 µM 0.0817× (z -10.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 70.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -10.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SW480 (line)]] | alt | 6.27 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +11.4) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.102× (z -11.4) |
| [[A-172 (line)]] | wt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +15.3) | — |
| [[A-427 (line)]] | wt | 5.72 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.39× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +9.9) | — |
| [[J82 (line)]] | alt | 9.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -9.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 4.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 3.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +8.9) | — |
| [[A498 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMD]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PIEZO2]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PCDH11X]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CDH18]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SLC9A9]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[ADAMTS3]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.63 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[NKAIN3]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LDB2]] | +0.61 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[FMN2]] | +0.61 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[OFCC1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 | same gene group |
| [[NPAS3]] | +0.61 | +0.68 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EGFEM1P's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CSMD3]] | B | CSMD3 activity raises EGFEM1P's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.21× lower at baseline in the lines without CSMD3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[NEGR1]] | C | NEGR1 activity raises EGFEM1P's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.05× lower at baseline in the lines without NEGR1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[MMP16]] | C | MMP16 activity raises EGFEM1P's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 3.83× lower at baseline in the lines without MMP16 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNIP4]] | B | EGFEM1P activity raises KCNIP4's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without EGFEM1P | 0.042 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent |
| [[GRIK2]] | C | EGFEM1P activity raises GRIK2's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 3.31× lower at baseline in the lines without EGFEM1P | 0.012 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |
| [[NEGR1]] | C | EGFEM1P activity raises NEGR1's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 3.74× lower at baseline in the lines without EGFEM1P | 0.051 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |
| [[MCC]] | C | EGFEM1P activity raises MCC's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without EGFEM1P | 0.052 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |
| [[MMP16]] | C | EGFEM1P activity raises MMP16's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 7.04× lower at baseline in the lines without EGFEM1P | 0.061 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |
| [[RGS7]] | C | EGFEM1P activity raises RGS7's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 3.22× lower at baseline in the lines without EGFEM1P | 0.072 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, 29.5); signed map (39.9, 31.0). **Vector** length 69.7, 17.5% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +21.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +7.1 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.5 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +22.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -1.9 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.6 | +6.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EGF like and EMI domain containing 1, pseudogene |
| Locus type | pseudogene |
| Location | 3q26.2 — chr3:168,249,941-168,821,335 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously C3orf50, NCRNA00259 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [Q0D2K5](https://www.uniprot.org/uniprotkb/Q0D2K5) carries no function annotation.

**Summary**, from NCBI Gene [93556](https://www.ncbi.nlm.nih.gov/gene/93556):

> Predicted to enable scavenger receptor activity. Predicted to be involved in vesicle-mediated transport. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25149) · Entrez [93556](https://www.ncbi.nlm.nih.gov/gene/93556) · UniProt [Q0D2K5](https://www.uniprot.org/uniprotkb/Q0D2K5) · Ensembl [ENSG00000206120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206120)

## Data

Gene col 13034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13034); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13034]; `tensor/DDL_lfc|DDL_z.npy` [13034]; `embed/gene_vectors.npy` [13034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13034 or target_col == 13034). Every well: [[EGFEM1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGFEM1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
