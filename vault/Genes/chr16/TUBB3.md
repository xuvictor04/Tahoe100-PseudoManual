---
symbol: "TUBB3"
type: "gene"
col: 15155
ensembl_id: "ENSG00000258947"
name: "tubulin beta 3 class III"
location: "16q24.3"
module: 93
arm: "+"
pooled_cpm: 8.55
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# TUBB3

*tubulin beta 3 class III* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +16.7, q 0e+00, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.496× (z -4.3, q 0.011, down in 15 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCN2]] (+0.69, fdr 7e-06), [[SNAI1]] (+0.64, fdr 1e-05), [[DALRD3]] (+0.60, fdr 1e-05); moves opposite to [[ATAD1]] (-0.55, fdr 6e-05), [[ABHD13]] (-0.53, fdr 3e-05), [[ANKRD13C]] (-0.52, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VASN]] → it (grade B ⚠); 4 go from it, the strongest it → [[SGSH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +16.7 | 0e+00 | 35/42 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.05×** | +16.2 | 0e+00 | 43/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.86×** | +15.7 | 0e+00 | 41/45 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.50×** | +14.5 | 1e-45 | 41/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +14.5 | 3e-45 | 37/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +11.2 | 3e-27 | 41/46 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.7 | 2e-09 | 25/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.6 | 1e-06 | 16/40 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.008 | 15/46 (LOX-IMVI, SNU-423, …) | all doses, flat | low cells (technical?); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.83×** | +3.7 | 0.014 | 6/41 (PANC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.014 | 11/47 (SW1417, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.021 | 13/44 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.2 | 0.056 | 4/29 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.089 | 3/39 (CFPAC-1, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Voriconazole (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.089 | 2/46 (A-172, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.496×** | -4.3 | 0.011 | 15/37 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.782×** | -4.1 | 0.014 | 17/45 (HT-29, NCI-H460, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.020 | 10/47 (SW48, CFPAC-1, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.023 | 14/42 (SNU-423, SHP-77, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.049 | 13/43 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.053 | 16/43 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.053 | 11/47 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Resveratrol (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.068 | 4/47 (SW 900, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.16 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +16.4) | — |
| [[SW480 (line)]] | alt | 8.38 | 10 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 17.4× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 14.6× (z +14.5) | — |
| [[SW1417 (line)]] | alt | 13.3 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.89× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0539× (z -10.8) |
| [[LoVo (line)]] | wt | 3.97 | 2 | 0 | [[Auranofin (drug)]] 5 µM 25.4× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0696× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[A-172 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 11.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.05× (z +9.0) | — |
| [[A549 (line)]] | wt | 9.01 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.159× (z -8.9) ⚠ toxic |
| [[C32 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0953× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0741× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 8.43 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0841× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 6.73 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.110× (z -10.9) |
| [[SHP-77 (line)]] | alt | 8.26 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.72× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 7.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +9.7) | — |
| [[A498 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCN2]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | pathway: Neuronal System |
| [[SNAI1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[DALRD3]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FAM222A]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SPSB2]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[APC2]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[POR]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[BAIAP2]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[LRRC23]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[WDR47]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[NCKAP5L]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | +0.55 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD1]] | -0.55 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[ABHD13]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD13C]] | -0.52 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CCDC66]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMEM209]] | -0.51 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[LSM6]] | -0.51 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[NHLRC2]] | -0.49 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[MTPAP]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[RNASEH2B]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SCO1]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NDUFAF5]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ANGEL1]] | -0.47 | -0.44 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VASN]] | B | VASN activity raises TUBB3's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without VASN | 0.075 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[HAP1]] | B | HAP1 activity raises TUBB3's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.18× lower at baseline in the lines without HAP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[DTWD1]] | C | DTWD1's natural level strengthens TUBB3's drug response | DTWD1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.17; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSH]] | B | TUBB1, [[TUBB2A]], TUBB3, TUBB4A, [[TUBB4B]] activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[MZT1]] | B | TUBB1, [[TUBB2A]], TUBB3, TUBB4A, [[TUBB4B]] activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000287352]] | B | TUBB1, [[TUBB2A]], TUBB3, TUBB4A, [[TUBB4B]] activity lowers ENSG00000287352's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[RAB28]] | B | TUBB1, [[TUBB2A]], TUBB3, TUBB4A, [[TUBB4B]] activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, -26.4); signed map (2.1, 19.0). **Vector** length 81.0, 15.3% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +15.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +16.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +16.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +14.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Auranofin (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.5 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | -2.2 | -1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tubulin beta 3 class III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,921,392-89,938,761 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta-4, CFEOM3, CFEOM3A; previously FEOM3 |
| Gene groups (HGNC) | Tubulin beta family |
| Reactome | 83 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13509](https://www.uniprot.org/uniprotkb/Q13509) (Tubulin beta-3 chain):

> Tubulin is the major constituent of microtubules, protein filaments consisting of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, alpha-beta tubulin heterodimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin. TUBB3 plays a critical role in proper axon guidance and maintenance. Binding of NTN1/Netrin-1 to its receptor UNC5C might cause dissociation of UNC5C from …

**Summary**, from NCBI Gene [10381](https://www.ncbi.nlm.nih.gov/gene/10381):

> This gene encodes a class III member of the beta tubulin protein family. Beta tubulins are one of two core protein families (alpha and beta tubulins) that heterodimerize and assemble to form microtubules. This protein is primarily expressed in neurons and may be involved in neurogenesis and axon guidance and maintenance. Mutations in this gene are the cause of congenital fibrosis of the extraocular muscles type 3. Alternate splicing results in multiple transcript variants. A pseudogene of this …

**Accessions** — [HGNC:20772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20772) · Entrez [10381](https://www.ncbi.nlm.nih.gov/gene/10381) · UniProt [Q13509](https://www.uniprot.org/uniprotkb/Q13509) · Ensembl [ENSG00000258947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258947)

## Data

Gene col 15155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15155); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15155]; `tensor/DDL_lfc|DDL_z.npy` [15155]; `embed/gene_vectors.npy` [15155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15155 or target_col == 15155). Every well: [[TUBB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
