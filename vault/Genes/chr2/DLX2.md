---
symbol: "DLX2"
type: "gene"
col: 3729
ensembl_id: "ENSG00000115844"
name: "distal-less homeobox 2"
location: "2q31.1"
module: 68
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 42
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# DLX2

*distal-less homeobox 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 20.0× (z +29.0, q 0e+00, up in 29 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H661 0.0791×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATA3]] (+0.65, fdr 7e-06), [[EIF4EBP3]] (+0.64, fdr 7e-06), [[MAP3K2-DT]] (+0.63, fdr 7e-06); moves opposite to [[STRAP]] (-0.68, fdr 7e-06), [[SNRNP40]] (-0.60, fdr 1e-05), [[OPA1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[IRF7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **20.0×** | +29.0 | 0e+00 | 29/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **14.5×** | +17.6 | 0e+00 | 31/34 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.1×** | +16.5 | 0e+00 | 25/26 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.54×** | +14.6 | 0e+00 | 25/27 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.98×** | +11.0 | 4e-26 | 34/39 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.52×** | +10.3 | 5e-23 | 32/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **4.13×** | +9.7 | 2e-20 | 32/39 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.05×** | +9.2 | 2e-18 | 9/11 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.83×** | +9.2 | 2e-18 | 20/24 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.66×** | +8.9 | 4e-17 | 28/38 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.18×** | +7.5 | 3e-12 | 13/39 (A-172, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.73×** | +6.9 | 3e-10 | 26/39 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.34×** | +5.8 | 3e-07 | 17/39 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.34×** | +5.8 | 3e-07 | 21/35 (NCI-H460, SW 900, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.23×** | +5.3 | 5e-06 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +5.0 | 2e-05 | 14/38 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +4.7 | 9e-05 | 15/34 (A-172, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.3 | 5e-04 | 10/40 (CFPAC-1, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +2.9 | 0.085 | 8/35 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H661 0.0791×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.624× | -3.3 | 0.60 | 12/38 (H4, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.40 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 33.9× (z +16.5) | — |
| [[PANC-1 (line)]] | alt | 4.72 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +20.7) | — |
| [[A498 (line)]] | wt | 0.841 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 87.9× (z +10.0) | — |
| [[A-172 (line)]] | wt | 3.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 0.798 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 91.5× (z +10.5) | — |
| [[C32 (line)]] | wt | 2.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.4× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.2× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 0.926 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 1.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.3× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 1.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.1× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 0.862 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.4× (z +9.1) | — |
| [[J82 (line)]] | alt | 1.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.2× (z +11.9) | — |
| [[LoVo (line)]] | wt | 1.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 6.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 1.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.0× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 5.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +10.4) | — |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0791× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[RPMI-7951 (line)]] | alt | 3.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 2.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.2× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 4.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +11.6) | — |
| [[SW480 (line)]] | alt | 2.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +12.1) | — |
| [[A-427 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATA3]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MAP3K2-DT]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[SLC31A2]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[FBXO48]] | +0.63 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TEF]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.61 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[LINC02307]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[GRINA]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ERF]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.68 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SNRNP40]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[OPA1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ANAPC10]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.56 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.56 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PARN]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[NAPG]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.55 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[IPO11]] | -0.55 | -0.65 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DLX2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CHGB]] | B | CHGB activity raises DLX2's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without CHGB | 0.042 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[DUSP10]] | B | DUSP10 activity lowers DLX2's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 1.75× higher at baseline in the lines without DUSP10 | 0.046 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[XKR7]] | B | XKR7 activity raises DLX2's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.63× lower at baseline in the lines without XKR7 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[TNK1]] | B | TNK1 activity lowers DLX2's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.76× higher at baseline in the lines without TNK1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[BMP2]] | B | BMP2 activity lowers DLX2's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.87× higher at baseline in the lines without BMP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[MEX3B]] | C | MEX3B activity raises DLX2's level | lines that do not express MEX3B (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without MEX3B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIF17, DPF1, CNTNAP1; its own permutation p |
| [[TRIM47]] | C | TRIM47 activity lowers DLX2's level | lines that do not express TRIM47 (4) vs lines expressing it (46) | 3.66× higher at baseline in the lines without TRIM47 | 0.073 | ⚠ few lines (4 vs 46); across organs; also absent: PERP, SOX13, ABCA5 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF7]] | B | DLX2 activity lowers IRF7's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.80× higher at baseline in the lines without DLX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[SPEN]] | B | DLX2 activity raises SPEN's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without DLX2 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[SYNGAP1]] | B | DLX2 activity raises SYNGAP1's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without DLX2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[FOXD1]] | B | DLX2 activity raises FOXD1's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 3.58× lower at baseline in the lines without DLX2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[VASN]] | B | DLX2 activity raises VASN's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without DLX2 | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[HDAC9]] | B | DLX2 activity raises HDAC9's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without DLX2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[BCOR]] | B | DLX2 activity raises BCOR's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.15× lower at baseline in the lines without DLX2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[PLEKHG3]] | B | DLX2 activity lowers PLEKHG3's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.63× higher at baseline in the lines without DLX2 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[NANOS3]] | B | DLX2 activity raises NANOS3's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without DLX2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (20.4, -3.8); signed map (5.2, -10.3). **Vector** length 54.6, 8.99% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +29.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +16.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | distal-less homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:172,099,438-172,102,900 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TES-1 |
| Gene groups (HGNC) | Distal-less homeobox family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07687](https://www.uniprot.org/uniprotkb/Q07687) (Homeobox protein DLX-2):

> Acts as a transcriptional activator (By similarity). Activates transcription of CGA/alpha-GSU, via binding to the downstream activin regulatory element (DARE) in the gene promoter (By similarity). Plays a role in terminal differentiation of interneurons, such as amacrine and bipolar cells in the developing retina. Likely to play a regulatory role in the development of the ventral forebrain (By similarity). May play a role in craniofacial patterning and morphogenesis (By similarity).

**Summary**, from NCBI Gene [1746](https://www.ncbi.nlm.nih.gov/gene/1746):

> Many vertebrate homeo box-containing genes have been identified on the basis of their sequence similarity with Drosophila developmental genes. Members of the Dlx gene family contain a homeobox that is related to that of Distal-less (Dll), a gene expressed in the head and limbs of the developing fruit fly. The Distal-less (Dlx) family of genes comprises at least 6 different members, DLX1-DLX6. The DLX proteins are postulated to play a role in forebrain and craniofacial development. This gene is …

**Accessions** — [HGNC:2915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2915) · Entrez [1746](https://www.ncbi.nlm.nih.gov/gene/1746) · UniProt [Q07687](https://www.uniprot.org/uniprotkb/Q07687) · Ensembl [ENSG00000115844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115844)

## Data

Gene col 3729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3729); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3729]; `tensor/DDL_lfc|DDL_z.npy` [3729]; `embed/gene_vectors.npy` [3729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3729 or target_col == 3729). Every well: [[DLX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
