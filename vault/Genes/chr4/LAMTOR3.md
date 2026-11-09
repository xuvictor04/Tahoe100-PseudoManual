---
symbol: "LAMTOR3"
type: "gene"
col: 3041
ensembl_id: "ENSG00000109270"
name: "late endosomal/lysosomal adaptor, MAPK and MTOR activator 3"
location: "4q23"
module: 23
arm: "+"
pooled_cpm: 25.19
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# LAMTOR3

*late endosomal/lysosomal adaptor, MAPK and MTOR activator 3* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.72× (z +20.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.712× (z -4.8, q 0.001, down in 18 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.824× (z -4.0, q 0.017, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (RPMI-7951 0.0849×, HEC-1-A 0.142×, BT-474 0.132×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.135×; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0815×); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0815×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPP1]] (+0.61, fdr 1e-05), [[PPP1R11]] (+0.60, fdr 1e-05), [[TSPAN31]] (+0.60, fdr 1e-05); moves opposite to [[NSMCE4A]] (-0.63, fdr 1e-05), [[HERC2P9]] (-0.61, fdr 1e-05), [[TCOF1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[FAM117A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +20.6 | 0e+00 | 45/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.53×** | +13.5 | 5e-39 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.5 | 2e-28 | 40/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.79×** | +10.1 | 5e-22 | 44/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +9.9 | 6e-21 | 38/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.82×** | +7.9 | 3e-13 | 34/47 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.3 | 2e-11 | 34/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +7.2 | 5e-11 | 31/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +7.2 | 5e-11 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.0 | 2e-10 | 31/48 (LoVo, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +6.8 | 8e-10 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.5 | 5e-09 | 36/48 (A-172, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.7 | 1e-04 | 19/38 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.3 | 8e-04 | 15/30 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.003 | 18/48 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.006 | 19/48 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.019 | 15/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.027 | 10/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (RPMI-7951 0.0849×, HEC-1-A 0.142×, BT-474 0.132×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.135×; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0815×); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0815×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.712×** | -4.8 | 0.001 | 18/35 (RPMI-7951, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -4.0 | 0.017 | 24/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.2 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +22.3) | — |
| [[NCI-H1573 (line)]] | alt | 41.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[PANC-1 (line)]] | alt | 18.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 16.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.0) | — |
| [[LoVo (line)]] | wt | 25.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.7) | — |
| [[A-172 (line)]] | wt | 19.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -12.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +15.3) | — |
| [[BT-474 (line)]] | alt | 17.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.81× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 33.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.91× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +13.9) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0815× (z -12.6) |
| [[J82 (line)]] | alt | 22.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +13.6) | — |
| [[KATO III (line)]] | alt | 31.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0849× (z -16.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 46.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +12.1) | — |
| [[C32 (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 50.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0815× (z -9.1) |
| [[Hs 766T (line)]] | wt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.2) | — |
| [[SW480 (line)]] | alt | 16.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +9.4) | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPP1]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R11]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TSPAN31]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | +0.58 | +0.61 / +0.41 | both halves | 4e-05 | pathway: Amino acids regulate mTORC1; STRING 720 |
| [[ATP6V1D]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Amino acids regulate mTORC1; STRING 726 |
| [[DAZAP2]] | +0.57 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[AMZ2]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[YME1L1]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[UFC1]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[OSER1-DT]] | +0.56 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[SNIP1]] | +0.56 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[BROX]] | +0.55 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMCE4A]] | -0.63 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.58 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[CEP85]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HERC2P2]] | -0.57 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[BRF1]] | -0.56 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NUP93]] | -0.55 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[HEATR3]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ANKS6]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[INPP4A]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[NR2C1]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[UBE2K]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 | STRING 485 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM117A]] | C | LAMTOR3's natural level weakens FAM117A's drug response | LAMTOR3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.01; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (23.7, -36.2); signed map (14.8, -5.0). **Vector** length 75.8, 15.9% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +20.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.1 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.7 | -0.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | +3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | late endosomal/lysosomal adaptor, MAPK and MTOR activator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:99,878,336-99,894,428 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MP1, MAPBP, Ragulator3; previously MAP2K1IP1, MAPKSP1 |
| Gene groups (HGNC) | Ragulator complex |
| Reactome | 21 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MAP2K and MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHA4](https://www.uniprot.org/uniprotkb/Q9UHA4) (Ragulator complex protein LAMTOR3):

> As part of the Ragulator complex it is involved in amino acid sensing and activation of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Activated by amino acids through a mechanism involving the lysosomal V-ATPase, the Ragulator plays a dual role for the small GTPases Rag (RagA/RRAGA, RagB/RRAGB, RagC/RRAGC and/or RagD/RRAGD): it (1) acts as a guanine nucleotide exchange factor (GEF), activating the small GTPases Rag and (2) …

**Summary**, from NCBI Gene [8649](https://www.ncbi.nlm.nih.gov/gene/8649):

> This gene encodes a scaffold protein that functions in the extracellular signal-regulated kinase (ERK) cascade. The protein is localized to late endosomes by the mitogen-activated protein-binding protein-interacting protein, and binds specifically to MAP kinase kinase MAP2K1/MEK1, MAP kinase MAPK3/ERK1, and MAP kinase MAPK1/ERK2. Studies of the orthologous gene in mouse indicate that it regulates late endosomal traffic and cell proliferation. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:15606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15606) · Entrez [8649](https://www.ncbi.nlm.nih.gov/gene/8649) · UniProt [Q9UHA4](https://www.uniprot.org/uniprotkb/Q9UHA4) · Ensembl [ENSG00000109270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109270)

## Data

Gene col 3041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3041); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3041]; `tensor/DDL_lfc|DDL_z.npy` [3041]; `embed/gene_vectors.npy` [3041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3041 or target_col == 3041). Every well: [[LAMTOR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMTOR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
