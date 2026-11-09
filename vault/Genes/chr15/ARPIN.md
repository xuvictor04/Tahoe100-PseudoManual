---
symbol: "ARPIN"
type: "gene"
col: 14319
ensembl_id: "ENSG00000242498"
name: "actin related protein 2/3 complex inhibitor"
location: "15q26.1"
module: 96
arm: "+"
pooled_cpm: 9.5
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 1
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# ARPIN

*actin related protein 2/3 complex inhibitor* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.06× (z +19.2, q 0e+00, up in 28 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.29× (z +3.5, q 0.062, up in 10 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 4.74×, NCI-H1792 9.79×, NCI-H2347 4.48×, HOP62 4.64×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 4.27×, NCI-H1792 7.63×, SW480 4.62×, A-172 4.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 4.27×, A-172 5.45×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.309× (z -22.6, q 0e+00, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROS]] (+0.70, fdr 1e-05), [[TKFC]] (+0.64, fdr 1e-05), [[ALDH5A1]] (+0.59, fdr 2e-05); moves opposite to [[CIAO2B]] (-0.56, fdr 3e-05), [[RPL36AL]] (-0.56, fdr 2e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[SEC61G]] (-0.56, fdr 5e-05), [[C16orf91]] (-0.56, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14319.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 4.74×, NCI-H1792 9.79×, NCI-H2347 4.48×, HOP62 4.64×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 4.27×, NCI-H1792 7.63×, SW480 4.62×, A-172 4.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 4.27×, A-172 5.45×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.06×** | +19.2 | 0e+00 | 28/29 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +17.6 | 0e+00 | 20/22 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +12.3 | 1e-32 | 22/25 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.3 | 2e-05 | 13/37 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.062 | 10/44 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.27× | +3.2 | 0.14 | 3/45 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.14 | 5/44 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.14 | 5/46 (SW480, LS 180, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.14 | 6/36 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.309×** | -22.6 | 0e+00 | 34/43 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.349×** | -14.4 | 3e-44 | 35/45 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.372×** | -13.5 | 5e-39 | 37/45 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.375×** | -13.4 | 1e-38 | 34/45 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.410×** | -12.2 | 5e-32 | 30/39 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.412×** | -12.1 | 9e-32 | 31/45 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -11.3 | 1e-27 | 29/43 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -9.0 | 2e-17 | 30/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.520×** | -8.9 | 3e-17 | 27/45 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -8.9 | 3e-17 | 28/40 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.529×** | -8.7 | 2e-16 | 29/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.537×** | -8.5 | 1e-15 | 27/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.532×** | -8.1 | 2e-14 | 25/43 (Panc 03.27, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.565×** | -7.8 | 3e-13 | 25/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.598×** | -6.7 | 6e-10 | 23/43 (J82, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.645×** | -5.8 | 2e-07 | 21/46 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.77 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.62× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.133× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 23.8 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.3) |
| [[A549 (line)]] | wt | 18.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.9) |
| [[A-172 (line)]] | wt | 11.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.45× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.116× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.4) |
| [[HT-29 (line)]] | alt | 9.29 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.103× (z -11.3) |
| [[LoVo (line)]] | wt | 14.2 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0814× (z -18.1) |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.6) |
| [[PANC-1 (line)]] | alt | 6.35 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.108× (z -12.3) |
| [[J82 (line)]] | alt | 16.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -17.3) |
| [[KATO III (line)]] | alt | 17.8 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0907× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.171× (z -11.8) |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.2) |
| [[HOP62 (line)]] | alt | 10.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 8.85 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 12.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.79× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 6.08 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0652× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 3.12 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.0) |
| [[RKO (line)]] | wt | 8.17 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -8.8) |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0652× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 5.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.1) |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0895× (z -9.6) |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.108× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 9.10 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 6.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -13.5) |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -8.7) |
| [[A-427 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROS]] | +0.70 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TKFC]] | +0.64 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[WDR31]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SCCPDH]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SIRT5]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[IDUA]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SPATA20]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[COX11]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PIGK]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[PTPN18]] | +0.57 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[SMG7]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.56 | -0.47 / -0.54 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SEC61G]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[C16orf91]] | -0.56 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TRAPPC2B]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NOSIP]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RNF181]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[FAM32A]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[GPR89B]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[MTF1]] | -0.52 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[GRIN2D]] | -0.52 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[QPCTL]] | -0.52 | -0.34 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSZ]] | B | CTSZ activity raises ARPIN's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without CTSZ | 0.034 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-28.2, 23.5); signed map (16.2, -42.7). **Vector** length 70.8, 13.3% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +19.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +12.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -13.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -14.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -7.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,895,006-89,912,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC61550; previously C15orf38 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6K5](https://www.uniprot.org/uniprotkb/Q7Z6K5) (Arpin):

> Regulates actin polymerization by inhibiting the actin-nucleating activity of the Arp2/3 complex; the function is competitive with nucleation promoting factors. Participates in an incoherent feedforward loop at the lamellipodium tip where it inhibits the Arp2/3 complex in response to Rac signaling and where Rac also stimulates actin polymerization through the WAVE complex. Involved in steering cell migration by controlling its directional persistence.

**Summary**, from NCBI Gene [348110](https://www.ncbi.nlm.nih.gov/gene/348110):

> Involved in directional locomotion; negative regulation of cell migration; and negative regulation of cellular component organization. Predicted to be located in lamellipodium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28782) · Entrez [348110](https://www.ncbi.nlm.nih.gov/gene/348110) · UniProt [Q7Z6K5](https://www.uniprot.org/uniprotkb/Q7Z6K5) · Ensembl [ENSG00000242498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242498)

## Data

Gene col 14319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14319); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14319]; `tensor/DDL_lfc|DDL_z.npy` [14319]; `embed/gene_vectors.npy` [14319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14319 or target_col == 14319). Every well: [[ARPIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
