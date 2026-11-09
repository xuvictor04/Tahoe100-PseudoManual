---
symbol: "IQCH"
type: "gene"
col: 2386
ensembl_id: "ENSG00000103599"
name: "IQ motif containing H"
location: "15q23"
module: 4
arm: "+"
pooled_cpm: 28.88
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# IQCH

*IQ motif containing H* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.44× (z +15.5, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.227× (z -15.4, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALT9]] (+0.63, fdr 1e-05), [[PCNX2]] (+0.60, fdr 1e-05), [[HLCS]] (+0.59, fdr 1e-05); moves opposite to [[APTR]] (-0.56, fdr 3e-05), [[KLC4]] (-0.54, fdr 5e-05), [[TSC22D4]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PCNX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.44×** | +15.5 | 0e+00 | 44/46 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.80×** | +13.9 | 2e-41 | 44/46 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.47×** | +13.0 | 4e-36 | 44/45 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.95×** | +8.9 | 8e-17 | 43/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +6.7 | 2e-09 | 35/45 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +5.7 | 1e-06 | 34/46 (KATO III, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +5.3 | 7e-06 | 29/46 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.9 | 7e-05 | 26/46 (NCI-H1792, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 6e-04 | 22/44 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.089 | 13/45 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.38×** | +3.1 | 0.092 | 14/34 (A549, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.34×** | +3.1 | 0.093 | 14/45 (A549, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.093 | 15/45 (LS 180, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.227×** | -15.4 | 0e+00 | 43/46 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.265×** | -13.8 | 1e-40 | 39/45 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.336×** | -11.3 | 3e-27 | 41/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.350×** | -10.9 | 2e-25 | 38/45 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -6.2 | 7e-08 | 28/45 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -6.0 | 2e-07 | 28/46 (SHP-77, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.341×** | -5.8 | 4e-07 | 30/42 (SK-MEL-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -5.7 | 7e-07 | 27/42 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.549×** | -4.9 | 6e-05 | 28/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.624×** | -4.9 | 6e-05 | 32/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.429×** | -4.6 | 2e-04 | 25/42 (C32, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.619×** | -3.9 | 0.004 | 20/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.678×** | -3.9 | 0.005 | 21/45 (PANC-1, J82, …) | top dose only | composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.031 | 19/46 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.558×** | -3.2 | 0.061 | 16/44 (LS 180, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.6 | 3 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.2) | [[Digitoxin (drug)]] 0.5 µM 0.0909× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 70.6 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0883× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.148× (z -15.2) |
| [[LoVo (line)]] | wt | 46.8 | 2 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -19.8) |
| [[NCI-H1573 (line)]] | alt | 55.6 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.115× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -13.0) |
| [[A549 (line)]] | wt | 32.7 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.97× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.2) |
| [[KATO III (line)]] | alt | 48.4 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.21× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 24.0 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.68× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -8.8) |
| [[SHP-77 (line)]] | alt | 67.6 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -16.0) |
| [[SW480 (line)]] | alt | 48.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -16.7) |
| [[A-427 (line)]] | wt | 27.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -14.1) |
| [[COLO 205 (line)]] | alt | 27.7 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 5.80× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.137× (z -10.3) |
| [[HOP62 (line)]] | alt | 33.6 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 5.77× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -12.4) |
| [[J82 (line)]] | alt | 27.7 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -13.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.154× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 30.8 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.35× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.0) |
| [[HT-29 (line)]] | alt | 23.6 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.52× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0625× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.180× (z -10.1) |
| [[A-172 (line)]] | wt | 27.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.36× (z +11.0) | — |
| [[A498 (line)]] | wt | 27.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.56× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 25.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 10.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.43× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 8.34 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 26.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0465× (z -17.6) |
| [[LS 180 (line)]] | wt | 14.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 6.93× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 10.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.95× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 36.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 57.4 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0124× (z -16.3) |
| [[SW 900 (line)]] | alt | 13.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.84× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -8.9) |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0559× (z -9.9) |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0850× (z -9.8) ⚠ toxic |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 21.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -11.3) |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0746× (z -9.0) |
| [[SNU-423 (line)]] | alt | 9.90 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALT9]] | +0.63 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.60 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[HLCS]] | +0.59 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CCDC57]] | +0.58 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[TRAPPC9]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[B3GALT6]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[CEP41]] | +0.56 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[GGACT]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[NAA15]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FGGY]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DPH6]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[HERPUD2-AS1]] | +0.53 | +0.68 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTR]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[KLC4]] | -0.54 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[TSC22D4]] | -0.53 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[VDAC1P8]] | -0.52 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[COG7]] | -0.51 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[NKIRAS1]] | -0.51 | -0.10 / -0.48 | ⚠ not reproduced | 0.003 |  |
| [[CD247]] | -0.50 | -0.24 / -0.37 | both halves | 5e-04 |  |
| [[TMEM94]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[DNASE2]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.50 | -0.21 / -0.44 | both halves | 6e-04 |  |
| [[RCOR3]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[EPHX1]] | -0.49 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[HOXB3]] | -0.49 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCNX2]] | B | PCNX2 activity raises IQCH's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without PCNX2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[SPATA17]] | C | SPATA17 activity raises IQCH's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CEP41]] | C | CEP41 activity raises IQCH's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without CEP41 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.8, -32.3); signed map (8.2, -49.0). **Vector** length 78.0, 20.5% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.8 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -1.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.4 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.9 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:67,254,786-67,502,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12476 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VS3](https://www.uniprot.org/uniprotkb/Q86VS3) (IQ domain-containing protein H):

> May play a regulatory role in spermatogenesis.

**Summary**, from NCBI Gene [64799](https://www.ncbi.nlm.nih.gov/gene/64799):

> Predicted to act upstream of or within lncRNA transcription and single fertilization. Predicted to be active in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25721) · Entrez [64799](https://www.ncbi.nlm.nih.gov/gene/64799) · UniProt [Q86VS3](https://www.uniprot.org/uniprotkb/Q86VS3) · Ensembl [ENSG00000103599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103599)

## Data

Gene col 2386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2386); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2386]; `tensor/DDL_lfc|DDL_z.npy` [2386]; `embed/gene_vectors.npy` [2386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2386 or target_col == 2386). Every well: [[IQCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
