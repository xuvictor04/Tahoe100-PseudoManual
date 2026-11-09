---
symbol: "DNAJC22"
type: "gene"
col: 10924
ensembl_id: "ENSG00000178401"
name: "DnaJ heat shock protein family (Hsp40) member C22"
location: "12q13.12"
module: 55
arm: "+"
pooled_cpm: 12.55
n_lines_expressing: 40
n_dd_up: 15
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# DNAJC22

*DnaJ heat shock protein family (Hsp40) member C22* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +11.8, q 3e-29, up in 22 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.451× (z -9.8, q 5e-20, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOTAIR]] (+0.61, fdr 1e-04), [[IL17RB]] (+0.56, fdr 5e-05), [[HFE]] (+0.54, fdr 2e-04); moves opposite to [[NUDCD3]] (-0.47, fdr 2e-04), [[CFDP1]] (-0.46, fdr 3e-04), [[ZNF598]] (-0.46, fdr 2e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TFF3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC00938]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +11.8 | 3e-29 | 22/36 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +10.1 | 1e-21 | 22/31 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +9.9 | 1e-20 | 25/38 (A-172, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.4 | 7e-15 | 10/19 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.0 | 2e-10 | 20/32 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.3 | 2e-08 | 13/22 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.1 | 1e-07 | 14/37 (A498, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 4e-05 | 16/37 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.006 | 10/37 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.020 | 12/36 (HEC-1-A, A-172, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.020 | 9/36 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.020 | 10/36 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +3.4 | 0.026 | 11/37 (H4, LoVo, …) | top dose only | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +3.3 | 0.045 | 12/36 (SW480, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.2 | 0.045 | 8/32 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -9.8 | 5e-20 | 25/33 (LS 180, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.619×** | -8.4 | 2e-14 | 20/34 (COLO 205, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.558×** | -7.2 | 1e-10 | 24/37 (H4, SW480, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -6.8 | 1e-09 | 20/37 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.657×** | -5.2 | 3e-05 | 15/37 (SNU-423, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -5.1 | 4e-05 | 20/34 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.675×** | -4.8 | 1e-04 | 14/36 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.676×** | -4.8 | 1e-04 | 13/37 (H4, A498, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -4.5 | 4e-04 | 13/38 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.693×** | -4.5 | 4e-04 | 16/36 (A-172, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -4.3 | 8e-04 | 17/37 (A-427, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.701×** | -4.1 | 0.002 | 13/37 (LS 180, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.532×** | -4.1 | 0.002 | 14/36 (A498, C32, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.711×** | -4.0 | 0.002 | 10/36 (A549, HepG2/C3A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.006 | 16/37 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -3.6 | 0.012 | 15/38 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.020 | 4/38 (LoVo, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.4 | 2 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.7) |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.168× (z -12.2) |
| [[RKO (line)]] | wt | 20.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -14.7) |
| [[COLO 205 (line)]] | alt | 29.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -14.8) |
| [[H4 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0841× (z -11.2) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -9.0) |
| [[A-172 (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0706× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 4.83 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0733× (z -8.6) |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.5) |
| [[LoVo (line)]] | wt | 56.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.167× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 8.05 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.72× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0895× (z -10.2) |
| [[SHP-77 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0912× (z -9.3) |
| [[A-427 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOTAIR]] | +0.61 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[IL17RB]] | +0.56 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[HFE]] | +0.54 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[QPCT]] | +0.52 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[TSPOAP1]] | +0.52 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[TMEM98]] | +0.51 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[TSPAN6]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CHDH]] | +0.49 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[KLK6]] | +0.49 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[LINC01819]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SOD3]] | +0.49 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[GSTM3]] | +0.49 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDCD3]] | -0.47 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[CFDP1]] | -0.46 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[ZNF598]] | -0.46 | -0.30 / -0.29 | both halves | 2e-04 |  |
| [[CCDC124]] | -0.45 | -0.25 / -0.34 | both halves | 4e-04 |  |
| [[SND1]] | -0.44 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[TAMM41]] | -0.44 | -0.29 / -0.29 | both halves | 2e-04 |  |
| [[NAA10]] ⚠ | -0.43 | -0.28 / -0.24 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM50A]] | -0.43 | -0.29 / -0.29 | both halves | 3e-04 |  |
| [[EIF3M]] | -0.43 | -0.34 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFF3]] | B | TFF3 activity raises DNAJC22's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without TFF3 | 0.070 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[TMEM98]] | B | TMEM98 activity raises DNAJC22's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.11× lower at baseline in the lines without TMEM98 | 0.087 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[HR]] | B | HR activity raises DNAJC22's level | lines that do not express HR (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without HR | 0.090 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[CLRN3]] | B | CLRN3 activity raises DNAJC22's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.77× lower at baseline in the lines without CLRN3 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[MBNL3]] | B | MBNL3 activity raises DNAJC22's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without MBNL3 | 0.099 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00938]] | B | DNAJC22 activity lowers LINC00938's level | lines that do not express DNAJC22 (10) vs lines expressing it (40) | 1.23× higher at baseline in the lines without DNAJC22 | 0.090 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 44.3); signed map (66.3, 14.1). **Vector** length 67.7, 13.3% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +11.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -7.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.5 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,346,888-49,357,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | wus, FLJ13236 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4W6](https://www.uniprot.org/uniprotkb/Q8N4W6) (DnaJ homolog subfamily C member 22):

> May function as a co-chaperone.

**Summary**, from NCBI Gene [79962](https://www.ncbi.nlm.nih.gov/gene/79962):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25802) · Entrez [79962](https://www.ncbi.nlm.nih.gov/gene/79962) · UniProt [Q8N4W6](https://www.uniprot.org/uniprotkb/Q8N4W6) · Ensembl [ENSG00000178401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178401)

## Data

Gene col 10924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10924); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10924]; `tensor/DDL_lfc|DDL_z.npy` [10924]; `embed/gene_vectors.npy` [10924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10924 or target_col == 10924). Every well: [[DNAJC22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
