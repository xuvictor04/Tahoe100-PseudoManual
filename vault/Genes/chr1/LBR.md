---
symbol: "LBR"
type: "gene"
col: 6809
ensembl_id: "ENSG00000143815"
name: "lamin B receptor"
location: "1q42.12"
module: 22
arm: "+"
pooled_cpm: 63.54
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# LBR

*lamin B receptor* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +16.7, q 0e+00, up in 44 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.48× (z +7.0, q 1e-10, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.620× (z -8.6, q 4e-15, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.747× (z -3.8, q 0.025, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAD2L1]] (+0.66, fdr 7e-06), [[LMNB1]] (+0.66, fdr 7e-06), [[ARHGAP11A]] (+0.65, fdr 7e-06); moves opposite to [[FBXO28]] (-0.63, fdr 1e-05), [[ADPRM]] (-0.61, fdr 1e-05), [[CCDC174]] (-0.61, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 21 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.55×** | +16.7 | 0e+00 | 44/47 (NCI-H1792, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.26×** | +14.1 | 2e-42 | 35/42 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +9.7 | 4e-20 | 36/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +9.7 | 6e-20 | 36/48 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.70×** | +9.5 | 4e-19 | 36/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.84×** | +9.4 | 4e-19 | 40/45 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.70×** | +9.2 | 4e-18 | 39/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.65×** | +9.0 | 2e-17 | 39/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.62×** | +8.6 | 4e-16 | 35/47 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.52×** | +7.5 | 3e-12 | 33/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.51×** | +7.3 | 1e-11 | 36/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.0 | 1e-10 | 36/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 3e-07 | 34/48 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 3e-07 | 35/47 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.5 | 2e-06 | 31/48 (SNU-423, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.9 | 4e-05 | 27/47 (SNU-423, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 13/49 (A498, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.007 | 18/48 (LOX-IMVI, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.042 | 16/47 (H4, HOP62, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +2.9 | 0.063 | 12/48 (HT-29, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.17× | +2.8 | 0.084 | 9/48 (HOP62, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.620×** | -8.6 | 4e-15 | 38/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.722×** | -8.3 | 3e-14 | 34/48 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.737×** | -5.5 | 7e-06 | 34/48 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.747×** | -3.8 | 0.025 | 26/46 (SW48, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.822×** | -3.4 | 0.076 | 20/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.100 | 12/48 (AsPC-1, A-172, …) | top dose only | plate-row cell shift |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.837× | -3.2 | 0.100 | 18/47 (RPMI-7951, J82, …) | inconsistent across doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.100 | 15/49 (HT-29, SW1417, …) | top dose only | plate-row cell shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.819× | -3.1 | 0.11 | 18/47 (BT-474, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.11 | 9/48 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.8 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 2.73× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 37.1 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 86.6 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 45.6 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 67.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.506× (z -11.8) ⚠ cell-cycle shift, explains ~65% of this change |
| [[CFPAC-1 (line)]] | alt | 63.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 68.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 83.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 159 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.393× (z -13.8) ⚠ cell-cycle shift, explains ~65% of this change |
| [[PANC-1 (line)]] | alt | 50.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 57.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 63.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 75.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 68.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 73.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 37.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 85.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 57.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.153× (z -9.4) |
| [[SW1417 (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.527× (z -9.2) ⚠ cell-cycle shift, explains ~65% of this change |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD2L1]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[LMNB1]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[ARHGAP11A]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 | pathway: RHOA GTPase cycle |
| [[BUB1B]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CEP55]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[KPNA2]] | +0.63 | +0.52 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[CCNA2]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ANLN]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[PRC1]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[MAPK9]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PBK]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO28]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ADPRM]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NGDN]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[YJU2B]] | -0.59 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TJAP1]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZSWIM3]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ALKBH1]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SCAND1]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[MRPS18C]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZNF593]] | -0.57 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[MFAP1]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -53.7); signed map (-47.3, -42.8). **Vector** length 121, 38.0% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.51 to 28); *Kinesins* (reactome, mean cos +0.50 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +8.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +8.0 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.2 | +9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +5.5 | +9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.5 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -7.9 | -8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -7.2 | -8.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.3 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lamin B receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,401,502-225,428,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHCR14B, TDRD18 |
| Gene groups (HGNC) | Tudor domain containing; Dehydrocholesterol reductases |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 24 pathways, smallest: Cholesterol biosynthesis via desmosterol (Bloch pathway); Initiation of Nuclear Envelope (NE) Reformation; Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14739](https://www.uniprot.org/uniprotkb/Q14739) (Delta(14)-sterol reductase LBR):

> Catalyzes the reduction of the C14-unsaturated bond of lanosterol, as part of the metabolic pathway leading to cholesterol biosynthesis. Plays a critical role in myeloid cell cholesterol biosynthesis which is essential to both myeloid cell growth and functional maturation (By similarity). Mediates the activation of NADPH oxidases, perhaps by maintaining critical levels of cholesterol required for membrane lipid raft formation during neutrophil differentiation (By similarity). Anchors the lamina …

**Summary**, from NCBI Gene [3930](https://www.ncbi.nlm.nih.gov/gene/3930):

> The protein encoded by this gene belongs to the ERG4/ERG24 family. It localized in the nuclear envelope inner membrane and anchors the lamina and the heterochromatin to the membrane. It may mediate interaction between chromatin and lamin B. Mutations of this gene has been associated with autosomal recessive HEM/Greenberg skeletal dysplasia. Alternative splicing occurs at this locus and two transcript variants encoding the same protein have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6518) · Entrez [3930](https://www.ncbi.nlm.nih.gov/gene/3930) · UniProt [Q14739](https://www.uniprot.org/uniprotkb/Q14739) · Ensembl [ENSG00000143815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143815)

## Data

Gene col 6809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6809); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6809]; `tensor/DDL_lfc|DDL_z.npy` [6809]; `embed/gene_vectors.npy` [6809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6809 or target_col == 6809). Every well: [[LBR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LBR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
