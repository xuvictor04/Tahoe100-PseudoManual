---
symbol: "LRSAM1"
type: "gene"
col: 7273
ensembl_id: "ENSG00000148356"
name: "leucine rich repeat and sterile alpha motif containing 1"
location: "9q33.3-q34.11"
module: 172
arm: "+"
pooled_cpm: 58.59
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# LRSAM1

*leucine rich repeat and sterile alpha motif containing 1* — 9q33.3-q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.44× (z +7.1, q 1e-09, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.495× (z -14.2, q 3e-43, down in 39 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.806× (z -6.0, q 9e-08, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK6]] (+0.72, fdr 7e-06), [[LRRC37B]] (+0.68, fdr 7e-06), [[TRNAU1AP]] (+0.65, fdr 7e-06); moves opposite to [[MED14]] (-0.64, fdr 7e-06), [[ACTB]] (-0.62, fdr 1e-05), [[ATP5F1B]] (-0.61, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +7.1 | 1e-09 | 30/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.0 | 5e-07 | 29/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +4.8 | 3e-04 | 24/47 (RKO, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.011 | 21/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.046 | 21/47 (RKO, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.075 | 22/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.095 | 10/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.098 | 12/48 (A549, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.13 | 13/47 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.16× | +3.0 | 0.14 | 7/49 (HOP62, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.495×** | -14.2 | 3e-43 | 39/49 (A549, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.551×** | -11.6 | 1e-28 | 33/41 (MIA PaCa-2, Hs 766T, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.565×** | -11.6 | 1e-28 | 43/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.559×** | -11.3 | 1e-27 | 35/47 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.550×** | -11.2 | 6e-27 | 33/45 (NCI-H23, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.583×** | -10.7 | 6e-25 | 41/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.654×** | -8.6 | 8e-16 | 36/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -6.3 | 2e-08 | 3/49 (H4, SW 1271, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -6.0 | 9e-08 | 25/48 (J82, SNU-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.763×** | -5.3 | 8e-06 | 23/48 (A-172, A498, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.9 | 6e-05 | 19/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.797×** | -4.6 | 2e-04 | 21/48 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.794×** | -4.5 | 3e-04 | 21/47 (RKO, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.802×** | -4.3 | 7e-04 | 21/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.671×** | -4.2 | 9e-04 | 20/48 (SK-MEL-2, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -4.2 | 0.001 | 23/48 (A-172, SNU-423, …) | top dose only |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.838× | -3.6 | 0.012 | 19/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.890× | -3.2 | 0.036 | 8/48 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -2.9 | 0.095 | 16/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 0.862× | -2.9 | 0.095 | 7/48 (HS-578T, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 149 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 99.7 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -15.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 75.0 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.448× (z -12.8) |
| [[SNU-423 (line)]] | alt | 96.2 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 67.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 59.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 46.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0672× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 52.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.446× (z -9.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 56.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 114 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -9.8) ⚠ toxic |
| [[H4 (line)]] | wt | 55.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 52.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 71.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LS 180 (line)]] | wt | 67.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.289× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H23 (line)]] | alt | 62.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0844× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 59.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0959× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[C-33 A (line)]] | alt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 91.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HT-29 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 61.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.365× (z -10.3) |
| [[SW 900 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.306× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AsPC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK6]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LRRC37B]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TRNAU1AP]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TBCA]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MTRFR]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GPATCH1]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF653]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NKAP]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TMEM79]] | +0.58 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[MRPL45P2]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[WBP4]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED14]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[ACTB]] | -0.62 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.61 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.58 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[VMA21]] | -0.57 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[DHX15]] | -0.56 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ICMT]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NUDT15]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers LRSAM1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.7, -4.1); signed map (-4.3, 0.8). **Vector** length 122, 35.3% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.3 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +2.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.6 | -11.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.2 | -11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.1 | -4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and sterile alpha motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3-q34.11 — chr9:127,451,489-127,503,499 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31641, CMT2P, RIFLE, TAL |
| Gene groups (HGNC) | Ring finger proteins; Sterile alpha motif domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWE0](https://www.uniprot.org/uniprotkb/Q6UWE0) (E3 ubiquitin-protein ligase LRSAM1):

> E3 ubiquitin-protein ligase that mediates monoubiquitination of TSG101 at multiple sites, leading to inactivate the ability of TSG101 to sort endocytic (EGF receptors) and exocytic (HIV-1 viral proteins) cargos. Bacterial recognition protein that defends the cytoplasm from invasive pathogens. Localizes to several intracellular bacterial pathogens and generates the bacteria-associated ubiquitin signal leading to autophagy-mediated intracellular bacteria degradation (xenophagy).

**Summary**, from NCBI Gene [90678](https://www.ncbi.nlm.nih.gov/gene/90678):

> This gene encodes a ring finger protein involved in a variety of functions, including regulation of signaling pathways and cell adhesion, mediation of self-ubiquitylation, and involvement in cargo sorting during receptor endocytosis. Mutations in this gene have been associated with Charcot-Marie-Tooth disease. Multiple transcript variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:25135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25135) · Entrez [90678](https://www.ncbi.nlm.nih.gov/gene/90678) · UniProt [Q6UWE0](https://www.uniprot.org/uniprotkb/Q6UWE0) · Ensembl [ENSG00000148356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148356)

## Data

Gene col 7273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7273); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7273]; `tensor/DDL_lfc|DDL_z.npy` [7273]; `embed/gene_vectors.npy` [7273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7273 or target_col == 7273). Every well: [[LRSAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRSAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
