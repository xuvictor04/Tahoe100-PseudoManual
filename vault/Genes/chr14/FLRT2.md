---
symbol: "FLRT2"
type: "gene"
col: 11620
ensembl_id: "ENSG00000185070"
name: "fibronectin leucine rich transmembrane protein 2"
location: "14q31.3"
module: 121
arm: "+"
pooled_cpm: 24.5
n_lines_expressing: 21
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 15
direction_downstream: 20
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# FLRT2

*fibronectin leucine rich transmembrane protein 2* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.16× (z +18.5, q 0e+00, up in 15 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.479× (z -8.4, q 2e-14, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA2D1]] (+0.71, fdr 3e-05), [[MAGI2-AS3]] (+0.69, fdr 6e-05), [[MAGI2]] (+0.66, fdr 1e-05); moves opposite to [[SGSM1]] (-0.56, fdr 2e-04), [[RALGPS1]] (-0.55, fdr 9e-05), [[CAMK2G]] (-0.55, fdr 3e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 20 go from it, the strongest it → [[RNF217-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +18.5 | 0e+00 | 15/19 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +11.3 | 4e-27 | 14/18 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +11.1 | 2e-26 | 16/18 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +10.0 | 2e-21 | 1/16 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.0 | 3e-17 | 11/19 (HOP62, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.3 | 1e-14 | 2/18 (NCI-H1573, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +8.1 | 5e-14 | 11/19 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.2 | 5e-11 | 10/19 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.6 | 2e-06 | 6/18 (NCI-H2030, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 8e-06 | 11/19 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.2 | 8e-06 | 2/17 (NCI-H2030, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +5.2 | 1e-05 | 8/18 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 7e-05 | 7/19 (NCI-H460, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.47×** | +4.3 | 8e-04 | 11/19 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.3 | 8e-04 | 5/19 (RPMI-7951, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 8/18 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.002 | 11/19 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.006 | 12/19 (NCI-H460, Hs 766T, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +3.7 | 0.007 | 6/18 (J82, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.479×** | -8.4 | 2e-14 | 16/19 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.553×** | -6.8 | 3e-09 | 15/19 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.579×** | -6.3 | 7e-08 | 16/19 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -3.7 | 0.028 | 6/18 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 120 | 9 | 4 (1 ⚠) | [[Trametinib (drug)]] 5 µM 5.80× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.172× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 151 | 2 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.0497× (z -22.6) |
| [[HOP62 (line)]] | alt | 18.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 101 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.239× (z -9.5) |
| [[H4 (line)]] | wt | 88.5 | 1 | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.83× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.0818× (z -12.7) |
| [[J82 (line)]] | alt | 39.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 76.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0489× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0773× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 75.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.239× (z -9.7) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0849× (z -14.7) |
| [[hTERT-HPNE (line)]] | wt | 56.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 20.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 22 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA2D1]] | +0.71 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[MAGI2-AS3]] | +0.69 | +0.75 / +0.38 | both halves | 6e-05 |  |
| [[MAGI2]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[HECW2]] | +0.66 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.65 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP24]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD18B]] | +0.65 | +0.64 / +0.29 | both halves | 2e-04 |  |
| [[TRHDE]] | +0.64 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[SYNPO2]] | +0.64 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[ARHGAP15]] | +0.64 | +0.64 / +0.29 | both halves | 3e-04 |  |
| [[DNAH11]] | +0.64 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PLAGL1]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM1]] | -0.56 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[RALGPS1]] | -0.55 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[CAMK2G]] | -0.55 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[YIF1B]] | -0.54 | -0.38 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[DHTKD1]] | -0.54 | -0.41 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[MAST3]] | -0.53 | -0.39 / -0.21 | both halves | 6e-04 |  |
| [[ANKRD27]] | -0.53 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[CEP131]] | -0.53 | -0.30 / -0.23 | both halves | 5e-04 |  |
| [[LCMT1]] | -0.53 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[ATP7B]] | -0.52 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[WASF3]] | -0.52 | -0.49 / -0.09 | ⚠ not reproduced | 0.003 |  |
| [[NBPF3]] | -0.52 | -0.45 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[TSC2]] | -0.51 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[BRF1]] | -0.51 | -0.39 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 3, C 12. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FLRT2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers FLRT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises FLRT2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 3.70× lower at baseline in the lines without PLS3-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[IL7R]] | C | IL7R activity raises FLRT2's level | lines that do not express IL7R (30) vs lines expressing it (20) | 6.04× lower at baseline in the lines without IL7R | 0.002 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[MIR3171HG]] | C | MIR3171HG activity raises FLRT2's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.40× lower at baseline in the lines without MIR3171HG | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[MAGI2]] | C | MAGI2 activity raises FLRT2's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 5.80× lower at baseline in the lines without MAGI2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[JAM2]] | C | JAM2 activity raises FLRT2's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 4.73× lower at baseline in the lines without JAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises FLRT2's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 4.42× lower at baseline in the lines without EBF1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[FLG-AS1]] | C | FLG-AS1 activity raises FLRT2's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 4.50× lower at baseline in the lines without FLG-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4; co-absent with the target |
| [[DNAH11]] | C | DNAH11 activity raises FLRT2's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 4.89× lower at baseline in the lines without DNAH11 | 0.069 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises FLRT2's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 5.73× lower at baseline in the lines without MSC-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises FLRT2's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 4.98× lower at baseline in the lines without NEGR1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 12, C 8. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF217-AS1]] | B | FLRT2 activity raises RNF217-AS1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without FLRT2 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[BRF1]] | B | FLRT2 activity lowers BRF1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.22× higher at baseline in the lines without FLRT2 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[RNF217]] | B | FLRT2 activity raises RNF217's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without FLRT2 | 0.034 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[CYP1B1-AS1]] | B | FLRT2 activity raises CYP1B1-AS1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without FLRT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[DPH6-DT]] | B | FLRT2 activity raises DPH6-DT's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without FLRT2 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[TMEM45A]] | B | FLRT2 activity raises TMEM45A's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 3.29× lower at baseline in the lines without FLRT2 | 0.051 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[PLAGL1]] | B | FLRT2 activity raises PLAGL1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without FLRT2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | B | FLRT2 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express FLRT2 (29) vs lines expressing it (19) | the lines without FLRT2: 1.41× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[ZBED5]] | B | FLRT2 activity raises ZBED5's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.09× lower at baseline in the lines without FLRT2 | 0.070 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[SUCLG2-DT]] | B | FLRT2 activity raises SUCLG2-DT's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without FLRT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | B | FLRT2 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express FLRT2 (29) vs lines expressing it (19) | the lines without FLRT2: 0.85× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[HECTD2]] | B | FLRT2 activity raises HECTD2's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without FLRT2 | 0.099 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 24.9); signed map (43.6, 25.7). **Vector** length 71.9, 23.1% of its response variance represented; |z| ≥ 3 in 522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +18.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +4.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -8.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | +0.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin leucine rich transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:85,530,144-85,654,428 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 4 pathways, smallest: Downstream signaling of activated FGFR1; Signaling by FGFR1; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [O43155](https://www.uniprot.org/uniprotkb/O43155) (Leucine-rich repeat transmembrane protein FLRT2):

> Functions in cell-cell adhesion, cell migration and axon guidance. Mediates cell-cell adhesion via its interactions with ADGRL3 and probably also other latrophilins that are expressed at the surface of adjacent cells. May play a role in the migration of cortical neurons during brain development via its interaction with UNC5D. Mediates axon growth cone collapse and plays a repulsive role in neuron guidance via its interaction with UNC5D, and possibly also other UNC-5 family members. Plays a role …

**Summary**, from NCBI Gene [23768](https://www.ncbi.nlm.nih.gov/gene/23768):

> This gene encodes a member of the fibronectin leucine rich transmembrane (FLRT) family of cell adhesion molecules, which regulate early embryonic vascular and neural development. The encoded type I transmembrane protein has an extracellular region consisting of an N-terminal leucine-rich repeat domain and a type 3 fibronectin domain, followed by a transmembrane domain and a short C-terminal cytoplasmic tail domain. It functions as both a homophilic cell adhesion molecule and a heterophilic …

**Accessions** — [HGNC:3761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3761) · Entrez [23768](https://www.ncbi.nlm.nih.gov/gene/23768) · UniProt [O43155](https://www.uniprot.org/uniprotkb/O43155) · Ensembl [ENSG00000185070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185070)

## Data

Gene col 11620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11620); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11620]; `tensor/DDL_lfc|DDL_z.npy` [11620]; `embed/gene_vectors.npy` [11620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11620 or target_col == 11620). Every well: [[FLRT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLRT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
