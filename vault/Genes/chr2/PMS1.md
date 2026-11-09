---
symbol: "PMS1"
type: "gene"
col: 763
ensembl_id: "ENSG00000064933"
name: "PMS1 homolog 1, mismatch repair system component"
location: "2q32.2"
module: 18
arm: "+"
pooled_cpm: 45.69
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PMS1

*PMS1 homolog 1, mismatch repair system component* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.50× (z +8.3, q 6e-14, up in 36 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.37× (z +5.7, q 1e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.555× (z -17.0, q 0e+00, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.439× (z -16.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKC1]] (+0.72, fdr 7e-06), [[TTC13]] (+0.71, fdr 7e-06), [[RIOX2]] (+0.70, fdr 7e-06); moves opposite to [[ZFYVE1]] (-0.63, fdr 1e-05), [[NDUFV2-AS1]] (-0.59, fdr 1e-04), [[TOX4]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +8.3 | 6e-14 | 36/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +6.7 | 5e-09 | 28/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.35×** | +6.2 | 1e-07 | 25/48 (A-172, COLO 205, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.34×** | +5.9 | 5e-07 | 27/48 (A-172, NCI-H2347, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.33×** | +5.8 | 6e-07 | 26/47 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.7 | 1e-06 | 25/48 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.33×** | +5.6 | 2e-06 | 21/41 (HEC-1-A, Panc 03.27, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +5.6 | 2e-06 | 22/48 (NCI-H23, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +5.5 | 2e-06 | 24/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +5.5 | 3e-06 | 31/48 (A-172, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.1 | 2e-05 | 22/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +4.8 | 8e-05 | 24/47 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 3e-04 | 19/48 (HepG2/C3A, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.007 | 14/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.19× | +3.6 | 0.014 | 15/48 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.017 | 7/48 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.024 | 13/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.029 | 10/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.033 | 15/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.555×** | -17.0 | 0e+00 | 41/48 (MIA PaCa-2, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.439×** | -16.8 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -15.8 | 0e+00 | 41/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -11.4 | 8e-28 | 35/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -11.3 | 2e-27 | 35/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -11.2 | 3e-27 | 44/48 (A498, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -6.6 | 5e-09 | 30/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -6.2 | 4e-08 | 27/48 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.789×** | -4.7 | 2e-04 | 19/48 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.827×** | -3.9 | 0.006 | 21/48 (SW1417, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.5 | 0.023 | 19/48 (LS 180, SW1417, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.825×** | -3.5 | 0.023 | 17/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.739×** | -3.2 | 0.055 | 15/43 (J82, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.078 | 11/48 (J82, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 90.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -19.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 48.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -10.3) |
| [[A498 (line)]] | wt | 85.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -22.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.153× (z -11.1) |
| [[A-427 (line)]] | wt | 62.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.164× (z -10.3) |
| [[SW480 (line)]] | alt | 51.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 54.4 | 0 | 3 (1 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.230× (z -11.2) |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -10.1) |
| [[J82 (line)]] | alt | 46.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.387× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 89.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -17.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -11.8) |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -13.6) |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.341× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.270× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 81.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -16.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 57.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -8.9) |
| [[A-172 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +8.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 51.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.124× (z -9.9) |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.324× (z -8.5) |
| [[HS-578T (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 35.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -9.4) |
| [[RKO (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 73.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0936× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKC1]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TTC13]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[AHCTF1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[GMPS]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CMSS1]] | +0.65 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[MDN1]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[UTP18]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE1]] | -0.63 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | -0.59 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[TOX4]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NECAP2]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MXD1]] | -0.55 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ACHE]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KDM5A]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MICU1]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ATP6V0C]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises PMS1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without NT5M | 0.017 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[RNF39]] | B | RNF39 activity lowers PMS1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 1.60× higher at baseline in the lines without RNF39 | 0.021 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[NT5M]] | B | NT5M activity strengthens PMS1's drug response | lines that do not express NT5M (7) vs lines expressing it (41) | the lines without NT5M respond 0.71× as strongly (z diff +1.48); strongest at TAK-901 5 µM: 0.53x vs 0.31x (z diff +3.1) | 0.065 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[MTHFD1L]] | C | MTHFD1L activity raises PMS1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.8, -38.8); signed map (-5.5, -52.6). **Vector** length 93.4, 23.0% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.7 | -17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -15.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.6 | -0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | PMS1 homolog 1, mismatch repair system component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,784,085-189,877,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLH2; previously PMSL1 |
| Gene groups (HGNC) | MutL homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [P54277](https://www.uniprot.org/uniprotkb/P54277) (PMS1 protein homolog 1):

> Probably involved in the repair of mismatches in DNA.

**Summary**, from NCBI Gene [5378](https://www.ncbi.nlm.nih.gov/gene/5378):

> This gene encodes a protein belonging to the DNA mismatch repair mutL/hexB family. This protein is thought to be involved in the repair of DNA mismatches, and it can form heterodimers with MLH1, a known DNA mismatch repair protein. Mutations in this gene cause hereditary nonpolyposis colorectal cancer type 3 (HNPCC3) either alone or in combination with mutations in other genes involved in the HNPCC phenotype, which is also known as Lynch syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9121) · Entrez [5378](https://www.ncbi.nlm.nih.gov/gene/5378) · UniProt [P54277](https://www.uniprot.org/uniprotkb/P54277) · Ensembl [ENSG00000064933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064933)

## Data

Gene col 763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 763); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 763]; `tensor/DDL_lfc|DDL_z.npy` [763]; `embed/gene_vectors.npy` [763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 763 or target_col == 763). Every well: [[PMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
