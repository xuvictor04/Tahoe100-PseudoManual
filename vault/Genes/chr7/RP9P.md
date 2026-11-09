---
symbol: "RP9P"
type: "gene"
col: 13009
ensembl_id: "ENSG00000205763"
name: "RP9 pseudogene"
location: "7p14.3"
module: 3
arm: "+"
pooled_cpm: 28.03
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RP9P

*RP9 pseudogene* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.09× (z +9.0, q 9e-17, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.523× (z -8.4, q 3e-14, down in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.568× (z -3.8, q 0.015, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.0775×, SW480 0.175×, C32 0.147×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW480 0.204×, SHP-77 0.122×, C32 0.175×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.0750×, NCI-H2030 0.0919×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[EX229 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0472×); [[Naproxen (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0652×); [[18β-Glycyrrhetinic acid (drug)]] 5 µM in 1 line (CHP-212 0.0960×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35D2]] (+0.63, fdr 1e-05), [[ARL8A]] (+0.63, fdr 1e-05), [[THAP3]] (+0.62, fdr 1e-05); moves opposite to [[CDC42]] (-0.59, fdr 1e-05), [[HNRNPC]] (-0.58, fdr 1e-05), [[ACTB]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MID2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.09×** | +9.0 | 9e-17 | 38/46 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +8.8 | 5e-16 | 34/46 (A-427, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.5 | 1e-08 | 28/45 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +6.5 | 1e-08 | 32/46 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +6.5 | 1e-08 | 28/46 (A498, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.83×** | +5.6 | 2e-06 | 27/46 (LoVo, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.5 | 3e-06 | 28/39 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +4.7 | 2e-04 | 23/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.69×** | +3.6 | 0.024 | 17/45 (A498, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.029 | 17/46 (C32, AsPC-1, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.029 | 15/46 (A498, A549, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.034 | 16/46 (A-172, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.042 | 15/45 (Hs 766T, MIA PaCa-2, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.085 | 17/46 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.0 | 0.087 | 12/45 (J82, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13009.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.0775×, SW480 0.175×, C32 0.147×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW480 0.204×, SHP-77 0.122×, C32 0.175×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.0750×, NCI-H2030 0.0919×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[EX229 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0472×); [[Naproxen (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0652×); [[18β-Glycyrrhetinic acid (drug)]] 5 µM in 1 line (CHP-212 0.0960×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.523×** | -8.4 | 3e-14 | 35/46 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.543×** | -7.9 | 1e-12 | 34/46 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.684×** | -4.9 | 2e-04 | 28/46 (SW480, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.721×** | -4.0 | 0.007 | 18/34 (A-172, NCI-H2030, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -3.8 | 0.015 | 24/47 (H4, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.8 | 0.015 | 1/46 (H4) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.025 | 20/46 (SW480, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.758×** | -3.6 | 0.025 | 19/41 (C-33 A, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.763×** | -3.2 | 0.081 | 15/38 (NCI-H2030, SW480, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 75.6 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 73.9 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -18.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.91× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.93× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.271× (z -10.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0775× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 132 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 43.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0750× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 26.6 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.14× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 28.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0472× (z -13.0) |
| [[C-33 A (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 5 µM 0.0960× (z -9.9) |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0652× (z -10.1) |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[PANC-1 (line)]] | alt | 24.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.79× (z +10.8) | — |
| [[RKO (line)]] | wt | 18.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.29× (z +8.7) | — |
| [[SW48 (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A549 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35D2]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[THAP3]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LRRC37B]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[UBR2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[AGO4]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ADPRM]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[IL17RA]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SNHG32]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[FLYWCH1]] | +0.56 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CARNMT1-AS1]] | +0.55 | +0.28 / +0.61 | both halves | 3e-04 |  |
| [[MED10]] | +0.55 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[HNRNPC]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ACTB]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.55 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[GNB1]] | -0.55 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[RBBP7]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[GPAA1]] | -0.54 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[VMA21]] | -0.54 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[VCL]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ARF3]] | -0.52 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[ITGB1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MID2]] | B | MID2 activity lowers RP9P's level | lines that do not express MID2 (17) vs lines expressing it (33) | 1.56× higher at baseline in the lines without MID2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF711, FRMPD3, RPS6KA6 |
| [[RNF135]] | B | RNF135 activity lowers RP9P's level | lines that do not express RNF135 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without RNF135 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000291063, TMEM54, ENSG00000266865; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity raises RP9P's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.409). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.3, -17.3); signed map (-22.2, 5.7). **Vector** length 114, 30.1% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.6 | +8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.5 | +9.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.2 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +6.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.2 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.5 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -8.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.8 | -2.4 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.4 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RP9 pseudogene |
| Locus type | pseudogene |
| Location | 7p14.3 — chr7:32,916,815-32,943,038 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33969) · Entrez [441212](https://www.ncbi.nlm.nih.gov/gene/441212) · Ensembl [ENSG00000205763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205763)

## Data

Gene col 13009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13009); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13009]; `tensor/DDL_lfc|DDL_z.npy` [13009]; `embed/gene_vectors.npy` [13009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13009 or target_col == 13009). Every well: [[RP9P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RP9P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
