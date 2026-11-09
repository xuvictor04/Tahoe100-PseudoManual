---
symbol: "CHRNA7"
type: "gene"
col: 10598
ensembl_id: "ENSG00000175344"
name: "cholinergic receptor nicotinic alpha 7 subunit"
location: "15q13.3"
module: 61
arm: "+"
pooled_cpm: 8.57
n_lines_expressing: 31
n_dd_up: 55
n_dd_down: 0
n_dd_up_clean: 35
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CHRNA7

*cholinergic receptor nicotinic alpha 7 subunit* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 55 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 10.3× (z +41.8, q 0e+00, up in 20 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.115×, A-427 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.117×; ⚠ toxic; cell-cycle shift, explains ~28% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APBB1]] (+0.54, fdr 4e-05), [[EFHD1]] (+0.54, fdr 3e-05), [[LRRC4B]] (+0.52, fdr 1e-04); moves opposite to [[TRAPPC9]] (-0.44, fdr 1e-04), [[BLTP2]] (-0.41, fdr 2e-04), [[DNAJC16]] (-0.41, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SYT9-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[SYT9-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 55 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **10.3×** | +41.8 | 0e+00 | 20/23 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **10.3×** | +29.5 | 0e+00 | 24/26 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **6.68×** | +24.0 | 0e+00 | 27/27 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.81×** | +23.9 | 0e+00 | 24/26 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.25×** | +21.0 | 0e+00 | 24/26 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +19.8 | 0e+00 | 18/25 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.38×** | +18.0 | 0e+00 | 21/25 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.89×** | +17.2 | 0e+00 | 20/23 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.06×** | +14.1 | 2e-43 | 18/26 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +14.0 | 5e-43 | 11/25 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.56×** | +11.9 | 8e-31 | 9/19 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.53×** | +11.7 | 3e-30 | 19/27 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.53×** | +11.3 | 7e-28 | 14/21 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.43×** | +11.2 | 1e-27 | 16/28 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.34×** | +10.7 | 2e-25 | 24/26 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +7.6 | 9e-13 | 14/27 (LoVo, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.78×** | +7.2 | 1e-11 | 11/26 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +6.4 | 4e-09 | 15/26 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +5.9 | 1e-07 | 17/26 (NCI-H2030, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10598.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.115×, A-427 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.117×; ⚠ toxic; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.747× | -3.7 | 0.11 | 8/26 (SK-MEL-2, RKO, …) | two highest doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | 0.772× | -3.2 | 0.40 | 5/26 (C32, A-427, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.0 | 0.44 | 1/29 (HCT15) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.36 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 8.93 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 48.2× (z +23.9) | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.5× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 3.81 | 7 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 18.3× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 10.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 37.8× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +22.2) | — |
| [[SW480 (line)]] | alt | 3.42 | 5 | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +12.7) | — |
| [[A549 (line)]] | wt | 5.54 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +11.8) | — |
| [[SW48 (line)]] | wt | 57.9 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.11× (z +12.5) | — |
| [[C32 (line)]] | wt | 3.95 | 3 | 0 | [[Auranofin (drug)]] 5 µM 51.0× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 2.82 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 15.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +15.6) | — |
| [[NCI-H1573 (line)]] | alt | 8.56 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +16.3) | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 57.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +16.6) | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HCT15 (line)]] | alt | 11.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.2× (z +9.3) | — |
| [[KATO III (line)]] | alt | 3.03 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.15× (z +9.1) | — |
| [[RKO (line)]] | wt | 37.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 2.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +10.1) | — |
| [[A-172 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APBB1]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[EFHD1]] | +0.54 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[LRRC4B]] | +0.52 | +0.33 / +0.55 | both halves | 1e-04 | pathway: Neuronal System |
| [[KCNIP1]] | +0.52 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[WIPF3]] | +0.51 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PLXNC1]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CACNA2D2]] | +0.51 | +0.46 / +0.58 | both halves | 2e-05 | pathway: Neuronal System |
| [[PLD5]] | +0.51 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[AGBL4]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[KCNG3]] | +0.50 | +0.43 / +0.55 | both halves | 3e-05 | pathway: Neuronal System |
| [[SPOCK3]] | +0.49 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NPTXR]] | +0.49 | +0.38 / +0.59 | both halves | 6e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC9]] | -0.44 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.41 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[DNAJC16]] | -0.41 | -0.15 / -0.33 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises CHRNA7's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.82× lower at baseline in the lines without SYT9-AS1 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CHRNA7's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.0% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NTN1]] | B | NTN1 activity raises CHRNA7's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.15× lower at baseline in the lines without NTN1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[SPOCK3]] | B | SPOCK3 activity lowers CHRNA7's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 1.62× higher at baseline in the lines without SPOCK3 | 0.092 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[ARMCX3]] | C | ARMCX3 activity lowers CHRNA7's level | lines that do not express ARMCX3 (3) vs lines expressing it (47) | 7.53× higher at baseline in the lines without ARMCX3 | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: ARMCX6, TRAF3IP2, SFXN3 |
| [[SRRM3]] | C | SRRM3 activity raises CHRNA7's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without SRRM3 | 0.038 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent; co-absent with the target |
| [[LRRC4B]] | C | LRRC4B activity raises CHRNA7's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without LRRC4B | 0.064 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent; co-absent with the target |
| [[ANKRD20A11P]] | C | ANKRD20A11P activity raises CHRNA7's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 2.32× lower at baseline in the lines without ANKRD20A11P | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT9-AS1]] | B | CHRNA7 activity raises SYT9-AS1's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without CHRNA7 | 0.003 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[NTN1]] | B | CHRNA7 activity raises NTN1's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without CHRNA7 | 0.024 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[ARHGAP10]] | B | CHRNA7 activity weakens ARHGAP10's drug response | lines that do not express CHRNA7 (16) vs lines expressing it (30) | the lines without CHRNA7 respond 1.97× as strongly (z diff -2.27); strongest at Panobinostat 5 µM: 0.59x vs 0.93x (z diff -4.8) | 0.047 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RFTN2]] | B | CHRNA7 activity raises RFTN2's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 1.35× lower at baseline in the lines without CHRNA7 | 0.061 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[SPOCK3]] | B | CHRNA7 activity lowers SPOCK3's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 1.61× higher at baseline in the lines without CHRNA7 | 0.062 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[GAS7]] | C | CHRNA7 activity raises GAS7's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 2.59× lower at baseline in the lines without CHRNA7 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, 35.8); signed map (27.0, 20.8). **Vector** length 69.1, 16.2% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +23.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.1 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +6.1 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +29.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +3.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | +1.1 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor nicotinic alpha 7 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:31,923,438-32,173,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | a7nAChR |
| Gene groups (HGNC) | Cholinergic receptors nicotinic subunits |
| Reactome | 5 pathways, smallest: Acetylcholine binding and downstream events; Postsynaptic nicotinic acetylcholine receptors; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [P36544](https://www.uniprot.org/uniprotkb/P36544) (Neuronal acetylcholine receptor subunit alpha-7):

> Component of neuronal acetylcholine receptors (nAChRs) that function as pentameric, ligand-gated cation channels with high calcium permeability among other activities. nAChRs are excitatory neurotrasnmitter receptors formed by a collection of nAChR subunits known to mediate synaptic transmission in the nervous system and the neuromuscular junction. Each nAchR subunit confers differential attributes to channel properties, including activation, deactivation and desensitization kinetics, pH …

**Summary**, from NCBI Gene [1139](https://www.ncbi.nlm.nih.gov/gene/1139):

> The nicotinic acetylcholine receptors (nAChRs) are members of a superfamily of ligand-gated ion channels that mediate fast signal transmission at synapses. The nAChRs are thought to be hetero-pentamers composed of homologous subunits. The proposed structure for each subunit is a conserved N-terminal extracellular domain followed by three conserved transmembrane domains, a variable cytoplasmic loop, a fourth conserved transmembrane domain, and a short C-terminal extracellular region. The protein …

**Accessions** — [HGNC:1960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1960) · Entrez [1139](https://www.ncbi.nlm.nih.gov/gene/1139) · UniProt [P36544](https://www.uniprot.org/uniprotkb/P36544) · Ensembl [ENSG00000175344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175344)

## Data

Gene col 10598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10598); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10598]; `tensor/DDL_lfc|DDL_z.npy` [10598]; `embed/gene_vectors.npy` [10598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10598 or target_col == 10598). Every well: [[CHRNA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRNA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
