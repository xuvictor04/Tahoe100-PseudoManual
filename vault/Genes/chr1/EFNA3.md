---
symbol: "EFNA3"
type: "gene"
col: 6776
ensembl_id: "ENSG00000143590"
name: "ephrin A3"
location: "1q21.3"
module: 79
arm: "+"
pooled_cpm: 10.34
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 40
n_dd_up_clean: 9
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# EFNA3

*ephrin A3* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.39× (z +10.2, q 8e-22, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.391× (z -15.5, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFNA4]] (+0.87, fdr 7e-06, ⚠ same locus), [[ALDOC]] (+0.74, fdr 7e-06), [[CABIN1]] (+0.72, fdr 1e-05), [[VKORC1]] (+0.72, fdr 7e-06); moves opposite to [[ZNF655]] (-0.69, fdr 1e-05), [[AVEN]] (-0.66, fdr 1e-05), [[CLHC1]] (-0.65, fdr 5e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ARMCX4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +10.2 | 8e-22 | 33/46 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +9.8 | 5e-20 | 34/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +9.6 | 2e-19 | 40/47 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.44×** | +4.3 | 0.003 | 17/39 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.007 | 12/47 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.039 | 12/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +3.5 | 0.039 | 10/47 (SW1417, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.039 | 12/44 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.066 | 12/45 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.088 | 7/47 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.11 | 14/45 (NCI-H1573, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.391×** | -15.5 | 0e+00 | 38/44 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.328×** | -13.0 | 3e-36 | 39/43 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.353×** | -11.7 | 3e-29 | 39/46 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.378×** | -11.3 | 1e-27 | 24/33 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.423×** | -9.3 | 2e-18 | 23/28 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.463×** | -8.6 | 6e-16 | 26/40 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.552×** | -6.9 | 3e-10 | 26/45 (PANC-1, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.324×** | -6.9 | 4e-10 | 27/46 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -5.9 | 2e-07 | 13/19 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -5.8 | 5e-07 | 22/47 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.713×** | -5.6 | 1e-06 | 26/48 (A549, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.639×** | -4.9 | 4e-05 | 21/44 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -4.8 | 8e-05 | 23/43 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -4.7 | 1e-04 | 20/47 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -4.7 | 1e-04 | 20/44 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.675×** | -4.6 | 2e-04 | 17/45 (C32, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Cilostazol (drug)]] 5 µM |  | **0.670×** | -4.5 | 3e-04 | 17/47 (NCI-H2030, SW480, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.682×** | -4.3 | 6e-04 | 23/44 (AsPC-1, KATO III, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -4.3 | 6e-04 | 20/46 (HS-578T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.706×** | -4.0 | 0.001 | 17/46 (HEC-1-A, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0258× (z -29.6) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.0) |
| [[HS-578T (line)]] | alt | 6.21 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0573× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0567× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.200× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 8.07 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0347× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -8.9) |
| [[Hs 766T (line)]] | wt | 9.43 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0724× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.5) |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.5) |
| [[A549 (line)]] | wt | 8.58 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0468× (z -19.8) |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -18.3) |
| [[C32 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -9.2) |
| [[KATO III (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -12.6) |
| [[LoVo (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.7) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0894× (z -13.4) ⚠ toxic |
| [[A498 (line)]] | wt | 5.42 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0211× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 7.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.9) |
| [[HT-29 (line)]] | alt | 5.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 7.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 5.98 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0623× (z -12.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0570× (z -11.1) |
| [[SNU-423 (line)]] | alt | 6.60 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0799× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0706× (z -11.0) |
| [[SW48 (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.6) |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | +0.87 | +0.80 / +0.76 | both halves | 7e-06 | same gene group; pathway: EPH-Ephrin signaling; STRING 576; ⚠ same locus (9.3 kb, same strand: neighbours can correlate without regulation) |
| [[ALDOC]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[CABIN1]] | +0.72 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[NCKIPSD]] | +0.71 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[RNASE4]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.69 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CARHSP1]] | +0.68 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PDK3]] | +0.66 | +0.70 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[SLC26A6]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[HOXA13]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PDXP]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.69 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[AVEN]] | -0.66 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.65 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[PPP3CB-AS1]] | -0.65 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[ST7L]] | -0.64 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[SDCBP2-AS1]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ARMCX4]] | -0.63 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SPTY2D1OS]] | -0.62 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[RAB30-DT]] | -0.62 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[ACYP2]] | -0.62 | -0.61 / -0.37 | both halves | 7e-05 |  |
| [[RIPK2-DT]] | -0.62 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[DPH5-DT]] | -0.61 | -0.58 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX4]] | B | ARMCX4 activity lowers EFNA3's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.47× higher at baseline in the lines without ARMCX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[RASSF4]] | B | RASSF4 activity lowers EFNA3's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 1.60× higher at baseline in the lines without RASSF4 | 0.051 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises EFNA3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NOS1AP]] | B | NOS1AP activity raises EFNA3's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without NOS1AP | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers EFNA3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TSC22D3]] | B | TSC22D3 activity lowers EFNA3's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.49× higher at baseline in the lines without TSC22D3 | 0.099 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, -14.3); signed map (-34.5, 21.7). **Vector** length 104, 24.3% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.8 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.4 | -11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.0 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.2 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ephrin A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:155,078,837-155,087,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LERK3, Ehk1-L; previously EPLG3 |
| Gene groups (HGNC) | Ephrins |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P52797](https://www.uniprot.org/uniprotkb/P52797) (Ephrin-A3):

> Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as …

**Summary**, from NCBI Gene [1944](https://www.ncbi.nlm.nih.gov/gene/1944):

> This gene encodes a member of the ephrin (EPH) family. The ephrins and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, especially in the nervous system and in erythropoiesis. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which …

**Accessions** — [HGNC:3223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3223) · Entrez [1944](https://www.ncbi.nlm.nih.gov/gene/1944) · UniProt [P52797](https://www.uniprot.org/uniprotkb/P52797) · Ensembl [ENSG00000143590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143590)

## Data

Gene col 6776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6776); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6776]; `tensor/DDL_lfc|DDL_z.npy` [6776]; `embed/gene_vectors.npy` [6776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6776 or target_col == 6776). Every well: [[EFNA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
