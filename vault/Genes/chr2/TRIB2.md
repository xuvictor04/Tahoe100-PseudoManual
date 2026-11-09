---
symbol: "TRIB2"
type: "gene"
col: 989
ensembl_id: "ENSG00000071575"
name: "tribbles pseudokinase 2"
location: "2p24.3"
module: 92
arm: "+"
pooled_cpm: 19.98
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 57
n_dd_up_clean: 0
n_dd_down_clean: 46
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# TRIB2

*tribbles pseudokinase 2* — 2p24.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (C32 5.38×).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.202× (z -31.4, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL13A1]] (+0.66, fdr 7e-06), [[ETV1]] (+0.57, fdr 1e-05), [[SPRED1]] (+0.57, fdr 1e-05); moves opposite to [[CLIP1]] (-0.55, fdr 3e-05), [[ANKRD30B]] (-0.52, fdr 3e-05), [[TLCD5]] (-0.49, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[MIR3681HG]] → it (grade B ⚠); 5 go from it, the strongest it → [[ADGRE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 989.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (C32 5.38×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.26× | +3.3 | 0.41 | 4/38 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.25× | +3.2 | 0.41 | 7/38 (KATO III, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.202×** | -31.4 | 0e+00 | 36/37 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.283×** | -17.5 | 0e+00 | 34/36 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.301×** | -16.0 | 0e+00 | 32/38 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.365×** | -14.0 | 3e-42 | 30/38 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.426×** | -11.8 | 3e-30 | 32/38 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.454×** | -11.0 | 6e-26 | 32/37 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.483×** | -10.1 | 6e-22 | 25/37 (C32, BT-474, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.506×** | -9.4 | 3e-19 | 29/38 (C32, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -9.3 | 1e-18 | 27/38 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.525×** | -8.9 | 3e-17 | 25/38 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -8.4 | 3e-15 | 27/35 (KATO III, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.538×** | -8.1 | 2e-14 | 23/36 (C32, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.568×** | -7.8 | 3e-13 | 21/38 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.593×** | -7.2 | 2e-11 | 22/38 (MIA PaCa-2, HS-578T, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.697×** | -7.1 | 6e-11 | 24/37 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -7.0 | 1e-10 | 22/35 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 72.8 | 0 | 29 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0454× (z -34.7) |
| [[C32 (line)]] | wt | 124 | 1 | 19 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 5.38× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -30.5) |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0364× (z -19.1) |
| [[RPMI-7951 (line)]] | alt | 59.6 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -19.6) |
| [[SK-MEL-2 (line)]] | alt | 60.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -21.0) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.0321× (z -18.5) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0789× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.3) |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -20.1) |
| [[SW480 (line)]] | alt | 15.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0194× (z -24.2) |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0501× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -16.3) |
| [[SHP-77 (line)]] | alt | 51.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.7) |
| [[SW 900 (line)]] | alt | 31.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.4) |
| [[CHP-212 (line)]] | wt | 596 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.4) |
| [[H4 (line)]] | wt | 20.9 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.103× (z -9.2) |
| [[KATO III (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.3) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 7.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.168× (z -10.3) |
| [[SNU-423 (line)]] | alt | 8.22 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.9) |
| [[SW 1088 (line)]] | alt | 65.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.8) |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -18.5) |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -19.2) |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.0) |
| [[J82 (line)]] | alt | 5.83 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0684× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 5.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.2) |
| [[SW48 (line)]] | wt | 12.0 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0716× (z -9.4) |
| [[A-427 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL13A1]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ETV1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[SPRED1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ADGRE2]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SHC4]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ITGA3]] | +0.55 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ETV4]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[TNIK]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 | same gene group |
| [[C10orf90]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SPRY4]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HEY1]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GLDC]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIP1]] | -0.55 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD30B]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 | same gene group |
| [[TLCD5]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RAB32]] | -0.45 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[LRRFIP2]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PATJ]] | -0.44 | -0.37 / -0.38 | both halves | 7e-05 | same gene group |
| [[GABARAPL1]] | -0.43 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[BEND7]] | -0.43 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3681HG]] | B | MIR3681HG activity raises TRIB2's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 4.04× lower at baseline in the lines without MIR3681HG | 3e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[SHC4]] | B | SHC4 activity raises TRIB2's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 3.03× lower at baseline in the lines without SHC4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises TRIB2's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without FKBP9P1-1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[SYTL5]] | B | SYTL5 activity raises TRIB2's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 3.13× lower at baseline in the lines without SYTL5 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[CEMIP]] | B | CEMIP activity raises TRIB2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without CEMIP | 0.021 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[AEBP1]] | B | AEBP1 activity raises TRIB2's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.59× lower at baseline in the lines without AEBP1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[PCDHGC3]] | B | PCDHGC3 activity raises TRIB2's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 3.36× lower at baseline in the lines without PCDHGC3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[COL6A3]] | B | COL6A3 activity raises TRIB2's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without COL6A3 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474 |
| [[TREM1]] | B | TREM1 activity raises TRIB2's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without TREM1 | 0.077 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[DUSP4]] | B | DUSP4 activity raises TRIB2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.03× lower at baseline in the lines without DUSP4 | 0.078 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ROR1]] | B | ROR1 activity raises TRIB2's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without ROR1 | 0.082 | ⚠ within organs, on part of the lines |
| [[ABHD17C]] | B | ABHD17C activity raises TRIB2's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.15× lower at baseline in the lines without ABHD17C | 0.091 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRE2]] | B | TRIB2 activity raises ADGRE2's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TRIB2 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SYTL5]] | B | TRIB2 activity raises SYTL5's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without TRIB2 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SNED1]] | B | TRIB2 activity raises SNED1's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 2.33× lower at baseline in the lines without TRIB2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MIR3681HG]] | B | TRIB2 activity raises MIR3681HG's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 3.05× lower at baseline in the lines without TRIB2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TRIB2's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | TRIB2's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.446 over the table, 0.068 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 6.5); signed map (7.5, 50.8). **Vector** length 91.7, 21.4% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +6.7 | -2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.0 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.8 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | tribbles pseudokinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.3 — chr2:12,716,910-12,742,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRB2, GS3955 |
| Gene groups (HGNC) | Pseudokinases; MicroRNA protein coding host genes; Tribbles pseudokinase family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92519](https://www.uniprot.org/uniprotkb/Q92519) (Tribbles homolog 2):

> Interacts with MAPK kinases and regulates activation of MAP kinases. Does not display kinase activity (By similarity).

**Summary**, from NCBI Gene [28951](https://www.ncbi.nlm.nih.gov/gene/28951):

> This gene encodes one of three members of the Tribbles family. The Tribbles members share a Trb domain, which is homologous to protein serine-threonine kinases, but lacks the active site lysine and probably lacks a catalytic function. The Tribbles proteins interact and modulate the activity of signal transduction pathways in a number of physiological and pathological processes. This Tribbles member induces apoptosis of cells mainly of the hematopoietic origin. It has been identified as a …

**Accessions** — [HGNC:30809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30809) · Entrez [28951](https://www.ncbi.nlm.nih.gov/gene/28951) · UniProt [Q92519](https://www.uniprot.org/uniprotkb/Q92519) · Ensembl [ENSG00000071575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071575)

## Data

Gene col 989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 989); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 989]; `tensor/DDL_lfc|DDL_z.npy` [989]; `embed/gene_vectors.npy` [989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 989 or target_col == 989). Every well: [[TRIB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
