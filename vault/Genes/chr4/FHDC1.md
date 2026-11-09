---
symbol: "FHDC1"
type: "gene"
col: 6015
ensembl_id: "ENSG00000137460"
name: "FH2 domain containing 1"
location: "4q31.3"
module: 39
arm: "+"
pooled_cpm: 9.93
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# FHDC1

*FH2 domain containing 1* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +9.8, q 4e-20, up in 24 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.514× (z -8.1, q 3e-13, down in 22 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.653× (z -5.2, q 3e-05, down in 17 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02284]] (+0.57, fdr 3e-05), [[SCAT1]] (+0.54, fdr 3e-05), [[HPN]] (+0.54, fdr 1e-05); moves opposite to [[PRKRA]] (-0.49, fdr 5e-05), [[THOC1]] (-0.47, fdr 3e-05), [[PEX3]] (-0.47, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TNNT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +9.8 | 4e-20 | 24/39 (SW1417, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +6.9 | 1e-09 | 21/42 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +6.5 | 1e-08 | 22/44 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.0 | 3e-07 | 25/45 (NCI-H2030, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 6e-06 | 17/43 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.2 | 2e-05 | 16/44 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.9 | 8e-05 | 15/38 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 16/39 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.004 | 14/41 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.006 | 13/46 (A498, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.8 | 0.009 | 4/17 (HOP62, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.017 | 11/44 (J82, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.021 | 8/35 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.052 | 12/40 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.058 | 7/44 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.061 | 8/41 (NCI-H23, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -8.1 | 3e-13 | 22/39 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.407×** | -5.7 | 3e-06 | 19/36 (SHP-77, RKO, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.649×** | -5.3 | 3e-05 | 19/45 (NCI-H1573, NCI-H2030, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -5.2 | 3e-05 | 17/43 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -4.5 | 6e-04 | 15/44 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -4.5 | 6e-04 | 17/43 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.7 | 0.021 | 12/42 (CFPAC-1, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0802× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0829× (z -8.6) |
| [[SW48 (line)]] | wt | 10.2 | 0 | 2 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0890× (z -8.7) |
| [[SW480 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0555× (z -12.5) |
| [[COLO 205 (line)]] | alt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.4) |
| [[KATO III (line)]] | alt | 10.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -10.6) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 3.22 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0682× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 7.29 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0807× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02284]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SCAT1]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[HPN]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CCDC162P]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SPTBN5]] | +0.50 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SMCO2]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[SSUH2]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CFAP161]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[B3GALT1-AS1]] | +0.49 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[LEMD1]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[PROX1-AS1]] | +0.48 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[TMEM236]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKRA]] | -0.49 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[THOC1]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PEX3]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ATPAF2]] | -0.47 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[DYNC2LI1]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TRIT1]] | -0.43 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RUFY1]] | -0.43 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[THAP8]] | -0.43 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[TENT2]] | -0.43 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ANKRD36B]] | -0.42 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ZNF594-DT]] | -0.42 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[NDUFB8]] | -0.42 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNT2]] | B | TNNT2 activity raises FHDC1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TNNT2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[LINC03040]] | B | LINC03040 activity raises FHDC1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.11× lower at baseline in the lines without LINC03040 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[LEMD1]] | B | LEMD1 activity raises FHDC1's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without LEMD1 | 0.001 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[MROH3P]] | B | MROH3P activity raises FHDC1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.12× lower at baseline in the lines without MROH3P | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[KRT23]] | B | KRT23 activity raises FHDC1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without KRT23 | 0.003 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[FAM110C]] | B | FAM110C activity raises FHDC1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without FAM110C | 0.011 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[LMO7DN]] | B | LMO7DN activity raises FHDC1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without LMO7DN | 0.012 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[PROX1-AS1]] | B | PROX1-AS1 activity raises FHDC1's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without PROX1-AS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[SLC30A10]] | B | SLC30A10 activity raises FHDC1's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without SLC30A10 | 0.028 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent |
| [[LINC02964]] | B | LINC02964 activity raises FHDC1's level | lines that do not express LINC02964 (38) vs lines expressing it (12) | 2.18× lower at baseline in the lines without LINC02964 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: CLRN3, GPA33, EPS8L3 |
| [[TSHZ2]] | B | TSHZ2 activity raises FHDC1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without TSHZ2 | 0.034 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[TSHZ2]] | B | TSHZ2 activity weakens FHDC1's drug response | lines that do not express TSHZ2 (27) vs lines expressing it (19) | the lines without TSHZ2 respond 1.34× as strongly (z diff -0.44); strongest at Panobinostat 0.5 µM: 1.76x vs 0.97x (z diff -2.4) | 0.034 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.453). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.9, -9.0); signed map (19.4, 13.8). **Vector** length 64.9, 9.74% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.4 | -5.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -0.6 |
|  | [[Afatinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | FH2 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:152,936,323-152,979,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1727, INF1 |
| Gene groups (HGNC) | Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D6](https://www.uniprot.org/uniprotkb/Q9C0D6) (FH2 domain-containing protein 1):

> Microtubule-associated formin which regulates both actin and microtubule dynamics. Induces microtubule acetylation and stabilization and actin stress fiber formation. Regulates Golgi ribbon formation. Required for normal cilia assembly. Early in cilia assembly, may assist in the maturation and positioning of the centrosome/basal body, and once cilia assembly has initiated, may also promote cilia elongation by inhibiting disassembly.

**Summary**, from NCBI Gene [85462](https://www.ncbi.nlm.nih.gov/gene/85462):

> Predicted to enable actin binding activity and microtubule binding activity. Involved in Golgi ribbon formation; cilium assembly; and stress fiber assembly. Located in cilium and microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29363) · Entrez [85462](https://www.ncbi.nlm.nih.gov/gene/85462) · UniProt [Q9C0D6](https://www.uniprot.org/uniprotkb/Q9C0D6) · Ensembl [ENSG00000137460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137460)

## Data

Gene col 6015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6015); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6015]; `tensor/DDL_lfc|DDL_z.npy` [6015]; `embed/gene_vectors.npy` [6015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6015 or target_col == 6015). Every well: [[FHDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
