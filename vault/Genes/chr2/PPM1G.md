---
symbol: "PPM1G"
type: "gene"
col: 3641
ensembl_id: "ENSG00000115241"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1G"
location: "2p23.3"
module: 23
arm: "-"
pooled_cpm: 99.91
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PPM1G

*protein phosphatase, Mg2+/Mn2+ dependent 1G* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (23 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.57× (z +11.1, q 6e-26, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.95× (z +7.8, q 4e-13, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.750× (z -4.8, q 9e-04, down in 28 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (LS 180 0.358×, A498 0.453×, A-427 0.522×, LOX-IMVI 0.506×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCOF1]] (+0.60, fdr 1e-05), [[ZBED4]] (+0.59, fdr 2e-05), [[TREX2]] (+0.56, fdr 6e-05); moves opposite to [[GIPC2]] (-0.63, fdr 7e-05), [[UFC1]] (-0.62, fdr 1e-05), [[DAZAP2]] (-0.62, fdr 1e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABCA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.57×** | +11.1 | 6e-26 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.55×** | +11.0 | 1e-25 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.61×** | +10.4 | 5e-23 | 47/49 (HT-29, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.42×** | +10.0 | 2e-21 | 39/43 (A498, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.31×** | +9.9 | 7e-21 | 47/48 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.95×** | +7.8 | 4e-13 | 45/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.94×** | +7.5 | 6e-12 | 45/47 (SNU-423, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.84×** | +7.2 | 5e-11 | 43/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.92×** | +7.1 | 9e-11 | 43/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.80×** | +6.7 | 2e-09 | 44/48 (C32, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.70×** | +6.2 | 2e-08 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.64×** | +5.8 | 2e-07 | 44/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.71×** | +5.8 | 3e-07 | 41/48 (C32, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.8 | 3e-07 | 42/48 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.7 | 3e-07 | 40/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 32/48 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.003 | 39/48 (NCI-H2030, C-33 A, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.003 | 31/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.004 | 23/49 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.81×** | +3.6 | 0.005 | 29/46 (NCI-H2030, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.6 | 0.005 | 34/48 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.008 | 31/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.010 | 29/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.034 | 24/48 (C32, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +3.0 | 0.045 | 27/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.19× | +2.9 | 0.052 | 17/49 (SHP-77, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.052 | 26/48 (hTERT-HPNE, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (LS 180 0.358×, A498 0.453×, A-427 0.522×, LOX-IMVI 0.506×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.750×** | -4.8 | 9e-04 | 28/48 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.772× | -3.0 | 0.32 | 29/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.829× | -3.0 | 0.32 | 22/48 (SW480, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 54.1 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[A-172 (line)]] | wt | 83.9 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.30× (z +11.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 2.60× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 43.7 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.07× (z +9.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 52.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[CFPAC-1 (line)]] | alt | 68.8 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 66.3 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.38× (z +10.4) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[PANC-1 (line)]] | alt | 93.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A498 (line)]] | wt | 154 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.453× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 79.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 68.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SW480 (line)]] | alt | 141 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[AsPC-1 (line)]] | alt | 87.4 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.94× (z +9.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[C32 (line)]] | wt | 45.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 47.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +8.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 84.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[LS 180 (line)]] | wt | 99.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.358× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 211 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.522× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[HEC-1-A (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[HS-578T (line)]] | alt | 63.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +8.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.506× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 98.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H460 (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Panc 03.27 (line)]] | alt | 81.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[RPMI-7951 (line)]] | alt | 69.9 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.77× (z +9.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SW 900 (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 162 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCOF1]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZBED4]] | +0.59 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TREX2]] | +0.56 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[NUP93]] | +0.56 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[SRPK1]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 549 |
| [[PAQR4]] | +0.55 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[FANCA]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[EIF5B]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NIN]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SERBP1]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RANBP17]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MSH5]] | +0.54 | +0.39 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPC2]] | -0.63 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[UFC1]] | -0.62 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[DAZAP2]] | -0.62 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[SUPT7L]] | -0.60 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TP53]] | -0.59 | -0.30 / -0.43 | both halves | 2e-04 | STRING 452 |
| [[RBM48]] | -0.58 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ANKRA2]] | -0.58 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[POLR2M]] | -0.58 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[RAB21]] | -0.57 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[PSMC2]] | -0.57 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CCNG2]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CLK1]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity raises PPM1G's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without ABCA3 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[ABCA3]] | B | ABCA3 activity weakens PPM1G's drug response | lines that do not express ABCA3 (9) vs lines expressing it (40) | the lines without ABCA3 respond 1.32× as strongly (z diff -1.07); strongest at Panobinostat 5 µM: 3.10x vs 2.16x (z diff -1.9) | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (12.3, 13.2); signed map (-45.0, -16.8). **Vector** length 67.6, 25.5% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.3 | +11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | -4.5 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +0.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,381,195-27,409,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP2CG, PP2Cgamma |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

UniProt [O15355](https://www.uniprot.org/uniprotkb/O15355) carries no function annotation.

**Summary**, from NCBI Gene [5496](https://www.ncbi.nlm.nih.gov/gene/5496):

> The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase is found to be responsible for the dephosphorylation of Pre-mRNA splicing factors, which is important for the formation of functional spliceosome. Studies of a similar gene in mice suggested a role of this phosphatase in regulating cell cycle progression. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:9278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9278) · Entrez [5496](https://www.ncbi.nlm.nih.gov/gene/5496) · UniProt [O15355](https://www.uniprot.org/uniprotkb/O15355) · Ensembl [ENSG00000115241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115241)

## Data

Gene col 3641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3641); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3641]; `tensor/DDL_lfc|DDL_z.npy` [3641]; `embed/gene_vectors.npy` [3641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3641 or target_col == 3641). Every well: [[PPM1G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
