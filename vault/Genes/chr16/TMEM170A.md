---
symbol: "TMEM170A"
type: "gene"
col: 9364
ensembl_id: "ENSG00000166822"
name: "transmembrane protein 170A"
location: "16q23.1"
module: 54
arm: "+"
pooled_cpm: 45.42
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TMEM170A

*transmembrane protein 170A* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.31× (z +4.8, q 9e-04, up in 25 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.36× (z +4.1, q 0.007, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.365× (z -9.3, q 6e-18, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC4]] (+0.62, fdr 2e-05), [[RPP21]] (+0.62, fdr 1e-04), [[PLEKHJ1]] (+0.61, fdr 2e-05); moves opposite to [[HNRNPUL1]] (-0.56, fdr 4e-05), [[NID1]] (-0.55, fdr 6e-05), [[ARPC4]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.31×** | +4.8 | 9e-04 | 25/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.4 | 0.004 | 24/47 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.007 | 22/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +4.0 | 0.008 | 23/48 (LS 180, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.008 | 22/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +3.9 | 0.010 | 22/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.23×** | +3.7 | 0.020 | 19/48 (LS 180, NCI-H2030, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.038 | 21/48 (COLO 205, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | 1.19× | +3.1 | 0.12 | 16/47 (SW1417, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.19× | +3.0 | 0.14 | 13/48 (NCI-H2030, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -9.3 | 6e-18 | 41/49 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -7.3 | 1e-10 | 29/44 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -5.0 | 1e-04 | 22/40 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.622×** | -4.4 | 0.002 | 25/48 (HOP62, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.868× | -3.6 | 0.044 | 21/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.053 | 21/48 (HOP62, SW 1088, …) | top dose only |  |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.837× | -3.2 | 0.13 | 12/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.838× | -3.0 | 0.19 | 10/48 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 64.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 50.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 79.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 1.92× (z +8.7) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -16.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0729× (z -10.5) |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.123× (z -9.1) |
| [[H4 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 67.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -9.4) ⚠ toxic |
| [[HOP62 (line)]] | alt | 46.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.183× (z -8.5) |
| [[Hs 766T (line)]] | wt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.9) ⚠ cell-cycle shift, explains <1% of this change |
| [[NCI-H1792 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.452× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 15 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC4]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[RPP21]] | +0.62 | +0.34 / +0.72 | both halves | 1e-04 |  |
| [[PLEKHJ1]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LSM10]] | +0.60 | +0.32 / +0.72 | both halves | 2e-04 |  |
| [[SAC3D1]] | +0.59 | +0.36 / +0.70 | both halves | 9e-05 |  |
| [[DSTYK]] | +0.59 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[C15orf61]] ⚠ | +0.58 | +0.32 / +0.66 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LIN7B]] | +0.57 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[CCDC107]] | +0.57 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[LSM2]] | +0.57 | +0.36 / +0.67 | both halves | 1e-04 |  |
| [[CCDC127]] | +0.56 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[ARL8A]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MRPL34]] | +0.55 | +0.31 / +0.64 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPUL1]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[NID1]] | -0.55 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[ARPC4]] | -0.54 | -0.30 / -0.63 | both halves | 2e-04 |  |
| [[SSU72]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[ERLIN2]] | -0.52 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[DHFR]] | -0.52 | -0.22 / -0.59 | both halves | 6e-04 |  |
| [[CDC37]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NCBP1]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[ETF1]] | -0.51 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[U2AF2]] | -0.51 | -0.28 / -0.65 | both halves | 3e-04 |  |
| [[PLEKHG2]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NDUFA10]] | -0.50 | -0.31 / -0.61 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.0, -14.0); signed map (-18.2, -3.3). **Vector** length 93.9, 21.7% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.6 | -7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.4 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.2 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.4 | -9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 170A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,443,054-75,465,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37611; previously TMEM170 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVE7](https://www.uniprot.org/uniprotkb/Q8WVE7) (Transmembrane protein 170A):

> Acts as a regulator of endoplasmic reticulum (ER) and nuclear envelope (NE) morphogenesis. Affects the ratio between tubular ER and ER sheets by promoting sheet formation at the expense of tubules. Influences NE expansion, nuclear pore complex formation and proper localization of inner nuclear membrane proteins.

**Summary**, from NCBI Gene [124491](https://www.ncbi.nlm.nih.gov/gene/124491):

> Involved in endoplasmic reticulum tubular network organization; nuclear envelope organization; and nuclear pore complex assembly. Located in endoplasmic reticulum membrane and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29577) · Entrez [124491](https://www.ncbi.nlm.nih.gov/gene/124491) · UniProt [Q8WVE7](https://www.uniprot.org/uniprotkb/Q8WVE7) · Ensembl [ENSG00000166822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166822)

## Data

Gene col 9364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9364); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9364]; `tensor/DDL_lfc|DDL_z.npy` [9364]; `embed/gene_vectors.npy` [9364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9364 or target_col == 9364). Every well: [[TMEM170A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM170A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
