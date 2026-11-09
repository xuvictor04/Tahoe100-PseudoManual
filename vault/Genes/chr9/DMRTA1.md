---
symbol: "DMRTA1"
type: "gene"
col: 10712
ensembl_id: "ENSG00000176399"
name: "DMRT like family A1"
location: "9p21.3"
module: 14
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# DMRTA1

*DMRT like family A1* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +16.2, q 0e+00, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[HI-TOPK-032 (drug)]] 5 µM: 0.473× (z -4.7, q 0.001, down in 9 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.117×; ⚠ cell-cycle shift, explains ~32% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0469×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A498 0.281×; ⚠ cell-cycle shift, would explain all of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (Hs 766T 0.0796×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.143×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SNU-423 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01239]] (+0.67, fdr 7e-06), [[CGNL1]] (+0.63, fdr 8e-06), [[ARHGAP42]] (+0.58, fdr 1e-05); moves opposite to [[ITGB1BP1]] (-0.50, fdr 3e-05), [[CLMP]] (-0.48, fdr 4e-05), [[HIRA]] (-0.46, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANO9]] → it (grade B ⚠); 7 go from it, the strongest it → [[CHST11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +16.2 | 0e+00 | 13/24 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +7.9 | 9e-13 | 10/26 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.0 | 3e-07 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 7e-05 | 5/24 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.9 | 1e-04 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +3.9 | 0.009 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +3.4 | 0.048 | 6/26 (HOP62, NCI-H460, …) | two highest doses | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.054 | 3/29 (Hs 766T, A498, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.054 | 1/28 (SNU-423) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.093 | 5/25 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +3.1 | 0.11 | 2/27 (A-172, SW480) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.11 | 4/28 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10712.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.117×; ⚠ cell-cycle shift, explains ~32% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0469×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A498 0.281×; ⚠ cell-cycle shift, would explain all of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (Hs 766T 0.0796×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.143×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SNU-423 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.473×** | -4.7 | 0.001 | 9/19 (SK-MEL-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.772×** | -4.4 | 0.003 | 16/23 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Sacubitril_Valsartan (drug)]] 0.05 µM |  | 0.739× | -3.4 | 0.15 | 5/29 (A-172, SNU-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | 0.693× | -3.1 | 0.24 | 3/29 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 8.26 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -9.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.158× (z -8.5) |
| [[SW480 (line)]] | alt | 3.59 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0469× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.143× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -9.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HOP62 (line)]] | alt | 1.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 5.05 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0796× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 4.47 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -14.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.390 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01239]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CGNL1]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ARHGAP42]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[AHR]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PROX1]] | +0.53 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[CDKN2B]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 | STRING 408 |
| [[AKR1B1]] | +0.52 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[TLR6]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[LRMDA]] | +0.51 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[TNFAIP6]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[KLRC2]] | +0.51 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CLMP]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[HIRA]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SENP5]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[VKORC1L1]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FOXK2]] | -0.44 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[DCUN1D2]] | -0.44 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[POM121]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[DIP2A]] | -0.44 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ZMYND19]] | -0.44 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[NLRP3]] | -0.43 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[FXYD5]] | -0.43 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity raises DMRTA1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without ANO9 | 0.005 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[CGNL1]] | B | CGNL1 activity raises DMRTA1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.70× lower at baseline in the lines without CGNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[CHST11]] | B | CHST11 activity raises DMRTA1's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without CHST11 | 0.043 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[LRMDA]] | B | LRMDA activity raises DMRTA1's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 1.58× lower at baseline in the lines without LRMDA | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10 |
| [[STAT5A]] | B | STAT5A activity raises DMRTA1's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.41× lower at baseline in the lines without STAT5A | 0.073 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[LINC01239]] | C | LINC01239 activity raises DMRTA1's level | lines that do not express LINC01239 (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without LINC01239 | 0.002 | ⚠ within organs, on part of the lines; also absent: DMRTA1, ZFPM2-AS1, MIR4500HG; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST11]] | B | DMRTA1 activity raises CHST11's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 3.44× lower at baseline in the lines without DMRTA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[IKBKE]] | B | DMRTA1 activity raises IKBKE's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without DMRTA1 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[DCUN1D2]] | B | DMRTA1 activity strengthens DCUN1D2's drug response | lines that do not express DMRTA1 (19) vs lines expressing it (30) | the lines without DMRTA1 respond 0.71× as strongly (z diff +0.75); strongest at Panobinostat 0.5 µM: 1.53x vs 1.86x (z diff +1.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN; target measured in part of the lines; artifact flags |
| [[FGD5]] | B | DMRTA1 activity raises FGD5's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without DMRTA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[TNFAIP2]] | B | DMRTA1 activity raises TNFAIP2's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without DMRTA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[LINC01239]] | C | DMRTA1 activity raises LINC01239's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 3.78× lower at baseline in the lines without DMRTA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN; co-absent with the target |
| [[KCNT2]] | C | DMRTA1 activity raises KCNT2's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 3.03× lower at baseline in the lines without DMRTA1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 1.6); signed map (46.1, 10.5). **Vector** length 47.0, 7.66% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +2.2 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Ixazomib (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.7 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.3 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.1 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -1.0 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DMRT like family A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:22,446,824-22,455,740 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DMRT4 |
| Gene groups (HGNC) | Doublesex and mab-3 related transcription factor family |
| Matched by | ensembl_id |

UniProt [Q5VZB9](https://www.uniprot.org/uniprotkb/Q5VZB9) carries no function annotation.

**Summary**, from NCBI Gene [63951](https://www.ncbi.nlm.nih.gov/gene/63951):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II and sex differentiation. Predicted to act upstream of or within male mating behavior and ovarian follicle development. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13826) · Entrez [63951](https://www.ncbi.nlm.nih.gov/gene/63951) · UniProt [Q5VZB9](https://www.uniprot.org/uniprotkb/Q5VZB9) · Ensembl [ENSG00000176399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176399)

## Data

Gene col 10712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10712); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10712]; `tensor/DDL_lfc|DDL_z.npy` [10712]; `embed/gene_vectors.npy` [10712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10712 or target_col == 10712). Every well: [[DMRTA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMRTA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
