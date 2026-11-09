---
symbol: "RNF32-DT"
type: "gene"
col: 11311
ensembl_id: "ENSG00000182648"
name: "RNF32 divergent transcript"
location: "7q36.3"
module: 23
arm: "+"
pooled_cpm: 16.82
n_lines_expressing: 45
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RNF32-DT

*RNF32 divergent transcript* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +8.0, q 1e-12, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.286× (z -11.3, q 4e-27, down in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.370× (z -9.0, q 4e-17, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERMAP]] (+0.61, fdr 5e-05), [[LINC02340]] (+0.59, fdr 2e-05), [[PKD1L1]] (+0.58, fdr 1e-05); moves opposite to [[PGAP1]] (-0.50, fdr 5e-04), [[NFATC3]] (-0.49, fdr 8e-04, ⚠ one half only (not replicated)), [[PDE7A]] (-0.49, fdr 1e-04), [[ECI2]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 5 go from it, the strongest it → [[RNF32]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +8.0 | 1e-12 | 24/41 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +6.7 | 6e-09 | 31/42 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +4.9 | 2e-04 | 25/42 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +4.4 | 0.001 | 25/42 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.4 | 0.001 | 22/41 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.023 | 18/40 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.027 | 21/42 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.032 | 17/41 (SW480, NCI-H23, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.094 | 16/40 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 16/41 (KATO III, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.286×** | -11.3 | 4e-27 | 35/42 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.332×** | -10.0 | 5e-21 | 35/40 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.370×** | -9.0 | 4e-17 | 36/42 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.403×** | -8.2 | 2e-14 | 33/42 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.426×** | -7.7 | 1e-12 | 29/42 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.446×** | -7.3 | 3e-11 | 32/41 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.274×** | -6.1 | 7e-08 | 35/41 (NCI-H1792, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.551×** | -5.2 | 1e-05 | 24/41 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.568×** | -4.9 | 5e-05 | 24/39 (PANC-1, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.597×** | -4.7 | 2e-04 | 25/40 (NCI-H2030, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.605×** | -4.3 | 9e-04 | 24/40 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -4.1 | 0.002 | 22/42 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -4.0 | 0.003 | 22/40 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.670×** | -3.6 | 0.011 | 16/41 (PANC-1, A549, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.661×** | -3.6 | 0.012 | 17/42 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.047 | 15/41 (H4, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.613×** | -3.2 | 0.048 | 15/42 (NCI-H23, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.4 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.234× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 46.5 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0753× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 31.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.2) |
| [[H4 (line)]] | wt | 21.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.123× (z -8.6) |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0674× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.0) |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0280× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0485× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 27.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.0801× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +10.4) | [[Ixazomib citrate (drug)]] 0.5 µM 0.134× (z -9.7) |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0780× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 9.14 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +19.4) | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 2 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0931× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 6.73 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.9) | [[Daptomycin (drug)]] 0.5 µM 0.183× (z -9.0) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 7.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0446× (z -12.4) |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0575× (z -8.8) |
| [[SW480 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMAP]] | +0.61 | +0.73 / +0.40 | both halves | 5e-05 |  |
| [[LINC02340]] | +0.59 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[PKD1L1]] | +0.58 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ESRRB]] | +0.57 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[LINC00486]] | +0.57 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[CFAP161]] | +0.57 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[DHRS12]] | +0.56 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[EFCAB8]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[C19orf18]] | +0.54 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[FKRP]] | +0.54 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[SMIM15-AS1]] | +0.53 | +0.69 / +0.43 | both halves | 4e-05 |  |
| [[RFX3-DT]] | +0.53 | +0.63 / +0.38 | both halves | 6e-05 | same gene group |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAP1]] | -0.50 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[NFATC3]] | -0.49 | -0.58 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PDE7A]] | -0.49 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[ECI2]] | -0.48 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[SPICE1]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[XYLT2]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[KATNB1]] | -0.47 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[VDAC3]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[RELCH]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[P3H3]] | -0.46 | -0.63 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[PIGN]] | -0.46 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[CCDC134]] | -0.46 | -0.49 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[TRIM62]] | -0.46 | -0.48 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RNF32-DT's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SLC13A3]] | B | SLC13A3 activity lowers RNF32-DT's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.92× higher at baseline in the lines without SLC13A3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF32]] | B | RNF32-DT activity raises RNF32's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without RNF32-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[CELSR3]] | B | RNF32-DT activity lowers CELSR3's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without RNF32-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[IPCEF1]] | B | RNF32-DT activity lowers IPCEF1's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 2.12× higher at baseline in the lines without RNF32-DT | 0.088 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[MAD2L1-DT]] | B | RNF32-DT activity lowers MAD2L1-DT's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 1.54× higher at baseline in the lines without RNF32-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[ELAPOR1]] | B | RNF32-DT activity lowers ELAPOR1's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 1.27× higher at baseline in the lines without RNF32-DT | 0.094 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (33.3, -8.3); signed map (21.4, 6.1). **Vector** length 75.3, 15.9% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RNF32 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q36.3 — chr7:156,388,922-156,640,654 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MY040; previously C7orf13, LINC01006 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

UniProt [Q8NI28](https://www.uniprot.org/uniprotkb/Q8NI28) carries no function annotation.

**Summary**, from NCBI Gene [100506380](https://www.ncbi.nlm.nih.gov/gene/100506380):

> Predicted to be located in cytoplasm and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:48971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48971) · Entrez [100506380](https://www.ncbi.nlm.nih.gov/gene/100506380) · UniProt [Q8NI28](https://www.uniprot.org/uniprotkb/Q8NI28) · Ensembl [ENSG00000182648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182648)

## Data

Gene col 11311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11311); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11311]; `tensor/DDL_lfc|DDL_z.npy` [11311]; `embed/gene_vectors.npy` [11311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11311 or target_col == 11311). Every well: [[RNF32-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF32-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
