---
symbol: "PIM3"
type: "gene"
col: 12576
ensembl_id: "ENSG00000198355"
name: "Pim-3 proto-oncogene, serine/threonine kinase"
location: "22q13.33"
module: 59
arm: "+"
pooled_cpm: 44.16
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# PIM3

*Pim-3 proto-oncogene, serine/threonine kinase* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.5× (z +29.3, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -5.4, q 3e-05, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HT-29 0.209×, H4 0.215×, BT-474 0.354×, NCI-H2347 0.462×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Hs 766T 0.0617×, NCI-H2347 0.154×, LS 180 0.113×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.333×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBC3]] (+0.74, fdr 7e-06), [[GLIS2]] (+0.71, fdr 7e-06), [[CBX4]] (+0.71, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.69, fdr 7e-06), [[AHSA1]] (-0.67, fdr 7e-06), [[RNPS1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ADGRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.5×** | +29.3 | 0e+00 | 47/47 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **7.78×** | +16.2 | 0e+00 | 46/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.07×** | +16.0 | 0e+00 | 46/47 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.09×** | +8.4 | 6e-15 | 44/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.77×** | +8.4 | 7e-15 | 46/47 (NCI-H460, HOP62, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.96×** | +5.5 | 4e-06 | 34/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +5.2 | 1e-05 | 35/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.82×** | +4.9 | 7e-05 | 31/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.79×** | +4.8 | 1e-04 | 33/46 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +4.5 | 4e-04 | 32/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.70×** | +4.3 | 7e-04 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.50×** | +3.3 | 0.042 | 25/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.065 | 25/48 (HOP62, SW 900, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.067 | 25/48 (SW480, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HT-29 0.209×, H4 0.215×, BT-474 0.354×, NCI-H2347 0.462×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Hs 766T 0.0617×, NCI-H2347 0.154×, LS 180 0.113×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.333×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.628×** | -5.4 | 3e-05 | 31/48 (HT-29, H4, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.760× | -3.2 | 0.31 | 26/48 (BT-474, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.679× | -3.1 | 0.31 | 22/38 (Hs 766T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.680× | -3.1 | 0.31 | 25/49 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.95 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.6 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.3× (z +24.9) | — |
| [[NCI-H2347 (line)]] | alt | 88.3 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +24.7) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -14.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 45.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.6× (z +31.2) | — |
| [[A-172 (line)]] | wt | 33.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +18.8) | — |
| [[A549 (line)]] | wt | 26.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +23.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +24.1) | — |
| [[SW 900 (line)]] | alt | 188 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.8× (z +33.4) | — |
| [[SW48 (line)]] | wt | 44.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +17.1) | — |
| [[C32 (line)]] | wt | 36.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +17.3) | — |
| [[HEC-1-A (line)]] | alt | 41.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +21.9) | — |
| [[HepG2_C3A (line)]] | wt | 42.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +22.6) | — |
| [[HS-578T (line)]] | alt | 44.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +22.3) | — |
| [[LS 180 (line)]] | wt | 37.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 93.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +25.2) | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +18.8) | — |
| [[SNU-1 (line)]] | wt | 36.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 58.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 64.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +19.7) | — |
| [[AsPC-1 (line)]] | alt | 34.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +26.4) | — |
| [[CFPAC-1 (line)]] | alt | 75.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +27.2) | — |
| [[COLO 205 (line)]] | alt | 33.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +22.5) | — |
| [[H4 (line)]] | wt | 33.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 54.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -16.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.5× (z +22.6) | — |
| [[J82 (line)]] | alt | 42.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +20.0) | — |
| [[KATO III (line)]] | alt | 54.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +23.6) | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +20.0) | — |
| [[Panc 03.27 (line)]] | alt | 57.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +20.8) | — |
| [[PANC-1 (line)]] | alt | 34.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +26.7) | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +19.0) | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +17.6) | — |
| [[SNU-423 (line)]] | alt | 39.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.9× (z +25.7) | — |
| [[SW480 (line)]] | alt | 31.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +16.7) | — |
| [[A-427 (line)]] | wt | 17.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.19× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.333× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 42.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 56.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -16.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 22.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +13.3) | — |
| [[CHP-212 (line)]] | wt | 58.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +16.2) | — |
| [[RKO (line)]] | wt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBC3]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[GLIS2]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CBX4]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[JUND]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[HES4]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[RAB9A]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ATF4]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TUBB2B]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[IRF2BP2]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ARRDC2]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[NR1D1]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.69 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[AHSA1]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[NAA50]] | -0.66 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[BCAP31]] | -0.66 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[NUP205]] | -0.64 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[CHID1]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[NDUFA10]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[THOC5]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.62 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[NUP155]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG1]] | B | ADGRG1 activity raises PIM3's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without ADGRG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[CX3CL1]] | B | CX3CL1 activity raises PIM3's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.37× lower at baseline in the lines without CX3CL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[RHOV]] | B | RHOV activity raises PIM3's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without RHOV | 0.044 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[IL15]] | B | IL15 activity raises PIM3's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without IL15 | 0.074 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[RNF223]] | B | RNF223 activity raises PIM3's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.38× lower at baseline in the lines without RNF223 | 0.080 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[ETS2]] | B | ETS2 activity raises PIM3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without ETS2 | 0.080 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[MARCKS]] | B | MARCKS activity raises PIM3's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without MARCKS | 0.081 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[TXNIP]] | B | TXNIP activity raises PIM3's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without TXNIP | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (22.7, -3.6); signed map (-3.7, 13.4). **Vector** length 117, 41.0% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members* (reactome, mean cos +0.52 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +29.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +16.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.8 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.4 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | Pim-3 proto-oncogene, serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:49,960,768-49,964,072 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; PIM kinase family |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V86](https://www.uniprot.org/uniprotkb/Q86V86) (Serine/threonine-protein kinase pim-3):

> Proto-oncogene with serine/threonine kinase activity that can prevent apoptosis, promote cell survival and protein translation. May contribute to tumorigenesis through: the delivery of survival signaling through phosphorylation of BAD which induces release of the anti-apoptotic protein Bcl-X(L), the regulation of cell cycle progression, protein synthesis and by regulation of MYC transcriptional activity. Additionally to this role on tumorigenesis, can also negatively regulate insulin secretion …

**Summary**, from NCBI Gene [415116](https://www.ncbi.nlm.nih.gov/gene/415116):

> The protein encoded by this gene belongs to the Ser/Thr protein kinase family, and PIM subfamily. This gene is overexpressed in hematological and epithelial tumors and is associated with MYC coexpression. It plays a role in the regulation of signal transduction cascades, contributing to both cell proliferation and survival, and provides a selective advantage in tumorigenesis. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:19310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19310) · Entrez [415116](https://www.ncbi.nlm.nih.gov/gene/415116) · UniProt [Q86V86](https://www.uniprot.org/uniprotkb/Q86V86) · Ensembl [ENSG00000198355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198355)

## Data

Gene col 12576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12576); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12576]; `tensor/DDL_lfc|DDL_z.npy` [12576]; `embed/gene_vectors.npy` [12576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12576 or target_col == 12576). Every well: [[PIM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
