---
symbol: "USP45"
type: "gene"
col: 4442
ensembl_id: "ENSG00000123552"
name: "ubiquitin specific peptidase 45"
location: "6q16.2"
module: 18
arm: "+"
pooled_cpm: 39.04
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# USP45

*ubiquitin specific peptidase 45* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +15.0, q 0e+00, up in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +14.9, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.578× (z -6.9, q 2e-09, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.472×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.280×; ⚠ toxic; transcription drop); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.235×); [[Mebendazole (drug)]] 0.05 µM in 1 line (SW48 0.241×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ME2]] (+0.69, fdr 7e-06), [[NUDT3]] (+0.63, fdr 2e-05), [[SLC9B2]] (+0.60, fdr 1e-05); moves opposite to [[ISCA2]] (-0.58, fdr 3e-05), [[C6orf47]] (-0.58, fdr 2e-04), [[RNF5]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +15.0 | 0e+00 | 32/40 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +14.9 | 0e+00 | 37/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +14.6 | 0e+00 | 34/46 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +12.8 | 2e-35 | 41/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +12.7 | 1e-34 | 32/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +12.1 | 1e-31 | 39/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +10.8 | 2e-25 | 40/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +10.5 | 6e-24 | 34/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +9.0 | 1e-17 | 33/48 (C32, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +8.8 | 8e-17 | 26/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +8.6 | 6e-16 | 34/47 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.5 | 8e-16 | 26/48 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +7.9 | 1e-13 | 31/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +7.3 | 2e-11 | 28/48 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +7.1 | 7e-11 | 27/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +6.3 | 1e-08 | 20/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +6.2 | 2e-08 | 27/48 (SW480, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +6.1 | 4e-08 | 23/48 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.8 | 1e-07 | 23/48 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +5.5 | 1e-06 | 17/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 5e-05 | 20/47 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4442.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.472×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.280×; ⚠ toxic; transcription drop); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.235×); [[Mebendazole (drug)]] 0.05 µM in 1 line (SW48 0.241×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.578×** | -6.9 | 2e-09 | 26/48 (PANC-1, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.793×** | -3.8 | 0.040 | 13/48 (SW 1271, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.779× | -3.2 | 0.30 | 13/46 (SNU-1, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 51.4 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.48× (z +18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 45.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.1) | — |
| [[SW480 (line)]] | alt | 38.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.3) | — |
| [[A-427 (line)]] | wt | 73.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -12.6) |
| [[HOP62 (line)]] | alt | 32.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 34.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +13.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 30.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.86× (z +8.8) | — |
| [[A549 (line)]] | wt | 38.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 38.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 42.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.4) | [[Bosentan (hydrate) (drug)]] 5 µM 0.235× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.26× (z +9.4) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 23.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.9) | — |
| [[C32 (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.22× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 31.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.9) | — |
| [[KATO III (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 44.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0835× (z -8.5) |
| [[PANC-1 (line)]] | alt | 64.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.4) | — |
| [[RKO (line)]] | wt | 72.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -20.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 61.5 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.241× (z -9.7) |
| [[AN3 CA (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ME2]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NUDT3]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SLC9B2]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MRPS25]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TTL]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CARNMT1]] | +0.57 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[PAK2]] | +0.57 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[CPNE7]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[UBE2G2]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[REEP3]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[HDDC2]] | +0.55 | +0.50 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[C6orf47]] | -0.58 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[RNF5]] | -0.55 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ASB8]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[DCTN3]] | -0.51 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ZNF622]] | -0.51 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[TBCC]] | -0.50 | -0.17 / -0.61 | ⚠ one half (not replicated) | 0.001 |  |
| [[CCDC34]] | -0.50 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[TFIP11]] | -0.50 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[RFC1]] | -0.50 | -0.53 / -0.38 | both halves | 7e-05 | pathway: Global Genome Nucleotide Excision Repair (GG-NER) |
| [[CFAP20]] | -0.50 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[CA9]] | -0.50 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ZDHHC12]] | -0.49 | -0.28 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises USP45's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without ADCY3 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[CA9]] | B | CA9 activity lowers USP45's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.42× higher at baseline in the lines without CA9 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.3, -34.5); signed map (-10.8, -42.1). **Vector** length 88.5, 19.6% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +14.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +9.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -3.0 | -3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -2.5 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +2.7 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.2 — chr6:99,432,325-99,521,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14793 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 4 pathways, smallest: Formation of Incision Complex in GG-NER; Global Genome Nucleotide Excision Repair (GG-NER); Nucleotide Excision Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70EL2](https://www.uniprot.org/uniprotkb/Q70EL2) (Ubiquitin carboxyl-terminal hydrolase 45):

> Catalyzes the deubiquitination of SPDL1. Plays a role in the repair of UV-induced DNA damage via deubiquitination of ERCC1, promoting its recruitment to DNA damage sites. May be involved in the maintenance of photoreceptor function. May play a role in normal retinal development (By similarity). Plays a role in cell migration.

**Summary**, from NCBI Gene [85015](https://www.ncbi.nlm.nih.gov/gene/85015):

> The protein encoded by this gene is a deubiquitylase that binds ERCC1, the catalytic subunit of the XPF-ERCC1 DNA repair endonuclease. This endonuclease is a critical regulator of DNA repair processes, and the deubiquitylase activity of the encoded protein is important for maintaining the DNA repair ability of XPF-ERCC1. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:20080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20080) · Entrez [85015](https://www.ncbi.nlm.nih.gov/gene/85015) · UniProt [Q70EL2](https://www.uniprot.org/uniprotkb/Q70EL2) · Ensembl [ENSG00000123552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123552)

## Data

Gene col 4442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4442); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4442]; `tensor/DDL_lfc|DDL_z.npy` [4442]; `embed/gene_vectors.npy` [4442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4442 or target_col == 4442). Every well: [[USP45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
