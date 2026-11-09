---
symbol: "CHORDC1"
type: "gene"
col: 3121
ensembl_id: "ENSG00000110172"
name: "cysteine and histidine rich domain containing 1"
location: "11q14.3"
module: 60
arm: "+"
pooled_cpm: 76.13
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CHORDC1

*cysteine and histidine rich domain containing 1* — 11q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 8.87× (z +23.3, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.231×, NCI-H2347 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (H4 0.177×); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (NCI-H1792 0.0656×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACYBP]] (+0.76, fdr 7e-06), [[AHSA1]] (+0.74, fdr 7e-06), [[HSPH1]] (+0.74, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.63, fdr 1e-05), [[POLR2L]] (-0.59, fdr 1e-05), [[RSPRY1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DGKG]] → it (grade B ⚠); 2 go from it, the strongest it → [[HSP90AA1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **8.87×** | +23.3 | 0e+00 | 48/48 (SW480, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **6.83×** | +20.5 | 0e+00 | 48/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **5.45×** | +18.1 | 0e+00 | 48/48 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.64×** | +15.4 | 0e+00 | 48/48 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.68×** | +13.3 | 2e-38 | 47/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.19×** | +10.9 | 1e-25 | 48/49 (RKO, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.77×** | +10.8 | 2e-25 | 48/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.67×** | +10.4 | 1e-23 | 48/48 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.49×** | +10.4 | 1e-23 | 43/43 (RKO, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +10.0 | 8e-22 | 41/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +7.6 | 2e-12 | 42/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +7.1 | 7e-11 | 39/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Infigratinib (drug)]] 5 µM |  | **3.07×** | +6.2 | 2e-08 | 46/48 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +6.0 | 7e-08 | 42/49 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.93×** | +6.0 | 8e-08 | 41/48 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +6.0 | 8e-08 | 32/48 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +4.8 | 6e-05 | 34/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +4.3 | 6e-04 | 35/49 (HOP62, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.231×, NCI-H2347 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (H4 0.177×); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (NCI-H1792 0.0656×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbamazepine (drug)]] 5 µM |  | 0.742× | -3.2 | 0.69 | 21/47 (C32, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 95.3 | 14 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.5× (z +27.5) | — |
| [[KATO III (line)]] | alt | 70.6 | 12 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 12.7× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 50.6 | 13 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.49× (z +15.2) | — |
| [[H4 (line)]] | wt | 44.7 | 10 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 12.8× (z +15.1) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.177× (z -10.2) |
| [[HT-29 (line)]] | alt | 62.1 | 11 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 25.6× (z +24.1) | — |
| [[Hs 766T (line)]] | wt | 61.2 | 10 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +18.6) | — |
| [[LS 180 (line)]] | wt | 59.3 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 15.1× (z +17.9) | — |
| [[CFPAC-1 (line)]] | alt | 33.9 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 16.0× (z +17.8) | — |
| [[A-172 (line)]] | wt | 32.4 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 19.6× (z +21.9) | — |
| [[C-33 A (line)]] | alt | 81.9 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 18.1× (z +19.8) | — |
| [[COLO 205 (line)]] | alt | 33.3 | 8 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 33.7× (z +19.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 8.25× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 36.7 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.6× (z +25.0) | — |
| [[PANC-1 (line)]] | alt | 107 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.17× (z +16.7) | — |
| [[RKO (line)]] | wt | 97.9 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 16.1× (z +23.5) | — |
| [[SNU-423 (line)]] | alt | 48.0 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 23.3× (z +23.1) | — |
| [[SW1417 (line)]] | alt | 123 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.3× (z +17.6) | — |
| [[LoVo (line)]] | wt | 70.8 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.7× (z +23.7) | — |
| [[NCI-H1573 (line)]] | alt | 43.1 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.29× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 81.3 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.80× (z +14.9) | — |
| [[A549 (line)]] | wt | 73.8 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.99× (z +13.3) | — |
| [[C32 (line)]] | wt | 62.8 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 34.2× (z +21.6) | — |
| [[NCI-H1792 (line)]] | alt | 43.2 | 5 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 6.38× (z +11.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.6) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0656× (z -9.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 72.7 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.83× (z +15.6) | — |
| [[A498 (line)]] | wt | 66.9 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.62× (z +18.4) | — |
| [[BT-474 (line)]] | alt | 60.2 | 5 | 0 | [[Auranofin (drug)]] 5 µM 16.6× (z +20.9) | — |
| [[HEC-1-A (line)]] | alt | 81.2 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.8× (z +18.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.8 | 5 | 0 | [[Auranofin (drug)]] 5 µM 22.0× (z +20.5) | — |
| [[NCI-H2347 (line)]] | alt | 78.1 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.51× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.3× (z +16.3) | — |
| [[HS-578T (line)]] | alt | 76.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.53× (z +15.3) | — |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.69× (z +13.8) | — |
| [[J82 (line)]] | alt | 110 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.49× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 76.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +16.8) | — |
| [[HCT15 (line)]] | alt | 66.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.62× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 117 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.62× (z +15.4) | — |
| [[NCI-H23 (line)]] | alt | 72.1 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.57× (z +14.3) | — |
| [[SHP-77 (line)]] | alt | 193 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.67× (z +11.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 5.00× (z +11.0) | — |
| [[SW48 (line)]] | wt | 104 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.56× (z +13.7) | — |
| [[A-427 (line)]] | wt | 71.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.88× (z +16.3) | — |
| [[CHP-212 (line)]] | wt | 87.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.97× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 83.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.82× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 103 | 2 | 0 | [[Auranofin (drug)]] 5 µM 17.0× (z +15.8) | — |
| [[AN3 CA (line)]] | alt | 110 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.7× (z +15.3) | — |
| [[AsPC-1 (line)]] | alt | 114 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.45× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 101 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 144 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +10.9) | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACYBP]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | STRING 582 |
| [[AHSA1]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 | STRING 858 |
| [[HSPH1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | STRING 666 |
| [[CCT4]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[HSPE1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[TCP1]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[HSPD1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.63 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HSP90AB3P]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[POPDC3]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.63 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[RSPRY1]] | -0.57 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PER2]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RELB]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TXNIP]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[HARBI1]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[LINS1]] | -0.51 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ZNF136]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[EP300]] | -0.49 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKG]] | B | DGKG activity lowers CHORDC1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.38× higher at baseline in the lines without DGKG | 0.081 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSP90AA1]] | C | CHORDC1's natural level strengthens HSP90AA1's drug response | CHORDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.13; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HSP90AB1]] | C | CHORDC1's natural level strengthens HSP90AB1's drug response | CHORDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.06; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.5, -11.3); signed map (-26.2, -29.1). **Vector** length 84.0, 29.8% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Attenuation phase* (reactome, mean cos +0.52 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.51 to 14); *Cellular response to heat stress* (reactome, mean cos +0.50 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.5 | +23.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.1 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +15.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.2 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +18.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +0.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.8 | +6.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.8 | +10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.2 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.6 | +6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +6.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cysteine and histidine rich domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.3 — chr11:90,200,429-90,223,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHP1, CHP-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHD1](https://www.uniprot.org/uniprotkb/Q9UHD1) (Cysteine and histidine-rich domain-containing protein 1):

> Regulates centrosome duplication, probably by inhibiting the kinase activity of ROCK2. Proposed to act as co-chaperone for HSP90. May play a role in the regulation of NOD1 via a HSP90 chaperone complex. In vitro, has intrinsic chaperone activity. This function may be achieved by inhibiting association of ROCK2 with NPM1. Plays a role in ensuring the localization of the tyrosine kinase receptor EGFR to the plasma membrane, and thus ensures the subsequent regulation of EGFR activity and …

**Summary**, from NCBI Gene [26973](https://www.ncbi.nlm.nih.gov/gene/26973):

> Enables Hsp90 protein binding activity. Predicted to be involved in several processes, including centrosome duplication; obsolete negative regulation of Rho-dependent protein serine/threonine kinase activity; and regulation of cellular response to heat. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14525) · Entrez [26973](https://www.ncbi.nlm.nih.gov/gene/26973) · UniProt [Q9UHD1](https://www.uniprot.org/uniprotkb/Q9UHD1) · Ensembl [ENSG00000110172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110172)

## Data

Gene col 3121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3121); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3121]; `tensor/DDL_lfc|DDL_z.npy` [3121]; `embed/gene_vectors.npy` [3121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3121 or target_col == 3121). Every well: [[CHORDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHORDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
