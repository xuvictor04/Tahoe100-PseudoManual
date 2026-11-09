---
symbol: "ANO9"
type: "gene"
col: 11625
ensembl_id: "ENSG00000185101"
name: "anoctamin 9"
location: "11p15.5"
module: 14
arm: "+"
pooled_cpm: 11.23
n_lines_expressing: 28
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 28
direction_downstream: 52
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ANO9

*anoctamin 9* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.03× (z +34.8, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.583× (z -6.0, q 9e-07, down in 15 of 26 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.637× (z -5.1, q 1e-04, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAT5A]] (+0.74, fdr 7e-06), [[SLC12A7]] (+0.73, fdr 7e-06), [[TNFAIP2]] (+0.69, fdr 7e-06); moves opposite to [[SENP5]] (-0.52, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[TJP2]] → it (grade B ⚠); 52 go from it, the strongest it → [[STAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.03×** | +34.8 | 0e+00 | 19/25 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **5.70×** | +18.7 | 0e+00 | 20/26 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +8.3 | 2e-14 | 10/25 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +7.8 | 9e-13 | 12/25 (J82, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +7.7 | 1e-12 | 14/26 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.7 | 2e-04 | 4/21 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.5 | 6e-04 | 11/25 (HepG2/C3A, NCI-H2347, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 10/26 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +3.6 | 0.022 | 8/25 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.068 | 7/25 (LoVo, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.068 | 5/25 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.2 | 0.075 | 1/15 (LS 180) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.583×** | -6.0 | 9e-07 | 15/26 (PANC-1, SW480, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -5.1 | 1e-04 | 18/26 (PANC-1, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.652×** | -4.8 | 3e-04 | 16/26 (PANC-1, SW1417, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.5 | 8e-04 | 3/26 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.009 | 13/25 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -3.8 | 0.011 | 12/25 (HT-29, PANC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.701×** | -3.8 | 0.011 | 8/26 (Hs 766T, NCI-H1573, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.038 | 1/25 (CFPAC-1) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.739×** | -3.4 | 0.044 | 12/25 (A549, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -3.3 | 0.057 | 10/25 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.747×** | -3.1 | 0.085 | 12/24 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **0.758×** | -3.1 | 0.086 | 8/25 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.086 | 3/25 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Relugolix (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.086 | 1/25 (A549) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.762×** | -3.1 | 0.086 | 9/26 (PANC-1, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.55 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 74.7× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +21.8) | — |
| [[LoVo (line)]] | wt | 21.2 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.06× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 22.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +23.7) | — |
| [[COLO 205 (line)]] | alt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.7) |
| [[HT-29 (line)]] | alt | 33.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 5.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 71.1× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 35.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +20.8) | — |
| [[SNU-423 (line)]] | alt | 5.13 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +13.5) | — |
| [[SW480 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 4.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.4× (z +14.7) | — |
| [[BT-474 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 5.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 6.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +14.6) | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 9.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 4.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT5A]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[SLC12A7]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TNFRSF14-AS1]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[COL16A1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CX3CL1]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[DDR1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ELF3-AS1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CGNL1]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[TNFRSF14]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PPFIBP2]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[NFIX]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 12, C 16. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | TJP2 activity raises ANO9's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.87× lower at baseline in the lines without TJP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[STAT5A]] | B | STAT5A activity raises ANO9's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 3.01× lower at baseline in the lines without STAT5A | 0.020 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[DENND2D]] | B | DENND2D activity raises ANO9's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without DENND2D | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[CX3CL1]] | B | CX3CL1 activity raises ANO9's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without CX3CL1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[STAP2]] | B | STAP2 activity raises ANO9's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 3.46× lower at baseline in the lines without STAP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |
| [[CYP2S1]] | B | CYP2S1 activity raises ANO9's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without CYP2S1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75 |
| [[ADGRG1]] | B | ADGRG1 activity raises ANO9's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.24× lower at baseline in the lines without ADGRG1 | 0.049 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises ANO9's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.23× lower at baseline in the lines without TNFAIP2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[TMEM184A]] | B | TMEM184A activity raises ANO9's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 3.05× lower at baseline in the lines without TMEM184A | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[GPNMB]] | B | GPNMB activity lowers ANO9's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.25× higher at baseline in the lines without GPNMB | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[ANKRD33B]] | B | ANKRD33B activity lowers ANO9's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 2.59× higher at baseline in the lines without ANKRD33B | 0.080 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[RAB17]] | B | RAB17 activity raises ANO9's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 2.67× lower at baseline in the lines without RAB17 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 36, C 16. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAP2]] | B | ANO9 activity raises STAP2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 3.15× lower at baseline in the lines without ANO9 | 0.001 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[PIK3C2B]] | B | ANO9 activity raises PIK3C2B's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without ANO9 | 0.001 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[PLEKHG3]] | B | ANO9 activity raises PLEKHG3's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without ANO9 | 0.002 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[DDR1]] | B | ANO9 activity raises DDR1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.52× lower at baseline in the lines without ANO9 | 0.003 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[TJP2]] | B | ANO9 activity raises TJP2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 3.01× lower at baseline in the lines without ANO9 | 0.004 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[DMRTA1]] | B | ANO9 activity raises DMRTA1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without ANO9 | 0.005 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[PLXNB2]] | B | ANO9 activity raises PLXNB2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without ANO9 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[TMEM184A]] | B | ANO9 activity raises TMEM184A's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without ANO9 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[SLC37A1]] | B | ANO9 activity raises SLC37A1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without ANO9 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[RAB17]] | B | ANO9 activity raises RAB17's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without ANO9 | 0.009 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[ADGRG1]] | B | ANO9 activity raises ADGRG1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without ANO9 | 0.012 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[CGN]] | B | ANO9 activity raises CGN's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without ANO9 | 0.024 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 3.4); signed map (46.0, 7.5). **Vector** length 71.7, 19.3% of its response variance represented; |z| ≥ 3 in 563 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +18.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +34.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.3 | -4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:417,933-442,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG5; previously TP53I5, TMEM16J |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 8 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [A1A5B4](https://www.uniprot.org/uniprotkb/A1A5B4) (Anoctamin-9):

> PKA-activated nonselective cation channel. Discriminates poorly among cations but is more permeable to Ca(2+) ions than to monovalent cations (By similarity). Acts as a calcium-activated calcium permeable channel which may operate as a endoplasmic reticulum (ER) Ca(2+)-leak channel, reducing the loading of the ER Ca(2+) store. Regulates intracellular Ca2+ signals, ion channel activity, and cytokine release in the renal tissue. Plays an important role in olfaction, amplifying cAMP-evoked cyclic …

**Summary**, from NCBI Gene [338440](https://www.ncbi.nlm.nih.gov/gene/338440):

> The protein encoded by this gene is a member of the TMEM16 (anoctamin) family of proteins, some of which form integral membrane calcium-activated chloride channels. The function of the encoded protein has yet to be elucidated, although it may have channel-forming abilities and also may have phospholipid scramblase activity. This gene has been observed to be upregulated in stage II and III colorectal cancers. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:20679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20679) · Entrez [338440](https://www.ncbi.nlm.nih.gov/gene/338440) · UniProt [A1A5B4](https://www.uniprot.org/uniprotkb/A1A5B4) · Ensembl [ENSG00000185101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185101)

## Data

Gene col 11625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11625); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11625]; `tensor/DDL_lfc|DDL_z.npy` [11625]; `embed/gene_vectors.npy` [11625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11625 or target_col == 11625). Every well: [[ANO9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
