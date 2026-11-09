---
symbol: "HERPUD2"
type: "gene"
col: 4351
ensembl_id: "ENSG00000122557"
name: "HERPUD family member 2"
location: "7p14.2"
module: 234
arm: "+"
pooled_cpm: 65.27
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/234"]
generated_by: "tahoemap"
---

# HERPUD2

*HERPUD family member 2* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +11.7, q 1e-28, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.468× (z -16.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C14orf28]] (+0.67, fdr 1e-05), [[SOS2]] (+0.67, fdr 7e-06), [[KIAA2026]] (+0.66, fdr 1e-05); moves opposite to [[MINDY4]] (-0.59, fdr 2e-05), [[BLMH]] (-0.57, fdr 2e-05), [[BMS1]] (-0.56, fdr 2e-05).
> It is in [[Module 234]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +11.7 | 1e-28 | 33/49 (SW1417, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.4 | 6e-23 | 33/48 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.0 | 3e-13 | 30/49 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +5.9 | 4e-07 | 25/47 (H4, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 5e-04 | 23/47 (hTERT-HPNE, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.035 | 13/49 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.077 | 15/50 (HEC-1-A, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.2 | 0.092 | 16/48 (KATO III, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.468×** | -16.6 | 0e+00 | 47/48 (HT-29, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.529×** | -13.9 | 2e-41 | 43/49 (LS 180, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.606×** | -10.5 | 1e-23 | 32/42 (A-427, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.601×** | -10.3 | 1e-22 | 32/43 (A-427, A-172, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.629×** | -10.1 | 5e-22 | 42/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -9.9 | 3e-21 | 42/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -9.5 | 2e-19 | 38/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -7.7 | 1e-12 | 33/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.706×** | -7.3 | 2e-11 | 33/48 (PANC-1, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.725×** | -7.0 | 1e-10 | 28/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -6.6 | 3e-09 | 31/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.566×** | -6.5 | 4e-09 | 33/48 (SHP-77, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.745×** | -6.4 | 6e-09 | 28/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.581×** | -6.2 | 2e-08 | 33/48 (LOX-IMVI, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.758×** | -6.0 | 6e-08 | 25/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -5.9 | 1e-07 | 26/48 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.596×** | -5.9 | 1e-07 | 30/48 (SW1417, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.608×** | -5.7 | 4e-07 | 30/48 (SW48, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -5.2 | 6e-06 | 26/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.745×** | -4.5 | 2e-04 | 22/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.759×** | -4.2 | 6e-04 | 23/49 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.817×** | -4.2 | 7e-04 | 21/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.763×** | -4.1 | 8e-04 | 22/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 98.8 | 1 | 7 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -15.0) |
| [[PANC-1 (line)]] | alt | 97.3 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.323× (z -14.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 86.5 | 3 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 64.4 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.366× (z -11.7) |
| [[A-427 (line)]] | wt | 63.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -21.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -8.9) |
| [[A498 (line)]] | wt | 70.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LoVo (line)]] | wt | 78.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -12.0) |
| [[SW480 (line)]] | alt | 29.9 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.389× (z -10.8) |
| [[A549 (line)]] | wt | 68.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HEC-1-A (line)]] | alt | 63.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -12.9) |
| [[HOP62 (line)]] | alt | 56.5 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.295× (z -13.7) |
| [[HS-578T (line)]] | alt | 63.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -11.2) |
| [[HT-29 (line)]] | alt | 86.4 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.209× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 97.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H1792 (line)]] | alt | 60.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.416× (z -9.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H2030 (line)]] | alt | 78.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 53.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.417× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 70.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[RKO (line)]] | wt | 41.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW 900 (line)]] | alt | 48.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.373× (z -8.9) |
| [[SW48 (line)]] | wt | 56.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.219× (z -9.9) |
| [[BT-474 (line)]] | alt | 62.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 48.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.165× (z -14.4) |
| [[C32 (line)]] | wt | 44.3 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 62.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.447× (z -9.1) |
| [[H4 (line)]] | wt | 106 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.281× (z -11.6) |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HepG2_C3A (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LS 180 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H661 (line)]] | alt | 68.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0827× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 79.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.251× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 87.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.276× (z -13.3) |
| [[SNU-423 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW 1088 (line)]] | alt | 159 | 0 | 1 | — | [[Eplerenone (drug)]] 0.05 µM 0.0973× (z -10.1) |
| [[SW 1271 (line)]] | alt | 85.7 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0970× (z -9.5) |
| [[SW1417 (line)]] | alt | 65.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C14orf28]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SOS2]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[KIAA2026]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[GPBP1L1]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[RSRP1]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CDK19]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[PCMTD1]] | +0.61 | +0.40 / +0.67 | both halves | 4e-05 |  |
| [[AAMDC]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LEMD3]] | +0.60 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[KLF3-AS1]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HECA]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[WDR20]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY4]] | -0.59 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[BLMH]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[BMS1]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NAA40]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[LMCD1-AS1]] | -0.55 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[RPAP3]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CLPB]] | -0.54 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ALKBH8]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DRG2]] | -0.53 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[NUDC]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MPHOSPH6]] | -0.51 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[SRPX2]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HERPUD2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 234]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.864). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.7, -42.0); signed map (4.7, 1.8). **Vector** length 107, 29.1% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.7 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +8.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.6 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -16.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.0 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -9.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -5.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | HERPUD family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:35,632,659-35,697,459 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22313 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSE4](https://www.uniprot.org/uniprotkb/Q9BSE4) (Homocysteine-responsive endoplasmic reticulum-resident ubiquitin-like domain member 2 protein):

> Could be involved in the unfolded protein response (UPR) pathway.

**Summary**, from NCBI Gene [64224](https://www.ncbi.nlm.nih.gov/gene/64224):

> Predicted to be involved in endoplasmic reticulum unfolded protein response. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21915) · Entrez [64224](https://www.ncbi.nlm.nih.gov/gene/64224) · UniProt [Q9BSE4](https://www.uniprot.org/uniprotkb/Q9BSE4) · Ensembl [ENSG00000122557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122557)

## Data

Gene col 4351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4351); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4351]; `tensor/DDL_lfc|DDL_z.npy` [4351]; `embed/gene_vectors.npy` [4351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4351 or target_col == 4351). Every well: [[HERPUD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERPUD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
