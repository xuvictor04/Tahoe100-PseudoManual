---
symbol: "THSD1"
type: "gene"
col: 5815
ensembl_id: "ENSG00000136114"
name: "thrombospondin type 1 domain containing 1"
location: "13q14.3"
module: 38
arm: "+"
pooled_cpm: 10.66
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# THSD1

*thrombospondin type 1 domain containing 1* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +9.4, q 4e-18, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.756× (z -4.5, q 0.003, down in 18 of 36 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~48% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.210×, A549 0.169×, A498 0.290×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.157×, A549 0.287×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.116×, A498 0.228×; ⚠ toxic; transcription drop); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0556×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A498 0.272×); [[Tadalafil (drug)]] 0.05 µM in 1 line (HT-29 0.0586×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL1]] (+0.55, fdr 1e-05), [[C3orf62]] (+0.51, fdr 2e-05), [[SLC22A13]] (+0.50, fdr 6e-05); moves opposite to [[CASC2]] (-0.48, fdr 1e-04), [[UBR5]] (-0.47, fdr 4e-05), [[SNHG31]] (-0.45, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +9.4 | 4e-18 | 24/45 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +7.1 | 3e-10 | 18/45 (A549, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +6.5 | 1e-08 | 18/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +5.4 | 1e-05 | 14/45 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.1 | 4e-05 | 9/32 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 2e-04 | 13/40 (AsPC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 14/45 (Hs 766T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 0.001 | 15/45 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.011 | 2/45 (NCI-H460, LoVo) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.025 | 8/44 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.070 | 12/40 (J82, A549, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.2 | 0.070 | 1/14 (SNU-423) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.2 | 0.070 | 1/15 (J82) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.1 | 0.082 | 3/45 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.097 | 3/43 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5815.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.210×, A549 0.169×, A498 0.290×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.157×, A549 0.287×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.116×, A498 0.228×; ⚠ toxic; transcription drop); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0556×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A498 0.272×); [[Tadalafil (drug)]] 0.05 µM in 1 line (HT-29 0.0586×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.756×** | -4.5 | 0.003 | 18/36 (CFPAC-1, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.762×** | -4.3 | 0.003 | 11/40 (J82, SW480, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.596×** | -4.3 | 0.003 | 11/36 (NCI-H460, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.774×** | -4.1 | 0.007 | 11/44 (A-427, RPMI-7951, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.860× | -3.4 | 0.071 | 12/39 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.807× | -3.2 | 0.14 | 13/40 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 0.5 µM |  | 0.823× | -3.1 | 0.14 | 5/43 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.824× | -3.1 | 0.14 | 12/45 (NCI-H1573, J82, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 60.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.272× (z -10.2) |
| [[A549 (line)]] | wt | 26.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -19.4) ⚠ cell-cycle shift, explains ~2% of this change |
| [[CFPAC-1 (line)]] | alt | 5.35 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0556× (z -10.4) |
| [[HT-29 (line)]] | alt | 5.43 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0586× (z -10.1) |
| [[J82 (line)]] | alt | 4.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 4.18 | 0 | 1 | — | [[Vismodegib (drug)]] 0.05 µM 0.0779× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 4.52 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.100× (z -10.0) |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL1]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[C3orf62]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SLC22A13]] | +0.50 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[SNHG16]] | +0.48 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[CEACAM19]] | +0.48 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[RAPGEFL1]] | +0.48 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[DNAJC6]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[EPHX3]] | +0.47 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC6-1]] | +0.47 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[ARL9]] | +0.47 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[LINC01030]] | +0.47 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[RFPL3S]] | +0.46 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC2]] | -0.48 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[UBR5]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SNHG31]] | -0.45 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[ZHX1]] | -0.43 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[RNF167]] | -0.43 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[CDKN2C]] | -0.42 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[HMGN2]] | -0.42 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ANAPC15]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[HMGN2P5]] | -0.41 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[KLHL3]] | -0.41 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[COMMD4]] | -0.41 | -0.17 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[RAD51B]] | -0.41 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[TET2]] | -0.40 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[TCTN2]] | -0.40 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.1, -16.0); signed map (15.4, 8.5). **Vector** length 58.2, 7.87% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -2.4 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -1.8 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -1.7 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | -1.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin type 1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,377,167-52,416,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMTSP |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS62](https://www.uniprot.org/uniprotkb/Q9NS62) (Thrombospondin type-1 domain-containing protein 1):

> Is a positive regulator of nascent focal adhesion assembly, involved in the modulation of endothelial cell attachment to the extracellular matrix.

**Summary**, from NCBI Gene [55901](https://www.ncbi.nlm.nih.gov/gene/55901):

> The protein encoded by this gene contains a type 1 thrombospondin domain, which is found in a number of proteins involved in the complement pathway, as well as in extracellular matrix proteins. Alternatively spliced transcript variants encoding different isoforms have been observed for this gene. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:17754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17754) · Entrez [55901](https://www.ncbi.nlm.nih.gov/gene/55901) · UniProt [Q9NS62](https://www.uniprot.org/uniprotkb/Q9NS62) · Ensembl [ENSG00000136114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136114)

## Data

Gene col 5815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5815); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5815]; `tensor/DDL_lfc|DDL_z.npy` [5815]; `embed/gene_vectors.npy` [5815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5815 or target_col == 5815). Every well: [[THSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
