---
symbol: "ADCY7"
type: "gene"
col: 4263
ensembl_id: "ENSG00000121281"
name: "adenylate cyclase 7"
location: "16q12.1"
module: 117
arm: "+"
pooled_cpm: 28.57
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 23
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# ADCY7

*adenylate cyclase 7* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.89× (z +11.3, q 4e-27, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.331× (z -28.0, q 0e+00, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICALL1]] (+0.64, fdr 9e-06), [[CPNE2]] (+0.63, fdr 7e-06), [[MPP3]] (+0.62, fdr 7e-06); moves opposite to [[ZNF608]] (-0.61, fdr 7e-06), [[DOP1A]] (-0.60, fdr 1e-05), [[TMEM14C]] (-0.59, fdr 1e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[GRB10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +11.3 | 4e-27 | 35/44 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.34×** | +7.4 | 5e-11 | 28/44 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.41×** | +6.2 | 1e-07 | 24/43 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +5.7 | 2e-06 | 20/44 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.5 | 4e-06 | 23/44 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +5.4 | 5e-06 | 20/44 (NCI-H460, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.2 | 2e-05 | 18/44 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.66×** | +4.7 | 2e-04 | 20/43 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.4 | 6e-04 | 20/43 (LoVo, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.60×** | +4.4 | 6e-04 | 12/40 (BT-474, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +4.3 | 9e-04 | 15/43 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.9 | 0.005 | 15/43 (HT-29, SW 900, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.7 | 0.009 | 8/30 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.015 | 11/41 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.5 | 0.017 | 11/40 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.024 | 11/44 (KATO III, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.033 | 12/43 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.331×** | -28.0 | 0e+00 | 40/43 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -18.1 | 0e+00 | 40/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.392×** | -16.8 | 0e+00 | 38/44 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.399×** | -16.4 | 0e+00 | 37/44 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -16.0 | 0e+00 | 39/43 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.413×** | -15.8 | 0e+00 | 33/43 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -14.1 | 3e-43 | 35/43 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.455×** | -14.1 | 3e-43 | 36/44 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -12.4 | 3e-33 | 35/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.510×** | -12.0 | 1e-31 | 39/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.298×** | -11.3 | 5e-28 | 36/44 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.628×** | -8.3 | 4e-15 | 28/41 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.632×** | -8.1 | 2e-14 | 27/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -7.9 | 2e-13 | 27/42 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -7.6 | 9e-13 | 29/44 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.507×** | -6.3 | 8e-09 | 24/44 (RKO, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 63.7 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -19.4) |
| [[MIA PaCa-2 (line)]] | alt | 60.1 | 2 (1 ⚠) | 11 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.03× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -28.3) |
| [[RKO (line)]] | wt | 125 | 1 | 12 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.62× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -25.4) |
| [[A-172 (line)]] | wt | 36.5 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 33.9 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -19.5) |
| [[HOP62 (line)]] | alt | 45.3 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.6) |
| [[KATO III (line)]] | alt | 60.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 45.0 | 1 | 6 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.2) |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.204× (z -11.8) |
| [[A498 (line)]] | wt | 56.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -17.3) |
| [[H4 (line)]] | wt | 63.8 | 1 (1 ⚠) | 5 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.09× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.5) |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.0) |
| [[SW48 (line)]] | wt | 48.4 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0640× (z -18.0) |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0752× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -11.0) |
| [[A549 (line)]] | wt | 24.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -12.4) |
| [[J82 (line)]] | alt | 14.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.3) |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 32.6 | 0 | 2 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0773× (z -13.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.1) |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.382× (z -8.7) |
| [[SW1417 (line)]] | alt | 9.97 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -12.1) |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0617× (z -9.9) |
| [[BT-474 (line)]] | alt | 8.30 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 0.5 µM 0.0473× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.9) |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.0) |
| [[SW480 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -9.8) |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICALL1]] | +0.64 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[CPNE2]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MPP3]] | +0.62 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ARHGEF2]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[ABCA15P]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC01564]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[FERMT3]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SFXN5]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[GTPBP2]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PCYT1A]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.57 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[B4GALNT1]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.61 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[DOP1A]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[TMEM14C]] | -0.59 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PCM1]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[MAP3K1]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SKA2]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 | same gene group |
| [[YY1AP1]] | -0.51 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[CTDSPL2]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[RNF5]] | -0.50 | -0.51 / -0.36 | both halves | 1e-04 | same gene group |
| [[ATG3]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SPRY1]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PEX2]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB10]] | C | ADCY7 activity raises GRB10's level | lines that do not express ADCY7 (4) vs lines expressing it (46) | 3.79× lower at baseline in the lines without ADCY7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MAPK11, FSCN2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.332). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.5, 49.9); signed map (-7.5, 25.1). **Vector** length 102, 26.7% of its response variance represented; |z| ≥ 3 in 1,510 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.5 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.3 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +8.2 | +5.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +6.8 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +4.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.1 | -18.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | -12.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -16.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,246,137-50,318,135 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0037, AC7 |
| Gene groups (HGNC) | Adenylate cyclases; MicroRNA protein coding host genes |
| Reactome | 42 pathways, smallest: Adenylate cyclase activating pathway; Adenylate cyclase inhibitory pathway; PKA activation in glucagon signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P51828](https://www.uniprot.org/uniprotkb/P51828) (Adenylate cyclase type 7):

> Adenylate cyclase that mediates formation of both cyclic AMP (cAMP) and cyclic di-AMP (c-di-AMP). Acts as a key mediator of G protein-coupled receptor signaling by catalyzing the formation of cAMP downstream of G protein-coupled receptors. Functions in G protein-coupled receptor signaling cascades activated by thrombin, sphingosine 1-phosphate, dopamine and anaphylatoxin C5a. Mediates regulation of cAMP synthesis through synergistic action of the G alpha protein G(s) (GNAS) with G(13) (GNA13). …

**Summary**, from NCBI Gene [113](https://www.ncbi.nlm.nih.gov/gene/113):

> This gene encodes a membrane-bound adenylate cyclase that catalyses the formation of cyclic AMP from ATP and is inhibitable by calcium. The product of this gene is a member of the adenylyl cyclase class-4/guanylyl cyclase enzyme family that is characterized by the presence of twelve membrane-spanning domains in its sequences. Several transcript variants have been observed for this gene, but the full-length natures of only two have been determined so far. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:238) · Entrez [113](https://www.ncbi.nlm.nih.gov/gene/113) · UniProt [P51828](https://www.uniprot.org/uniprotkb/P51828) · Ensembl [ENSG00000121281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121281)

## Data

Gene col 4263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4263); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4263]; `tensor/DDL_lfc|DDL_z.npy` [4263]; `embed/gene_vectors.npy` [4263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4263 or target_col == 4263). Every well: [[ADCY7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
