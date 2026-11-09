---
symbol: "MVB12B"
type: "gene"
col: 12288
ensembl_id: "ENSG00000196814"
name: "multivesicular body subunit 12B"
location: "9q33.3"
module: 18
arm: "+"
pooled_cpm: 28.59
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 35
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 9
direction_downstream: 25
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MVB12B

*multivesicular body subunit 12B* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.37× (z +4.1, q 0.021, up in 17 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.343× (z -20.8, q 0e+00, down in 36 of 42 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.302× (z -16.5, q 0e+00, down in 35 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.65, fdr 1e-05), [[TGFBRAP1]] (+0.62, fdr 1e-05), [[NSMAF]] (+0.62, fdr 7e-06); moves opposite to [[PC]] (-0.50, fdr 2e-04), [[PTPRH]] (-0.50, fdr 4e-05), [[NBEAL1]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[FAM169A]] → it (grade B ⚠); 25 go from it, the strongest it → [[SLC25A26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.021 | 17/41 (C32, BT-474, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.036 | 15/42 (SW480, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.056 | 15/41 (C32, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.095 | 12/41 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.343×** | -20.8 | 0e+00 | 36/42 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.302×** | -16.5 | 0e+00 | 35/41 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.309×** | -16.2 | 0e+00 | 38/42 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.323×** | -15.6 | 0e+00 | 40/41 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -13.9 | 5e-42 | 34/41 (Panc 03.27, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.350×** | -13.9 | 5e-42 | 33/41 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.464×** | -10.6 | 3e-24 | 32/41 (LOX-IMVI, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.465×** | -10.6 | 4e-24 | 30/41 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.482×** | -10.1 | 5e-22 | 30/42 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.473×** | -9.5 | 8e-20 | 27/34 (NCI-H2030, C-33 A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -8.7 | 1e-16 | 24/42 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.520×** | -8.7 | 2e-16 | 17/30 (A549, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.515×** | -8.1 | 2e-14 | 27/38 (SHP-77, RKO, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -8.1 | 2e-14 | 26/42 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.545×** | -8.0 | 4e-14 | 33/40 (NCI-H460, J82, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -7.7 | 4e-13 | 29/42 (NCI-H1792, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.623×** | -6.5 | 3e-09 | 29/42 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -6.1 | 3e-08 | 24/41 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.477×** | -5.3 | 3e-06 | 30/41 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -4.8 | 4e-05 | 18/42 (SNU-1, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.717×** | -4.6 | 1e-04 | 22/41 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.002 | 17/42 (LoVo, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -3.7 | 0.004 | 18/41 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -28.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0892× (z -18.7) |
| [[A-172 (line)]] | wt | 56.3 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -23.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0603× (z -19.2) |
| [[J82 (line)]] | alt | 19.5 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -9.9) |
| [[RKO (line)]] | wt | 89.8 | 0 | 9 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -17.1) |
| [[A549 (line)]] | wt | 42.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -24.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 39.6 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.304× (z -10.8) |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -21.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 51.5 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0567× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -15.0) |
| [[SNU-1 (line)]] | wt | 69.7 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.165× (z -12.0) |
| [[C-33 A (line)]] | alt | 72.9 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -12.7) |
| [[LoVo (line)]] | wt | 67.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -20.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -16.4) |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.125× (z -13.7) |
| [[SHP-77 (line)]] | alt | 49.8 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -14.2) |
| [[SW480 (line)]] | alt | 14.4 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -10.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.246× (z -10.0) |
| [[A-427 (line)]] | wt | 30.6 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -12.6) |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -22.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -9.0) |
| [[SW48 (line)]] | wt | 61.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -9.9) |
| [[LS 180 (line)]] | wt | 39.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.294× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 8.73 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -8.5) |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -8.8) |
| [[A498 (line)]] | wt | 20.4 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.272× (z -9.4) |
| [[AN3 CA (line)]] | alt | 87.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.1) |
| [[C32 (line)]] | wt | 26.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -17.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -11.9) |
| [[COLO 205 (line)]] | alt | 76.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -19.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0280× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.65 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.62 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZNF618]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[TTC7B]] | +0.60 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[AKAP7]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MACROH2A2]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[METTL8]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[VWA8]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.58 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TANGO6]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PC]] | -0.50 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PTPRH]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[NBEAL1]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LINC02036]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MTHFR]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[PLAG1]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises MVB12B's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without FAM169A | 0.019 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[TOP2A]] | B | TOP2A activity raises MVB12B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MSI1]] | B | MSI1 activity raises MVB12B's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.77× lower at baseline in the lines without MSI1 | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[LAMC3]] | B | LAMC3 activity raises MVB12B's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without LAMC3 | 0.069 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[PRTG]] | B | PRTG activity raises MVB12B's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.32× lower at baseline in the lines without PRTG | 0.077 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[LRRN2]] | B | LRRN2 activity raises MVB12B's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without LRRN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[PLAG1]] | B | PLAG1 activity lowers MVB12B's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.91× higher at baseline in the lines without PLAG1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[NUP210]] | B | NUP210 activity raises MVB12B's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without NUP210 | 0.087 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[KIAA1549]] | C | KIAA1549 activity raises MVB12B's level | lines that do not express KIAA1549 (4) vs lines expressing it (46) | 4.17× lower at baseline in the lines without KIAA1549 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HHAT, WHRN, GNAL; maybe low, not absent; its own permutation p |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 24, C 1. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A26]] | B | MVB12B activity raises SLC25A26's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without MVB12B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[C3orf33]] | B | MVB12B activity raises C3orf33's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without MVB12B | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[MRPS27]] | B | MVB12B activity raises MRPS27's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without MVB12B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[AADAT]] | B | MVB12B activity raises AADAT's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without MVB12B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[RAD51D]] | B | MVB12B activity raises RAD51D's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without MVB12B | 0.037 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[CHCHD6]] | B | MVB12B activity raises CHCHD6's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.56× lower at baseline in the lines without MVB12B | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[FXN]] | B | MVB12B activity raises FXN's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without MVB12B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[EXOG]] | B | MVB12B activity raises EXOG's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without MVB12B | 0.048 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[ZNF236]] | B | MVB12B activity raises ZNF236's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without MVB12B | 0.055 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[PAXBP1]] | B | MVB12B activity raises PAXBP1's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without MVB12B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[FAM169A]] | B | MVB12B activity raises FAM169A's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 3.66× lower at baseline in the lines without MVB12B | 0.061 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[ZFYVE9]] | B | MVB12B activity raises ZFYVE9's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without MVB12B | 0.063 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.9, 14.0); signed map (13.3, -44.7). **Vector** length 95.7, 26.2% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.4 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.0 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.4 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +4.1 |
| fall | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.5 | -13.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -8.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -10.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -5.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | multivesicular body subunit 12B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:126,326,829-126,507,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00001; previously C9orf28, FAM125B |
| Gene groups (HGNC) | ESCRT-I |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7P6](https://www.uniprot.org/uniprotkb/Q9H7P6) (Multivesicular body subunit 12B):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies.

**Summary**, from NCBI Gene [89853](https://www.ncbi.nlm.nih.gov/gene/89853):

> The protein encoded by this gene is a component of the ESCRT-I complex, a heterotetramer, which mediates the sorting of ubiquitinated cargo protein from the plasma membrane to the endosomal vesicle. ESCRT-I complex plays an essential role in HIV budding and endosomal protein sorting. Depletion and overexpression of this and related protein (MVB12A) inhibit HIV-1 infectivity and induce unusual viral assembly defects, indicating a role for MVB12 subunits in regulating ESCRT-mediated virus …

**Accessions** — [HGNC:23368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23368) · Entrez [89853](https://www.ncbi.nlm.nih.gov/gene/89853) · UniProt [Q9H7P6](https://www.uniprot.org/uniprotkb/Q9H7P6) · Ensembl [ENSG00000196814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196814)

## Data

Gene col 12288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12288); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12288]; `tensor/DDL_lfc|DDL_z.npy` [12288]; `embed/gene_vectors.npy` [12288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12288 or target_col == 12288). Every well: [[MVB12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MVB12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
