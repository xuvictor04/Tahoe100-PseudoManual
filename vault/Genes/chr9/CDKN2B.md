---
symbol: "CDKN2B"
type: "gene"
col: 7230
ensembl_id: "ENSG00000147883"
name: "cyclin dependent kinase inhibitor 2B"
location: "9p21.3"
module: 14
arm: "+"
pooled_cpm: 18.57
n_lines_expressing: 38
n_dd_up: 50
n_dd_down: 4
n_dd_up_clean: 45
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CDKN2B

*cyclin dependent kinase inhibitor 2B* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.82× (z +29.7, q 0e+00, up in 31 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.859× (z -8.1, q 5e-13, down in 10 of 36 measured lines) ⚠ position not correctable. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.504× (z -5.6, q 5e-06, down in 14 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSX2]] (+0.64, fdr 7e-06), [[ARL14]] (+0.63, fdr 1e-05), [[TUBB2A]] (+0.60, fdr 1e-05); moves opposite to [[BDH1]] (-0.58, fdr 1e-05), [[ELAVL1]] (-0.57, fdr 1e-05), [[IPO11]] (-0.56, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[ENSG00000264545]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.82×** | +29.7 | 0e+00 | 31/35 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.94×** | +20.6 | 0e+00 | 31/35 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.73×** | +20.6 | 0e+00 | 28/33 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +15.7 | 0e+00 | 31/36 (LS 180, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +12.3 | 2e-32 | 27/36 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +10.5 | 1e-23 | 25/36 (SW480, hTERT-HPNE, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +10.3 | 8e-23 | 21/35 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +9.3 | 7e-19 | 18/32 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +8.5 | 1e-15 | 16/36 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +8.4 | 2e-15 | 18/36 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.72×** | +8.1 | 2e-14 | 20/35 (hTERT-HPNE, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +7.7 | 5e-13 | 17/36 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +7.4 | 8e-12 | 20/35 (J82, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +6.8 | 4e-10 | 15/36 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.2 | 2e-08 | 13/36 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +6.2 | 2e-08 | 14/36 (SNU-1, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.859× | -8.1 | 5e-13 | 10/36 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.504×** | -5.6 | 5e-06 | 14/33 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.795×** | -5.1 | 7e-05 | 15/36 (C32, SHP-77, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.792×** | -3.5 | 0.078 | 8/35 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.085 | 10/35 (LoVo, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.690× | -3.0 | 0.22 | 3/36 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 38.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +22.9) | — |
| [[SW480 (line)]] | alt | 35.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.6) | — |
| [[LoVo (line)]] | wt | 59.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 12.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +16.5) | — |
| [[HS-578T (line)]] | alt | 36.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +19.2) | — |
| [[HT-29 (line)]] | alt | 28.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +20.8) | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.6) | [[Selinexor (drug)]] 5 µM 0.342× (z -9.1) |
| [[C32 (line)]] | wt | 13.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +22.0) | — |
| [[HOP62 (line)]] | alt | 24.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +20.4) | — |
| [[Hs 766T (line)]] | wt | 94.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +19.5) | — |
| [[KATO III (line)]] | alt | 15.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 7.47 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +12.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0966× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 37.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 30.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 43.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 6.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSX2]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ARL14]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[GEM]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[AHR]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ISG20]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RND1]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.59 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[MARCKS]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[LYST]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CHD2]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DUSP10]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDH1]] | -0.58 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[ELAVL1]] | -0.57 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[IPO11]] | -0.56 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[PPIH]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[GMPS]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[EBPL]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PHKA2]] | -0.54 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[WDR5]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[NDC1]] | -0.53 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.53 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D14]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDKN2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.2% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC9]] | B | HDAC9 activity raises CDKN2B's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without HDAC9 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[SRC]] | B | SRC activity raises CDKN2B's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CDKN2A]] | C | CDKN2A activity raises CDKN2B's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 4.04× lower at baseline in the lines without CDKN2A | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENSG00000264545]] | B | CDKN2B activity raises ENSG00000264545's level | recorded loss-of-function mutation of CDKN2B in 13 lines vs 37 not recorded | 4.13× lower at baseline in the CDKN2B-altered lines | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[CDKN2A]] | B | CDKN2B activity raises CDKN2A's level | recorded loss-of-function mutation of CDKN2B in 13 lines vs 37 not recorded | 7.11× lower at baseline in the CDKN2B-altered lines | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[SNED1]] | B | CDKN2B activity weakens SNED1's drug response | recorded loss-of-function mutation of CDKN2B in 11 lines vs 29 not recorded | the CDKN2B-altered lines respond 1.73× as strongly (z diff -1.73); strongest at Digitoxin 5 µM: 0.41x vs 0.71x (z diff -2.8) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; artifact flags |
| [[IPO11]] | B | CDKN2B activity lowers IPO11's level | lines that do not express CDKN2B (12) vs lines expressing it (38) | 1.26× higher at baseline in the lines without CDKN2B | 0.072 | ⚠ within organs, on part of the lines; deletion recorded too; co-occurs with CDKN2A; also absent: ENSG00000264545, CDKN2A, MTAP |
| [[CDKN2A]] | C | CDKN2B activity raises CDKN2A's level | lines that do not express CDKN2B (12) vs lines expressing it (38) | 8.45× lower at baseline in the lines without CDKN2B | 7e-04 | ⚠ within organs, on part of the lines; deletion recorded too; co-occurs with CDKN2A; also absent: ENSG00000264545, CDKN2A, MTAP; co-absent with the target |
| [[ENSG00000259316]] | C | CDKN2B activity weakens ENSG00000259316's drug response | recorded loss-of-function mutation of CDKN2B in 12 lines vs 36 not recorded | the CDKN2B-altered lines respond 1.50× as strongly (z diff -0.82); strongest at Dinaciclib 0.05 µM: 3.85x vs 1.63x (z diff -3.4) | 0.172 over the table, 0.070 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; artifact flags |
| [[PPCS]] | C | CDKN2B activity strengthens PPCS's drug response | recorded loss-of-function mutation of CDKN2B in 11 lines vs 36 not recorded | the CDKN2B-altered lines respond 1.01× as strongly (z diff -0.01); strongest at Homoharringtonine 0.05 µM: 1.47x vs 1.67x (z diff +1.6) | 0.203 over the table, 0.070 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; both ways; the reference differs; artifact flags |
| [[ANKMY1]] | C | CDKN2B activity weakens ANKMY1's drug response | recorded loss-of-function mutation of CDKN2B in 13 lines vs 36 not recorded | the CDKN2B-altered lines respond 1.18× as strongly (z diff -1.16); strongest at Harringtonine 0.5 µM: 0.28x vs 0.58x (z diff -3.2) | 0.285 over the table, 0.094 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; the reference differs; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.6, 3.7); signed map (6.5, 21.7). **Vector** length 102, 24.3% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +20.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +12.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.9 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +20.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +5.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -1.8 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -5.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:22,002,903-22,009,305 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P15, MTS2, INK4B, TP15, CDK4I, p15INK4b |
| Gene groups (HGNC) | Cyclin dependent kinase inhibitor 2 family |
| Hallmark sets | UV_RESPONSE_UP, P53_PATHWAY |
| Reactome | 15 pathways, smallest: Oncogene Induced Senescence; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription; Cyclin D associated events in G1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P42772](https://www.uniprot.org/uniprotkb/P42772) (Cyclin-dependent kinase 4 inhibitor B):

> Interacts strongly with CDK4 and CDK6. Potent inhibitor. Potential effector of TGF-beta induced cell cycle arrest.

**Summary**, from NCBI Gene [1030](https://www.ncbi.nlm.nih.gov/gene/1030):

> This gene lies adjacent to the tumor suppressor gene CDKN2A in a region that is frequently mutated and deleted in a wide variety of tumors. This gene encodes a cyclin-dependent kinase inhibitor, which forms a complex with CDK4 or CDK6, and prevents the activation of the CDK kinases, thus the encoded protein functions as a cell growth regulator that controls cell cycle G1 progression. The expression of this gene was found to be dramatically induced by TGF beta, which suggested its role in the …

**Accessions** — [HGNC:1788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1788) · Entrez [1030](https://www.ncbi.nlm.nih.gov/gene/1030) · UniProt [P42772](https://www.uniprot.org/uniprotkb/P42772) · Ensembl [ENSG00000147883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147883)

## Data

Gene col 7230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7230); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7230]; `tensor/DDL_lfc|DDL_z.npy` [7230]; `embed/gene_vectors.npy` [7230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7230 or target_col == 7230). Every well: [[CDKN2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
