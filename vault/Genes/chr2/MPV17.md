---
symbol: "MPV17"
type: "gene"
col: 3632
ensembl_id: "ENSG00000115204"
name: "mitochondrial inner membrane protein MPV17"
location: "2p23.3"
module: 28
arm: "+"
pooled_cpm: 24.39
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MPV17

*mitochondrial inner membrane protein MPV17* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.17× (z +5.0, q 2e-04, up in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2030 3.70×, A-172 3.24×, NCI-H23 2.53×, A-427 2.37×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 3.16×, A-172 3.16×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.515× (z -14.9, q 0e+00, down in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.518× (z -14.7, q 0e+00, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFX1]] (+0.57, fdr 1e-05), [[TMEM260]] (+0.56, fdr 3e-05), [[METTL25B]] (+0.53, fdr 1e-04); moves opposite to [[KIF2A]] (-0.53, fdr 2e-05), [[ASAP3]] (-0.52, fdr 5e-05), [[SRPK2]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR9-3HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3632.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2030 3.70×, A-172 3.24×, NCI-H23 2.53×, A-427 2.37×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 3.16×, A-172 3.16×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.0 | 2e-04 | 14/48 (HS-578T, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.0 | 2e-04 | 18/42 (SW 900, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +4.9 | 2e-04 | 12/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.018 | 16/47 (A-427, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.043 | 20/47 (NCI-H2030, A-172, …) | rises with dose | composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +3.4 | 0.066 | 7/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.066 | 4/48 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.13 | 5/47 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.13 | 7/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.0 | 0.14 | 8/48 (NCI-H23, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -14.9 | 0e+00 | 35/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -14.7 | 0e+00 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -11.4 | 1e-27 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.618×** | -10.8 | 7e-25 | 33/48 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.655×** | -9.5 | 3e-19 | 28/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -8.6 | 6e-16 | 28/46 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.489×** | -8.4 | 5e-15 | 29/47 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -8.2 | 2e-14 | 27/48 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.747×** | -6.2 | 5e-08 | 25/48 (Hs 766T, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -6.1 | 5e-08 | 21/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -5.0 | 4e-05 | 16/40 (SNU-423, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.829×** | -4.2 | 0.001 | 15/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.836× | -4.0 | 0.003 | 12/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | 0.842× | -3.8 | 0.005 | 15/45 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.844× | -3.8 | 0.006 | 11/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.844× | -3.6 | 0.010 | 13/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **0.765×** | -3.1 | 0.050 | 2/48 (LoVo, BT-474) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 0.907× | -3.1 | 0.061 | 2/48 (A498, SHP-77) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.829×** | -3.0 | 0.071 | 2/48 (SW480, A498) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.9 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 34.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -12.1) |
| [[A-172 (line)]] | wt | 24.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 36.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0485× (z -17.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0861× (z -8.7) |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.329× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.371× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -9.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.411× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.192× (z -12.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFX1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TMEM260]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[METTL25B]] | +0.53 | +0.67 / +0.36 | both halves | 1e-04 |  |
| [[CHM]] | +0.53 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[AIMP1]] | +0.53 | +0.65 / +0.34 | both halves | 1e-04 |  |
| [[FCF1]] | +0.52 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[GOLGA1]] | +0.52 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[C1S]] | +0.51 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PCID2]] | +0.49 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[TM9SF4]] | +0.49 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[C1orf43]] | +0.49 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[GOSR1]] | +0.49 | +0.52 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2A]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ASAP3]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SRPK2]] | -0.52 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CDC42SE2]] | -0.51 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[RALGPS1]] | -0.51 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[FAM102B]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[CDYL]] | -0.49 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TCF20]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[MAST2]] | -0.48 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[STRN]] | -0.48 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[RNF38]] | -0.47 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[TSPAN17]] | -0.47 | -0.58 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR9-3HG]] | B | MIR9-3HG activity raises MPV17's level | lines that do not express MIR9-3HG (21) vs lines expressing it (29) | 1.21× lower at baseline in the lines without MIR9-3HG | 0.059 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, SNAP91 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.7, 16.3); signed map (9.5, -22.5). **Vector** length 71.5, 12.4% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -10.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.4 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial inner membrane protein MPV17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,309,492-27,325,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYM1 |
| Reactome | 2 pathways, smallest: Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P39210](https://www.uniprot.org/uniprotkb/P39210) (Mitochondrial inner membrane protein Mpv17):

> Non-selective channel that modulates the membrane potential under normal conditions and oxidative stress, and is involved in mitochondrial homeostasis. Involved in mitochondrial deoxynucleoside triphosphates (dNTP) pool homeostasis and mitochondrial DNA (mtDNA) maintenance. May be involved in the regulation of reactive oxygen species metabolism and the control of oxidative phosphorylation (By similarity).

**Summary**, from NCBI Gene [4358](https://www.ncbi.nlm.nih.gov/gene/4358):

> This gene encodes a mitochondrial inner membrane protein that is implicated in the metabolism of reactive oxygen species. Mutations in this gene have been associated with the hepatocerebral form of mitochondrial DNA depletion syndrome (MDDS). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7224) · Entrez [4358](https://www.ncbi.nlm.nih.gov/gene/4358) · UniProt [P39210](https://www.uniprot.org/uniprotkb/P39210) · Ensembl [ENSG00000115204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115204)

## Data

Gene col 3632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3632); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3632]; `tensor/DDL_lfc|DDL_z.npy` [3632]; `embed/gene_vectors.npy` [3632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3632 or target_col == 3632). Every well: [[MPV17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPV17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
