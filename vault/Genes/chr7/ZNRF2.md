---
symbol: "ZNRF2"
type: "gene"
col: 11091
ensembl_id: "ENSG00000180233"
name: "zinc and ring finger 2"
location: "7p14.3"
module: 145
arm: "+"
pooled_cpm: 71.09
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# ZNRF2

*zinc and ring finger 2* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +8.4, q 3e-14, up in 30 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.505× (z -14.6, q 1e-45, down in 30 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.595× (z -11.5, q 1e-28, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLPP1]] (+0.64, fdr 1e-05), [[ELF2]] (+0.62, fdr 1e-05), [[RSBN1L]] (+0.60, fdr 1e-05); moves opposite to [[GTF2H3]] (-0.59, fdr 1e-05), [[NRAS]] (-0.54, fdr 3e-05), [[MYSM1]] (-0.54, fdr 2e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DEPTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.4 | 3e-14 | 30/49 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.9 | 8e-07 | 26/48 (Hs 766T, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +5.1 | 6e-05 | 25/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 4e-04 | 22/48 (Hs 766T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 5e-04 | 22/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.004 | 18/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +4.1 | 0.004 | 16/50 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.010 | 22/48 (A-172, SNU-423, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.019 | 19/48 (A-172, A498, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.019 | 15/47 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.053 | 11/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.091 | 9/49 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -14.6 | 1e-45 | 30/40 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -12.0 | 4e-31 | 37/48 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.556×** | -12.0 | 4e-31 | 34/42 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -11.5 | 1e-28 | 38/48 (SW480, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -9.8 | 1e-20 | 39/48 (A498, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -8.5 | 3e-15 | 31/47 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 5 µM |  | **0.496×** | -8.0 | 8e-14 | 31/48 (A498, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.507×** | -7.8 | 6e-13 | 30/48 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.796×** | -6.4 | 9e-09 | 26/47 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.610×** | -5.6 | 1e-06 | 24/48 (HEC-1-A, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.712×** | -5.3 | 6e-06 | 26/49 (A498, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -5.2 | 1e-05 | 24/48 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.801×** | -4.9 | 4e-05 | 22/48 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.806×** | -4.6 | 2e-04 | 22/47 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.670×** | -4.6 | 2e-04 | 21/46 (A498, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.672×** | -4.5 | 2e-04 | 19/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.3 | 6e-04 | 20/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.868× | -3.9 | 0.003 | 7/48 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.799×** | -3.5 | 0.014 | 12/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Naproxen (drug)]] 5 µM |  | 0.850× | -3.4 | 0.016 | 14/48 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -3.2 | 0.038 | 13/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.864× | -3.1 | 0.049 | 12/47 (NCI-H1573, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.5 | 9 (7 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.80× (z +15.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.38× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 106 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[EX229 (drug)]] 5 µM 0.277× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 74.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.277× (z -8.8) |
| [[HT-29 (line)]] | alt | 166 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.259× (z -13.7) |
| [[SW1417 (line)]] | alt | 117 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.421× (z -12.2) |
| [[KATO III (line)]] | alt | 134 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 56.8 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -9.4) |
| [[SW480 (line)]] | alt | 74.3 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.385× (z -14.2) |
| [[A-427 (line)]] | wt | 70.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 71.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 86.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -12.3) |
| [[A-172 (line)]] | wt | 50.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 82.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -10.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0691× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -8.9) |
| [[H4 (line)]] | wt | 94.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -8.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 58.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 56.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 74.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -9.8) |
| [[RKO (line)]] | wt | 32.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -12.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -14.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 63.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 125 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.01× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 43.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -8.9) |
| [[HS-578T (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLPP1]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ELF2]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CDC42SE2]] | +0.59 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[BCL2L14]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[MAGI3]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PPM1B]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[RANBP9]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[RPS6KA5]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[LPCAT3]] | +0.53 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[PAN3]] | +0.53 | +0.47 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NRAS]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[HUS1]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NCDN]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SLC30A9]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ZSCAN20]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CHM]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 | same gene group |
| [[ZNF460]] | -0.49 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[DDX1]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TTPAL]] | -0.48 | -0.54 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEPTOR]] | B | DEPTOR activity raises ZNRF2's level | lines that do not express DEPTOR (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without DEPTOR | 0.061 | ⚠ within organs, on part of the lines; also absent: WWOX; maybe low, not absent |
| [[KIRREL1]] | B | KIRREL1 activity lowers ZNRF2's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.75× higher at baseline in the lines without KIRREL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[MNX1]] | B | MNX1 activity raises ZNRF2's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without MNX1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.2, -41.0); signed map (-18.4, 15.7). **Vector** length 118, 32.2% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +6.0 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.0 | +4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.5 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.0 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -12.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -8.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.1 | -7.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.5 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc and ring finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,284,597-30,367,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF202 |
| Gene groups (HGNC) | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHG8](https://www.uniprot.org/uniprotkb/Q8NHG8) (E3 ubiquitin-protein ligase ZNRF2):

> E3 ubiquitin-protein ligase that plays a role in the establishment and maintenance of neuronal transmission and plasticity. Ubiquitinates the Na(+)/K(+) ATPase alpha-1 subunit/ATP1A1 and thereby influences its endocytosis and/or degradation. Acts also as a positive regulator of mTORC1 activation by amino acids, which functions upstream of the V-ATPase and of Rag-GTPases. In turn, phosphorylation by mTOR leads to its inhibition via targeting to the cytosol allowing a self-regulating feedback …

**Summary**, from NCBI Gene [223082](https://www.ncbi.nlm.nih.gov/gene/223082):

> Enables ubiquitin protein ligase activity. Involved in positive regulation of autophagosome-lysosome fusion. Located in cytoplasmic vesicle membrane and plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22316) · Entrez [223082](https://www.ncbi.nlm.nih.gov/gene/223082) · UniProt [Q8NHG8](https://www.uniprot.org/uniprotkb/Q8NHG8) · Ensembl [ENSG00000180233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180233)

## Data

Gene col 11091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11091); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11091]; `tensor/DDL_lfc|DDL_z.npy` [11091]; `embed/gene_vectors.npy` [11091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11091 or target_col == 11091). Every well: [[ZNRF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNRF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
