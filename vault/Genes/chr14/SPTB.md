---
symbol: "SPTB"
type: "gene"
col: 941
ensembl_id: "ENSG00000070182"
name: "spectrin beta, erythrocytic"
location: "14q23.3"
module: 9
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 28
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SPTB

*spectrin beta, erythrocytic* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.16× (z +18.6, q 0e+00, up in 22 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.719× (z -3.8, q 0.042, down in 6 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.159×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.127×; ⚠ cell-cycle shift, explains ~13% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0746×; ⚠ toxic); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW1417 0.0763×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYT1]] (+0.66, fdr 7e-06), [[MPP7]] (+0.58, fdr 2e-05), [[MIR325HG]] (+0.58, fdr 7e-06); moves opposite to [[PRR14L]] (-0.55, fdr 6e-05), [[C1orf109]] (-0.52, fdr 3e-04), [[EXOSC3]] (-0.51, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SCN8A]] → it (grade B ⚠); 6 go from it, the strongest it → [[LINC00937]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.16×** | +18.6 | 0e+00 | 22/24 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +17.1 | 0e+00 | 11/19 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.01×** | +15.9 | 0e+00 | 20/24 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +12.9 | 1e-35 | 3/11 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +12.5 | 8e-34 | 18/22 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +12.2 | 2e-32 | 18/23 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +11.8 | 5e-30 | 13/20 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.50×** | +10.5 | 7e-24 | 19/22 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.2 | 1e-22 | 2/5 (NCI-H2347, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.24×** | +9.2 | 1e-18 | 20/23 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.0 | 4e-14 | 2/6 (NCI-H2347, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +5.1 | 2e-05 | 1/16 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +5.0 | 2e-05 | 12/21 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 7e-04 | 5/23 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +4.3 | 8e-04 | 9/22 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 5/23 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 1/23 (A549) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.007 | 9/20 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.023 | 5/23 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 941.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.159×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.127×; ⚠ cell-cycle shift, explains ~13% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0746×; ⚠ toxic); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW1417 0.0763×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.719×** | -3.8 | 0.042 | 6/23 (HEC-1-A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -3.8 | 0.042 | 4/23 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.603× | -3.0 | 0.44 | 7/22 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -11.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0746× (z -10.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 5.91 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0675× (z -8.9) ⚠ cell-cycle shift, explains ~2% of this change |
| [[NCI-H460 (line)]] | wt | 2.11 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.69× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 4.20 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0763× (z -9.5) |
| [[A-172 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYT1]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[MPP7]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 | same gene group |
| [[MIR325HG]] | +0.58 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KCNH7]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[FREM2]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[AMOT]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 | same gene group |
| [[KSR2]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[ELAPOR2]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[OLFM1]] | +0.56 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[SH3GL2]] | +0.55 | +0.44 / +0.64 | both halves | 3e-05 | pathway: L1CAM interactions |
| [[STXBP5L]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 | same gene group |
| [[SLAIN1]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR14L]] | -0.55 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[C1orf109]] | -0.52 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[EXOSC3]] | -0.51 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[APTX]] | -0.47 | -0.38 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN8A]] | B | SCN8A activity raises SPTB's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without SCN8A | 0.055 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[TMEM150C]] | B | TMEM150C activity raises SPTB's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without TMEM150C | 0.061 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[TSPAN15]] | B | TSPAN15 activity strengthens SPTB's drug response | lines that do not express TSPAN15 (7) vs lines expressing it (17) | the lines without TSPAN15 respond 0.39× as strongly (z diff +1.82); strongest at Panobinostat 0.5 µM: 1.70x vs 3.63x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GRIK4]] | B | GRIK4 activity raises SPTB's level | lines that do not express GRIK4 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without GRIK4 | 0.071 | ⚠ within organs, on part of the lines; also absent: PRKAA2, RADIL, CHN1; maybe low, not absent |
| [[FAM167A]] | B | FAM167A activity raises SPTB's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without FAM167A | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[REEP1]] | B | REEP1 activity raises SPTB's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 2.08× lower at baseline in the lines without REEP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[ELAVL2]] | B | ELAVL2 activity raises SPTB's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without ELAVL2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10 |
| [[BSN]] | C | BSN activity raises SPTB's level | lines that do not express BSN (17) vs lines expressing it (33) | 2.50× lower at baseline in the lines without BSN | 0.010 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent; co-absent with the target |
| [[MPP7]] | C | MPP7 activity raises SPTB's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without MPP7 | 0.014 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent; co-absent with the target |
| [[SLAIN1]] | C | SLAIN1 activity raises SPTB's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without SLAIN1 | 0.073 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[KSR2]] | C | KSR2 activity raises SPTB's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without KSR2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00937]] | B | SPTB activity raises LINC00937's level | lines that do not express SPTB (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without SPTB | 0.065 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent |
| [[RAB17]] | B | SPTB activity raises RAB17's level | lines that do not express SPTB (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without SPTB | 0.098 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent |
| [[SLAIN1]] | C | SPTB activity raises SLAIN1's level | lines that do not express SPTB (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without SPTB | 0.014 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent; co-absent with the target |
| [[MPP7]] | C | SPTB activity raises MPP7's level | lines that do not express SPTB (22) vs lines expressing it (28) | 3.28× lower at baseline in the lines without SPTB | 0.026 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent; co-absent with the target |
| [[OLFM1]] | C | SPTB activity raises OLFM1's level | lines that do not express SPTB (22) vs lines expressing it (28) | 3.04× lower at baseline in the lines without SPTB | 0.036 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent; co-absent with the target |
| [[KLRC3]] | C | SPTB activity raises KLRC3's level | lines that do not express SPTB (22) vs lines expressing it (28) | 2.21× lower at baseline in the lines without SPTB | 0.074 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.1, 35.4); signed map (44.2, 30.6). **Vector** length 48.8, 9.75% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | spectrin beta, erythrocytic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,746,283-64,879,907 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Spectrins; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 14 pathways, smallest: Interaction between L1 and Ankyrins; NCAM signaling for neurite out-growth; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P11277](https://www.uniprot.org/uniprotkb/P11277) (Spectrin beta chain, erythrocytic):

> Spectrin is the major constituent of the cytoskeletal network underlying the erythrocyte plasma membrane. It associates with band 4.1 and actin to form the cytoskeletal superstructure of the erythrocyte plasma membrane.

**Summary**, from NCBI Gene [6710](https://www.ncbi.nlm.nih.gov/gene/6710):

> This locus encodes a member of the spectrin gene family. Spectrin proteins, along with ankyrin, play a role in cell membrane organization and stability. The protein encoded by this locus functions in stability of erythrocyte membranes, and mutations in this gene have been associated with spherocytosis type 2, hereditary elliptocytosis, and neonatal hemolytic anemia. Alternatively spliced transcript variants have been described. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:11274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11274) · Entrez [6710](https://www.ncbi.nlm.nih.gov/gene/6710) · UniProt [P11277](https://www.uniprot.org/uniprotkb/P11277) · Ensembl [ENSG00000070182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070182)

## Data

Gene col 941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 941); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 941]; `tensor/DDL_lfc|DDL_z.npy` [941]; `embed/gene_vectors.npy` [941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 941 or target_col == 941). Every well: [[SPTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
