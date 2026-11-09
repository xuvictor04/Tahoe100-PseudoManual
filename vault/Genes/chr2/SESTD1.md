---
symbol: "SESTD1"
type: "gene"
col: 11902
ensembl_id: "ENSG00000187231"
name: "SEC14 and spectrin domain containing 1"
location: "2q31.2"
module: 163
arm: "+"
pooled_cpm: 104.62
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# SESTD1

*SEC14 and spectrin domain containing 1* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.39× (z +5.8, q 5e-06, up in 30 of 43 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.31× (z +4.8, q 4e-04, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.424× (z -21.9, q 0e+00, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGPP1]] (+0.58, fdr 1e-05), [[DPY19L1]] (+0.57, fdr 4e-05), [[XPR1]] (+0.56, fdr 5e-05); moves opposite to [[GOLGA1]] (-0.57, fdr 4e-05), [[GOSR1]] (-0.53, fdr 4e-05), [[MYSM1]] (-0.51, fdr 9e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[LHFPL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +5.8 | 5e-06 | 30/43 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 4e-04 | 24/43 (LS 180, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 7e-04 | 26/44 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.022 | 24/44 (SNU-423, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.7 | 0.023 | 10/44 (H4, Hs 766T, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.023 | 22/44 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.037 | 18/43 (H4, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.44× | +3.0 | 0.18 | 12/45 (LoVo, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.424×** | -21.9 | 0e+00 | 36/44 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -13.2 | 2e-37 | 37/44 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -9.9 | 1e-20 | 29/45 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.584×** | -9.7 | 3e-20 | 32/44 (HepG2/C3A, AsPC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.576×** | -9.6 | 1e-19 | 28/44 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.609×** | -8.9 | 4e-17 | 32/44 (SW1417, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.601×** | -8.8 | 7e-17 | 30/38 (C-33 A, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.614×** | -8.8 | 9e-17 | 31/44 (HepG2/C3A, AsPC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -7.8 | 5e-13 | 33/44 (SK-MEL-2, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -6.9 | 3e-10 | 33/44 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.684×** | -5.9 | 2e-07 | 25/40 (J82, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -5.8 | 3e-07 | 31/44 (SNU-1, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.720×** | -5.7 | 5e-07 | 26/43 (HepG2/C3A, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.743×** | -5.4 | 3e-06 | 24/44 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.750×** | -5.2 | 8e-06 | 28/45 (HOP62, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -5.0 | 2e-05 | 21/44 (A-427, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -3.7 | 0.006 | 20/44 (AsPC-1, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.840× | -3.1 | 0.044 | 20/44 (COLO 205, HOP62, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.884× | -3.1 | 0.044 | 9/44 (A498, A549, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.792×** | -3.0 | 0.066 | 14/44 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.849× | -3.0 | 0.070 | 13/44 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.848× | -2.9 | 0.091 | 10/45 (HOP62, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 261 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -22.1) |
| [[HepG2_C3A (line)]] | wt | 671 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -18.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.4) |
| [[A549 (line)]] | wt | 139 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.0) |
| [[A-172 (line)]] | wt | 104 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 279 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 171 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.4) |
| [[SW1417 (line)]] | alt | 168 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -13.7) |
| [[LoVo (line)]] | wt | 156 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -18.9) |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -15.8) |
| [[COLO 205 (line)]] | alt | 156 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.5) |
| [[KATO III (line)]] | alt | 112 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 67.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -13.8) |
| [[A498 (line)]] | wt | 169 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -13.0) |
| [[HS-578T (line)]] | alt | 77.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -18.3) |
| [[J82 (line)]] | alt | 100 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.7) |
| [[C32 (line)]] | wt | 121 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.324× (z -11.3) |
| [[Hs 766T (line)]] | wt | 93.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.7) |
| [[SW480 (line)]] | alt | 70.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -10.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-427 (line)]] | wt | 65.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.588× (z -8.5) |
| [[BT-474 (line)]] | alt | 76.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.127× (z -9.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -9.0) |
| [[HOP62 (line)]] | alt | 70.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -19.5) |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.261× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 99.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.9) |
| [[NCI-H2030 (line)]] | alt | 78.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 76.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.245× (z -12.5) |
| [[SNU-423 (line)]] | alt | 98.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -11.2) |
| [[C-33 A (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[H4 (line)]] | wt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 45.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.8) |
| [[SNU-1 (line)]] | wt | 47.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.355× (z -10.0) |
| [[SW 900 (line)]] | alt | 105 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.285× (z -10.0) |
| [[SW48 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPP1]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DPY19L1]] | +0.57 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[XPR1]] | +0.56 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[PPP4R1]] | +0.55 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DIAPH1]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SYTL4]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[RNF38]] | +0.53 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[STRN]] | +0.53 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[FDX1]] | +0.53 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[MAST2]] | +0.52 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[MFSD14B]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[MGAT4A]] | +0.51 | +0.57 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA1]] | -0.57 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[GOSR1]] | -0.53 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[MYSM1]] | -0.51 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[RPAP1]] | -0.51 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[FCF1]] | -0.50 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[LINC01473]] | -0.49 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[DARS1]] | -0.49 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[MYNN]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[YJU2]] | -0.47 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[CYB5D1]] | -0.47 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[ALG12]] | -0.46 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[PAN2]] | -0.46 | -0.58 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SESTD1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGFBP1]] | B | IGFBP1 activity raises SESTD1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.27× lower at baseline in the lines without IGFBP1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[LHFPL2]] | C | LHFPL2 activity raises SESTD1's level | lines that do not express LHFPL2 (4) vs lines expressing it (46) | 4.25× lower at baseline in the lines without LHFPL2 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, SESTD1, HIPK2; maybe low, not absent; co-absent with the target |
| [[PELI1]] | C | PELI1 activity raises SESTD1's level | lines that do not express PELI1 (4) vs lines expressing it (46) | 3.22× lower at baseline in the lines without PELI1 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC44A1, PHLDA3, RASSF5; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHFPL2]] | C | SESTD1 activity raises LHFPL2's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 3.71× lower at baseline in the lines without SESTD1 | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent; co-absent with the target |
| [[DARS1]] | C | SESTD1 activity lowers DARS1's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without SESTD1 | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[CYB5D1]] | C | SESTD1 activity lowers CYB5D1's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.76× higher at baseline in the lines without SESTD1 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[ACAD11]] | C | SESTD1 activity lowers ACAD11's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.72× higher at baseline in the lines without SESTD1 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[TSPAN3]] | C | SESTD1 activity raises TSPAN3's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without SESTD1 | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[YJU2]] | C | SESTD1 activity lowers YJU2's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.53× higher at baseline in the lines without SESTD1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[STRIP2]] | C | SESTD1 activity raises STRIP2's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without SESTD1 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[DPY19L1]] | C | SESTD1 activity raises DPY19L1's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without SESTD1 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| cells under [[Auranofin (drug)]] 5 µM | C | SESTD1 activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express SESTD1 (4) vs lines expressing it (44) | the lines without SESTD1: 0.66× the cells of the other lines | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[LMLN]] | C | SESTD1 activity lowers LMLN's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.76× higher at baseline in the lines without SESTD1 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[SART3]] | C | SESTD1 activity lowers SART3's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.31× higher at baseline in the lines without SESTD1 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[ARHGAP21]] | C | SESTD1 activity raises ARHGAP21's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without SESTD1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.3, -7.0); signed map (-18.1, 19.0). **Vector** length 105, 30.4% of its response variance represented; |z| ≥ 3 in 1,319 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +6.6 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +6.4 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +4.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -21.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.1 | -9.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.5 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | SEC14 and spectrin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:179,101,678-179,264,832 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434O0515, Solo |
| Gene groups (HGNC) | CRAL-TRIO lipid binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VW0](https://www.uniprot.org/uniprotkb/Q86VW0) (SEC14 domain and spectrin repeat-containing protein 1):

> May act as the primary docking protein directing membrane turnover and assembly of the transient receptor potential channels TRPC4 and TRPC5. Binds phospholipids such as phosphatidylinositol monophosphates, phosphatidylinositol diphosphates (PIP2s) and phosphatidic acid, but not less polar lipids including phosphatidylcholine, phosphatidylserine, and phosphatidylinositol. The binding to PIP2s is calcium dependent. Might be involved in the plasma membrane localization of CTNNB1.

**Summary**, from NCBI Gene [91404](https://www.ncbi.nlm.nih.gov/gene/91404):

> Enables phosphatidylinositol-3,4-bisphosphate binding activity and phospholipid binding activity. Involved in negative regulation of calcium ion transmembrane transport via high voltage-gated calcium channel. Located in calcium channel complex and intermediate filament cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18379) · Entrez [91404](https://www.ncbi.nlm.nih.gov/gene/91404) · UniProt [Q86VW0](https://www.uniprot.org/uniprotkb/Q86VW0) · Ensembl [ENSG00000187231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187231)

## Data

Gene col 11902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11902); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11902]; `tensor/DDL_lfc|DDL_z.npy` [11902]; `embed/gene_vectors.npy` [11902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11902 or target_col == 11902). Every well: [[SESTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SESTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
