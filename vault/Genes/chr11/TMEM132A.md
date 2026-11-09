---
symbol: "TMEM132A"
type: "gene"
col: 103
ensembl_id: "ENSG00000006118"
name: "transmembrane protein 132A"
location: "11q12.2"
module: 81
arm: "+"
pooled_cpm: 16.84
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# TMEM132A

*transmembrane protein 132A* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +7.6, q 2e-11, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.576× (z -10.0, q 9e-21, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMTN]] (+0.61, fdr 7e-06), [[PKIA]] (+0.60, fdr 1e-05), [[PDLIM7]] (+0.59, fdr 1e-05); moves opposite to [[MYO16-AS1]] (-0.49, fdr 3e-05), [[TDRD3]] (-0.45, fdr 6e-05), [[HECTD1]] (-0.45, fdr 6e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[EDNRA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +7.6 | 2e-11 | 31/45 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.1 | 4e-10 | 31/36 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.4 | 3e-08 | 11/23 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.9 | 1e-04 | 15/29 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +4.2 | 0.003 | 21/45 (AsPC-1, Panc 03.27, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.007 | 16/45 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.76×** | +3.9 | 0.007 | 11/43 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.9 | 0.008 | 15/43 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.009 | 16/45 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.6 | 0.017 | 8/45 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.4 | 0.031 | 0/45 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.071 | 5/39 (A-172, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.071 | 4/39 (BT-474, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.071 | 10/42 (H4, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.28×** | +3.1 | 0.075 | 14/45 (AsPC-1, SW1417, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.083 | 7/40 (H4, KATO III, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.088 | 8/39 (BT-474, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.576×** | -10.0 | 9e-21 | 27/42 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.631×** | -5.7 | 4e-06 | 24/44 (NCI-H2030, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -5.2 | 3e-05 | 23/41 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.766×** | -4.9 | 2e-04 | 20/45 (H4, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -4.5 | 8e-04 | 21/41 (SW 900, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.716×** | -4.3 | 0.002 | 16/45 (H4, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.004 | 15/41 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.712×** | -4.0 | 0.004 | 17/42 (NCI-H23, BT-474, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -3.8 | 0.008 | 20/45 (NCI-H1792, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.033 | 13/45 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.048 | 17/44 (H4, hTERT-HPNE, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.062 | 11/45 (hTERT-HPNE, A549, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.790× | -3.0 | 0.10 | 15/45 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 37.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 8.39 | 0 | 1 | — | [[Altretamine (drug)]] 5 µM 0.0762× (z -8.7) |
| [[HS-578T (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.9) |
| [[SHP-77 (line)]] | alt | 5.97 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.05 µM 0.0561× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 7.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -10.1) |
| [[SNU-423 (line)]] | alt | 66.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.5) |
| [[SW48 (line)]] | wt | 14.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0952× (z -8.6) |
| [[A-172 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMTN]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PKIA]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PDLIM7]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MMP1]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 | pathway: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| [[STC1]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PPFIBP1]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ROBO3]] | +0.55 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[TMEM158]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TNFSF9]] | +0.55 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[GDPD5]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PAEP]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NPTX1]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO16-AS1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TDRD3]] | -0.45 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[HECTD1]] | -0.45 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[HOPX]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDNRA]] | B | EDNRA activity raises TMEM132A's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.62× lower at baseline in the lines without EDNRA | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[IL1B]] | B | IL1B activity raises TMEM132A's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without IL1B | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[INSYN2B]] | B | INSYN2B activity raises TMEM132A's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without INSYN2B | 0.053 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[ITGB3]] | B | ITGB3 activity raises TMEM132A's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without ITGB3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[TNFSF9]] | B | TNFSF9 activity lowers TMEM132A's level | lines that do not express TNFSF9 (6) vs lines expressing it (44) | 2.27× higher at baseline in the lines without TNFSF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI1; its own permutation p |
| [[SMOX]] | B | SMOX activity raises TMEM132A's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without SMOX | 0.060 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[GEM]] | B | GEM activity raises TMEM132A's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without GEM | 0.063 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[COL7A1]] | B | COL7A1 activity raises TMEM132A's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without COL7A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity raises TMEM132A's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without PTGS2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[MMP1]] | B | MMP1 activity raises TMEM132A's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 2.04× lower at baseline in the lines without MMP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[SPOCD1]] | B | SPOCD1 activity raises TMEM132A's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.91× lower at baseline in the lines without SPOCD1 | 0.089 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[LINC01705]] | B | LINC01705 activity strengthens TMEM132A's drug response | lines that do not express LINC01705 (26) vs lines expressing it (19) | the lines without LINC01705 respond 0.72× as strongly (z diff +0.43); strongest at Homoharringtonine 5 µM: 0.74x vs 0.48x (z diff +3.6) | 0.097 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.8, 1.6); signed map (2.4, 47.5). **Vector** length 86.6, 19.1% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +7.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -10.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.9 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.9 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.8 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 132A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:60,924,460-60,937,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GBP, FLJ20539; previously HSPA5BP1 |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q24JP5](https://www.uniprot.org/uniprotkb/Q24JP5) (Transmembrane protein 132A):

> May play a role in embryonic and postnatal development of the brain. Increased resistance to cell death induced by serum starvation in cultured cells. Regulates cAMP-induced GFAP gene expression via STAT3 phosphorylation (By similarity).

**Summary**, from NCBI Gene [54972](https://www.ncbi.nlm.nih.gov/gene/54972):

> This gene encodes a protein that is highly similar to the rat Grp78-binding protein (GBP). Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:31092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31092) · Entrez [54972](https://www.ncbi.nlm.nih.gov/gene/54972) · UniProt [Q24JP5](https://www.uniprot.org/uniprotkb/Q24JP5) · Ensembl [ENSG00000006118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006118)

## Data

Gene col 103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 103); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 103]; `tensor/DDL_lfc|DDL_z.npy` [103]; `embed/gene_vectors.npy` [103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 103 or target_col == 103). Every well: [[TMEM132A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM132A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
