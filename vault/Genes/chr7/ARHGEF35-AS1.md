---
symbol: "ARHGEF35-AS1"
type: "gene"
col: 14395
ensembl_id: "ENSG00000244198"
name: "ARHGEF35 antisense RNA 1"
location: "7q35"
module: 137
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 37
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# ARHGEF35-AS1

*ARHGEF35 antisense RNA 1* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +8.7, q 3e-15, up in 14 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.470× (z -8.3, q 5e-14, down in 18 of 33 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.678× (z -4.3, q 0.001, down in 6 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.149×, NCI-H1792 0.176×, NCI-H23 0.147×, PANC-1 0.320×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.0666×, J82 0.107×, SNU-423 0.0778×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (J82 0.0736×, RKO 0.0263×; ⚠ cell-cycle shift, explains ~31% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.299×); [[Drospirenone (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0565×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP58]] (+0.56, fdr 1e-04), [[LINC00862]] (+0.52, fdr 9e-05), [[MIR583HG]] (+0.49, fdr 6e-05); moves opposite to [[SSBP3]] (-0.48, fdr 1e-04), [[TNFRSF19]] (-0.48, fdr 1e-04), [[RHPN2]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[SLC22A15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.7 | 3e-15 | 14/28 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.6 | 5e-06 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.2 | 0.004 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.012 | 7/32 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.014 | 11/32 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.5 | 0.045 | 1/13 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.23× | +3.2 | 0.10 | 5/34 (J82, NCI-H23, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.12 | 6/32 (NCI-H1792, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14395.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.149×, NCI-H1792 0.176×, NCI-H23 0.147×, PANC-1 0.320×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.0666×, J82 0.107×, SNU-423 0.0778×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (J82 0.0736×, RKO 0.0263×; ⚠ cell-cycle shift, explains ~31% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.299×); [[Drospirenone (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0565×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.470×** | -8.3 | 5e-14 | 18/33 (J82, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.525×** | -7.1 | 3e-10 | 17/34 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.835× | -6.7 | 3e-09 | 18/35 (HOP62, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.575×** | -6.0 | 3e-07 | 16/33 (J82, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.589×** | -5.8 | 6e-07 | 14/26 (J82, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.639×** | -4.9 | 8e-05 | 9/34 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.732×** | -4.9 | 9e-05 | 14/30 (J82, NCI-H1792, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.670×** | -4.3 | 0.001 | 9/33 (PANC-1, hTERT-HPNE, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -4.3 | 0.001 | 6/34 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.636×** | -3.9 | 0.005 | 14/33 (J82, NCI-H2030, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.698×** | -3.9 | 0.005 | 13/32 (PANC-1, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -3.9 | 0.005 | 8/23 (SNU-423, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.523×** | -3.7 | 0.008 | 14/30 (J82, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 22.1 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0666× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.76 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 9.42 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 2.88 | 0 | 1 | — | [[Drospirenone (drug)]] 0.05 µM 0.0565× (z -9.9) |
| [[RKO (line)]] | wt | 7.68 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0263× (z -13.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 7.48 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0778× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP58]] | +0.56 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[LINC00862]] | +0.52 | +0.47 / +0.36 | both halves | 9e-05 |  |
| [[MIR583HG]] | +0.49 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[PHC2-AS1]] | +0.49 | +0.43 / +0.38 | both halves | 6e-05 | same gene group |
| [[SPRY3]] | +0.49 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[HIPK3]] | +0.47 | +0.28 / +0.36 | both halves | 3e-04 |  |
| [[PRDM5]] | +0.47 | +0.42 / +0.26 | both halves | 4e-04 |  |
| [[NPR3]] | +0.46 | +0.34 / +0.37 | both halves | 1e-04 |  |
| [[STXBP5-AS1]] | +0.46 | +0.32 / +0.39 | both halves | 2e-04 | same gene group |
| [[OSMR-DT]] | +0.45 | +0.34 / +0.37 | both halves | 1e-04 |  |
| [[ANKRD7]] | +0.45 | +0.32 / +0.20 | both halves | 7e-04 |  |
| [[CDNF]] | +0.45 | +0.35 / +0.38 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSBP3]] | -0.48 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[TNFRSF19]] | -0.48 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[RHPN2]] | -0.47 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[NET1]] | -0.47 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[MAPRE2]] | -0.46 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[HMSD]] | -0.45 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[IFFO2]] | -0.45 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[DLG3]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ATP8B1]] | -0.44 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[EDA]] | -0.44 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[GDE1]] | -0.44 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[NCAM2]] | -0.44 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A15]] | B | ARHGEF35-AS1 activity raises SLC22A15's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 3.01× lower at baseline in the lines without ARHGEF35-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |
| [[PHF2]] | B | ARHGEF35-AS1 activity lowers PHF2's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without ARHGEF35-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |
| [[CADM2]] | B | ARHGEF35-AS1 activity lowers CADM2's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 7.34× higher at baseline in the lines without ARHGEF35-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |
| [[LINC00607]] | B | ARHGEF35-AS1 activity raises LINC00607's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without ARHGEF35-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |
| [[RHPN2]] | B | ARHGEF35-AS1 activity raises RHPN2's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without ARHGEF35-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.354). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.4, 17.6); signed map (17.5, -3.1). **Vector** length 46.6, 6.74% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +3.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.7 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ARHGEF35 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q35 — chr7:144,194,858-144,280,547 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DDGC |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41292) · Entrez [101928605](https://www.ncbi.nlm.nih.gov/gene/101928605) · Ensembl [ENSG00000244198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244198)

## Data

Gene col 14395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14395); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14395]; `tensor/DDL_lfc|DDL_z.npy` [14395]; `embed/gene_vectors.npy` [14395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14395 or target_col == 14395). Every well: [[ARHGEF35-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF35-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
