---
symbol: "NSL1"
type: "gene"
col: 3943
ensembl_id: "ENSG00000117697"
name: "NSL1 component of MIS12 kinetochore complex"
location: "1q32.3"
module: 17
arm: "+"
pooled_cpm: 32.71
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NSL1

*NSL1 component of MIS12 kinetochore complex* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.53× (z +9.2, q 3e-17, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.523× (z -13.9, q 4e-41, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FPGT]] (+0.63, fdr 7e-06), [[SASS6]] (+0.63, fdr 2e-05), [[MBIP]] (+0.61, fdr 1e-05); moves opposite to [[FSCN2]] (-0.58, fdr 9e-06), [[MAPKAPK2]] (-0.54, fdr 1e-05), [[C19orf38]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +9.2 | 3e-17 | 34/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +7.6 | 6e-12 | 31/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +6.6 | 7e-09 | 26/48 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 4e-08 | 28/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +6.0 | 2e-07 | 26/48 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +5.4 | 8e-06 | 22/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.28×** | +5.1 | 2e-05 | 22/45 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +4.7 | 2e-04 | 22/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.6 | 3e-04 | 16/48 (LoVo, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.004 | 17/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +3.9 | 0.005 | 16/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +3.9 | 0.005 | 19/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.007 | 13/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.6 | 0.011 | 11/48 (Hs 766T, COLO 205, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | 1.18× | +3.3 | 0.037 | 11/42 (NCI-H23, A549, …) | inconsistent across doses | composition shift |
| [[Regorafenib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.045 | 5/48 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.046 | 7/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.047 | 7/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.059 | 10/47 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.067 | 12/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.523×** | -13.9 | 4e-41 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -11.5 | 5e-28 | 39/47 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.367×** | -11.2 | 6e-27 | 36/48 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -9.9 | 6e-21 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -9.6 | 1e-19 | 35/48 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -9.5 | 3e-19 | 34/47 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -8.5 | 1e-15 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.772×** | -7.8 | 3e-13 | 27/47 (NCI-H460, Hs 766T, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -6.4 | 8e-09 | 26/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.568×** | -6.3 | 1e-08 | 24/47 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -6.3 | 2e-08 | 28/48 (HCT15, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -6.0 | 7e-08 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -5.2 | 1e-05 | 23/41 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.799×** | -4.8 | 6e-05 | 18/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.863× | -4.4 | 3e-04 | 14/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.814×** | -4.4 | 4e-04 | 15/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.778×** | -3.8 | 0.004 | 13/48 (H4, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.845× | -3.6 | 0.009 | 10/48 (hTERT-HPNE, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.858× | -3.3 | 0.027 | 12/48 (PANC-1, SW1417, …) | rises with dose |  |
| [[Naproxen (drug)]] 5 µM |  | 0.863× | -3.0 | 0.060 | 7/47 (NCI-H2347, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.4 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -19.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -16.8) |
| [[PANC-1 (line)]] | alt | 33.6 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -17.2) |
| [[SW480 (line)]] | alt | 43.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -16.5) |
| [[H4 (line)]] | wt | 35.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -8.8) |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -10.2) |
| [[HOP62 (line)]] | alt | 43.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -11.3) |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -12.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.140× (z -9.0) |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0605× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 37.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.163× (z -8.8) |
| [[C-33 A (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.205× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 23.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -8.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FPGT]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SASS6]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[MBIP]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NUP37]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[TRAPPC11]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.58 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PEX2]] | +0.58 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PHC3]] | +0.57 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.56 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TTC8]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HPF1]] | +0.56 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSCN2]] | -0.58 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[MAPKAPK2]] | -0.54 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[C19orf38]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.53 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SLC8A2]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[AXDND1]] | -0.53 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[LINC02133]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CSPG5]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SGSM3-AS1]] | -0.52 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[SPTBN5]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RAB7A]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZDHHC11]] | -0.50 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-42.7, -57.4); signed map (-43.0, -34.0). **Vector** length 74.2, 14.7% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +9.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -0.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +6.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.1 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | -3.7 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | NSL1 component of MIS12 kinetochore complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,726,153-212,791,782 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DC8, DKFZP566O1646, MIS14; previously C1orf48 |
| Gene groups (HGNC) | MIS12 kinetochore complex |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IY1](https://www.uniprot.org/uniprotkb/Q96IY1) (Kinetochore-associated protein NSL1 homolog):

> Part of the MIS12 complex which is required for normal chromosome alignment and segregation and kinetochore formation during mitosis.

**Summary**, from NCBI Gene [25936](https://www.ncbi.nlm.nih.gov/gene/25936):

> This gene encodes a protein with two coiled-coil domains that localizes to kinetochores, which are chromosome-associated structures that attach to microtubules and mediate chromosome movements during cell division. The encoded protein is part of a conserved protein complex that includes two chromodomain-containing proteins and a component of the outer plate of the kinetochore. This protein complex is proposed to bridge centromeric heterochromatin with the outer kinetochore structure. Multiple …

**Accessions** — [HGNC:24548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24548) · Entrez [25936](https://www.ncbi.nlm.nih.gov/gene/25936) · UniProt [Q96IY1](https://www.uniprot.org/uniprotkb/Q96IY1) · Ensembl [ENSG00000117697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117697)

## Data

Gene col 3943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3943); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3943]; `tensor/DDL_lfc|DDL_z.npy` [3943]; `embed/gene_vectors.npy` [3943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3943 or target_col == 3943). Every well: [[NSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
