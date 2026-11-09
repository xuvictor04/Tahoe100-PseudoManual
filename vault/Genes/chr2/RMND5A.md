---
symbol: "RMND5A"
type: "gene"
col: 7730
ensembl_id: "ENSG00000153561"
name: "required for meiotic nuclear division 5 homolog A"
location: "2p11.2"
module: 232
arm: "+"
pooled_cpm: 60.26
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 2
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/232"]
generated_by: "tahoemap"
---

# RMND5A

*required for meiotic nuclear division 5 homolog A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +22.0, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[EX229 (drug)]] 5 µM: 0.657× (z -3.8, q 0.041, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.136×, KATO III 0.341×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.160×); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.141×; ⚠ transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.133×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF103]] (+0.61, fdr 7e-06), [[BROX]] (+0.61, fdr 3e-05), [[ATP9A]] (+0.57, fdr 2e-04); moves opposite to [[TUBGCP5]] (-0.59, fdr 4e-05), [[PIGU]] (-0.55, fdr 1e-05), [[ATP5MC1]] (-0.55, fdr 2e-04).
> It is in [[Module 232]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OCLN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +22.0 | 0e+00 | 43/47 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +14.8 | 0e+00 | 46/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +12.3 | 1e-32 | 37/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +10.6 | 4e-24 | 30/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.4 | 4e-19 | 36/49 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +9.2 | 4e-18 | 39/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +8.9 | 7e-17 | 38/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +8.4 | 4e-15 | 40/48 (NCI-H460, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +8.2 | 2e-14 | 36/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 3e-12 | 37/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 3e-12 | 33/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +7.2 | 4e-11 | 35/48 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +7.2 | 4e-11 | 31/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +6.8 | 3e-10 | 31/47 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.5 | 3e-09 | 30/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.7 | 3e-07 | 29/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +5.7 | 4e-07 | 33/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +5.3 | 3e-06 | 30/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7730.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.136×, KATO III 0.341×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.160×); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.141×; ⚠ transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[EX229 (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.041 | 21/47 (CHP-212, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.660×** | -3.8 | 0.041 | 19/47 (AsPC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | 0.695× | -3.3 | 0.16 | 19/47 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.733× | -3.1 | 0.29 | 13/49 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 79.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 26.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.3) | — |
| [[LoVo (line)]] | wt | 87.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +23.8) | — |
| [[NCI-H460 (line)]] | wt | 45.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +16.3) | — |
| [[A-172 (line)]] | wt | 41.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.5) | — |
| [[A498 (line)]] | wt | 59.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +27.8) | — |
| [[AsPC-1 (line)]] | alt | 98.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +19.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -9.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 66.9 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.29× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 47.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +17.4) | — |
| [[A549 (line)]] | wt | 40.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 54.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.95× (z +10.3) | — |
| [[KATO III (line)]] | alt | 169 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.8) | — |
| [[Panc 03.27 (line)]] | alt | 82.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +17.7) | — |
| [[RKO (line)]] | wt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 45.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.7) | — |
| [[SW1417 (line)]] | alt | 149 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.2) | — |
| [[C32 (line)]] | wt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +14.7) | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.133× (z -8.7) |
| [[COLO 205 (line)]] | alt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +17.5) | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.141× (z -10.2) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 90.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +9.3) | — |
| [[J82 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 37.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 84.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 64.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.3) | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.160× (z -188.6) |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 46.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.4) | — |
| [[SW48 (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF103]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[BROX]] | +0.61 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[ATP9A]] | +0.57 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[LINC02035]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CNBP]] | +0.56 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[NR1D2]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[DDX3X]] | +0.54 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[UBL3]] | +0.53 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[SATB1]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PLEKHA3]] | +0.52 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[YPEL5]] | +0.52 | +0.32 / +0.48 | both halves | 2e-04 | same gene group; STRING 943 |
| [[CREBL2]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBGCP5]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PIGU]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ATP5MC1]] | -0.55 | -0.30 / -0.61 | both halves | 2e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[MYO19]] | -0.54 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PDSS1]] | -0.51 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[BOLA3]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[GLMN]] | -0.47 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[NUDT22]] | -0.46 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[DHRS7B]] | -0.46 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[RABEPK]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NVL]] | -0.45 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[ORC2]] | -0.45 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCLN]] | B | OCLN activity raises RMND5A's level | lines that do not express OCLN (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without OCLN | 0.034 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises RMND5A's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without MTUS1-DT | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 232]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.1, -18.0); signed map (13.4, -2.1). **Vector** length 101, 28.2% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +14.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +7.2 |
| fall | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | -3.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | required for meiotic nuclear division 5 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,720,291-86,778,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13910, RMD5, GID2, GID2A, p44CTLH |
| Gene groups (HGNC) | CTLH complex subunits; Degenerate RING E3 ubiquitin ligases |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H871](https://www.uniprot.org/uniprotkb/Q9H871) (E3 ubiquitin-protein transferase RMND5A):

> Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. MAEA and RMND5A are both required for catalytic activity of the CTLH E3 ubiquitin-protein ligase complex. Catalytic activity of the complex is required for normal cell proliferation. The CTLH E3 ubiquitin-protein ligase complex is not required for the degradation of enzymes involved in …

**Summary**, from NCBI Gene [64795](https://www.ncbi.nlm.nih.gov/gene/64795):

> Predicted to enable ubiquitin protein ligase activity and zinc ion binding activity. Predicted to contribute to ubiquitin-protein transferase activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process and protein polyubiquitination. Located in cytoplasm and nucleoplasm. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25850) · Entrez [64795](https://www.ncbi.nlm.nih.gov/gene/64795) · UniProt [Q9H871](https://www.uniprot.org/uniprotkb/Q9H871) · Ensembl [ENSG00000153561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153561)

## Data

Gene col 7730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7730); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7730]; `tensor/DDL_lfc|DDL_z.npy` [7730]; `embed/gene_vectors.npy` [7730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7730 or target_col == 7730). Every well: [[RMND5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMND5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
