---
symbol: "PHF12"
type: "gene"
col: 3032
ensembl_id: "ENSG00000109118"
name: "PHD finger protein 12"
location: "17q11.2"
module: 134
arm: "+"
pooled_cpm: 51.14
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# PHF12

*PHD finger protein 12* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.48× (z +14.3, q 1e-43, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.402× (z -19.9, q 0e+00, down in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.629× (z -10.2, q 4e-22, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD2L]] (+0.64, fdr 1e-05), [[ALKBH5]] (+0.64, fdr 1e-05), [[KIAA2013]] (+0.63, fdr 7e-06); moves opposite to [[TTC27]] (-0.54, fdr 3e-05), [[MCOLN3]] (-0.54, fdr 6e-05), [[MATR3-1]] (-0.52, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.48×** | +14.3 | 1e-43 | 43/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +12.6 | 8e-34 | 40/48 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +8.2 | 6e-14 | 30/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +7.7 | 1e-12 | 35/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +6.8 | 1e-09 | 27/48 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 2e-04 | 21/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +4.7 | 2e-04 | 24/48 (SW480, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.2 | 0.11 | 0/49 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.12 | 13/48 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.14 | 8/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.402×** | -19.9 | 0e+00 | 46/47 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -15.9 | 0e+00 | 35/42 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.495×** | -14.3 | 8e-44 | 35/44 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -10.2 | 4e-22 | 29/48 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.769×** | -8.1 | 5e-14 | 25/48 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -7.3 | 4e-11 | 28/48 (SW 900, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.776×** | -5.5 | 2e-06 | 25/48 (SW 900, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -5.5 | 3e-06 | 25/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.772×** | -5.4 | 3e-06 | 25/48 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -5.0 | 4e-05 | 24/48 (SW 900, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -4.8 | 7e-05 | 18/48 (SK-MEL-2, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.812×** | -4.6 | 2e-04 | 23/47 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.680×** | -4.4 | 5e-04 | 22/48 (A498, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.822×** | -4.3 | 8e-04 | 15/49 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.2 | 0.001 | 21/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.827×** | -3.9 | 0.003 | 19/48 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -3.8 | 0.004 | 18/48 (NCI-H1792, HS-578T, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 0.838× | -3.7 | 0.006 | 13/47 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.035 | 12/46 (SW480, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.068 | 16/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.831×** | -2.9 | 0.087 | 7/49 (NCI-H1792, hTERT-HPNE, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 125 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -20.1) |
| [[A498 (line)]] | wt | 68.6 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.405× (z -11.2) |
| [[A-172 (line)]] | wt | 57.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 55.4 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.159× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.8) |
| [[C32 (line)]] | wt | 68.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -13.4) |
| [[PANC-1 (line)]] | alt | 62.7 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.03× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -11.0) |
| [[SW480 (line)]] | alt | 43.6 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.36× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 63.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -14.3) |
| [[LS 180 (line)]] | wt | 35.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.63× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 83.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -13.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 71.1 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 72.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 49.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -12.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 59.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -12.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 61.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.50× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 48.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -18.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.8) |
| [[HS-578T (line)]] | alt | 48.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.11× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 62.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -22.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 38.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -8.6) |
| [[COLO 205 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -12.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.104× (z -9.1) |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD2L]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[KIAA2013]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GLRX5]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD13D]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NIF3L1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PDXP]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[KMT5C]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[WRAP53]] | +0.56 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[HDGFL2]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[BAG4]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CHSY1]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC27]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MCOLN3]] | -0.54 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[MATR3-1]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[PEA15]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LINC00520]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ZFPM2]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.49 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[GCFC2]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[NAALADL2-AS2]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[LINC01186]] | -0.48 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CPEB1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PHF12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.7, -16.0); signed map (-37.2, 4.6). **Vector** length 117, 32.3% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.7 | +14.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.5 | +12.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.3 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -19.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,905,250-28,951,771 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PF1, KIAA1523 |
| Gene groups (HGNC) | PHD finger proteins; EMSY complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QT6](https://www.uniprot.org/uniprotkb/Q96QT6) (PHD finger protein 12):

> Transcriptional repressor acting as key scaffolding subunit of SIN3 complexes which contributes to complex assembly by contacting each core subunit domain, stabilizes the complex and constitutes the substrate receptor by recruiting the H3 histone tail. SIN3 complexes are composed of a SIN3 scaffold subunit, one catalytic core (HDAC1 or HDAC2) and 2 chromatin targeting modules. SIN3B complex represses transcription and counteracts the histone acetyltransferase activity of EP300 through the …

**Summary**, from NCBI Gene [57649](https://www.ncbi.nlm.nih.gov/gene/57649):

> Enables phosphatidylinositol binding activity and transcription corepressor activity. Involved in negative regulation of DNA-templated transcription. Acts upstream of or within negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of Sin3-type complex and transcription repressor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20816) · Entrez [57649](https://www.ncbi.nlm.nih.gov/gene/57649) · UniProt [Q96QT6](https://www.uniprot.org/uniprotkb/Q96QT6) · Ensembl [ENSG00000109118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109118)

## Data

Gene col 3032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3032); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3032]; `tensor/DDL_lfc|DDL_z.npy` [3032]; `embed/gene_vectors.npy` [3032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3032 or target_col == 3032). Every well: [[PHF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
