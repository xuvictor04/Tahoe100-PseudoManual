---
symbol: "SNAP29"
type: "gene"
col: 1831
ensembl_id: "ENSG00000099940"
name: "synaptosome associated protein 29"
location: "22q11.21"
module: 41
arm: "+"
pooled_cpm: 27.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SNAP29

*synaptosome associated protein 29* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.77× (z +21.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.704× (z -7.2, q 3e-10, down in 28 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.745× (z -6.1, q 4e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INIP]] (+0.70, fdr 7e-06), [[SENP2]] (+0.68, fdr 1e-05), [[MOSPD2]] (+0.67, fdr 1e-05); moves opposite to [[EPM2A]] (-0.57, fdr 3e-04), [[RCC1]] (-0.56, fdr 4e-04), [[RCC2]] (-0.56, fdr 9e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +21.0 | 0e+00 | 46/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.65×** | +20.1 | 0e+00 | 46/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +17.3 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +6.8 | 2e-09 | 23/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.0 | 3e-07 | 18/36 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.5 | 4e-06 | 18/48 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.2 | 1e-05 | 20/43 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.4 | 6e-04 | 19/44 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.4 | 6e-04 | 18/48 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.4 | 7e-04 | 14/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 14/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.19× | +3.6 | 0.017 | 13/48 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~5% of this change | 1.18× | +3.5 | 0.019 | 16/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.021 | 4/47 (Hs 766T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.16× | +3.0 | 0.089 | 13/47 (COLO 205, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.704×** | -7.2 | 3e-10 | 28/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -6.1 | 4e-07 | 27/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.739×** | -6.0 | 4e-07 | 24/47 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -5.9 | 5e-07 | 26/47 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.777×** | -5.2 | 3e-05 | 22/48 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.621×** | -5.1 | 3e-05 | 23/48 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.635×** | -4.9 | 8e-05 | 19/40 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.803×** | -4.5 | 4e-04 | 21/48 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.796×** | -4.4 | 6e-04 | 20/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.831×** | -3.8 | 0.008 | 14/47 (hTERT-HPNE, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.840× | -3.4 | 0.031 | 7/48 (hTERT-HPNE, PANC-1, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.729×** | -3.4 | 0.031 | 11/31 (Panc 03.27, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.032 | 10/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.740×** | -3.2 | 0.049 | 10/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.2 | 0.052 | 10/47 (SW480, NCI-H460, …) | all doses, flat | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.756×** | -3.0 | 0.092 | 9/46 (Panc 03.27, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.092 | 10/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.8 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -8.9) |
| [[A-172 (line)]] | wt | 21.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.03× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.55× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 24.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 37.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +10.3) | — |
| [[SW480 (line)]] | alt | 26.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +15.3) | — |
| [[C32 (line)]] | wt | 20.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0499× (z -9.6) |
| [[HOP62 (line)]] | alt | 22.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.24× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 40.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +9.1) | — |
| [[KATO III (line)]] | alt | 38.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 22.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.00× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 58.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +10.3) | — |
| [[A549 (line)]] | wt | 22.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.220× (z -8.7) |
| [[HS-578T (line)]] | alt | 32.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +9.2) | — |
| [[J82 (line)]] | alt | 23.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.215× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0792× (z -8.5) |
| [[SW48 (line)]] | wt | 20.5 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0518× (z -13.3) |
| [[A-427 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INIP]] | +0.70 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SENP2]] | +0.68 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[MOSPD2]] | +0.67 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[POLM]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[NAGK]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GPATCH11]] | +0.58 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[ZXDC]] | +0.57 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[CDKN2D]] | +0.57 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[ZCCHC9]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DNAL4]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[STAM2]] | +0.57 | +0.36 / +0.44 | both halves | 9e-05 |  |
| [[DAD1]] | +0.57 | +0.40 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | -0.57 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[RCC1]] | -0.56 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[RCC2]] | -0.56 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.55 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[BEND3]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SUMO3]] | -0.55 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[LAPTM4B]] | -0.54 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[KCNIP3]] | -0.53 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[MRM1]] | -0.53 | -0.34 / -0.26 | both halves | 4e-04 |  |
| [[LINC02966]] | -0.53 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[ILF3]] | -0.52 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ARSB]] | -0.52 | -0.20 / -0.38 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.9, -2.1); signed map (-19.6, -9.5). **Vector** length 79.9, 15.6% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +21.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +20.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +1.5 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | synaptosome associated protein 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,859,007-20,891,214 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP-29, CEDNIK |
| Gene groups (HGNC) | SNAREs |
| Reactome | 6 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95721](https://www.uniprot.org/uniprotkb/O95721) (Synaptosomal-associated protein 29):

> SNAREs, soluble N-ethylmaleimide-sensitive factor-attachment protein receptors, are essential proteins for fusion of cellular membranes. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four alpha-helical bundle that drives membrane fusion. SNAP29 is a SNARE involved in autophagy through the direct control of autophagosome membrane fusion with the lysososome membrane. Also plays a role in ciliogenesis by regulating membrane fusions.

**Summary**, from NCBI Gene [9342](https://www.ncbi.nlm.nih.gov/gene/9342):

> This gene, a member of the SNAP25 gene family, encodes a protein involved in multiple membrane trafficking steps. Two other members of this gene family, SNAP23 and SNAP25, encode proteins that bind a syntaxin protein and mediate synaptic vesicle membrane docking and fusion to the plasma membrane. The protein encoded by this gene binds tightly to multiple syntaxins and is localized to intracellular membrane structures rather than to the plasma membrane. While the protein is mostly …

**Accessions** — [HGNC:11133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11133) · Entrez [9342](https://www.ncbi.nlm.nih.gov/gene/9342) · UniProt [O95721](https://www.uniprot.org/uniprotkb/O95721) · Ensembl [ENSG00000099940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099940)

## Data

Gene col 1831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1831); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1831]; `tensor/DDL_lfc|DDL_z.npy` [1831]; `embed/gene_vectors.npy` [1831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1831 or target_col == 1831). Every well: [[SNAP29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAP29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
