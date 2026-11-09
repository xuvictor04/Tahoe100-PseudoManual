---
symbol: "LGALS3BP"
type: "gene"
col: 2986
ensembl_id: "ENSG00000108679"
name: "galectin 3 binding protein"
location: "17q25"
module: 50
arm: "+"
pooled_cpm: 70.99
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 34
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# LGALS3BP

*galectin 3 binding protein* — 17q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.13× (z +8.2, q 1e-13, up in 29 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HEC-1-A 3.51×, J82 3.25×, HOP62 3.72×, NCI-H2030 3.56×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (J82 3.07×, HOP62 3.84×, Panc 03.27 3.25×, C32 3.06×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 2.61×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.153× (z -28.8, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIPA]] (+0.70, fdr 9e-06), [[LY6E]] (+0.69, fdr 7e-06), [[BSG]] (+0.66, fdr 1e-05); moves opposite to [[C15orf40]] (-0.56, fdr 1e-05), [[NSRP1]] (-0.51, fdr 4e-05), [[PPIG]] (-0.49, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GPX3]] → it (grade B ⚠); 34 go from it, the strongest it → [[ATP5F1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HEC-1-A 3.51×, J82 3.25×, HOP62 3.72×, NCI-H2030 3.56×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (J82 3.07×, HOP62 3.84×, Panc 03.27 3.25×, C32 3.06×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 2.61×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.2 | 1e-13 | 29/40 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.9 | 1e-09 | 30/37 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.7 | 0.031 | 22/37 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.7 | 0.031 | 22/40 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.34× | +3.2 | 0.14 | 28/42 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.2 | 0.14 | 1/42 (MIA PaCa-2) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.14 | 25/41 (A-172, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.153×** | -28.8 | 0e+00 | 41/41 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.222×** | -15.7 | 0e+00 | 40/41 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.248×** | -15.1 | 0e+00 | 41/41 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.389×** | -9.8 | 1e-20 | 40/42 (SW 900, A-172, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.524×** | -7.0 | 3e-10 | 37/41 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -5.9 | 3e-07 | 33/41 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.684×** | -5.8 | 5e-07 | 30/42 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.562×** | -5.4 | 4e-06 | 32/41 (KATO III, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.616×** | -5.2 | 1e-05 | 30/41 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.728×** | -4.8 | 7e-05 | 26/42 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.642×** | -4.8 | 9e-05 | 28/42 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.742×** | -4.6 | 2e-04 | 34/42 (CHP-212, Panc 03.27, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.482×** | -4.1 | 0.002 | 26/39 (RPMI-7951, H4, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -3.8 | 0.005 | 28/41 (KATO III, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -3.6 | 0.011 | 26/41 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.730×** | -3.4 | 0.024 | 23/41 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 110 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -32.7) |
| [[J82 (line)]] | alt | 123 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -24.5) |
| [[HOP62 (line)]] | alt | 44.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.115× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 66.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -28.9) |
| [[A-172 (line)]] | wt | 126 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -27.9) |
| [[KATO III (line)]] | alt | 127 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -28.7) |
| [[LoVo (line)]] | wt | 65.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -24.8) |
| [[NCI-H2030 (line)]] | alt | 85.6 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -22.5) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -28.5) |
| [[SW 900 (line)]] | alt | 92.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -25.2) |
| [[A498 (line)]] | wt | 142 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -21.0) |
| [[A549 (line)]] | wt | 44.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -17.7) |
| [[C32 (line)]] | wt | 105 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -21.8) |
| [[COLO 205 (line)]] | alt | 125 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.4) |
| [[HS-578T (line)]] | alt | 100 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -22.1) |
| [[hTERT-HPNE (line)]] | wt | 88.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -13.9) |
| [[LS 180 (line)]] | wt | 80.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -24.9) |
| [[PANC-1 (line)]] | alt | 32.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -22.8) |
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.1) |
| [[SNU-423 (line)]] | alt | 146 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -26.8) |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -15.0) |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 67.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.1) |
| [[Hs 766T (line)]] | wt | 63.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 36.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 78.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0618× (z -27.8) |
| [[NCI-H2347 (line)]] | alt | 89.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -22.7) |
| [[Panc 03.27 (line)]] | alt | 98.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.6) |
| [[SHP-77 (line)]] | alt | 79.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -20.4) |
| [[SW 1088 (line)]] | alt | 115 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0790× (z -13.7) |
| [[SW1417 (line)]] | alt | 60.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -23.2) |
| [[SW480 (line)]] | alt | 40.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -21.5) |
| [[HCT15 (line)]] | alt | 60.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.2) |
| [[HepG2_C3A (line)]] | wt | 91.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.2) |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -23.1) |
| [[SW48 (line)]] | wt | 54.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -20.5) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -23.1) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.4) |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -9.8) |
| [[A-427 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPA]] | +0.70 | +0.57 / +0.75 | both halves | 9e-06 | **novel candidate** |
| [[LY6E]] | +0.69 | +0.69 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 502 |
| [[BSG]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[CD74]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SCARB2]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[BST2]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[NAGA]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[LRPAP1]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[AGPAT1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TRIM14]] | +0.59 | +0.52 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[UBA7]] | +0.58 | +0.49 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[CD68]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf40]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.51 | -0.53 / -0.43 | both halves | 4e-05 |  |
| [[PPIG]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NDUFB9]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | GPX3 activity raises LGALS3BP's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without GPX3 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[CD74]] | B | CD74 activity raises LGALS3BP's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without CD74 | 0.009 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[APOL1]] | B | APOL1 activity raises LGALS3BP's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.88× lower at baseline in the lines without APOL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[HLA-DRA]] | B | HLA-DRA activity raises LGALS3BP's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.04× lower at baseline in the lines without HLA-DRA | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 34, C 0. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP5F1B]] | B | LGALS3BP activity lowers ATP5F1B's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.70× higher at baseline in the lines without LGALS3BP | 0.014 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[vincristine (drug)]] 0.05 µM | B | LGALS3BP activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[Infigratinib (drug)]] 0.5 µM | B | LGALS3BP activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | LGALS3BP activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | B | LGALS3BP activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.58× the cells of the other lines | 0.032 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[SELENON]] | B | LGALS3BP activity lowers SELENON's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 2.06× higher at baseline in the lines without LGALS3BP | 0.035 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[UBA7]] | B | LGALS3BP activity raises UBA7's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 2.50× lower at baseline in the lines without LGALS3BP | 0.040 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[PPT1]] | B | LGALS3BP activity lowers PPT1's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.49× higher at baseline in the lines without LGALS3BP | 0.041 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | LGALS3BP activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.78× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[Afatinib (drug)]] 0.05 µM | B | LGALS3BP activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.16× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[AGPAT1]] | B | LGALS3BP activity lowers AGPAT1's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.40× higher at baseline in the lines without LGALS3BP | 0.047 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | LGALS3BP activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.75× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.4, 51.1); signed map (67.5, 27.7). **Vector** length 124, 42.3% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.5 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | -0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.8 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -15.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.6 | -5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -5.2 | -9.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.2 | -4.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | galectin 3 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25 — chr17:78,971,238-78,979,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAC-2-BP, 90K, BTBD17B, TANGO10B, M2BP, gp90, CyCAP |
| Gene groups (HGNC) | Receptor ligands; BTB domain containing; Scavenger receptor cysteine rich domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08380](https://www.uniprot.org/uniprotkb/Q08380) (Galectin-3-binding protein):

> Promotes integrin-mediated cell adhesion. May stimulate host defense against viruses and tumor cells.

**Summary**, from NCBI Gene [3959](https://www.ncbi.nlm.nih.gov/gene/3959):

> The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. LGALS3BP has been found elevated in the serum of patients with cancer and in those infected by the human immunodeficiency virus (HIV). It appears to be implicated in immune response associated with natural killer (NK) and lymphokine-activated killer (LAK) cell cytotoxicity. Using fluorescence in situ hybridization the full length 90K cDNA has been localized to …

**Accessions** — [HGNC:6564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6564) · Entrez [3959](https://www.ncbi.nlm.nih.gov/gene/3959) · UniProt [Q08380](https://www.uniprot.org/uniprotkb/Q08380) · Ensembl [ENSG00000108679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108679)

## Data

Gene col 2986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2986); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2986]; `tensor/DDL_lfc|DDL_z.npy` [2986]; `embed/gene_vectors.npy` [2986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2986 or target_col == 2986). Every well: [[LGALS3BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALS3BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
