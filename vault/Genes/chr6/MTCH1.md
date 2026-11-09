---
symbol: "MTCH1"
type: "gene"
col: 6009
ensembl_id: "ENSG00000137409"
name: "mitochondrial carrier 1"
location: "6p21.2"
module: 1
arm: "-"
pooled_cpm: 72.28
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MTCH1

*mitochondrial carrier 1* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +11.1, q 4e-26, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +9.7, q 1e-19, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.755× (z -3.9, q 0.045, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5B]] (+0.66, fdr 7e-06), [[MBOAT7]] (+0.64, fdr 7e-06), [[SEM1]] (+0.59, fdr 1e-05); moves opposite to [[CEP83]] (-0.62, fdr 8e-06), [[C12orf29]] (-0.62, fdr 1e-05), [[PAK1IP1]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.23×** | +11.1 | 4e-26 | 47/49 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.7 | 1e-19 | 44/49 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.94×** | +8.9 | 1e-16 | 41/43 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.82×** | +8.3 | 1e-14 | 42/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +8.3 | 1e-14 | 44/48 (C32, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +8.2 | 3e-14 | 46/48 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +7.3 | 3e-11 | 44/48 (A498, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +7.1 | 6e-11 | 36/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.64×** | +6.9 | 4e-10 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.2 | 2e-08 | 36/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +6.0 | 8e-08 | 41/48 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 29/50 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.35×** | +4.2 | 0.001 | 31/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.1 | 0.002 | 28/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.4 | 0.023 | 26/45 (MIA PaCa-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.035 | 24/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +3.1 | 0.064 | 22/49 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.045 | 34/48 (SW480, LoVo, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.787× | -3.4 | 0.22 | 21/48 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.793× | -3.0 | 0.50 | 11/48 (SW480, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 71.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.9) | — |
| [[A498 (line)]] | wt | 45.2 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 66.9 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +10.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 61.9 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.52× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[LoVo (line)]] | wt | 54.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 71.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 61.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 84.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 86.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.9) | — |
| [[KATO III (line)]] | alt | 80.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 70.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.6) | — |
| [[A-172 (line)]] | wt | 69.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[BT-474 (line)]] | alt | 60.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.84× (z +8.6) | — |
| [[C32 (line)]] | wt | 57.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.94× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 88.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 71.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 77.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 68.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.84× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5B]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MBOAT7]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SEM1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NLGN2]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PSAP]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FAM229A]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MYL6B]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PANX2]] | +0.57 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ATF6B]] | +0.57 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[ERGIC3]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MED31]] | +0.56 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | -0.62 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[C12orf29]] | -0.62 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[RIOK1]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ICE2]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[PEX1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ATIC]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[CHAMP1]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[BIRC3]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TMA16]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MRPL24]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZNF22]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.4, -36.6); signed map (-22.4, 8.6). **Vector** length 78.7, 22.8% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | -0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial carrier 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:36,965,807-36,986,298 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-64, PSAP, SLC25A49 |
| Gene groups (HGNC) | Solute carrier family 25 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZJ7](https://www.uniprot.org/uniprotkb/Q9NZJ7) (Mitochondrial carrier homolog 1):

> Protein insertase that mediates insertion of transmembrane proteins into the mitochondrial outer membrane. Catalyzes insertion of proteins with alpha-helical transmembrane regions, such as signal-anchored, tail-anchored and multi-pass membrane proteins (By similarity). Does not mediate insertion of beta-barrel transmembrane proteins (By similarity). May play a role in apoptosis.

**Summary**, from NCBI Gene [23787](https://www.ncbi.nlm.nih.gov/gene/23787):

> This gene encodes a member of the mitochondrial carrier family. The encoded protein is localized to the mitochondrion inner membrane and induces apoptosis independent of the proapoptotic proteins Bax and Bak. Pseudogenes on chromosomes 6 and 11 have been identified for this gene. Alternatively spliced transcript variants encoding multiple isoforms have been observed. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:17586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17586) · Entrez [23787](https://www.ncbi.nlm.nih.gov/gene/23787) · UniProt [Q9NZJ7](https://www.uniprot.org/uniprotkb/Q9NZJ7) · Ensembl [ENSG00000137409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137409)

## Data

Gene col 6009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6009); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6009]; `tensor/DDL_lfc|DDL_z.npy` [6009]; `embed/gene_vectors.npy` [6009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6009 or target_col == 6009). Every well: [[MTCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
