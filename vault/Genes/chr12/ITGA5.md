---
symbol: "ITGA5"
type: "gene"
col: 8443
ensembl_id: "ENSG00000161638"
name: "integrin subunit alpha 5"
location: "12q13.13"
module: 97
arm: "+"
pooled_cpm: 95.97
n_lines_expressing: 39
n_dd_up: 13
n_dd_down: 33
n_dd_up_clean: 11
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 19
direction_downstream: 9
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ITGA5

*integrin subunit alpha 5* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 4.52× (z +10.7, q 8e-24, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.434× (z -11.3, q 7e-27, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR84-AS1]] (+0.65, fdr 7e-06, ⚠ same locus), [[SEC14L2]] (+0.63, fdr 1e-05), [[ANPEP]] (+0.62, fdr 7e-06), [[ABLIM3]] (+0.60, fdr 1e-05); moves opposite to [[HNF4G]] (-0.49, fdr 6e-05), [[PARD3B]] (-0.43, fdr 2e-04), [[TXNRD2]] (-0.43, fdr 5e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[WNT5A]] → it (grade B ⚠); 9 go from it, the strongest it → [[FXYD5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **4.52×** | +10.7 | 8e-24 | 36/37 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **4.27×** | +10.3 | 3e-22 | 35/38 (NCI-H1573, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.4 | 1e-05 | 23/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.3 | 1e-05 | 28/38 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +5.1 | 3e-05 | 25/37 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **2.06×** | +5.1 | 3e-05 | 28/37 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 6e-04 | 21/37 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.002 | 17/36 (RKO, H4, …) | two highest doses | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 23/38 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.0 | 0.004 | 18/37 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.017 | 17/37 (A498, Panc 03.27, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.5 | 0.026 | 19/37 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.030 | 15/37 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.081 | 14/36 (RKO, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -11.3 | 7e-27 | 26/37 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -10.9 | 3e-25 | 35/37 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -10.4 | 5e-23 | 24/30 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.441×** | -9.9 | 4e-21 | 33/37 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.551×** | -8.1 | 8e-14 | 27/38 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -7.9 | 3e-13 | 26/38 (RPMI-7951, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -6.9 | 5e-10 | 24/36 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.605×** | -6.8 | 7e-10 | 25/37 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.620×** | -6.5 | 6e-09 | 27/37 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.635×** | -6.1 | 5e-08 | 29/37 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.731×** | -5.8 | 3e-07 | 25/38 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.643×** | -5.5 | 2e-06 | 22/32 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -4.9 | 4e-05 | 20/37 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.689×** | -4.9 | 5e-05 | 26/36 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.706×** | -4.7 | 9e-05 | 24/38 (SNU-423, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -4.7 | 1e-04 | 21/37 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.755×** | -4.5 | 2e-04 | 22/37 (SK-MEL-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.719×** | -4.4 | 4e-04 | 20/39 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.712×** | -4.1 | 0.001 | 23/37 (SK-MEL-2, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 145 | 5 | 7 (2 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 3.52× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.127× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 427 | 2 | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 9.23× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.211× (z -15.6) |
| [[HS-578T (line)]] | alt | 681 | 2 | 9 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.03× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -19.6) |
| [[AsPC-1 (line)]] | alt | 61.9 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.191× (z -10.6) |
| [[A-172 (line)]] | wt | 322 | 1 | 8 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.85× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 109 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -12.0) |
| [[SW480 (line)]] | alt | 84.2 | 6 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.34× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 11.2× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -9.4) |
| [[HOP62 (line)]] | alt | 203 | 1 | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.18× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 59.4 | 3 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 17.2× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.285× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 112 | 1 (1 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.56× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -12.1) |
| [[SW 1088 (line)]] | alt | 591 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -11.0) |
| [[H4 (line)]] | wt | 218 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -14.5) |
| [[PANC-1 (line)]] | alt | 47.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 100.0 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.253× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 101 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.01× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 64.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 110 | 3 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.21× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.339× (z -8.5) |
| [[RKO (line)]] | wt | 92.2 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.66× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -9.8) |
| [[SNU-423 (line)]] | alt | 157 | 2 | 2 | [[PH-797804 (drug)]] 5 µM 5.78× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.335× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 277 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 34.0 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +9.7) | — |
| [[A549 (line)]] | wt | 77.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -9.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 80.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 60.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 82.3 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 10.7× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 70.5 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0844× (z -8.6) |
| [[A-427 (line)]] | wt | 8.90 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR84-AS1]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SEC14L2]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ANPEP]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 498 |
| [[ABLIM3]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SERPINE1]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 564 |
| [[PTPN1]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 | pathway: Cellular responses to mechanical stimuli |
| [[COL6A3]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 870 |
| [[MEIS3]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SH3RF3]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MFGE8]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 | STRING 503 |
| [[MTSS1]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EHD2]] | +0.53 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FAH]] | +0.52 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.49 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[PARD3B]] | -0.43 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[TXNRD2]] | -0.43 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[ZNF33A]] | -0.43 | -0.18 / -0.44 | ⚠ not reproduced | 1e-03 |  |
| [[SH2D4A]] | -0.43 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5A]] | B | WNT5A activity raises ITGA5's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.25× lower at baseline in the lines without WNT5A | 0.005 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[SRPX]] | B | SRPX activity raises ITGA5's level | lines that do not express SRPX (22) vs lines expressing it (28) | 3.38× lower at baseline in the lines without SRPX | 0.013 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[ABTB3]] | B | ABTB3 activity raises ITGA5's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.79× lower at baseline in the lines without ABTB3 | 0.014 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[FOXL1]] | B | FOXL1 activity raises ITGA5's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 4.17× lower at baseline in the lines without FOXL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[SERPINE1]] | B | SERPINE1 activity raises ITGA5's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 4.05× lower at baseline in the lines without SERPINE1 | 0.020 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[LOX]] | B | LOX activity raises ITGA5's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without LOX | 0.022 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[CLMP]] | B | CLMP activity raises ITGA5's level | lines that do not express CLMP (25) vs lines expressing it (25) | 3.76× lower at baseline in the lines without CLMP | 0.026 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[PLAT]] | B | PLAT activity raises ITGA5's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.49× lower at baseline in the lines without PLAT | 0.032 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[FN1]] | B | FN1 activity raises ITGA5's level | lines that do not express FN1 (29) vs lines expressing it (21) | 3.76× lower at baseline in the lines without FN1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[SNAI2]] | B | SNAI2 activity raises ITGA5's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 3.88× lower at baseline in the lines without SNAI2 | 0.044 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[HSD11B1]] | B | HSD11B1 activity raises ITGA5's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 3.67× lower at baseline in the lines without HSD11B1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[F3]] | B | F3 activity raises ITGA5's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.80× lower at baseline in the lines without F3 | 0.054 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FXYD5]] | B | ITGA5 activity raises FXYD5's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without ITGA5 | 0.013 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[FSCN1]] | B | ITGA5 activity raises FSCN1's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without ITGA5 | 0.034 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[PTPN1]] | B | ITGA5 activity raises PTPN1's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without ITGA5 | 0.048 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[MAP4K4]] | B | ITGA5 activity strengthens MAP4K4's drug response | lines that do not express ITGA5 (9) vs lines expressing it (38) | the lines without ITGA5 respond 0.64× as strongly (z diff +1.70); strongest at Idarubicin (hydrochloride) 5 µM: 0.92x vs 0.51x (z diff +5.6) | 0.076 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1; target measured in part of the lines; artifact flags |
| [[MAP4K4]] | B | ITGA5 activity raises MAP4K4's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without ITGA5 | 0.087 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[AKAP12]] | B | ITGA5 activity raises AKAP12's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.24× lower at baseline in the lines without ITGA5 | 0.093 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[GPR84-AS1]] | B | ITGA5 activity raises GPR84-AS1's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without ITGA5 | 0.094 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[RAC2]] | B | ITGA5 activity raises RAC2's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 3.46× lower at baseline in the lines without ITGA5 | 0.098 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[TNFRSF10D]] | B | ITGA5 activity raises TNFRSF10D's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without ITGA5 | 0.098 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.6, 12.0); signed map (15.2, 35.9). **Vector** length 117, 37.0% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | +5.1 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +0.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.1 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,395,261-54,419,266 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD49e; previously FNRA |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Hallmark sets | INFLAMMATORY_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 21 pathways, smallest: RUNX2 regulates genes involved in cell migration; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; Fibronectin matrix formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P08648](https://www.uniprot.org/uniprotkb/P08648) (Integrin alpha-5):

> Integrin alpha-5/beta-1 (ITGA5:ITGB1) is a receptor for fibronectin and fibrinogen. It recognizes the sequence R-G-D in its ligands. ITGA5:ITGB1 binds to PLA2G2A via a site (site 2) which is distinct from the classical ligand-binding site (site 1) and this induces integrin conformational changes and enhanced ligand binding to site 1. ITGA5:ITGB1 acts as a receptor for fibrillin-1 (FBN1) and mediates R-G-D-dependent cell adhesion to FBN1. ITGA5:ITGB1 acts as a receptor for fibronectin (FN1) and …

**Summary**, from NCBI Gene [3678](https://www.ncbi.nlm.nih.gov/gene/3678):

> The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 5 subunit. This subunit associates with the beta 1 subunit to form a fibronectin receptor. This integrin may promote tumor invasion, and higher expression of …

**Accessions** — [HGNC:6141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6141) · Entrez [3678](https://www.ncbi.nlm.nih.gov/gene/3678) · UniProt [P08648](https://www.uniprot.org/uniprotkb/P08648) · Ensembl [ENSG00000161638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161638)

## Data

Gene col 8443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8443); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8443]; `tensor/DDL_lfc|DDL_z.npy` [8443]; `embed/gene_vectors.npy` [8443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8443 or target_col == 8443). Every well: [[ITGA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
