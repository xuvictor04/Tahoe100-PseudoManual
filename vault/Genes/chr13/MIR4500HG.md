---
symbol: "MIR4500HG"
type: "gene"
col: 13677
ensembl_id: "ENSG00000228824"
name: "MIR4500 host gene"
location: "13q31.2"
module: 27
arm: "+"
pooled_cpm: 15.57
n_lines_expressing: 21
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MIR4500HG

*MIR4500 host gene* — 13q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +12.0, q 2e-30, up in 14 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.635× (z -3.9, q 0.054, down in 11 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.0457×, SW480 0.170×; ⚠ cell-cycle shift, explains ~40% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.0851×, COLO 205 0.0992×; ⚠ cell-cycle shift, explains ~55% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (COLO 205 0.0932×, SW480 0.123×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.287×, COLO 205 0.320×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (KATO III 0.116×, PANC-1 0.141×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (COLO 205 0.185×, SW480 0.223×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK4-AS1]] (+0.62, fdr 4e-05), [[LINC02466]] (+0.61, fdr 1e-05), [[THNSL2]] (+0.61, fdr 1e-04); moves opposite to [[MPG]] (-0.53, fdr 3e-04), [[ZCCHC17]] (-0.53, fdr 5e-05), [[DCUN1D2]] (-0.52, fdr 7e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANKRD20A21P]] → it (grade C ⚠); 9 go from it, the strongest it → [[HTR2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +12.0 | 2e-30 | 14/19 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +11.9 | 5e-30 | 4/18 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +7.5 | 2e-11 | 2/12 (NCI-H460, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +7.0 | 3e-10 | 8/19 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.9 | 3e-07 | 1/14 (LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +5.9 | 4e-07 | 10/19 (SNU-423, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.7 | 8e-07 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.81×** | +5.0 | 5e-05 | 15/18 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +4.7 | 1e-04 | 14/19 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.64×** | +4.3 | 8e-04 | 10/19 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.2 | 0.001 | 5/18 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.002 | 12/18 (KATO III, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.005 | 7/19 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.010 | 6/19 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.51×** | +3.3 | 0.034 | 4/18 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.0457×, SW480 0.170×; ⚠ cell-cycle shift, explains ~40% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.0851×, COLO 205 0.0992×; ⚠ cell-cycle shift, explains ~55% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (COLO 205 0.0932×, SW480 0.123×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.287×, COLO 205 0.320×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (KATO III 0.116×, PANC-1 0.141×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (COLO 205 0.185×, SW480 0.223×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -3.9 | 0.054 | 11/19 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.769× | -3.2 | 0.27 | 10/19 (SHP-77, KATO III, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.694× | -3.1 | 0.27 | 3/19 (SW480, COLO 205, …) | two highest doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.697× | -3.1 | 0.27 | 6/19 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 263 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0457× (z -18.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -9.9) |
| [[SW480 (line)]] | alt | 48.1 | 0 | 7 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0851× (z -14.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.223× (z -9.0) |
| [[KATO III (line)]] | alt | 35.9 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0719× (z -13.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 4.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +12.3) | — |
| [[SK-MEL-2 (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.3) |
| [[SNU-423 (line)]] | alt | 14.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +16.8) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0836× (z -10.7) |
| [[PANC-1 (line)]] | alt | 52.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.141× (z -11.1) |
| [[A-172 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK4-AS1]] | +0.62 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[LINC02466]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[THNSL2]] | +0.61 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[TSHZ2]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[LINC00491]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ZNF747]] | +0.60 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[LINC02058]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[IQCH-AS1]] | +0.59 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SLCO2B1]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LINC02428]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.53 | -0.67 / -0.27 | both halves | 3e-04 |  |
| [[ZCCHC17]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[DCUN1D2]] | -0.52 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[STARD3]] | -0.52 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[MARF1]] | -0.52 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[DNAJC5]] | -0.51 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[SS18L1]] | -0.51 | -0.56 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | C | ANKRD20A21P activity raises MIR4500HG's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without ANKRD20A21P | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; co-absent with the target |
| [[LINC01239]] | C | LINC01239 activity raises MIR4500HG's level | lines that do not express LINC01239 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without LINC01239 | 0.059 | ⚠ within organs, on part of the lines; also absent: DMRTA1, ZFPM2-AS1, MIR4500HG; co-absent with the target |
| [[ANKRD18B]] | C | ANKRD18B activity raises MIR4500HG's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without ANKRD18B | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2; co-absent with the target |
| [[LINC01876]] | C | LINC01876 activity raises MIR4500HG's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without LINC01876 | 0.087 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B; co-absent with the target |
| [[RMST]] | C | RMST activity raises MIR4500HG's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without RMST | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR2C]] | B | MIR4500HG activity raises HTR2C's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without MIR4500HG | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA |
| [[LINC00649]] | B | MIR4500HG activity raises LINC00649's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without MIR4500HG | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA |
| [[MIR2052HG]] | C | MIR4500HG activity raises MIR2052HG's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 2.88× lower at baseline in the lines without MIR4500HG | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[LINC02058]] | C | MIR4500HG activity raises LINC02058's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without MIR4500HG | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[LINC01239]] | C | MIR4500HG activity raises LINC01239's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without MIR4500HG | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[LINC00491]] | C | MIR4500HG activity raises LINC00491's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without MIR4500HG | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[LINC01876]] | C | MIR4500HG activity raises LINC01876's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without MIR4500HG | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[ANKRD20A21P]] | C | MIR4500HG activity raises ANKRD20A21P's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without MIR4500HG | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |
| [[CARD18]] | C | MIR4500HG activity raises CARD18's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without MIR4500HG | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.8, 42.5); signed map (48.7, 32.0). **Vector** length 62.2, 19.2% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.9 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | MIR4500 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q31.2 — chr13:87,427,214-87,674,235 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42773) · Entrez [642345](https://www.ncbi.nlm.nih.gov/gene/642345) · Ensembl [ENSG00000228824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228824)

## Data

Gene col 13677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13677); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13677]; `tensor/DDL_lfc|DDL_z.npy` [13677]; `embed/gene_vectors.npy` [13677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13677 or target_col == 13677). Every well: [[MIR4500HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4500HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
