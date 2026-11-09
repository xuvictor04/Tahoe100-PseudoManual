---
symbol: "RGS7"
type: "gene"
col: 11340
ensembl_id: "ENSG00000182901"
name: "regulator of G protein signaling 7"
location: "1q43"
module: 61
arm: "+"
pooled_cpm: 24.5
n_lines_expressing: 25
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# RGS7

*regulator of G protein signaling 7* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.28× (z +40.3, q 0e+00, up in 22 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.141×, SHP-77 0.347×, A-427 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.173×, LOX-IMVI 0.241×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.441×, LOX-IMVI 0.367×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.284×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.352×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMN2]] (+0.67, fdr 7e-06), [[CHRM3]] (+0.65, fdr 7e-06), [[SLC35F1]] (+0.62, fdr 7e-06); moves opposite to [[GLT8D1]] (-0.49, fdr 2e-05), [[GDAP2]] (-0.48, fdr 3e-05), [[DZANK1]] (-0.48, fdr 4e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[B3GALT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.28×** | +40.3 | 0e+00 | 22/23 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **4.76×** | +31.7 | 0e+00 | 21/23 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.02×** | +23.2 | 0e+00 | 22/23 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +21.4 | 0e+00 | 12/22 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.48×** | +17.9 | 0e+00 | 22/23 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.54×** | +17.5 | 0e+00 | 19/23 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.06×** | +16.1 | 0e+00 | 19/22 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.00×** | +15.8 | 0e+00 | 20/23 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.93×** | +15.4 | 0e+00 | 21/23 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.74×** | +14.5 | 1e-45 | 19/23 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +13.3 | 7e-39 | 18/23 (NCI-H460, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.35×** | +12.2 | 9e-33 | 5/18 (LoVo, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +11.5 | 6e-29 | 17/23 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.0 | 5e-22 | 13/23 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.04×** | +9.9 | 2e-21 | 8/17 (SW480, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +9.8 | 4e-21 | 10/23 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +9.4 | 1e-19 | 13/22 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11340.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.141×, SHP-77 0.347×, A-427 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.173×, LOX-IMVI 0.241×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.441×, LOX-IMVI 0.367×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.284×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.352×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.9 | 5e-04 | 3/23 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.800× | -3.1 | 0.40 | 7/22 (J82, NCI-H460, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.794× | -3.1 | 0.40 | 4/23 (HS-578T, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.5 | 16 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 18.6× (z +22.4) | — |
| [[A-172 (line)]] | wt | 51.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +20.0) | — |
| [[SW 900 (line)]] | alt | 30.4 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +20.0) | — |
| [[BT-474 (line)]] | alt | 61.5 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +19.6) | — |
| [[HOP62 (line)]] | alt | 16.4 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +17.9) | [[Adagrasib (drug)]] 0.05 µM 0.637× (z -9.0) ⚠ position not correctable |
| [[LOX-IMVI (line)]] | wt | 176 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -13.0) |
| [[PANC-1 (line)]] | alt | 7.43 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 11.0× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.38 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 42.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +15.7) | — |
| [[SW480 (line)]] | alt | 12.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 12.6× (z +24.0) | — |
| [[LoVo (line)]] | wt | 6.35 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 16.6× (z +16.7) | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +14.8) | — |
| [[J82 (line)]] | alt | 115 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +19.1) | — |
| [[SHP-77 (line)]] | alt | 341 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.4) |
| [[A-427 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 8.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.47× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.99× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.26× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 7.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.71× (z +11.9) | — |
| [[A498 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMN2]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 | same gene group; STRING 449 |
| [[CHRM3]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ERC2]] | +0.62 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[KCNH1]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SH3GL2]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PRKG1]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[EGFEM1P]] | +0.59 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PTPRO]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CHST8]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[WIPF3]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLT8D1]] | -0.49 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[GDAP2]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[DZANK1]] | -0.48 | -0.24 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RGS7's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SNTG2]] | B | SNTG2 activity raises RGS7's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without SNTG2 | 0.053 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent |
| [[SYNPO2]] | B | SYNPO2 activity lowers RGS7's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 2.09× higher at baseline in the lines without SYNPO2 | 0.089 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[NETO1]] | C | NETO1 activity raises RGS7's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.60× lower at baseline in the lines without NETO1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[ELAVL2]] | C | ELAVL2 activity raises RGS7's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without ELAVL2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |
| [[CAMK4]] | C | CAMK4 activity raises RGS7's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.25× lower at baseline in the lines without CAMK4 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[EGFEM1P]] | C | EGFEM1P activity raises RGS7's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 3.22× lower at baseline in the lines without EGFEM1P | 0.072 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GALT1]] | B | RGS7 activity raises B3GALT1's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without RGS7 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[LINC01117]] | B | RGS7 activity raises LINC01117's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without RGS7 | 0.038 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[SCN8A]] | B | RGS7 activity raises SCN8A's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without RGS7 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[AP3B2]] | B | RGS7 activity raises AP3B2's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 1.87× lower at baseline in the lines without RGS7 | 0.095 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[OLFM1]] | C | RGS7 activity raises OLFM1's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.81× lower at baseline in the lines without RGS7 | 0.001 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent; co-absent with the target |
| [[CAMK4]] | C | RGS7 activity raises CAMK4's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 4.57× lower at baseline in the lines without RGS7 | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent; co-absent with the target |
| [[TRIM58]] | C | RGS7 activity raises TRIM58's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without RGS7 | 0.054 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 31.3); signed map (34.6, 25.3). **Vector** length 76.2, 21.0% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +31.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +8.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +8.6 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.6 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:240,767,636-241,357,374 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulators of G-protein signaling; DEP domain containing |
| Reactome | 6 pathways, smallest: Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [P49802](https://www.uniprot.org/uniprotkb/P49802) (Regulator of G protein signaling 7):

> GTPase activator component of the RGS7-GNB5 complex that regulates G protein-coupled receptor signaling cascades. The RGS7-GNB5 complex acts as an inhibitor signal transduction by promoting the GTPase activity of G protein alpha subunits, such as GNAO1, thereby driving them into their inactive GDP-bound form. May play a role in synaptic vesicle exocytosis (Probable). Glycine-dependent regulation of the RGS7-GNB5 complex by GPR158 affects mood and cognition via its ability to regulate neuronal …

**Summary**, from NCBI Gene [6000](https://www.ncbi.nlm.nih.gov/gene/6000):

> Enables G-protein alpha-subunit binding activity; G-protein beta-subunit binding activity; and GTPase activator activity. Involved in G protein-coupled receptor signaling pathway; negative regulation of G protein-coupled receptor signaling pathway; and positive regulation of GTPase activity. Located in cytosol. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10003) · Entrez [6000](https://www.ncbi.nlm.nih.gov/gene/6000) · UniProt [P49802](https://www.uniprot.org/uniprotkb/P49802) · Ensembl [ENSG00000182901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182901)

## Data

Gene col 11340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11340); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11340]; `tensor/DDL_lfc|DDL_z.npy` [11340]; `embed/gene_vectors.npy` [11340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11340 or target_col == 11340). Every well: [[RGS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
