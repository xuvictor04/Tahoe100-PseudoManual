---
symbol: "CHRM3"
type: "gene"
col: 5402
ensembl_id: "ENSG00000133019"
name: "cholinergic receptor muscarinic 3"
location: "1q43"
module: 61
arm: "+"
pooled_cpm: 38.16
n_lines_expressing: 30
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CHRM3

*cholinergic receptor muscarinic 3* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.34× (z +31.0, q 0e+00, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.440× (z -14.4, q 3e-44, down in 20 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.592× (z -9.6, q 3e-19, down in 19 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS7]] (+0.65, fdr 7e-06), [[NYAP2]] (+0.65, fdr 3e-05), [[GRIA4]] (+0.61, fdr 9e-06); moves opposite to [[SDHAP4]] (-0.48, fdr 3e-05), [[RARS2]] (-0.48, fdr 3e-05), [[GLE1]] (-0.47, fdr 2e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[NLGN1]] → it (grade B ⚠); 6 go from it, the strongest it → [[LINC01933]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.34×** | +31.0 | 0e+00 | 24/28 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.08×** | +29.0 | 0e+00 | 27/28 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.38×** | +21.3 | 0e+00 | 21/28 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.93×** | +19.6 | 0e+00 | 23/26 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +15.2 | 0e+00 | 21/28 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +11.9 | 8e-31 | 16/28 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +9.8 | 6e-21 | 22/28 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +8.7 | 3e-16 | 15/28 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +8.6 | 3e-16 | 18/27 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +8.1 | 3e-14 | 12/27 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.9 | 2e-10 | 11/26 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +6.8 | 5e-10 | 11/28 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 4e-09 | 14/28 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 8e-08 | 13/26 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +5.6 | 7e-07 | 14/28 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +5.4 | 3e-06 | 10/28 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 12/26 (NCI-H23, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -14.4 | 3e-44 | 20/25 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.592×** | -9.6 | 3e-19 | 19/27 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.664×** | -7.5 | 2e-11 | 17/26 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -7.4 | 2e-11 | 18/27 (C32, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.683×** | -6.6 | 6e-09 | 20/27 (C32, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.745×** | -5.4 | 7e-06 | 15/26 (NCI-H661, HT-29, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -4.4 | 8e-04 | 10/28 (LOX-IMVI, C32, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.814×** | -3.8 | 0.012 | 15/26 (SK-MEL-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.812×** | -3.7 | 0.016 | 13/26 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.845× | -3.1 | 0.12 | 7/26 (HT-29, H4, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.12 | 9/27 (HT-29, H4, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.3 | 16 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +24.4) | — |
| [[C32 (line)]] | wt | 160 | 1 | 11 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.60× (z +8.8) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0640× (z -17.9) |
| [[NCI-H1573 (line)]] | alt | 62.8 | 7 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.65× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 139 | 1 | 8 (7 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.24× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0368× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.366× (z -8.6) |
| [[A-172 (line)]] | wt | 72.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +28.0) | — |
| [[A-427 (line)]] | wt | 24.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +19.0) | — |
| [[LS 180 (line)]] | wt | 117 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 82.9 | 1 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.62× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -8.8) |
| [[SW48 (line)]] | wt | 176 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -9.6) |
| [[HS-578T (line)]] | alt | 30.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +19.2) | — |
| [[H4 (line)]] | wt | 169 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -9.0) |
| [[HT-29 (line)]] | alt | 137 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -20.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 48.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +19.6) | [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -8.7) |
| [[SW1417 (line)]] | alt | 40.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +22.9) | — |
| [[A549 (line)]] | wt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +15.6) | — |
| [[LOX-IMVI (line)]] | wt | 87.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0385× (z -14.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HCT15 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.79× (z +12.4) | — |
| [[SW480 (line)]] | alt | 40.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.36× (z +12.1) | — |
| [[A498 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS7]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NYAP2]] | +0.65 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[GRIA4]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[CAMK4]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ELAVL2]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[LINC02438]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CHST11]] | +0.56 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[KCTD12]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CDH18]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LRRC7]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ERC2]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RARS2]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GLE1]] | -0.47 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[ZFYVE21]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[GID4]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CCT6P3-1]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN1]] | B | NLGN1 activity raises CHRM3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without NLGN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1 |
| [[ELAPOR2]] | B | ELAPOR2 activity raises CHRM3's level | lines that do not express ELAPOR2 (17) vs lines expressing it (33) | 3.81× lower at baseline in the lines without ELAPOR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SCN2A, CACNB2, ENSG00000227681 |
| [[AGMO]] | B | AGMO activity raises CHRM3's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without AGMO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[EPHA3]] | B | EPHA3 activity raises CHRM3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without EPHA3 | 0.050 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[ANKRD20A8P]], [[FAM95A]] | B | ANKRD20A8P, FAM95A activity raises CHRM3's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.76× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent genes |
| [[PSMB5]] | B | PSMB5 activity raises CHRM3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NLGN4X]] | C | NLGN4X activity raises CHRM3's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 3.01× lower at baseline in the lines without NLGN4X | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises CHRM3's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.83× lower at baseline in the lines without F11-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[NELL1]] | C | NELL1 activity raises CHRM3's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 3.86× lower at baseline in the lines without NELL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |
| [[MDGA2]] | C | MDGA2 activity raises CHRM3's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without MDGA2 | 0.0997 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01933]] | B | CHRM3 activity raises LINC01933's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 1.39× lower at baseline in the lines without CHRM3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[ELAPOR2]] | B | CHRM3 activity raises ELAPOR2's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without CHRM3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[NLGN1]] | B | CHRM3 activity raises NLGN1's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 2.62× lower at baseline in the lines without CHRM3 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[AGMO]] | B | CHRM3 activity raises AGMO's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without CHRM3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[CCDC148]] | B | CHRM3 activity raises CCDC148's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 1.63× lower at baseline in the lines without CHRM3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[CSMD3]] | C | CHRM3 activity raises CSMD3's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without CHRM3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.7, 31.9); signed map (29.3, 36.1). **Vector** length 90.7, 23.2% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +29.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +19.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +31.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -9.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | +1.1 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor muscarinic 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:239,386,565-239,915,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | m3AChR |
| Gene groups (HGNC) | Cholinergic receptors muscarinic |
| Reactome | 9 pathways, smallest: Acetylcholine regulates insulin secretion; Amine ligand-binding receptors; Regulation of insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P20309](https://www.uniprot.org/uniprotkb/P20309) (Muscarinic acetylcholine receptor M3):

> The muscarinic acetylcholine receptor mediates various cellular responses, including inhibition of adenylate cyclase, breakdown of phosphoinositides and modulation of potassium channels through the action of G proteins. Primary transducing effect is Pi turnover.

**Summary**, from NCBI Gene [1131](https://www.ncbi.nlm.nih.gov/gene/1131):

> The muscarinic cholinergic receptors belong to a larger family of G protein-coupled receptors. The functional diversity of these receptors is defined by the binding of acetylcholine and includes cellular responses such as adenylate cyclase inhibition, phosphoinositide degeneration, and potassium channel mediation. Muscarinic receptors influence many effects of acetylcholine in the central and peripheral nervous system. The muscarinic cholinergic receptor 3 controls smooth muscle contraction and …

**Accessions** — [HGNC:1952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1952) · Entrez [1131](https://www.ncbi.nlm.nih.gov/gene/1131) · UniProt [P20309](https://www.uniprot.org/uniprotkb/P20309) · Ensembl [ENSG00000133019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133019)

## Data

Gene col 5402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5402); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5402]; `tensor/DDL_lfc|DDL_z.npy` [5402]; `embed/gene_vectors.npy` [5402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5402 or target_col == 5402). Every well: [[CHRM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
