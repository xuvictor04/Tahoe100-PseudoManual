---
symbol: "TBC1D7"
type: "gene"
col: 7048
ensembl_id: "ENSG00000145979"
name: "TBC1 domain family member 7"
location: "6p24.1"
module: 54
arm: "+"
pooled_cpm: 21.64
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TBC1D7

*TBC1 domain family member 7* — 6p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.42× (z +23.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.532× (z -11.9, q 1e-29, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (54 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 46 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD2]] (+0.51, fdr 6e-04), [[WRAP73]] (+0.49, fdr 0.002, ⚠ not reproduced), [[MIR210HG]] (+0.49, fdr 7e-04), [[MAPKBP1]] (+0.48, fdr 1e-04); moves opposite to [[SNHG31]] (-0.56, fdr 9e-04, ⚠ not reproduced), [[MTR]] (-0.55, fdr 2e-04), [[NFKBID]] (-0.55, fdr 8e-05), [[ZNF436]] (-0.52, fdr 4e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +23.1 | 0e+00 | 47/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.33×** | +22.5 | 0e+00 | 48/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +19.5 | 0e+00 | 45/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +11.0 | 4e-26 | 40/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +9.5 | 4e-19 | 34/48 (SW480, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +6.9 | 4e-10 | 27/48 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 6e-10 | 23/47 (HOP62, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +6.1 | 7e-08 | 23/48 (A549, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 2e-06 | 20/47 (Panc 03.27, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +5.3 | 5e-06 | 22/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.3 | 7e-06 | 25/48 (J82, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.19× | +4.5 | 3e-04 | 13/48 (NCI-H2347, C32, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 19/47 (COLO 205, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 17/47 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.001 | 13/47 (COLO 205, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.006 | 18/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.013 | 12/47 (A498, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.532×** | -11.9 | 1e-29 | 31/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -9.3 | 3e-18 | 29/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -8.1 | 1e-13 | 24/46 (HepG2/C3A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -7.6 | 5e-12 | 24/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.714×** | -6.1 | 1e-07 | 22/48 (NCI-H2030, A549, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -5.8 | 8e-07 | 25/46 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -5.3 | 1e-05 | 19/38 (LoVo, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.774×** | -4.8 | 1e-04 | 21/47 (SW480, BT-474, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.659×** | -4.1 | 0.003 | 15/48 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -4.0 | 0.004 | 16/47 (NCI-H2347, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.8 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.91× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.0555× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -10.2) |
| [[SW480 (line)]] | alt | 23.4 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.75× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.193× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -16.8) |
| [[PANC-1 (line)]] | alt | 20.1 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.89× (z +13.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -10.8) |
| [[KATO III (line)]] | alt | 32.2 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.05× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 26.3 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.27× (z +10.6) | [[Bosentan (hydrate) (drug)]] 5 µM 0.353× (z -9.0) |
| [[A-172 (line)]] | wt | 11.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.91× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.03× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 25.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.57× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.30× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0894× (z -11.2) ⚠ cell-cycle shift, explains ~87% of this change |
| [[J82 (line)]] | alt | 29.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.97× (z +14.3) | — |
| [[LoVo (line)]] | wt | 20.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -16.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.5 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.25× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.50× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -9.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 21.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +11.6) | — |
| [[A549 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.125× (z -11.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HEC-1-A (line)]] | alt | 13.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0776× (z -15.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 13.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +10.7) | — |
| [[A-427 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -9.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 31.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.96× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0828× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.30× (z +8.5) | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0373× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW1417 (line)]] | alt | 18.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +8.5) | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 25 of them with an alert (⚠; 25 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | +0.51 | +0.22 / +0.48 | both halves | 6e-04 |  |
| [[WRAP73]] | +0.49 | +0.12 / +0.45 | ⚠ not reproduced | 0.002 |  |
| [[MIR210HG]] | +0.49 | +0.21 / +0.44 | both halves | 7e-04 |  |
| [[MAPKBP1]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[CELF1]] | +0.48 | +0.29 / +0.39 | both halves | 3e-04 |  |
| [[VPS37C]] | +0.47 | +0.16 / +0.41 | ⚠ not reproduced | 0.001 |  |
| [[ATG5]] | +0.47 | +0.07 / +0.51 | ⚠ one half (not replicated) | 0.004 |  |
| [[RABIF]] | +0.47 | +0.25 / +0.45 | both halves | 4e-04 |  |
| [[DTNBP1]] | +0.47 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[CLDN12]] | +0.47 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[NDUFA8]] | +0.47 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[PET117]] | +0.46 | +0.25 / +0.47 | both halves | 4e-04 |  |
| [[GTF2H2]] | +0.46 | +0.23 / +0.49 | both halves | 5e-04 |  |
| [[PFDN2]] | +0.46 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[PUS3]] | +0.46 | +0.30 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG31]] | -0.56 | -0.19 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[MTR]] | -0.55 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[NFKBID]] | -0.55 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[ZNF436]] | -0.52 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[PNISR-AS1]] | -0.49 | -0.12 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[LINC01135]] | -0.49 | -0.16 / -0.37 | ⚠ not reproduced | 0.001 |  |
| [[TGFB3]] | -0.49 | -0.16 / -0.26 | ⚠ not reproduced | 0.001 |  |
| [[UBR5]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CFAP418]] | -0.47 | -0.12 / -0.26 | ⚠ not reproduced | 0.002 |  |
| [[SIM2]] | -0.46 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[SIX4]] | -0.45 | -0.16 / -0.32 | ⚠ not reproduced | 0.001 |  |
| [[HAS2-AS1]] | -0.45 | -0.20 / -0.27 | both halves | 7e-04 |  |
| [[CDK2AP1]] | -0.45 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[GNAS]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[OXR1-AS1]] | -0.45 | -0.21 / -0.21 | both halves | 7e-04 |  |
| [[LMBRD2]] | -0.45 | -0.20 / -0.40 | both halves | 7e-04 |  |
| [[IFT140]] | -0.41 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[ANP32A]] | -0.41 | -0.29 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.383). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.3, 19.2); signed map (-32.6, 2.0). **Vector** length 75.3, 14.7% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +22.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +23.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +19.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +6.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.0 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -5.0 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.5 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.1 — chr6:13,266,542-13,328,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ257A7.3, FLJ32666, TBC7 |
| Gene groups (HGNC) | TSC complex; TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0N9](https://www.uniprot.org/uniprotkb/Q9P0N9) (TBC1 domain family member 7):

> Non-catalytic component of the TSC-TBC complex, a multiprotein complex that acts as a negative regulator of the canonical mTORC1 complex, an evolutionarily conserved central nutrient sensor that stimulates anabolic reactions and macromolecule biosynthesis to promote cellular biomass generation and growth. The TSC-TBC complex acts as a GTPase-activating protein (GAP) for the small GTPase RHEB, a direct activator of the protein kinase activity of mTORC1. In absence of nutrients, the TSC-TBC …

**Summary**, from NCBI Gene [51256](https://www.ncbi.nlm.nih.gov/gene/51256):

> This gene encodes a member of the TBC-domain containing protein family. The encoded protein functions as a subunit of the tuberous sclerosis TSC1-TSC2 complex which plays a role in the regulation of cellular growth and differentiation. Mutations in this gene have been associated with autosomal recessive megalencephaly. Alternative splicing results in multiple transcript variants. Naturally occurring readthrough transcription occurs between this locus and downstream LOC100130357. [provided by …

**Accessions** — [HGNC:21066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21066) · Entrez [51256](https://www.ncbi.nlm.nih.gov/gene/51256) · UniProt [Q9P0N9](https://www.uniprot.org/uniprotkb/Q9P0N9) · Ensembl [ENSG00000145979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145979)

## Data

Gene col 7048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7048); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7048]; `tensor/DDL_lfc|DDL_z.npy` [7048]; `embed/gene_vectors.npy` [7048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7048 or target_col == 7048). Every well: [[TBC1D7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
