---
symbol: "ABHD17B"
type: "gene"
col: 2847
ensembl_id: "ENSG00000107362"
name: "abhydrolase domain containing 17B, depalmitoylase"
location: "9q21.13"
module: 93
arm: "+"
pooled_cpm: 43.02
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# ABHD17B

*abhydrolase domain containing 17B, depalmitoylase* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.85× (z +16.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.302× (z -18.2, q 0e+00, down in 31 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.704× (z -5.3, q 1e-05, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (KATO III 0.0559×, SW480 0.178×, SW 900 0.0631×, AsPC-1 0.0760×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.0356×, J82 0.177×, NCI-H460 0.267×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.152×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 5 µM in 1 line (C32 0.282×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.264×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED26]] (+0.70, fdr 7e-06), [[DEDD2]] (+0.62, fdr 1e-05), [[GTF2B]] (+0.59, fdr 1e-05); moves opposite to [[NHLRC2]] (-0.63, fdr 1e-05), [[ZC3H7B]] (-0.59, fdr 1e-05), [[COA7]] (-0.58, fdr 2e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +16.5 | 0e+00 | 46/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +16.2 | 0e+00 | 47/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.42×** | +14.0 | 6e-42 | 44/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +13.1 | 5e-37 | 39/48 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.25×** | +12.1 | 1e-31 | 46/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +11.8 | 4e-30 | 37/48 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +11.7 | 8e-30 | 37/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.48×** | +10.3 | 5e-23 | 41/49 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +9.7 | 2e-20 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.23×** | +8.9 | 3e-17 | 44/48 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.8 | 9e-17 | 34/49 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +8.6 | 2e-16 | 35/48 (LoVo, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +7.2 | 2e-11 | 35/47 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.87×** | +7.1 | 6e-11 | 39/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +6.5 | 2e-09 | 35/43 (SNU-423, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +6.1 | 4e-08 | 31/48 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2847.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (KATO III 0.0559×, SW480 0.178×, SW 900 0.0631×, AsPC-1 0.0760×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.0356×, J82 0.177×, NCI-H460 0.267×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.152×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 5 µM in 1 line (C32 0.282×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.264×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.302×** | -18.2 | 0e+00 | 31/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.397×** | -14.6 | 1e-45 | 42/47 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -8.1 | 1e-13 | 31/43 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.704×** | -5.3 | 1e-05 | 29/48 (C32, SNU-423, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.825× | -3.1 | 0.25 | 16/47 (hTERT-HPNE, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.9 | 9 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -20.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 75.8 | 6 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.7 | 5 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 51.6 | 5 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.22× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -13.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.8 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 65.1 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.0559× (z -28.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 59.9 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.1 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.34× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 45.2 | 4 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 38.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.63× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 75.6 | 2 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 3.12× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -15.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 46.1 | 4 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.74× (z +10.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -9.1) |
| [[C32 (line)]] | wt | 70.9 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 13.0× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.282× (z -9.9) |
| [[HOP62 (line)]] | alt | 32.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 77.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 24.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 38.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -13.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 29.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0760× (z -16.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 36.9 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.99× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 41.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.6 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 70.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.85× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -16.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 44.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0631× (z -19.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0356× (z -20.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +9.1) | — |
| [[SW48 (line)]] | wt | 31.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[DEDD2]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LGMN]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[POR]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[TPI1]] | +0.56 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[BMT2]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CNOT8]] | +0.56 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[NDUFAF7]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[NFATC3]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TMEM41A]] | +0.55 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[MACO1]] | +0.55 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[COA7]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PIGL]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[EFR3A]] | -0.54 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MDC1]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TEX261]] | -0.54 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MDM4]] | -0.52 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[MGA]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LIG4]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[CHTOP]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABHD17B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.8, -6.5); signed map (-23.7, 11.6). **Vector** length 87.2, 24.6% of its response variance represented; |z| ≥ 3 in 1,249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +6.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +8.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -18.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 17B, depalmitoylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:71,862,452-71,911,193 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-67; previously C9orf77, FAM108B1 |
| Gene groups (HGNC) | Abhydrolase domain containing; Depalmitoylases; Thioester hydrolases |
| Reactome | 4 pathways, smallest: RAS processing; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VST6](https://www.uniprot.org/uniprotkb/Q5VST6) (Alpha/beta hydrolase domain-containing protein 17B):

> Hydrolyzes fatty acids from S-acylated cysteine residues in proteins. Has depalmitoylating activity towards DLG4/PSD95. Has depalmitoylating activity towards GAP43 (By similarity). Has depalmitoylating activity towards MAP6 (By similarity). Has depalmitoylating activity towards NRAS.

**Summary**, from NCBI Gene [51104](https://www.ncbi.nlm.nih.gov/gene/51104):

> Enables palmitoyl-(protein) hydrolase activity. Involved in protein depalmitoylation. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24278) · Entrez [51104](https://www.ncbi.nlm.nih.gov/gene/51104) · UniProt [Q5VST6](https://www.uniprot.org/uniprotkb/Q5VST6) · Ensembl [ENSG00000107362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107362)

## Data

Gene col 2847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2847); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2847]; `tensor/DDL_lfc|DDL_z.npy` [2847]; `embed/gene_vectors.npy` [2847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2847 or target_col == 2847). Every well: [[ABHD17B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD17B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
