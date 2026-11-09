---
symbol: "NFKBID"
type: "gene"
col: 9498
ensembl_id: "ENSG00000167604"
name: "NFKB inhibitor delta"
location: "19q13.12"
module: 26
arm: "+"
pooled_cpm: 14.14
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# NFKBID

*NFKB inhibitor delta* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.12× (z +21.8, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.564× (z -5.4, q 4e-05, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC14A]] (+0.64, fdr 1e-05), [[IRF3]] (+0.62, fdr 1e-05), [[IFNGR2]] (+0.62, fdr 1e-05); moves opposite to [[EXOC2]] (-0.60, fdr 2e-05), [[COMMD2]] (-0.57, fdr 4e-05), [[PSMD3]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.12×** | +21.8 | 0e+00 | 46/46 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.48×** | +20.0 | 0e+00 | 38/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.04×** | +10.1 | 1e-21 | 38/45 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.9 | 3e-13 | 32/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +7.8 | 7e-13 | 31/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +7.4 | 1e-11 | 33/40 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +7.3 | 2e-11 | 31/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +7.1 | 7e-11 | 28/44 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +5.4 | 4e-06 | 24/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.004 | 14/47 (HOP62, SW480, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +3.8 | 0.008 | 18/45 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.015 | 17/46 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.021 | 13/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.024 | 14/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.034 | 12/46 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.564×** | -5.4 | 4e-05 | 25/46 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -5.3 | 4e-05 | 14/22 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -4.8 | 2e-04 | 27/46 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.632×** | -4.3 | 0.002 | 20/43 (MIA PaCa-2, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -4.3 | 0.002 | 20/46 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -4.0 | 0.005 | 20/46 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.012 | 23/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -3.8 | 0.012 | 18/46 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.16 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 10.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +17.4) | — |
| [[HEC-1-A (line)]] | alt | 56.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +19.2) | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0672× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 22.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +16.5) | — |
| [[A498 (line)]] | wt | 27.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +15.9) | — |
| [[A549 (line)]] | wt | 14.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.131× (z -9.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 23.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +11.1) | — |
| [[J82 (line)]] | alt | 10.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +17.2) | — |
| [[LoVo (line)]] | wt | 4.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.39× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 4.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.99× (z +14.5) | — |
| [[SW1417 (line)]] | alt | 13.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.6) | — |
| [[SW48 (line)]] | wt | 13.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +10.4) | [[Bortezomib (drug)]] 0.05 µM 0.0440× (z -10.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 1 | — | [[Aprepitant (drug)]] 0.05 µM 0.0558× (z -9.2) |
| [[C32 (line)]] | wt | 5.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +9.3) | — |
| [[H4 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 8.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +15.7) | — |
| [[NCI-H1573 (line)]] | alt | 8.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.57× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 5.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.110× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 6.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +9.3) | — |
| [[SW480 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +11.9) | — |
| [[A-427 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC14A]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[IRF3]] | +0.62 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[IFNGR2]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PPP1R15B-AS1]] | +0.60 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[SPEN-AS1]] | +0.59 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[LMNB1-DT]] | +0.59 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[PSD]] | +0.58 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SNHG31]] | +0.58 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[STARD4-AS1]] | +0.57 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[ERICH2-DT]] | +0.57 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[UPK2]] | +0.57 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[SIN3A]] | +0.57 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC2]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[COMMD2]] | -0.57 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[PSMD3]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[RNF216]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MRFAP1]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[TBC1D7]] | -0.55 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[GTF3C3]] | -0.54 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[POLR3B]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RRP1B]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SRRD]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[VTA1]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SMIM8]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NFKBID's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises NFKBID's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers NFKBID's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.392). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.5, 9.0); signed map (33.0, -0.4). **Vector** length 98.8, 23.9% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +21.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +20.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | -0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +0.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | +3.0 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,887,630-35,902,303 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TA-NFKBH, IkappaBNS, IkBNS |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NFKB inhibitor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI38](https://www.uniprot.org/uniprotkb/Q8NI38) (NF-kappa-B inhibitor delta):

> Regulates the expression of IL-2, IL-6, and other cytokines through regulation on NF-kappa-B activity. Functions in the regulation of inflammatory responses. Involved in the induction of T helper 17 cells (Th17) differentiation upon recognition of antigen by T cell antigen receptor (TCR). May also regulate TCR-induced negative selection of thymocytes.

**Summary**, from NCBI Gene [84807](https://www.ncbi.nlm.nih.gov/gene/84807):

> Predicted to enable NF-kappaB binding activity. Predicted to be involved in T cell receptor signaling pathway; positive regulation of T-helper 17 cell differentiation; and regulation of gene expression. Predicted to act upstream of or within several processes, including negative regulation of canonical NF-kappaB signal transduction; obsolete negative regulation of NF-kappaB transcription factor activity; and positive regulation of thymocyte apoptotic process. Predicted to be active in nucleus. …

**Accessions** — [HGNC:15671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15671) · Entrez [84807](https://www.ncbi.nlm.nih.gov/gene/84807) · UniProt [Q8NI38](https://www.uniprot.org/uniprotkb/Q8NI38) · Ensembl [ENSG00000167604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167604)

## Data

Gene col 9498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9498); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9498]; `tensor/DDL_lfc|DDL_z.npy` [9498]; `embed/gene_vectors.npy` [9498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9498 or target_col == 9498). Every well: [[NFKBID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKBID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
