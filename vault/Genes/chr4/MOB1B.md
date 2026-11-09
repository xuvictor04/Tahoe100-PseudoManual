---
symbol: "MOB1B"
type: "gene"
col: 10400
ensembl_id: "ENSG00000173542"
name: "MOB kinase activator 1B"
location: "4q13.3"
module: 18
arm: "+"
pooled_cpm: 71.05
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MOB1B

*MOB kinase activator 1B* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +8.9, q 4e-16, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.655× (z -9.4, q 3e-18, down in 32 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.855× (z -3.9, q 0.013, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.127×, A-427 0.242×, NCI-H460 0.357×, Panc 03.27 0.365×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.259×, SHP-77 0.235×, SW1417 0.274×, Panc 03.27 0.347×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (AN3 CA 0.0651×, SW48 0.266×, Panc 03.27 0.381×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0906×); [[Auranofin (drug)]] 5 µM in 1 line (AN3 CA 0.318×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHRS7]] (+0.63, fdr 1e-05), [[PTPN9]] (+0.60, fdr 1e-05), [[CMTM4]] (+0.60, fdr 1e-05); moves opposite to [[THRAP3]] (-0.56, fdr 4e-05), [[KAT5]] (-0.45, fdr 1e-04), [[RNF40]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +8.9 | 4e-16 | 41/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.5 | 4e-15 | 39/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +8.3 | 3e-14 | 31/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.7 | 4e-09 | 37/47 (RPMI-7951, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +6.5 | 9e-09 | 33/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.4 | 1e-08 | 33/47 (RPMI-7951, HT-29, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 3e-08 | 32/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +5.9 | 2e-07 | 24/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.6 | 1e-06 | 25/47 (SW480, SW1417, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.25×** | +5.0 | 3e-05 | 26/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.9 | 4e-05 | 24/44 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +4.7 | 1e-04 | 22/47 (A498, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.4 | 6e-04 | 17/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.002 | 22/47 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.20×** | +4.1 | 0.002 | 22/47 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.20× | +4.0 | 0.002 | 19/47 (SW1417, C-33 A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.004 | 20/47 (SNU-423, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10400.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.127×, A-427 0.242×, NCI-H460 0.357×, Panc 03.27 0.365×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.259×, SHP-77 0.235×, SW1417 0.274×, Panc 03.27 0.347×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (AN3 CA 0.0651×, SW48 0.266×, Panc 03.27 0.381×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0906×); [[Auranofin (drug)]] 5 µM in 1 line (AN3 CA 0.318×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.655×** | -9.4 | 3e-18 | 32/48 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.708×** | -7.4 | 4e-11 | 25/43 (AN3 CA, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -7.0 | 5e-10 | 27/44 (A-427, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.855× | -3.9 | 0.013 | 16/47 (HOP62, NCI-H2347, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.026 | 20/46 (SW48, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.026 | 16/47 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.847× | -3.5 | 0.041 | 14/47 (CHP-212, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.3 | 0.069 | 14/49 (NCI-H1573, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.2 | 0.074 | 20/47 (C32, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.886× | -3.1 | 0.11 | 15/48 (NCI-H2347, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 62.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.442× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 64.3 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.9) | — |
| [[A-427 (line)]] | wt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 77.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 69.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0651× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.318× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 68.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.3) ⚠ cell-cycle shift, explains ~10% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -12.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 67.4 | 2 | 0 | [[Selinexor (drug)]] 5 µM 1.58× (z +9.9) | — |
| [[RKO (line)]] | wt | 59.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 43.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -12.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.477× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.9) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HCT15 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 94.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.513× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 99.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 94.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -20.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 77.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0906× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 69.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 83.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -15.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 98.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS7]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PTPN9]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CMTM4]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[CBFB]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[FAM89A]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[NDUFB2]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[CRYL1]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RBPMS2]] | +0.52 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[MEMO1]] | +0.52 | +0.62 / +0.31 | both halves | 2e-04 |  |
| [[PAQR3]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CRTC3]] | +0.51 | +0.54 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRAP3]] | -0.56 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[KAT5]] | -0.45 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[RNF40]] | -0.43 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[EXOC3]] | -0.42 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[CYP2E1]] | -0.42 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[MYOF]] | -0.41 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[NELFE]] | -0.41 | -0.50 / -0.24 | both halves | 4e-04 |  |
| [[ZNF548]] | -0.41 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[POLR2E]] | -0.41 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[SF3A2]] | -0.41 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[C1QTNF3]] | -0.40 | -0.32 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers MOB1B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PALS2]] | C | PALS2 activity raises MOB1B's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.43× lower at baseline in the lines without PALS2 | 0.002 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.5, 18.2); signed map (-19.8, 47.2). **Vector** length 93.5, 22.5% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.5 | +8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.4 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.3 | +5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.7 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +3.4 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +3.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MOB kinase activator 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:70,902,326-71,022,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOB4A; previously MOBKL1A |
| Gene groups (HGNC) | MOB kinase activators |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L9L4](https://www.uniprot.org/uniprotkb/Q7L9L4) (MOB kinase activator 1B):

> Activator of LATS1/2 in the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Phosphorylation of YAP1 by …

**Summary**, from NCBI Gene [92597](https://www.ncbi.nlm.nih.gov/gene/92597):

> The protein encoded by this gene is similar to the yeast Mob1 protein. Yeast Mob1 binds Mps1p, a protein kinase essential for spindle pole body duplication and mitotic checkpoint regulation. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:29801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29801) · Entrez [92597](https://www.ncbi.nlm.nih.gov/gene/92597) · UniProt [Q7L9L4](https://www.uniprot.org/uniprotkb/Q7L9L4) · Ensembl [ENSG00000173542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173542)

## Data

Gene col 10400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10400); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10400]; `tensor/DDL_lfc|DDL_z.npy` [10400]; `embed/gene_vectors.npy` [10400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10400 or target_col == 10400). Every well: [[MOB1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
