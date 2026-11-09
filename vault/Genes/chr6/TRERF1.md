---
symbol: "TRERF1"
type: "gene"
col: 4534
ensembl_id: "ENSG00000124496"
name: "transcriptional regulating factor 1"
location: "6p21.1"
module: 45
arm: "+"
pooled_cpm: 89.31
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 57
n_dd_up_clean: 21
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TRERF1

*transcriptional regulating factor 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.58× (z +8.3, q 5e-14, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.258× (z -34.9, q 0e+00, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM22]] (+0.64, fdr 8e-06), [[DBP]] (+0.60, fdr 1e-05), [[TMEM14A]] (+0.59, fdr 1e-05); moves opposite to [[ZNF778]] (-0.59, fdr 3e-05), [[MROH1]] (-0.52, fdr 4e-05), [[CC2D1B]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +8.3 | 5e-14 | 37/42 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +7.5 | 2e-11 | 31/42 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.7 | 4e-09 | 26/42 (KATO III, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 7e-09 | 31/43 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 9e-09 | 31/42 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.75×** | +5.3 | 9e-06 | 27/42 (NCI-H1792, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.23×** | +5.3 | 9e-06 | 19/42 (HOP62, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Bentamapimod (drug)]] 5 µM |  | **1.67×** | +4.9 | 6e-05 | 25/42 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.32×** | +4.8 | 1e-04 | 27/41 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 26/42 (NCI-H1792, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 2e-04 | 25/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 3e-04 | 23/42 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +4.3 | 8e-04 | 19/42 (SW 900, KATO III, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.3 | 8e-04 | 21/42 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.001 | 18/42 (J82, HOP62, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 19/42 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Regorafenib (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.003 | 20/42 (AsPC-1, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.258×** | -34.9 | 0e+00 | 34/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.305×** | -21.6 | 0e+00 | 38/42 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.358×** | -18.7 | 0e+00 | 32/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -17.5 | 0e+00 | 36/42 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.392×** | -16.4 | 0e+00 | 32/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.434×** | -15.2 | 0e+00 | 35/43 (C-33 A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -14.1 | 2e-43 | 36/43 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.481×** | -13.3 | 2e-38 | 40/42 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -12.9 | 4e-36 | 37/42 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.495×** | -12.8 | 1e-35 | 37/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.476×** | -12.8 | 2e-35 | 39/42 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.471×** | -12.7 | 5e-35 | 34/40 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -12.4 | 8e-34 | 37/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.529×** | -11.6 | 2e-29 | 34/42 (SW480, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -10.8 | 2e-25 | 29/41 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.553×** | -10.8 | 2e-25 | 37/42 (AN3 CA, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -10.3 | 1e-23 | 29/42 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.671×** | -10.3 | 3e-23 | 40/43 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.576×** | -10.0 | 3e-22 | 34/42 (SW480, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.6 | 0 | 24 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -41.2) |
| [[PANC-1 (line)]] | alt | 215 | 0 | 22 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0806× (z -56.3) |
| [[HT-29 (line)]] | alt | 87.3 | 0 | 21 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -19.1) |
| [[SNU-1 (line)]] | wt | 442 | 0 | 20 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0370× (z -36.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.163× (z -29.2) |
| [[MIA PaCa-2 (line)]] | alt | 217 | 0 | 17 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0966× (z -22.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 192 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -18.8) |
| [[SW480 (line)]] | alt | 124 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -38.8) |
| [[NCI-H23 (line)]] | alt | 93.3 | 0 | 16 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0247× (z -28.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.9) |
| [[Hs 766T (line)]] | wt | 177 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -18.7) |
| [[COLO 205 (line)]] | alt | 531 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -27.0) |
| [[LS 180 (line)]] | wt | 80.9 | 0 | 11 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -17.6) |
| [[A-427 (line)]] | wt | 63.9 | 0 | 10 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -16.5) |
| [[RKO (line)]] | wt | 62.1 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0742× (z -17.9) |
| [[SW48 (line)]] | wt | 147 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -22.0) |
| [[H4 (line)]] | wt | 93.7 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.1) |
| [[HCT15 (line)]] | alt | 98.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.1) |
| [[SW1417 (line)]] | alt | 49.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.5) |
| [[AN3 CA (line)]] | alt | 235 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0383× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0539× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -36.5) |
| [[RPMI-7951 (line)]] | alt | 77.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0713× (z -29.0) |
| [[AsPC-1 (line)]] | alt | 59.2 | 2 | 5 (1 ⚠) | [[Radotinib (drug)]] 5 µM 2.46× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.133× (z -16.2) |
| [[C-33 A (line)]] | alt | 89.2 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0540× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -13.9) |
| [[J82 (line)]] | alt | 68.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -20.0) |
| [[SNU-423 (line)]] | alt | 79.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.3) |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.5) |
| [[A498 (line)]] | wt | 28.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -17.9) |
| [[hTERT-HPNE (line)]] | wt | 87.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.5) |
| [[KATO III (line)]] | alt | 38.1 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.66× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.1) |
| [[HOP62 (line)]] | alt | 53.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 57.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 74.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -12.4) |
| [[SHP-77 (line)]] | alt | 68.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.9) |
| [[HS-578T (line)]] | alt | 75.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.2) |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.7) |
| [[A-172 (line)]] | wt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.7) |
| [[CHP-212 (line)]] | wt | 112 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.218× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +12.6) | — |
| [[NCI-H596 (line)]] | alt | 87.5 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.155× (z -9.0) |
| [[SW 1088 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0638× (z -9.3) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.45 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM22]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[DBP]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TMEM14A]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[LRIG3]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MAP3K4]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ATP6V0E2]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[PIK3C2B]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PPM1H]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[CXXC5]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[THRA]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ALDH3A2]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF778]] | -0.59 | -0.49 / -0.44 | both halves | 3e-05 | same gene group |
| [[MROH1]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CC2D1B]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[CHFR]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[MUC20-OT1]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TPD52L2]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[DESI1]] | -0.48 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[HGS]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TMED5]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[LINC02804]] | -0.46 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[SPON1-AS1]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[FAM120B]] | -0.45 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers TRERF1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.5% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ONECUT2]] | B | ONECUT2 activity lowers TRERF1's level | lines that do not express ONECUT2 (10) vs lines expressing it (40) | 1.88× higher at baseline in the lines without ONECUT2 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PCDH18]] | B | PCDH18 activity raises TRERF1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.32× lower at baseline in the lines without PCDH18 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AR]] | B | TRERF1 activity raises AR's level | lines that do not express TRERF1 (6) vs lines expressing it (44) | 3.14× lower at baseline in the lines without TRERF1 | 0.079 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (20.3, -6.4); signed map (-5.6, 15.0). **Vector** length 105, 34.0% of its response variance represented; |z| ≥ 3 in 1,933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.5 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.6 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +2.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +4.0 | +4.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -6.2 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.5 | -10.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.7 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -7.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.0 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional regulating factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,224,931-42,452,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TReP-132, HSA277276, RAPA, dJ139D8.5; previously BCAR2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Myb/SANT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PN7](https://www.uniprot.org/uniprotkb/Q96PN7) (Transcriptional-regulating factor 1):

> Binds DNA and activates transcription of CYP11A1. Interaction with CREBBP and EP300 results in a synergistic transcriptional activation of CYP11A1.

**Summary**, from NCBI Gene [55809](https://www.ncbi.nlm.nih.gov/gene/55809):

> This gene encodes a zinc-finger transcriptional regulating protein which interacts with CBP/p300 to regulate the human gene CYP11A1. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:18273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18273) · Entrez [55809](https://www.ncbi.nlm.nih.gov/gene/55809) · UniProt [Q96PN7](https://www.uniprot.org/uniprotkb/Q96PN7) · Ensembl [ENSG00000124496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124496)

## Data

Gene col 4534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4534); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4534]; `tensor/DDL_lfc|DDL_z.npy` [4534]; `embed/gene_vectors.npy` [4534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4534 or target_col == 4534). Every well: [[TRERF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRERF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
