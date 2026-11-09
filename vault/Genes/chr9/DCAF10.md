---
symbol: "DCAF10"
type: "gene"
col: 4373
ensembl_id: "ENSG00000122741"
name: "DDB1 and CUL4 associated factor 10"
location: "9p13.2"
module: 114
arm: "+"
pooled_cpm: 112.61
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# DCAF10

*DDB1 and CUL4 associated factor 10* — 9p13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H23 2.05×, PANC-1 1.65×, LOX-IMVI 1.87×, NCI-H2030 1.96×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.574× (z -14.7, q 0e+00, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.715× (z -8.9, q 2e-16, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.304×, HCT15 0.234×, PANC-1 0.367×, Panc 03.27 0.338×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.101×, A-427 0.244×, SK-MEL-2 0.288×, NCI-H460 0.436×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.316×, J82 0.367×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change); [[Decitabine (drug)]] 5 µM in 1 line (SW 1088 0.0974×); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.148×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.649×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF766]] (+0.71, fdr 7e-06), [[TRIM4]] (+0.64, fdr 1e-05), [[SLC30A5]] (+0.63, fdr 7e-06); moves opposite to [[AZIN1]] (-0.57, fdr 7e-06), [[YWHAQ]] (-0.57, fdr 1e-05), [[TBL1XR1]] (-0.54, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H23 2.05×, PANC-1 1.65×, LOX-IMVI 1.87×, NCI-H2030 1.96×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.055 | 15/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.055 | 7/49 (H4, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.055 | 21/47 (SW1417, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.304×, HCT15 0.234×, PANC-1 0.367×, Panc 03.27 0.338×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.101×, A-427 0.244×, SK-MEL-2 0.288×, NCI-H460 0.436×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.316×, J82 0.367×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change); [[Decitabine (drug)]] 5 µM in 1 line (SW 1088 0.0974×); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.148×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.574×** | -14.7 | 0e+00 | 38/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.649×** | -11.0 | 1e-25 | 32/44 (NCI-H23, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -8.9 | 2e-16 | 36/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -8.7 | 5e-16 | 36/48 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -8.4 | 6e-15 | 37/47 (NCI-H1792, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -4.5 | 8e-04 | 5/48 (A498, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 0.852× | -3.9 | 0.008 | 20/45 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.859× | -3.8 | 0.009 | 13/49 (A498, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Auranofin (drug)]] 5 µM |  | 0.869× | -3.7 | 0.013 | 17/48 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -3.4 | 0.040 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 143 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.649× (z -9.2) |
| [[J82 (line)]] | alt | 147 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 237 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0765× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 245 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -34.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 101 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.367× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 61.5 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.181× (z -8.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -13.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 93.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.381× (z -11.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -16.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -17.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.480× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LoVo (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 99.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 95.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H2030 (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.148× (z -9.6) |
| [[SNU-423 (line)]] | alt | 99.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0974× (z -10.9) |
| [[SW 900 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 133 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF766]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ALG2]] | +0.61 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ZNF721]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZNF251]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[XPNPEP3]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ZNF264]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[ANKS3]] | +0.59 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[LAMB2P1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[FBXO28]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TIMM29]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AZIN1]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.57 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 | same gene group |
| [[PFKM]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.49 | -0.52 / -0.43 | both halves | 4e-05 | same gene group; pathway: Neddylation; STRING 561 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.5, -9.9); signed map (-6.9, -10.3). **Vector** length 116, 30.8% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.6 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +0.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -6.4 | -11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -6.3 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -14.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,800,554-37,867,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10765, FLJ23201; previously WDR32 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5QP82](https://www.uniprot.org/uniprotkb/Q5QP82) (DDB1- and CUL4-associated factor 10):

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [79269](https://www.ncbi.nlm.nih.gov/gene/79269):

> Predicted to be involved in regulation of apoptotic process. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23686) · Entrez [79269](https://www.ncbi.nlm.nih.gov/gene/79269) · UniProt [Q5QP82](https://www.uniprot.org/uniprotkb/Q5QP82) · Ensembl [ENSG00000122741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122741)

## Data

Gene col 4373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4373); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4373]; `tensor/DDL_lfc|DDL_z.npy` [4373]; `embed/gene_vectors.npy` [4373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4373 or target_col == 4373). Every well: [[DCAF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
