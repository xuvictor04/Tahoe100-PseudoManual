---
symbol: "DRG1"
type: "gene"
col: 11720
ensembl_id: "ENSG00000185721"
name: "developmentally regulated GTP binding protein 1"
location: "22q12.2"
module: 12
arm: "+"
pooled_cpm: 56.08
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DRG1

*developmentally regulated GTP binding protein 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.31× (z +15.9, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.721× (z -7.7, q 1e-11, down in 25 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.158×, SW1417 0.466×, RPMI-7951 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.189×, HCT15 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (H4 0.214×, SW 900 0.399×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARL]] (+0.78, fdr 7e-06), [[VIRMA]] (+0.78, fdr 7e-06), [[TMEM216]] (+0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.31×** | +15.9 | 0e+00 | 46/49 (SW1417, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +12.0 | 7e-31 | 32/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +10.4 | 3e-23 | 37/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +8.7 | 7e-16 | 32/48 (SW1417, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +8.0 | 1e-13 | 28/48 (J82, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.5 | 6e-12 | 32/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.5 | 6e-12 | 36/48 (LOX-IMVI, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +4.7 | 2e-04 | 22/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 7e-04 | 18/48 (LoVo, LS 180, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.002 | 19/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.004 | 17/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.16× | +3.7 | 0.009 | 17/48 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.042 | 7/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | 1.13× | +3.1 | 0.078 | 17/47 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.094 | 0/49 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11720.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.158×, SW1417 0.466×, RPMI-7951 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.189×, HCT15 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (H4 0.214×, SW 900 0.399×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.721×** | -7.7 | 1e-11 | 25/45 (RPMI-7951, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -7.0 | 7e-10 | 26/47 (RPMI-7951, AN3 CA, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.775×** | -6.5 | 2e-08 | 27/48 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | **0.823×** | -4.7 | 3e-04 | 22/42 (C-33 A, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | 0.839× | -4.4 | 0.001 | 23/48 (COLO 205, SW1417, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.850× | -4.1 | 0.004 | 22/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.9 | 0.008 | 17/49 (HEC-1-A, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.6 | 0.019 | 11/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.867× | -3.6 | 0.019 | 19/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.863× | -3.6 | 0.019 | 17/47 (hTERT-HPNE, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.874× | -3.4 | 0.033 | 13/48 (H4, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.914× | -3.2 | 0.062 | 10/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.885× | -3.1 | 0.093 | 20/48 (HOP62, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 69.7 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +9.1) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.197× (z -9.9) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 62.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.473× (z -8.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[LoVo (line)]] | wt | 54.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +18.2) | — |
| [[RPMI-7951 (line)]] | alt | 54.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 86.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.91× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[COLO 205 (line)]] | alt | 49.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[HCT15 (line)]] | alt | 86.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[LS 180 (line)]] | wt | 48.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 46.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.3) | — |
| [[SW480 (line)]] | alt | 43.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.78× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.222× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[CFPAC-1 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -11.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.6) | — |
| [[KATO III (line)]] | alt | 67.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.45× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 52.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -12.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[PANC-1 (line)]] | alt | 47.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.96× (z +9.5) | — |
| [[RKO (line)]] | wt | 67.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.27× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 61.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.4) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[SW 900 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.399× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARL]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.78 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[TMEM216]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SCNM1]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[RINT1]] | +0.70 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[PRPF6]] | +0.69 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[SUGP1]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.68 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[ZNHIT3]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ZNF251]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PSMD5]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[BRAP]] | +0.67 | +0.74 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.1, -7.3); signed map (-13.3, -11.8). **Vector** length 110, 27.1% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +15.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +12.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.2 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -6.3 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -6.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -5.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | developmentally regulated GTP binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,399,604-31,528,740 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NEDD3 |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y295](https://www.uniprot.org/uniprotkb/Q9Y295) (Developmentally-regulated GTP-binding protein 1):

> Catalyzes the conversion of GTP to GDP through hydrolysis of the gamma-phosphate bond in GTP. Appears to have an intrinsic GTPase activity that is stimulated by ZC3H15/DFRP1 binding likely by increasing the affinity for the potassium ions. When hydroxylated at C-3 of 'Lys-22' by JMJD7, may bind to RNA and play a role in translation. Binds to microtubules and promotes microtubule polymerization and stability that are required for mitotic spindle assembly during prophase to anaphase transition. …

**Summary**, from NCBI Gene [4733](https://www.ncbi.nlm.nih.gov/gene/4733):

> Enables GTPase activity; microtubule binding activity; and potassium ion binding activity. Involved in positive regulation of microtubule polymerization and regulation of mitotic spindle assembly. Located in cytosol and nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3029) · Entrez [4733](https://www.ncbi.nlm.nih.gov/gene/4733) · UniProt [Q9Y295](https://www.uniprot.org/uniprotkb/Q9Y295) · Ensembl [ENSG00000185721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185721)

## Data

Gene col 11720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11720); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11720]; `tensor/DDL_lfc|DDL_z.npy` [11720]; `embed/gene_vectors.npy` [11720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11720 or target_col == 11720). Every well: [[DRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
