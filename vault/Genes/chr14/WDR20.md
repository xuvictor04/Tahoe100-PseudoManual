---
symbol: "WDR20"
type: "gene"
col: 6375
ensembl_id: "ENSG00000140153"
name: "WD repeat domain 20"
location: "14q32.31"
module: 15
arm: "+"
pooled_cpm: 95.61
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# WDR20

*WD repeat domain 20* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.35× (z +12.5, q 5e-33, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.299× (z -17.7, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.831× (z -3.8, q 0.014, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1573 0.0992×, NCI-H23 0.129×, A-427 0.173×, HOP62 0.203×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW48 0.0688×, SK-MEL-2 0.124×, NCI-H1573 0.147×, SW 900 0.182×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.0350×, LOX-IMVI 0.169×, NCI-H2030 0.159×; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.119×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD8]] (+0.71, fdr 1e-05), [[GPBP1L1]] (+0.71, fdr 1e-05), [[URM1]] (+0.69, fdr 1e-05); moves opposite to [[RPAP3]] (-0.63, fdr 1e-05), [[MAP9]] (-0.60, fdr 1e-05), [[ALAS1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.35×** | +12.5 | 5e-33 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +9.1 | 2e-17 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.80×** | +8.6 | 2e-15 | 46/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.4 | 4e-15 | 42/49 (AsPC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.8 | 6e-13 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +6.0 | 2e-07 | 34/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.4 | 5e-06 | 37/48 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.008 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.008 | 27/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.017 | 24/50 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +3.3 | 0.049 | 26/48 (LoVo, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1573 0.0992×, NCI-H23 0.129×, A-427 0.173×, HOP62 0.203×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW48 0.0688×, SK-MEL-2 0.124×, NCI-H1573 0.147×, SW 900 0.182×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.0350×, LOX-IMVI 0.169×, NCI-H2030 0.159×; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.299×** | -17.7 | 0e+00 | 47/49 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.321×** | -16.0 | 0e+00 | 40/44 (SW48, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.364×** | -13.7 | 3e-40 | 41/45 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.736×** | -4.5 | 0.001 | 34/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.014 | 24/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.839× | -3.6 | 0.025 | 19/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -3.5 | 0.045 | 25/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.805× | -3.2 | 0.11 | 27/48 (HOP62, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 132 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -22.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 93.9 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -14.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 76.7 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 95.8 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -14.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 109 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.7 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -20.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 135 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -16.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 116 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -16.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 85.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 75.4 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 69.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 79.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -14.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 97.7 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 122 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 229 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -17.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -14.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 88.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -17.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 64.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 68.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.31× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 75.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 74.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 58.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -14.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 92.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -18.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 53.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 96.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 83.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -16.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 87.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0350× (z -25.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 132 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -12.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 80.9 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.210× (z -14.1) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 82.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -18.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0688× (z -19.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0961× (z -14.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 71.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.119× (z -8.8) |
| [[RKO (line)]] | wt | 93.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[GPBP1L1]] | +0.71 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[URM1]] | +0.69 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[GLUD1P3]] | +0.69 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[SLC12A9]] | +0.67 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[TRPC4AP]] | +0.67 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[NUDT2]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[LEMD3]] | +0.66 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TAF11]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[PRDM10]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP3]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[MAP9]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ALAS1]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[C12orf29]] | -0.60 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[BMS1]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SMARCA5]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.58 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[DDX1]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[WDR7]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 | same gene group |
| [[RTL6]] | -0.57 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[TBC1D19]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[G3BP1]] | -0.56 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WDR20's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.3, 23.2); signed map (3.6, 0.7). **Vector** length 92.0, 29.8% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | -0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.8 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.8 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:102,139,503-102,224,847 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DMR, MGC33177, FLJ33659, Bun107 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBZ3](https://www.uniprot.org/uniprotkb/Q8TBZ3) (WD repeat-containing protein 20):

> Regulator of deubiquitinating complexes. Activates deubiquitinating activity of complexes containing USP12. Anchors at the base of the ubiquitin-contacting loop of USP12 and remotely modulates the catalytic center of the enzyme. Regulates shuttling of the USP12 deubiquitinase complex between the plasma membrane, cytoplasm and nucleus.

**Summary**, from NCBI Gene [91833](https://www.ncbi.nlm.nih.gov/gene/91833):

> This gene encodes a WD repeat-containing protein that functions to preserve and regulate the activity of the USP12-UAF1 deubiquitinating enzyme complex. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:19667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19667) · Entrez [91833](https://www.ncbi.nlm.nih.gov/gene/91833) · UniProt [Q8TBZ3](https://www.uniprot.org/uniprotkb/Q8TBZ3) · Ensembl [ENSG00000140153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140153)

## Data

Gene col 6375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6375); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6375]; `tensor/DDL_lfc|DDL_z.npy` [6375]; `embed/gene_vectors.npy` [6375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6375 or target_col == 6375). Every well: [[WDR20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
