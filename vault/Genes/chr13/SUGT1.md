---
symbol: "SUGT1"
type: "gene"
col: 9117
ensembl_id: "ENSG00000165416"
name: "SGT1 assembly cochaperone of MIS12 kinetochore complex"
location: "13q14.3"
module: 60
arm: "+"
pooled_cpm: 79.78
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SUGT1

*SGT1 assembly cochaperone of MIS12 kinetochore complex* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.06× (z +12.9, q 1e-35, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.726× (z -5.7, q 6e-06, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.477×; ⚠ cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (SW 1088 0.0746×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.515×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPB1]] (+0.65, fdr 1e-05), [[FXR1]] (+0.65, fdr 7e-06), [[SNRNP48]] (+0.62, fdr 1e-05); moves opposite to [[OPA3]] (-0.54, fdr 1e-05), [[TET3]] (-0.53, fdr 1e-05), [[HIVEP1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +12.9 | 1e-35 | 46/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.99×** | +12.4 | 1e-32 | 47/48 (A498, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.92×** | +11.1 | 4e-26 | 46/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.2 | 3e-14 | 35/49 (NCI-H23, A-172, …) | two highest doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +7.3 | 2e-11 | 30/48 (RKO, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +6.9 | 4e-10 | 29/48 (C32, HT-29, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.8 | 1e-09 | 28/43 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~22% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.98×** | +6.4 | 9e-09 | 41/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.3 | 2e-08 | 34/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.6 | 1e-06 | 34/44 (A-427, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.9 | 5e-05 | 25/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +4.9 | 5e-05 | 32/49 (A-172, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.32×** | +4.8 | 6e-05 | 30/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +4.5 | 2e-04 | 28/48 (A-172, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +4.0 | 0.002 | 27/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.002 | 26/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 10/48 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 18/48 (LoVo, SW480, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.016 | 25/48 (A498, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.477×; ⚠ cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (SW 1088 0.0746×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.515×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.726×** | -5.7 | 6e-06 | 33/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.795×** | -4.1 | 0.012 | 25/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.871× | -3.5 | 0.092 | 10/48 (SW1417, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.092 | 21/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.3 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +11.9) | — |
| [[A498 (line)]] | wt | 93.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.03× (z +12.9) | — |
| [[C32 (line)]] | wt | 50.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 116 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.52× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 88.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.80× (z +11.5) | — |
| [[J82 (line)]] | alt | 82.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +9.1) | — |
| [[LoVo (line)]] | wt | 94.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 116 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 58.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 84.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 66.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.55× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 66.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +8.9) | — |
| [[KATO III (line)]] | alt | 91.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 93.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.55× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 83.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 89.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.477× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 70.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 66.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 76.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +11.3) | — |
| [[SW480 (line)]] | alt | 129 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.07× (z +11.6) | — |
| [[A-427 (line)]] | wt | 73.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 64.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.32× (z +12.9) ⚠ toxic; cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H1792 (line)]] | alt | 45.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.3) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2347 (line)]] | alt | 90.6 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.06× (z +8.8) | — |
| [[RKO (line)]] | wt | 69.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +10.7) | — |
| [[SW 1088 (line)]] | alt | 82.7 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0746× (z -9.1) |
| [[AN3 CA (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 89.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPB1]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[FXR1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SNRNP48]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[CMAS]] | +0.61 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[DEDD2]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TVP23C]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[BCAS2]] | +0.60 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[CDC40]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.59 | +0.74 / +0.33 | both halves | 1e-04 |  |
| [[GNPDA2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TXNL1]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ST13]] | +0.58 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA3]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TET3]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.52 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[ARID1A]] | -0.51 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[FAM86HP]] | -0.50 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[GGA3]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.4, -6.8); signed map (-27.3, -20.0). **Vector** length 117, 35.1% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +12.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.3 | +5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +7.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.6 | +3.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -11.2 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.9 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -10.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.1 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SGT1 assembly cochaperone of MIS12 kinetochore complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,652,709-52,700,909 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SGT1 |
| Reactome | 8 pathways, smallest: The NLRP3 inflammasome; Inflammasomes; Cell recruitment (pro-inflammatory response) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Z0](https://www.uniprot.org/uniprotkb/Q9Y2Z0) (Protein SGT1 homolog):

> May play a role in ubiquitination and subsequent proteasomal degradation of target proteins.

**Summary**, from NCBI Gene [10910](https://www.ncbi.nlm.nih.gov/gene/10910):

> This gene encodes a highly conserved nuclear protein involved in kinetochore function and required for the G1/S and G2/M transitions. This protein interacts with heat shock protein 90. Alternative splicing results in multiple transcript variants. Pseudogenes for this gene have been defined on several different chromosomes. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:16987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16987) · Entrez [10910](https://www.ncbi.nlm.nih.gov/gene/10910) · UniProt [Q9Y2Z0](https://www.uniprot.org/uniprotkb/Q9Y2Z0) · Ensembl [ENSG00000165416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165416)

## Data

Gene col 9117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9117); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9117]; `tensor/DDL_lfc|DDL_z.npy` [9117]; `embed/gene_vectors.npy` [9117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9117 or target_col == 9117). Every well: [[SUGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
