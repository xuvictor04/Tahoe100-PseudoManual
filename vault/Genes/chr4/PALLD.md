---
symbol: "PALLD"
type: "gene"
col: 4949
ensembl_id: "ENSG00000129116"
name: "palladin, cytoskeletal associated protein"
location: "4q32.3"
module: 66
arm: "+"
pooled_cpm: 150.69
n_lines_expressing: 39
n_dd_up: 42
n_dd_down: 9
n_dd_up_clean: 36
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# PALLD

*palladin, cytoskeletal associated protein* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.17× (z +19.2, q 0e+00, up in 34 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.695× (z -9.1, q 5e-17, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALPK2]] (+0.61, fdr 7e-06), [[DST]] (+0.61, fdr 1e-05), [[SULF1]] (+0.58, fdr 1e-05); moves opposite to [[ARMC10]] (-0.57, fdr 2e-05), [[ANKRD13D]] (-0.51, fdr 3e-05), [[TMEM87B]] (-0.50, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C5orf46]] → it (grade B ⚠); 7 go from it, the strongest it → [[CLIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +19.2 | 0e+00 | 34/37 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +12.7 | 2e-34 | 34/38 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +10.0 | 4e-21 | 21/37 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +9.9 | 8e-21 | 27/37 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +9.3 | 1e-18 | 23/37 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +8.8 | 1e-16 | 22/37 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +8.8 | 1e-16 | 21/38 (SK-MEL-2, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.57×** | +8.1 | 3e-14 | 29/39 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +7.9 | 2e-13 | 26/38 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.44×** | +7.7 | 7e-13 | 27/37 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.4 | 7e-12 | 21/37 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +7.2 | 3e-11 | 24/36 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +6.9 | 3e-10 | 23/37 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 4e-09 | 25/38 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.4 | 5e-09 | 21/34 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +6.4 | 6e-09 | 24/37 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +5.8 | 3e-07 | 19/37 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -9.1 | 5e-17 | 23/38 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -7.7 | 3e-12 | 24/37 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.751×** | -7.2 | 1e-10 | 24/37 (NCI-H2347, HepG2/C3A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -5.4 | 1e-05 | 22/37 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.759×** | -4.9 | 1e-04 | 20/37 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.780×** | -4.4 | 9e-04 | 22/37 (hTERT-HPNE, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.786×** | -4.3 | 0.001 | 20/37 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -4.1 | 0.002 | 16/37 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.7 | 0.016 | 17/37 (SW 1088, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.9 | 12 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.83× (z +20.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.420× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 493 | 8 | 4 (2 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.48× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -17.1) |
| [[HOP62 (line)]] | alt | 157 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.1) | — |
| [[J82 (line)]] | alt | 73.1 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +26.9) | — |
| [[LS 180 (line)]] | wt | 319 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -22.2) |
| [[A549 (line)]] | wt | 240 | 7 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 3.25× (z +10.0) | — |
| [[A498 (line)]] | wt | 400 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +14.7) | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.73× (z +18.0) | — |
| [[Hs 766T (line)]] | wt | 443 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 270 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +22.5) | — |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +11.4) | — |
| [[SW48 (line)]] | wt | 87.5 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 85.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 261 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 276 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.18× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 125 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.32× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.2) |
| [[SHP-77 (line)]] | alt | 120 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.8) |
| [[C32 (line)]] | wt | 53.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.83× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 107 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.21× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 141 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.1) |
| [[HT-29 (line)]] | alt | 56.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.88× (z +11.6) | — |
| [[KATO III (line)]] | alt | 160 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.1) |
| [[COLO 205 (line)]] | alt | 59.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +9.8) | — |
| [[H4 (line)]] | wt | 181 | 1 | 0 | [[Trametinib (drug)]] 5 µM 3.63× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 39.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +8.9) | — |
| [[LoVo (line)]] | wt | 369 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 134 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[NCI-H596 (line)]] | alt | 141 | 1 | 0 | [[Methylthiouracil (drug)]] 5 µM 4.13× (z +14.0) | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -8.7) |
| [[RKO (line)]] | wt | 85.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 115 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 258 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.7) |
| [[A-172 (line)]] | wt | 29.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 142 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 36.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALPK2]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 | same gene group |
| [[DST]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[SULF1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[DSEL]] | +0.57 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CREB5]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[STK38L]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TGFB2]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DIO2]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RAB31]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SH3RF2]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SEMA3C]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 | same gene group |
| [[LMCD1]] | +0.53 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC10]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ANKRD13D]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TMEM87B]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[POM121]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[POM121C]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DPY19L3]] | -0.48 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[POLR1HASP]] | -0.48 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[PHC2-AS1]] | -0.47 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[KANSL2]] | -0.46 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[ELK1]] | -0.45 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ACP6]] | -0.45 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[GLE1]] | -0.45 | -0.30 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C5orf46]] | B | C5orf46 activity raises PALLD's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.93× lower at baseline in the lines without C5orf46 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN |
| [[EGF]] | B | EGF activity raises PALLD's level | lines that do not express EGF (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without EGF | 0.024 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[SRPX2]] | B | SRPX2 activity raises PALLD's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without SRPX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLIP1]] | B | PALLD activity lowers CLIP1's level | lines that do not express PALLD (11) vs lines expressing it (39) | 1.42× higher at baseline in the lines without PALLD | 0.031 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[EGF]] | B | PALLD activity raises EGF's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without PALLD | 0.031 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[SPTLC3]] | B | PALLD activity raises SPTLC3's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.64× lower at baseline in the lines without PALLD | 0.040 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[PTGR1]] | B | PALLD activity raises PTGR1's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without PALLD | 0.070 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[TACC1]] | B | PALLD activity raises TACC1's level | lines that do not express PALLD (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without PALLD | 0.091 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[ALCAM]] | B | PALLD activity raises ALCAM's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.60× lower at baseline in the lines without PALLD | 0.098 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[TGFB2]] | B | PALLD activity raises TGFB2's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without PALLD | 0.098 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.0, 20.0); signed map (46.9, 20.5). **Vector** length 129, 37.8% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.2 | +19.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.8 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.0 | +7.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.8 | +7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.3 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.3 | -7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -9.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -5.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | palladin, cytoskeletal associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:168,497,052-168,928,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0992, SIH002, CGI-151 |
| Gene groups (HGNC) | I-set domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WX93](https://www.uniprot.org/uniprotkb/Q8WX93) (Palladin):

> Cytoskeletal protein required for organization of normal actin cytoskeleton. Roles in establishing cell morphology, motility, cell adhesion and cell-extracellular matrix interactions in a variety of cell types. May function as a scaffolding molecule with the potential to influence both actin polymerization and the assembly of existing actin filaments into higher-order arrays. Binds to proteins that bind to either monomeric or filamentous actin. Localizes at sites where active actin remodeling …

**Summary**, from NCBI Gene [23022](https://www.ncbi.nlm.nih.gov/gene/23022):

> This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:17068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17068) · Entrez [23022](https://www.ncbi.nlm.nih.gov/gene/23022) · UniProt [Q8WX93](https://www.uniprot.org/uniprotkb/Q8WX93) · Ensembl [ENSG00000129116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129116)

## Data

Gene col 4949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4949); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4949]; `tensor/DDL_lfc|DDL_z.npy` [4949]; `embed/gene_vectors.npy` [4949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4949 or target_col == 4949). Every well: [[PALLD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALLD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
