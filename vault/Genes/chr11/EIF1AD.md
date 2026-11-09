---
symbol: "EIF1AD"
type: "gene"
col: 10603
ensembl_id: "ENSG00000175376"
name: "eukaryotic translation initiation factor 1A domain containing"
location: "11q13.1"
module: 52
arm: "+"
pooled_cpm: 16.44
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# EIF1AD

*eukaryotic translation initiation factor 1A domain containing* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.11× (z +18.3, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.524× (z -10.4, q 1e-22, down in 28 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HOP62 0.0659×, J82 0.127×, PANC-1 0.173×, C32 0.147×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (Panc 03.27 0.0785×, A-172 0.111×, NCI-H1573 0.156×, SW1417 0.284×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.112×, HEC-1-A 0.269×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (RPMI-7951 0.178×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.223×); [[Brimonidine (drug)]] 0.5 µM in 1 line (SW48 0.0858×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIC8A]] (+0.72, fdr 7e-06), [[PHRF1]] (+0.70, fdr 7e-06), [[ZNF384]] (+0.68, fdr 7e-06); moves opposite to [[CYB5D2]] (-0.60, fdr 1e-05), [[MYEF2]] (-0.58, fdr 4e-05), [[POGLUT1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +18.3 | 0e+00 | 43/47 (SW480, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.66×** | +14.6 | 1e-45 | 44/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.44×** | +14.4 | 2e-44 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.10×** | +11.9 | 1e-30 | 43/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.03×** | +11.4 | 4e-28 | 43/47 (SW480, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.64×** | +10.9 | 1e-25 | 35/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +7.3 | 3e-11 | 30/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +7.0 | 2e-10 | 27/46 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.9 | 4e-10 | 29/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.7 | 9e-10 | 24/41 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.6 | 3e-09 | 33/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.49×** | +6.4 | 7e-09 | 26/46 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +6.1 | 5e-08 | 25/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 2e-07 | 25/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.2 | 6e-06 | 23/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.030 | 8/48 (SW1417, Hs 766T, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.038 | 14/46 (Panc 03.27, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10603.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HOP62 0.0659×, J82 0.127×, PANC-1 0.173×, C32 0.147×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (Panc 03.27 0.0785×, A-172 0.111×, NCI-H1573 0.156×, SW1417 0.284×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.112×, HEC-1-A 0.269×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (RPMI-7951 0.178×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.223×); [[Brimonidine (drug)]] 0.5 µM in 1 line (SW48 0.0858×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.524×** | -10.4 | 1e-22 | 28/39 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -9.7 | 7e-20 | 23/29 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.771×** | -3.7 | 0.038 | 15/47 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.792×** | -3.5 | 0.066 | 13/33 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.11 | 6/48 (HEC-1-A, C32, …) | all doses, flat | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.818× | -3.2 | 0.11 | 7/48 (A-172, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.14 | 12/48 (SW48, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.4 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.22× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 20.4 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.37× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 17.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.17× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 10.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.90× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0659× (z -17.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.223× (z -9.5) |
| [[J82 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0785× (z -16.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Thymol (drug)]] 0.5 µM 0.178× (z -9.8) |
| [[SW1417 (line)]] | alt | 24.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.31× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -13.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.39× (z +9.0) | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 19.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.63× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.123× (z -8.5) |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 13.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.20× (z +9.7) | — |
| [[LoVo (line)]] | wt | 11.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 8.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 11.3 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0858× (z -8.8) |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIC8A]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[PHRF1]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ZNF384]] | +0.68 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[MGAT1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MTF1]] | +0.65 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ESS2]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ATG101]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SDHAF1]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ZNF526]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CTDP1]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MYEF2]] | -0.58 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[POGLUT1]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TIA1]] | -0.55 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[KLHL5]] | -0.55 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[ITGAV]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[VPS13C]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[GALNT7]] | -0.53 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[SPPL2A]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[AGL]] | -0.53 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[HACD2]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ATRX]] | -0.53 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-30.7, -10.9); signed map (-41.8, 4.8). **Vector** length 85.5, 17.9% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +18.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.3 | +11.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.8 | +11.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +5.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.2 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.3 | -10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.6 | -9.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 1A domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,996,545-66,002,176 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11102, haponin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9N8](https://www.uniprot.org/uniprotkb/Q8N9N8) (Probable RNA-binding protein EIF1AD):

> Plays a role into cellular response to oxidative stress. Decreases cell proliferation.

**Summary**, from NCBI Gene [84285](https://www.ncbi.nlm.nih.gov/gene/84285):

> Predicted to enable RNA binding activity and translation initiation factor activity. Predicted to be involved in translational initiation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28147) · Entrez [84285](https://www.ncbi.nlm.nih.gov/gene/84285) · UniProt [Q8N9N8](https://www.uniprot.org/uniprotkb/Q8N9N8) · Ensembl [ENSG00000175376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175376)

## Data

Gene col 10603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10603); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10603]; `tensor/DDL_lfc|DDL_z.npy` [10603]; `embed/gene_vectors.npy` [10603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10603 or target_col == 10603). Every well: [[EIF1AD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF1AD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
