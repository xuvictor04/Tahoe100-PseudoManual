---
symbol: "NCF2"
type: "gene"
col: 3825
ensembl_id: "ENSG00000116701"
name: "neutrophil cytosolic factor 2"
location: "1q25.3"
module: 75
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 41
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# NCF2

*neutrophil cytosolic factor 2* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.81× (z +15.2, q 0e+00, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.81× (z +9.8, q 2e-20, up in 23 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.152×, Hs 766T 0.178×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.195×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.106×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.236×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACR3-AS1]] (+0.58, fdr 5e-05), [[KCND3]] (+0.57, fdr 3e-05), [[HSPB8]] (+0.57, fdr 3e-05); moves opposite to [[TCTN3]] (-0.55, fdr 2e-05), [[RMDN3]] (-0.50, fdr 3e-05), [[TPCN1]] (-0.49, fdr 3e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[KRT14]] → it (grade B ⚠); 5 go from it, the strongest it → [[ATP9B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +15.2 | 0e+00 | 4/6 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +12.8 | 8e-35 | 7/14 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.81×** | +9.8 | 2e-20 | 23/28 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +9.6 | 1e-19 | 5/8 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +8.5 | 3e-15 | 24/34 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +7.4 | 2e-11 | 9/15 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +7.2 | 4e-11 | 8/26 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +6.6 | 4e-09 | 18/30 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.39×** | +6.4 | 9e-09 | 8/11 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.4 | 4e-06 | 8/16 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 13/34 (Panc 03.27, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.64×** | +4.8 | 8e-05 | 13/30 (A498, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.4 | 6e-04 | 8/26 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.83×** | +4.3 | 6e-04 | 9/34 (CFPAC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.2 | 9e-04 | 13/30 (SW480, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.002 | 9/33 (NCI-H2030, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 4/35 (AsPC-1, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.005 | 8/29 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.006 | 13/34 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.009 | 6/26 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.022 | 11/31 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.152×, Hs 766T 0.178×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.195×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.106×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.236×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 0.701× | -3.6 | 0.16 | 10/32 (LoVo, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.712× | -3.4 | 0.16 | 13/34 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.77 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.106× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.2) |
| [[Hs 766T (line)]] | wt | 47.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.2) |
| [[A498 (line)]] | wt | 6.52 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +9.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 2.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +8.7) | — |
| [[A-172 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACR3-AS1]] | +0.58 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[KCND3]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[HSPB8]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[MLLT11]] | +0.57 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[TPRXL]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ADCY7]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[NIBAN1]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[GCKR]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LINC02582]] | +0.52 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[CPEB1]] | +0.52 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[LINC00616]] | +0.52 | +0.54 / +0.37 | both halves | 7e-05 |  |
| [[CLIC2]] | +0.51 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN3]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[RMDN3]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TPCN1]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT14]] | B | KRT14 activity raises NCF2's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 3.18× lower at baseline in the lines without KRT14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13 |
| [[CALB1]] | B | CALB1 activity raises NCF2's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.31× lower at baseline in the lines without CALB1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[DSG4]] | B | DSG4 activity raises NCF2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.90× lower at baseline in the lines without DSG4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[LINC00520]] | B | LINC00520 activity raises NCF2's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without LINC00520 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[LINC02582]] | B | LINC02582 activity raises NCF2's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.14× lower at baseline in the lines without LINC02582 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[PKP1]] | B | PKP1 activity raises NCF2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without PKP1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[KRT16]] | B | KRT16 activity raises NCF2's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without KRT16 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[ZNF736P9Y]] | B | ZNF736P9Y activity raises NCF2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.08× lower at baseline in the lines without ZNF736P9Y | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364 |
| [[CYP4F11]] | B | CYP4F11 activity raises NCF2's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without CYP4F11 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP9B]] | B | NCF2 activity lowers ATP9B's level | lines that do not express NCF2 (9) vs lines expressing it (41) | 1.71× higher at baseline in the lines without NCF2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent |
| [[LINC01033]] | B | NCF2 activity raises LINC01033's level | lines that do not express NCF2 (9) vs lines expressing it (41) | 1.37× lower at baseline in the lines without NCF2 | 0.080 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent |
| [[DYSF]] | B | NCF2 activity raises DYSF's level | lines that do not express NCF2 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without NCF2 | 0.091 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent |
| cells under [[EX229 (drug)]] 0.05 µM | B | NCF2 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express NCF2 (9) vs lines expressing it (39) | the lines without NCF2: 0.90× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent |
| [[ASIC2]] | B | NCF2 activity strengthens ASIC2's drug response | lines that do not express NCF2 (9) vs lines expressing it (37) | the lines without NCF2 respond 0.30× as strongly (z diff +1.91); strongest at Dinaciclib 0.5 µM: 0.80x vs 3.82x (z diff +6.7) | 0.098 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.6, 37.9); signed map (34.4, 22.5). **Vector** length 58.1, 10.4% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +15.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | neutrophil cytosolic factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,554,461-183,590,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p67phox, NOXA2 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; SH3 domain containing |
| Reactome | 21 pathways, smallest: Cross-presentation of particulate exogenous antigens (phagosomes); RHO GTPases Activate NADPH Oxidases; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P19878](https://www.uniprot.org/uniprotkb/P19878) (Neutrophil cytosol factor 2):

> Subunit of the phagocyte NADPH oxidase complex that mediates the transfer of electrons from cytosolic NADPH to O2 to produce the superoxide anion (O2(-)). In the activated complex, electrons are first transferred from NADPH to flavin adenine dinucleotide (FAD) and subsequently transferred via two heme molecules to molecular oxygen, producing superoxide through an outer-sphere reaction. Activation of the NADPH oxidase complex is initiated by the assembly of cytosolic subunits of the NADPH …

**Summary**, from NCBI Gene [4688](https://www.ncbi.nlm.nih.gov/gene/4688):

> This gene encodes neutrophil cytosolic factor 2, the 67-kilodalton cytosolic subunit of the multi-protein NADPH oxidase complex found in neutrophils. This oxidase produces a burst of superoxide which is delivered to the lumen of the neutrophil phagosome. Mutations in this gene, as well as in other NADPH oxidase subunits, can result in chronic granulomatous disease, a disease that causes recurrent infections by catalase-positive organisms. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:7661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7661) · Entrez [4688](https://www.ncbi.nlm.nih.gov/gene/4688) · UniProt [P19878](https://www.uniprot.org/uniprotkb/P19878) · Ensembl [ENSG00000116701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116701)

## Data

Gene col 3825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3825); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3825]; `tensor/DDL_lfc|DDL_z.npy` [3825]; `embed/gene_vectors.npy` [3825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3825 or target_col == 3825). Every well: [[NCF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
