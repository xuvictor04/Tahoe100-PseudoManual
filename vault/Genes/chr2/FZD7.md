---
symbol: "FZD7"
type: "gene"
col: 7916
ensembl_id: "ENSG00000155760"
name: "frizzled class receptor 7"
location: "2q33.1"
module: 11
arm: "+"
pooled_cpm: 10.73
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# FZD7

*frizzled class receptor 7* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +12.8, q 8e-35, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.564× (z -6.8, q 7e-09, down in 15 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.358× (z -6.6, q 1e-08, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D1]] (+0.61, fdr 1e-05), [[PNRC1]] (+0.60, fdr 1e-05), [[IRX5]] (+0.60, fdr 1e-05); moves opposite to [[OPA1]] (-0.55, fdr 3e-05), [[HTT]] (-0.53, fdr 1e-04), [[ANAPC10]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[SLFN5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +12.8 | 8e-35 | 38/41 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +12.5 | 3e-33 | 28/43 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.2 | 4e-05 | 19/40 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.0 | 7e-05 | 21/39 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.46×** | +4.7 | 3e-04 | 15/44 (Panc 03.27, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 0.001 | 20/42 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 0.001 | 16/45 (J82, HOP62, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.002 | 17/43 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.015 | 10/43 (PANC-1, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +3.5 | 0.028 | 8/45 (PANC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.053 | 12/45 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.090 | 2/42 (LS 180, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.59× | +3.0 | 0.10 | 6/40 (J82, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.10 | 5/45 (A498, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -6.8 | 7e-09 | 15/23 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -6.6 | 1e-08 | 28/43 (A498, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.614×** | -5.8 | 2e-06 | 26/42 (PANC-1, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.638×** | -5.1 | 5e-05 | 17/29 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.662×** | -5.1 | 5e-05 | 17/32 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -4.7 | 3e-04 | 20/43 (SW 900, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -4.0 | 0.005 | 15/44 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -4.0 | 0.005 | 17/44 (A498, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.543×** | -3.9 | 0.005 | 13/41 (H4, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **0.730×** | -3.9 | 0.007 | 14/42 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -3.8 | 0.008 | 18/43 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.739×** | -3.7 | 0.010 | 10/44 (SK-MEL-2, SW 1088, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.011 | 16/43 (NCI-H661, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.4 | 0.024 | 5/45 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -3.4 | 0.030 | 6/43 (A-427, LS 180, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.604×** | -3.2 | 0.039 | 6/39 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.1 | 0.057 | 11/45 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.776×** | -3.0 | 0.082 | 8/43 (AN3 CA, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -11.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.48 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.1) |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.220× (z -9.3) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 6.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +10.3) | — |
| [[J82 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.6) | — |
| [[KATO III (line)]] | alt | 6.09 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0544× (z -9.2) |
| [[LoVo (line)]] | wt | 8.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 8.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0859× (z -12.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0826× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.05 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.110× (z -9.5) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0988× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D1]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PNRC1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IRX5]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[TBCC]] | +0.59 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[CASP3]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MEPCE]] | +0.58 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[C14orf119]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZIC2]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[TOPORS]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[EP300]] | +0.57 | +0.44 / +0.31 | both halves | 2e-04 | pathway: Signaling by WNT |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.55 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[HTT]] | -0.53 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[ANAPC10]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TTC14]] | -0.52 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[TM9SF2]] | -0.51 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[STRAP]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GAK]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[BTAF1]] | -0.50 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SUDS3]] | -0.50 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[PABIR2]] | -0.50 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[NDRG3]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[GFM2]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FZD7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAB34]] | B | RAB34 activity raises FZD7's level | lines that do not express RAB34 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without RAB34 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RNF150, PYGO1 |
| [[IRX3]] | B | IRX3 activity raises FZD7's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without IRX3 | 0.018 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLFN5]] | C | FZD7 activity raises SLFN5's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 5.04× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[SIX5]] | C | FZD7 activity raises SIX5's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[ARPC1A]] | C | FZD7 activity raises ARPC1A's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[TOB2]] | C | FZD7 activity raises TOB2's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[FOXC1]] | C | FZD7 activity lowers FOXC1's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 2.63× higher at baseline in the lines without FZD7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2 |
| [[ZNF703]] | C | FZD7 activity lowers ZNF703's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 3.58× higher at baseline in the lines without FZD7 | 0.080 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2 |
| [[HTT]] | C | FZD7 activity raises HTT's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 1.45× lower at baseline in the lines without FZD7 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2 |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (20.0, -4.7); signed map (13.6, -6.7). **Vector** length 85.4, 16.2% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:202,033,855-202,038,441 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FzE3 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 11 pathways, smallest: Killing mechanisms; WNT5:FZD7-mediated leishmania damping; Class B/2 (Secretin family receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [O75084](https://www.uniprot.org/uniprotkb/O75084) (Frizzled-7):

> Receptor for Wnt proteins. Most frizzled receptors are coupled to the beta-catenin canonical signaling pathway, which leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin and activation of Wnt target genes. A second signaling pathway involving PKC and calcium fluxes has been seen for some family members, but it is not yet clear if it represents a distinct pathway or if it can be integrated in the canonical pathway, as PKC seems to be …

**Summary**, from NCBI Gene [8324](https://www.ncbi.nlm.nih.gov/gene/8324):

> Members of the 'frizzled' gene family encode 7-transmembrane domain proteins that are receptors for Wnt signaling proteins. The FZD7 protein contains an N-terminal signal sequence, 10 cysteine residues typical of the cysteine-rich extracellular domain of Fz family members, 7 putative transmembrane domains, and an intracellular C-terminal tail with a PDZ domain-binding motif. FZD7 gene expression may downregulate APC function and enhance beta-catenin-mediated signals in poorly differentiated …

**Accessions** — [HGNC:4045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4045) · Entrez [8324](https://www.ncbi.nlm.nih.gov/gene/8324) · UniProt [O75084](https://www.uniprot.org/uniprotkb/O75084) · Ensembl [ENSG00000155760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155760)

## Data

Gene col 7916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7916); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7916]; `tensor/DDL_lfc|DDL_z.npy` [7916]; `embed/gene_vectors.npy` [7916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7916 or target_col == 7916). Every well: [[FZD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
