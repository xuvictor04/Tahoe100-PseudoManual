---
symbol: "CNKSR3"
type: "gene"
col: 7734
ensembl_id: "ENSG00000153721"
name: "CNKSR family member 3"
location: "6q25.2"
module: 217
arm: "+"
pooled_cpm: 51.57
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# CNKSR3

*CNKSR family member 3* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +27.9, q 0e+00, up in 37 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 22 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SHP-77 0.163×, SK-MEL-2 0.256×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.340×, AN3 CA 0.280×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.192×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.101×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIP2C-AS1]] (+0.55, fdr 6e-05), [[ZFHX3]] (+0.55, fdr 4e-05), [[IPCEF1]] (+0.55, fdr 1e-05, ⚠ same locus), [[ETS2]] (+0.54, fdr 3e-05); moves opposite to [[GON4L]] (-0.47, fdr 9e-05), [[ODF2]] (-0.46, fdr 3e-04), [[SENP5]] (-0.45, fdr 3e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FGL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[DIP2C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +27.9 | 0e+00 | 37/44 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +14.9 | 0e+00 | 29/45 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +14.7 | 0e+00 | 35/44 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +14.5 | 1e-45 | 33/44 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +13.5 | 2e-39 | 30/44 (C32, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.99×** | +12.4 | 2e-33 | 32/44 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.51×** | +12.0 | 3e-31 | 35/45 (Panc 03.27, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +9.2 | 3e-18 | 26/44 (PANC-1, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +9.1 | 7e-18 | 23/44 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +9.0 | 1e-17 | 26/44 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +8.8 | 6e-17 | 28/44 (NCI-H2347, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.9 | 3e-10 | 21/43 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +6.9 | 3e-10 | 24/45 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.5 | 3e-09 | 23/43 (HEC-1-A, CHP-212, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 3e-08 | 20/44 (PANC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +5.7 | 6e-07 | 14/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7734.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 22 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SHP-77 0.163×, SK-MEL-2 0.256×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.340×, AN3 CA 0.280×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.192×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -5.3 | 8e-05 | 3/46 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | 0.848× | -3.3 | 0.21 | 15/43 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 0.855× | -3.2 | 0.21 | 14/42 (NCI-H2030, A-172, …) | two highest doses | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.856× | -3.2 | 0.21 | 12/44 (RPMI-7951, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 832 | 0 | 31 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 38.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.2) | — |
| [[C32 (line)]] | wt | 57.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +19.7) | — |
| [[NCI-H2347 (line)]] | alt | 43.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +18.5) | — |
| [[Panc 03.27 (line)]] | alt | 31.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +20.6) | — |
| [[PANC-1 (line)]] | alt | 41.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.0) | — |
| [[A498 (line)]] | wt | 44.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +20.9) | — |
| [[BT-474 (line)]] | alt | 37.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.1) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.235× (z -8.7) |
| [[HS-578T (line)]] | alt | 47.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.2) | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.2) |
| [[SNU-423 (line)]] | alt | 63.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +16.0) | — |
| [[A-172 (line)]] | wt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 36.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +18.7) | — |
| [[HepG2_C3A (line)]] | wt | 94.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.95× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 26.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +15.7) | [[Adagrasib (drug)]] 0.05 µM 0.665× (z -9.4) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +18.6) | — |
| [[hTERT-HPNE (line)]] | wt | 60.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +14.8) | — |
| [[J82 (line)]] | alt | 30.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +16.1) | — |
| [[LS 180 (line)]] | wt | 26.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 51.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +11.9) | — |
| [[A549 (line)]] | wt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 93.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 63.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 25.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.9) | — |
| [[KATO III (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.0) | — |
| [[LoVo (line)]] | wt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +9.0) | — |
| [[RKO (line)]] | wt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.5) | — |
| [[SW48 (line)]] | wt | 33.7 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.146× (z -9.7) |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2C-AS1]] | +0.55 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[ZFHX3]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[IPCEF1]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 | STRING 749; ⚠ same locus (30.7 kb, same strand: neighbours can correlate without regulation) |
| [[ETS2]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[FLVCR2]] | +0.52 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TRIM29]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[BATF]] | +0.51 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[TSPAN12]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CREB3L4]] | +0.50 | +0.57 / +0.26 | both halves | 4e-04 |  |
| [[DIP2C]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TRPS1]] | +0.50 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[CEBPD]] | +0.49 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[DENND2B]] | +0.49 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GON4L]] | -0.47 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ODF2]] | -0.46 | -0.56 / -0.26 | both halves | 3e-04 |  |
| [[SENP5]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.44 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[POLR2J4]] | -0.44 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[STK4]] | -0.44 | -0.48 / -0.24 | both halves | 4e-04 |  |
| [[FAM3C2P]] | -0.43 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SFT2D1]] | -0.43 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[ALDOA]] | -0.43 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[TMEM104]] | -0.43 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[SBNO1]] | -0.42 | -0.48 / -0.26 | both halves | 3e-04 |  |
| [[TXNDC12]] | -0.42 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGL1]] | B | FGL1 activity raises CNKSR3's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.02× lower at baseline in the lines without FGL1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[PLXDC2]] | B | PLXDC2 activity raises CNKSR3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without PLXDC2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[DIP2C-AS1]] | C | DIP2C-AS1's natural level weakens CNKSR3's drug response | DIP2C-AS1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.11; direction clear | 0.064 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIP2C]] | C | CNKSR3 activity raises DIP2C's level | lines that do not express CNKSR3 (4) vs lines expressing it (46) | 3.84× lower at baseline in the lines without CNKSR3 | 0.040 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GFOD1, CMTM7, NBEAP2; maybe low, not absent |
| [[ZNF428]] | C | CNKSR3 activity raises ZNF428's level | lines that do not express CNKSR3 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without CNKSR3 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GFOD1, CMTM7, NBEAP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.4, 13.9); signed map (48.8, 11.9). **Vector** length 105, 25.3% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +27.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.7 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.8 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | CNKSR family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:154,387,515-154,510,685 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31349; previously MAGI1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9H4](https://www.uniprot.org/uniprotkb/Q6P9H4) (Connector enhancer of kinase suppressor of ras 3):

> Involved in transepithelial sodium transport. Regulates aldosterone-induced and epithelial sodium channel (ENaC)-mediated sodium transport through regulation of ENaC cell surface expression. Acts as a scaffold protein coordinating the assembly of an ENaC-regulatory complex (ERC).

**Summary**, from NCBI Gene [154043](https://www.ncbi.nlm.nih.gov/gene/154043):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be involved in several processes, including negative regulation of ERK1 and ERK2 cascade; negative regulation of peptidyl-serine phosphorylation; and positive regulation of sodium ion transport. Predicted to act upstream of or within positive regulation of sodium ion transmembrane transporter activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23034) · Entrez [154043](https://www.ncbi.nlm.nih.gov/gene/154043) · UniProt [Q6P9H4](https://www.uniprot.org/uniprotkb/Q6P9H4) · Ensembl [ENSG00000153721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153721)

## Data

Gene col 7734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7734); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7734]; `tensor/DDL_lfc|DDL_z.npy` [7734]; `embed/gene_vectors.npy` [7734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7734 or target_col == 7734). Every well: [[CNKSR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNKSR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
