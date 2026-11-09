---
symbol: "IDH2"
type: "gene"
col: 11235
ensembl_id: "ENSG00000182054"
name: "isocitrate dehydrogenase (NADP(+)) 2"
location: "15q26.1"
module: 40
arm: "+"
pooled_cpm: 36.19
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IDH2

*isocitrate dehydrogenase (NADP(+)) 2* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.89× (z +7.8, q 3e-12, up in 33 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 2.81×, KATO III 3.91×, PANC-1 2.73×, NCI-H1573 4.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 2.80×, KATO III 3.96×, PANC-1 2.81×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 3.29×, A549 2.77×; ⚠ cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.327× (z -19.4, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF710-AS1]] (+0.77, fdr 7e-06, ⚠ same locus), [[POGLUT2]] (+0.72, fdr 7e-06), [[APAF1]] (+0.72, fdr 7e-06), [[TRPT1]] (+0.66, fdr 1e-05); moves opposite to [[GTF2H1]] (-0.66, fdr 1e-05), [[ST7L]] (-0.66, fdr 1e-05), [[WARS2-AS1]] (-0.65, fdr 4e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZNF710-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11235.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 2.81×, KATO III 3.91×, PANC-1 2.73×, NCI-H1573 4.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 2.80×, KATO III 3.96×, PANC-1 2.81×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 3.29×, A549 2.77×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.89×** | +7.8 | 3e-12 | 33/43 (A498, KATO III, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.77×** | +6.8 | 4e-09 | 22/34 (A498, KATO III, …) | two highest doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.1 | 8e-05 | 23/45 (NCI-H460, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.45×** | +4.4 | 0.002 | 23/47 (SW48, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.36×** | +3.8 | 0.019 | 20/43 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.32×** | +3.4 | 0.066 | 20/47 (NCI-H1573, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.327×** | -19.4 | 0e+00 | 43/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.251×** | -16.9 | 0e+00 | 45/46 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -10.6 | 5e-24 | 41/47 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -9.3 | 2e-18 | 39/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -8.7 | 3e-16 | 40/47 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -7.8 | 8e-13 | 40/47 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -6.8 | 1e-09 | 35/45 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.605×** | -6.2 | 5e-08 | 37/47 (A-172, SW 1088, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.610×** | -6.1 | 9e-08 | 34/47 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.618×** | -5.6 | 1e-06 | 32/47 (A-172, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -5.4 | 3e-06 | 35/47 (C32, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.646×** | -5.0 | 2e-05 | 31/46 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.671×** | -4.9 | 5e-05 | 27/47 (A-172, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -4.8 | 6e-05 | 26/45 (J82, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -4.7 | 9e-05 | 26/47 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -4.4 | 4e-04 | 27/47 (SHP-77, C32, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.466×** | -4.0 | 0.002 | 24/46 (LS 180, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.721×** | -4.0 | 0.002 | 23/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 54.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -16.3) |
| [[A498 (line)]] | wt | 64.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.519× (z -9.4) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -9.1) |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.9) |
| [[J82 (line)]] | alt | 46.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.8) |
| [[LoVo (line)]] | wt | 46.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.9) |
| [[C32 (line)]] | wt | 21.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -11.1) |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.5) |
| [[KATO III (line)]] | alt | 48.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.1) |
| [[PANC-1 (line)]] | alt | 49.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.9) |
| [[A549 (line)]] | wt | 33.8 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.0) |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.7) |
| [[NCI-H460 (line)]] | wt | 11.4 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.8) |
| [[BT-474 (line)]] | alt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -18.1) |
| [[COLO 205 (line)]] | alt | 49.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -9.9) |
| [[H4 (line)]] | wt | 21.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0704× (z -12.4) |
| [[LS 180 (line)]] | wt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -23.7) |
| [[NCI-H1573 (line)]] | alt | 12.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 50.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -9.9) |
| [[RKO (line)]] | wt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0498× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 37.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.4) |
| [[SHP-77 (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -16.1) |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -8.6) |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0455× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.3) |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.0) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.99 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF710-AS1]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.8 kb, same strand: neighbours can correlate without regulation) |
| [[POGLUT2]] | +0.72 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[APAF1]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TRPT1]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GLT8D1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ARL3]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[SMAP2]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[C1orf21]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SPICE1]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MED26]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H1]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ST7L]] | -0.66 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.65 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[SEMA6A-AS1]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[TIAM2]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.63 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.63 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ATXN7L1]] | -0.62 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[COA7]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[ZBTB40]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DPH5-DT]] | -0.60 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CLDN15]] | -0.60 | -0.62 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF710-AS1]] | C | IDH2's natural level strengthens ZNF710-AS1's drug response | IDH2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.57; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.7, -17.5); signed map (-41.2, 16.1). **Vector** length 97.2, 27.1% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.0 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.4 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -7.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | isocitrate dehydrogenase (NADP(+)) 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,083,045-90,102,477 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IDH-2 |
| Gene groups (HGNC) | Isocitrate dehydrogenases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ESTROGEN_RESPONSE_LATE, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P48735](https://www.uniprot.org/uniprotkb/P48735) (Isocitrate dehydrogenase):

> Catalyzes the NADP(+)-dependent oxidative decarboxylation of isocitrate (D-threo-isocitrate) to 2-ketoglutarate (2-oxoglutarate), playing a role in intermediary metabolism and energy production. Can also use 2-oxoglutarate as substrate and catalyze the reduction of 2-oxoglutarate to R-2-hydroxyglutarate. It may tightly associate or interact with the pyruvate dehydrogenase complex.

**Summary**, from NCBI Gene [3418](https://www.ncbi.nlm.nih.gov/gene/3418):

> Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isocitrate dehydrogenases, one of which is mitochondrial and the other predominantly cytosolic. Each …

**Accessions** — [HGNC:5383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5383) · Entrez [3418](https://www.ncbi.nlm.nih.gov/gene/3418) · UniProt [P48735](https://www.uniprot.org/uniprotkb/P48735) · Ensembl [ENSG00000182054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182054)

## Data

Gene col 11235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11235); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11235]; `tensor/DDL_lfc|DDL_z.npy` [11235]; `embed/gene_vectors.npy` [11235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11235 or target_col == 11235). Every well: [[IDH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
