---
symbol: "APEH"
type: "gene"
col: 8851
ensembl_id: "ENSG00000164062"
name: "acylaminoacyl-peptide hydrolase"
location: "3p21.31"
module: 50
arm: "+"
pooled_cpm: 11.29
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# APEH

*acylaminoacyl-peptide hydrolase* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.85× (z +16.1, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.35× (z +3.3, q 0.052, up in 12 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 5.43×, A498 5.94×, LoVo 6.75×, NCI-H460 6.24×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 7.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 3.17×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.685× (z -4.5, q 0.003, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL12]] (+0.78, fdr 7e-06), [[BOP1]] (+0.69, fdr 7e-06), [[TUBG1]] (+0.68, fdr 7e-06); moves opposite to [[LRRC37B]] (-0.63, fdr 2e-05), [[ZMYM5]] (-0.62, fdr 2e-05), [[ZCCHC8]] (-0.62, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8851.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 5.43×, A498 5.94×, LoVo 6.75×, NCI-H460 6.24×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 7.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 3.17×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.85×** | +16.1 | 0e+00 | 35/36 (SW480, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.17×** | +13.2 | 2e-37 | 16/16 (SW480, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.12×** | +12.5 | 8e-34 | 22/25 (LS 180, A549, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.47×** | +10.8 | 6e-25 | 44/47 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.28×** | +9.8 | 8e-21 | 42/47 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.88×** | +7.5 | 5e-12 | 36/47 (SW480, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.46×** | +4.3 | 0.001 | 14/39 (NCI-H2347, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.41×** | +4.1 | 0.003 | 18/38 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.8 | 0.008 | 9/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +3.3 | 0.052 | 10/46 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.052 | 12/43 (RKO, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +3.3 | 0.052 | 12/43 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.065 | 8/40 (PANC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.31×** | +3.1 | 0.083 | 10/37 (MIA PaCa-2, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.685×** | -4.5 | 0.003 | 20/46 (Panc 03.27, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.714×** | -4.0 | 0.019 | 18/48 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -3.8 | 0.023 | 13/47 (J82, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.033 | 16/45 (RKO, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.033 | 15/47 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.748×** | -3.5 | 0.047 | 15/47 (J82, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.813×** | -3.3 | 0.063 | 16/48 (CHP-212, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.063 | 23/45 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -3.3 | 0.071 | 14/43 (Panc 03.27, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.099 | 11/46 (NCI-H23, J82, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.748× | -3.1 | 0.11 | 7/47 (NCI-H1573, BT-474, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.775× | -3.0 | 0.11 | 10/48 (A-427, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.18× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.5) |
| [[A498 (line)]] | wt | 8.09 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.7) |
| [[LoVo (line)]] | wt | 9.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.18 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.190× (z -9.5) |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0956× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 5.62 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0662× (z -10.0) |
| [[A-172 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL12]] | +0.78 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[BOP1]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TUBG1]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.67 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[E2F4]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP4]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FAAP100]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[NOC2L]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ARHGDIA]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.64 | +0.65 / +0.49 | both halves | 2e-05 |  |
| [[SIGMAR1]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TAF6]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC37B]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.62 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ZCCHC8]] | -0.62 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[KIF9-AS1]] | -0.61 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ARID4B]] | -0.61 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MRPL33]] | -0.61 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[ZCCHC10]] | -0.61 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[C2]] | -0.60 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.60 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MAFG]] | -0.59 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[N4BP2L2]] | -0.59 | -0.64 / -0.32 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.58 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.4, -27.0); signed map (-27.4, -43.7). **Vector** length 73.3, 13.2% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.3 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.9 | +13.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.3 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.8 | +12.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.3 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.3 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | acylaminoacyl-peptide hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,674,014-49,683,971 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously D3F15S2, DNF15S2, D3S48E |
| Reactome | 4 pathways, smallest: Eukaryotic Translation Termination; Translation; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13798](https://www.uniprot.org/uniprotkb/P13798) (Acylamino-acid-releasing enzyme):

> Aminopeptidase involved in the degradation of N(alpha)-acylated peptides. Displays exopeptidase activity toward N-formyl and N-acetyl peptides with a preference for dipeptide substrates (By similarity). Catalyzes the hydrolysis of the N-terminal peptide bond of an N-acetylated peptide to generate an N-acetylated amino acid and a peptide with a free N-terminus. It preferentially cleaves off Ac-Ala, Ac-Met and Ac-Ser (By similarity). Hydrolyzes N-formylated peptides likely arising from N-terminal …

**Summary**, from NCBI Gene [327](https://www.ncbi.nlm.nih.gov/gene/327):

> This gene encodes the enzyme acylpeptide hydrolase, which catalyzes the hydrolysis of the terminal acetylated amino acid preferentially from small acetylated peptides. The acetyl amino acid formed by this hydrolase is further processed to acetate and a free amino acid by an aminoacylase. This gene is located within the same region of chromosome 3 (3p21) as the aminoacylase gene, and deletions at this locus are also associated with a decrease in aminoacylase activity. The acylpeptide hydrolase …

**Accessions** — [HGNC:586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:586) · Entrez [327](https://www.ncbi.nlm.nih.gov/gene/327) · UniProt [P13798](https://www.uniprot.org/uniprotkb/P13798) · Ensembl [ENSG00000164062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164062)

## Data

Gene col 8851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8851); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8851]; `tensor/DDL_lfc|DDL_z.npy` [8851]; `embed/gene_vectors.npy` [8851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8851 or target_col == 8851). Every well: [[APEH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APEH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
