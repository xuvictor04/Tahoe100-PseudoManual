---
symbol: "OCLN"
type: "gene"
col: 12471
ensembl_id: "ENSG00000197822"
name: "occludin"
location: "5q13.2"
module: 8
arm: "+"
pooled_cpm: 49.42
n_lines_expressing: 31
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 114
direction_downstream: 41
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# OCLN

*occludin* — 5q13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.77×; ⚠ cell-cycle shift, explains ~81% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 3.41×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 3.07×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.552× (z -7.6, q 1e-11, down in 23 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.564× (z -7.4, q 5e-11, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.81, fdr 7e-06), [[INAVA]] (+0.76, fdr 7e-06), [[ADGRF1]] (+0.71, fdr 7e-06); moves opposite to [[ST3GAL3]] (-0.53, fdr 2e-05), [[SSH1]] (-0.51, fdr 2e-04), [[CHD1L]] (-0.50, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 114 arrows point to it, the strongest [[FUT3]] → it (grade B ⚠); 41 go from it, the strongest it → [[PATJ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12471.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.77×; ⚠ cell-cycle shift, explains ~81% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 3.41×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 3.07×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.35× | +3.6 | 0.12 | 15/30 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 1.78× | +3.5 | 0.12 | 12/30 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.30× | +3.4 | 0.14 | 9/29 (LoVo, KATO III, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.19 | 9/29 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.67× | +3.1 | 0.19 | 12/29 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.552×** | -7.6 | 1e-11 | 23/27 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -7.4 | 5e-11 | 17/29 (NCI-H1573, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.570×** | -7.2 | 1e-10 | 21/29 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -6.6 | 8e-09 | 20/30 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.628×** | -6.0 | 3e-07 | 19/29 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.629×** | -5.7 | 1e-06 | 17/24 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -5.2 | 2e-05 | 6/30 (PANC-1, SW 1271, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.683×** | -4.9 | 6e-05 | 18/29 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -4.9 | 6e-05 | 15/29 (HT-29, CFPAC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.788×** | -4.3 | 9e-04 | 16/29 (NCI-H1573, COLO 205, …) | two highest doses | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -4.1 | 0.002 | 18/29 (COLO 205, SW 1271, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.713×** | -4.1 | 0.002 | 14/27 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.707×** | -4.1 | 0.002 | 15/25 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.808×** | -3.9 | 0.004 | 14/29 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.038 | 13/29 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.784×** | -3.0 | 0.099 | 11/29 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.263× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0727× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -12.8) |
| [[HT-29 (line)]] | alt | 166 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.185× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.311× (z -9.1) |
| [[KATO III (line)]] | alt | 104 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H2347 (line)]] | alt | 270 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -15.3) |
| [[SW1417 (line)]] | alt | 70.9 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -11.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -8.9) |
| [[COLO 205 (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.3) ⚠ cell-cycle shift, explains ~81% of this change |
| [[LoVo (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[LS 180 (line)]] | wt | 89.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[PANC-1 (line)]] | alt | 27.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.3) ⚠ cell-cycle shift, explains ~81% of this change | — |
| [[A-427 (line)]] | wt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[HEC-1-A (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.81 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[CDH1]] | +0.71 | +0.67 / +0.79 | both halves | 7e-06 | pathway: Apoptosis; STRING 993 |
| [[FRK]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[SPINT1]] | +0.65 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[MACC1]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TMC4]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MAL2]] | +0.65 | +0.75 / +0.50 | both halves | 1e-05 | same gene group; STRING 644 |
| [[ERBB3]] | +0.63 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[FAAH2]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.53 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[SSH1]] | -0.51 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[CHD1L]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[PARVB]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*114 arrows, 114 of them with an alert ⚠; grade A 0, B 69, C 45. Shown: the 12 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT3]] | B | FUT3 activity raises OCLN's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 4.14× lower at baseline in the lines without FUT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[DAPP1]] | B | DAPP1 activity raises OCLN's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 6.26× lower at baseline in the lines without DAPP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[PLEKHG1]] | B | PLEKHG1 activity raises OCLN's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.76× lower at baseline in the lines without PLEKHG1 | 0.001 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[GRHL2]] | B | GRHL2 activity strengthens OCLN's drug response | lines that do not express GRHL2 (15) vs lines expressing it (15) | the lines without GRHL2 respond 0.19× as strongly (z diff +4.98); strongest at Homoharringtonine 5 µM: 1.10x vs 0.40x (z diff +8.3) | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; target measured in part of the lines; artifact flags |
| [[CDS1]] | B | CDS1 activity raises OCLN's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 4.43× lower at baseline in the lines without CDS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[TMEM125]] | B | TMEM125 activity strengthens OCLN's drug response | lines that do not express TMEM125 (14) vs lines expressing it (16) | the lines without TMEM125 respond 0.17× as strongly (z diff +4.88); strongest at Homoharringtonine 5 µM: 1.12x vs 0.42x (z diff +8.2) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; target measured in part of the lines; artifact flags |
| [[TMEM30B]] | B | TMEM30B activity strengthens OCLN's drug response | lines that do not express TMEM30B (16) vs lines expressing it (14) | the lines without TMEM30B respond 0.22× as strongly (z diff +4.95); strongest at Homoharringtonine 5 µM: 1.07x vs 0.39x (z diff +8.3) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; target measured in part of the lines; artifact flags |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises OCLN's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 4.09× lower at baseline in the lines without SLC44A3-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[LINC03041]] | B | LINC03041 activity lowers OCLN's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 4.82× higher at baseline in the lines without LINC03041 | 0.006 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[MUC4]] | B | MUC4 activity raises OCLN's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 5.76× lower at baseline in the lines without MUC4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[RORC]] | B | RORC activity raises OCLN's level | lines that do not express RORC (30) vs lines expressing it (20) | 3.51× lower at baseline in the lines without RORC | 0.007 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[GPR87]] | B | GPR87 activity raises OCLN's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 4.10× lower at baseline in the lines without GPR87 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 17, C 24. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATJ]] | B | OCLN activity raises PATJ's level | lines that do not express OCLN (19) vs lines expressing it (31) | 3.73× lower at baseline in the lines without OCLN | 0.002 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[AP1G2]] | B | OCLN activity raises AP1G2's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without OCLN | 0.014 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[CHD1L]] | B | OCLN activity lowers CHD1L's level | lines that do not express OCLN (19) vs lines expressing it (31) | 1.72× higher at baseline in the lines without OCLN | 0.025 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[SLC44A3-AS1]] | B | OCLN activity raises SLC44A3-AS1's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.64× lower at baseline in the lines without OCLN | 0.028 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[RMND5A]] | B | OCLN activity raises RMND5A's level | lines that do not express OCLN (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without OCLN | 0.034 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[PLEKHG1]] | B | OCLN activity raises PLEKHG1's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.64× lower at baseline in the lines without OCLN | 0.037 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[SLC44A3]] | B | OCLN activity raises SLC44A3's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.54× lower at baseline in the lines without OCLN | 0.044 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[EPS8L1]] | B | OCLN activity raises EPS8L1's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without OCLN | 0.057 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[CD2AP]] | B | OCLN activity raises CD2AP's level | lines that do not express OCLN (19) vs lines expressing it (31) | 1.68× lower at baseline in the lines without OCLN | 0.059 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[CDS1]] | B | OCLN activity raises CDS1's level | lines that do not express OCLN (19) vs lines expressing it (31) | 3.38× lower at baseline in the lines without OCLN | 0.061 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[USP6NL]] | B | OCLN activity raises USP6NL's level | lines that do not express OCLN (19) vs lines expressing it (31) | 1.93× lower at baseline in the lines without OCLN | 0.067 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[RAB11FIP4]] | B | OCLN activity raises RAB11FIP4's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without OCLN | 0.071 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.5, 56.7); signed map (57.0, 7.0). **Vector** length 93.3, 31.7% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | -6.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.2 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -1.7 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -4.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.1 | -0.5 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | occludin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,492,292-69,558,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R115 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Tetraspan junctional complex superfamily; MARVEL domain containing |
| Reactome | 9 pathways, smallest: RUNX1 regulates expression of components of tight junctions; Epithelial-Mesenchymal Transition (EMT) during gastrulation; Apoptotic cleavage of cell adhesion  proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16625](https://www.uniprot.org/uniprotkb/Q16625) (Occludin):

> May play a role in the formation and regulation of the tight junction (TJ) paracellular permeability barrier. It is able to induce adhesion when expressed in cells lacking tight junctions.; (Microbial infection) Acts as a coreceptor for hepatitis C virus (HCV) in hepatocytes.

**Summary**, from NCBI Gene [100506658](https://www.ncbi.nlm.nih.gov/gene/100506658):

> This gene encodes an integral membrane protein that is required for cytokine-induced regulation of the tight junction paracellular permeability barrier. Mutations in this gene are thought to be a cause of band-like calcification with simplified gyration and polymicrogyria (BLC-PMG), an autosomal recessive neurologic disorder that is also known as pseudo-TORCH syndrome. Alternative splicing results in multiple transcript variants. A related pseudogene is present 1.5 Mb downstream on the q arm of …

**Accessions** — [HGNC:8104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8104) · Entrez [100506658](https://www.ncbi.nlm.nih.gov/gene/100506658) · UniProt [Q16625](https://www.uniprot.org/uniprotkb/Q16625) · Ensembl [ENSG00000197822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197822)

## Data

Gene col 12471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12471); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12471]; `tensor/DDL_lfc|DDL_z.npy` [12471]; `embed/gene_vectors.npy` [12471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12471 or target_col == 12471). Every well: [[OCLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OCLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
