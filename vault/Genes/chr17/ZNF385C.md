---
symbol: "ZNF385C"
type: "gene"
col: 11925
ensembl_id: "ENSG00000187595"
name: "zinc finger protein 385C"
location: "17q21.2"
module: 14
arm: "+"
pooled_cpm: 3.88
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ZNF385C

*zinc finger protein 385C* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.24× (z +18.7, q 0e+00, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -6.9, q 3e-09, down in 13 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEANC]] (+0.66, fdr 7e-06), [[KPNA5]] (+0.64, fdr 7e-06), [[EPHA10]] (+0.62, fdr 1e-05); moves opposite to [[MYCBP]] (-0.59, fdr 1e-05), [[TMED4]] (-0.56, fdr 1e-05), [[PDCD6]] (-0.56, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[VAV1]] → it (grade B ⚠); 3 go from it, the strongest it → [[ABCA5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.24×** | +18.7 | 0e+00 | 24/32 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +8.0 | 3e-13 | 20/37 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +7.0 | 4e-10 | 19/40 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +6.9 | 6e-10 | 14/33 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.8 | 1e-09 | 3/7 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +5.9 | 3e-07 | 16/35 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.3 | 1e-05 | 11/42 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.003 | 5/40 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.9 | 0.005 | 9/21 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.028 | 6/37 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.040 | 1/36 (RKO) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.077 | 9/39 (SW480, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.10 | 3/40 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -6.9 | 3e-09 | 13/31 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.551×** | -6.7 | 5e-09 | 19/37 (SW480, NCI-H23, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -6.2 | 8e-08 | 15/40 (SW48, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.590×** | -6.0 | 2e-07 | 17/41 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.590×** | -5.8 | 7e-07 | 15/32 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.604×** | -5.5 | 3e-06 | 12/28 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -5.3 | 8e-06 | 16/37 (PANC-1, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -5.3 | 8e-06 | 18/40 (HCT15, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.665×** | -4.7 | 2e-04 | 9/37 (SW480, PANC-1, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.670×** | -4.5 | 4e-04 | 17/37 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.699×** | -3.9 | 0.004 | 6/40 (SW480, SNU-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.712×** | -3.7 | 0.012 | 10/34 (MIA PaCa-2, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.740×** | -3.4 | 0.025 | 9/40 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.745×** | -3.4 | 0.032 | 12/28 (A549, NCI-H23, …) | all doses, flat | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -3.2 | 0.044 | 6/40 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.583×** | -3.2 | 0.045 | 4/33 (COLO 205, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.766×** | -3.0 | 0.079 | 4/37 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.14 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0682× (z -11.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 4.89 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +14.8) | — |
| [[SW480 (line)]] | alt | 7.51 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 8.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.8× (z +23.4) | — |
| [[HOP62 (line)]] | alt | 3.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +15.4) | — |
| [[J82 (line)]] | alt | 2.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 71.1× (z +15.3) | — |
| [[A549 (line)]] | wt | 5.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[BT-474 (line)]] | alt | 3.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 3.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.9× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.01 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0475× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 2.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 3.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 6.59 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -9.3) |
| [[A-172 (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEANC]] | +0.66 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[KPNA5]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[EPHA10]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[EBI3]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SUGT1P3-1]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.60 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CCDC102A]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[CD72]] | +0.60 | +0.75 / +0.39 | both halves | 5e-05 |  |
| [[ZFHX2]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[PIM3]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CX3CL1]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.59 | +0.58 / +0.64 | both halves | 8e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYCBP]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TMED4]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.56 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[MFN1]] | -0.55 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[VPS53]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SENP5]] | -0.54 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[TUSC2]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[VTI1A]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[DPAGT1]] | -0.53 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[EMC4]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TUFM]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAV1]] | B | VAV1 activity raises ZNF385C's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.47× lower at baseline in the lines without VAV1 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[RPS6KA6]] | B | RPS6KA6 activity raises ZNF385C's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without RPS6KA6 | 0.049 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[EPHA10]] | B | EPHA10 activity raises ZNF385C's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without EPHA10 | 0.068 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[TESMIN]] | B | TESMIN activity raises ZNF385C's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without TESMIN | 0.070 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ZNF385C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CX3CL1]] | B | CX3CL1 activity raises ZNF385C's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.32× lower at baseline in the lines without CX3CL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[ABCA5]] | C | ABCA5 activity raises ZNF385C's level | lines that do not express ABCA5 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without ABCA5 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: ABCA10, TRIM47, GPAT3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA5]] | C | ZNF385C activity raises ABCA5's level | lines that do not express ZNF385C (4) vs lines expressing it (46) | 3.75× lower at baseline in the lines without ZNF385C | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: SMC1B, ARG2, SPRY1; maybe low, not absent |
| [[SUGT1P3-1]] | C | ZNF385C activity raises SUGT1P3-1's level | lines that do not express ZNF385C (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without ZNF385C | 0.065 | ⚠ few lines (4 vs 46); across organs; also absent: SMC1B, ARG2, SPRY1; maybe low, not absent |
| [[SUGT1P3]] | C | ZNF385C activity raises SUGT1P3's level | lines that do not express ZNF385C (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without ZNF385C | 0.070 | ⚠ few lines (4 vs 46); across organs; also absent: SMC1B, ARG2, SPRY1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.3, 28.8); signed map (9.1, -18.5). **Vector** length 66.0, 11.4% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +18.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +5.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.0 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 385C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,025,576-42,098,479 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Matched by | ensembl_id |

UniProt [Q66K41](https://www.uniprot.org/uniprotkb/Q66K41) carries no function annotation.

**Summary**, from NCBI Gene [201181](https://www.ncbi.nlm.nih.gov/gene/201181):

> Predicted to enable nucleic acid binding activity and zinc ion binding activity. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33722) · Entrez [201181](https://www.ncbi.nlm.nih.gov/gene/201181) · UniProt [Q66K41](https://www.uniprot.org/uniprotkb/Q66K41) · Ensembl [ENSG00000187595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187595)

## Data

Gene col 11925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11925); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11925]; `tensor/DDL_lfc|DDL_z.npy` [11925]; `embed/gene_vectors.npy` [11925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11925 or target_col == 11925). Every well: [[ZNF385C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF385C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
