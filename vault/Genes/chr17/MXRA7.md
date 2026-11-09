---
symbol: "MXRA7"
type: "gene"
col: 11296
ensembl_id: "ENSG00000182534"
name: "matrix remodeling associated 7"
location: "17q25.1"
module: 51
arm: "-"
pooled_cpm: 27.45
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# MXRA7

*matrix remodeling associated 7* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.03× (z +12.3, q 5e-32, up in 28 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.40× (z +5.8, q 8e-07, up in 20 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.448× (z -12.7, q 2e-34, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P3H1]] (+0.66, fdr 7e-06), [[PRKACA]] (+0.63, fdr 3e-05), [[BCAP31]] (+0.63, fdr 1e-05); moves opposite to [[DHX36]] (-0.62, fdr 1e-05), [[COIL]] (-0.62, fdr 5e-05), [[C1orf131]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CERCAM]] → it (grade B ⚠); 4 go from it, the strongest it → [[COLGALT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +12.3 | 5e-32 | 28/37 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +11.4 | 7e-28 | 20/26 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +7.7 | 2e-12 | 19/32 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.8 | 8e-07 | 20/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.6 | 2e-06 | 19/41 (LOX-IMVI, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +5.4 | 7e-06 | 18/42 (SW480, C32, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.2 | 2e-05 | 23/42 (SW480, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 3e-04 | 17/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.0 | 0.004 | 19/42 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.006 | 15/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.8 | 0.006 | 14/29 (MIA PaCa-2, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +3.2 | 0.055 | 6/41 (PANC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.448×** | -12.7 | 2e-34 | 35/42 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.631×** | -11.4 | 1e-27 | 25/41 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.508×** | -10.8 | 9e-25 | 30/41 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -7.1 | 1e-10 | 23/42 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.710×** | -6.0 | 2e-07 | 21/42 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -5.3 | 1e-05 | 3/42 (CFPAC-1, NCI-H661, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.9 | 0.007 | 13/42 (HOP62, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.094 | 15/42 (C32, HOP62, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.828× | -3.1 | 0.11 | 15/42 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.835× | -3.0 | 0.15 | 7/41 (HOP62, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 122 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.5) |
| [[SW480 (line)]] | alt | 16.8 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.06× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 86.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -15.2) |
| [[J82 (line)]] | alt | 59.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.169× (z -11.8) |
| [[A-172 (line)]] | wt | 61.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.295× (z -10.5) |
| [[A498 (line)]] | wt | 46.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.9) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.225× (z -8.5) ⚠ toxic |
| [[A549 (line)]] | wt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.5) |
| [[HS-578T (line)]] | alt | 36.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.8) |
| [[PANC-1 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 65.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.0) |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0963× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -9.6) |
| [[C32 (line)]] | wt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -15.2) |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -9.7) |
| [[SW48 (line)]] | wt | 16.2 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0902× (z -9.2) |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P3H1]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PRKACA]] | +0.63 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[BCAP31]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SRD5A1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CTSB]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ENTPD4]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MAPK1]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[AKT1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX36]] | -0.62 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[COIL]] | -0.62 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[C1orf131]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[EPC1]] | -0.61 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ING3]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.60 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[WARS2]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CWC22]] | -0.60 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[THG1L]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.59 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[EIF4EBP3]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | CERCAM activity raises MXRA7's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 4.07× lower at baseline in the lines without CERCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[RFLNB]] | B | RFLNB activity raises MXRA7's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without RFLNB | 0.031 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[COL5A1]] | B | COL5A1 activity raises MXRA7's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without COL5A1 | 0.065 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[BVES]] | B | BVES activity raises MXRA7's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.69× lower at baseline in the lines without BVES | 0.066 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[ID3]] | B | ID3 activity raises MXRA7's level | lines that do not express ID3 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without ID3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |
| [[P3H1]] | C | P3H1 activity raises MXRA7's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 3.44× lower at baseline in the lines without P3H1 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |
| [[TERT]] | C | TERT activity strengthens MXRA7's drug response | recorded gain-of-function mutation of TERT in 8 lines vs 31 not recorded | the TERT-altered lines respond 1.06× as strongly (z diff +0.04); strongest at Homoharringtonine 0.5 µM: 0.32x vs 0.52x (z diff -4.3) | 0.096 | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COLGALT1]] | B | MXRA7 activity raises COLGALT1's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without MXRA7 | 0.060 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1; its own permutation p |
| [[ZNF317]] | B | MXRA7 activity raises ZNF317's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 1.22× lower at baseline in the lines without MXRA7 | 0.060 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1; its own permutation p |
| [[ELAVL1]] | B | MXRA7 activity raises ELAVL1's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without MXRA7 | 0.089 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1; its own permutation p |
| [[TMEM265]] | B | MXRA7 activity lowers TMEM265's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 2.02× higher at baseline in the lines without MXRA7 | 0.090 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1 |

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-33.4, 3.1); signed map (-47.5, -6.0). **Vector** length 93.9, 20.5% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -11.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | matrix remodeling associated 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,672,551-76,711,004 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46603, TMAP1, PS1TP1 |
| Matched by | ensembl_id |

UniProt [P84157](https://www.uniprot.org/uniprotkb/P84157) carries no function annotation.

**Summary**, from NCBI Gene [439921](https://www.ncbi.nlm.nih.gov/gene/439921):

> Involved in megakaryocyte differentiation. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7541) · Entrez [439921](https://www.ncbi.nlm.nih.gov/gene/439921) · UniProt [P84157](https://www.uniprot.org/uniprotkb/P84157) · Ensembl [ENSG00000182534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182534)

## Data

Gene col 11296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11296); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11296]; `tensor/DDL_lfc|DDL_z.npy` [11296]; `embed/gene_vectors.npy` [11296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11296 or target_col == 11296). Every well: [[MXRA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXRA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
