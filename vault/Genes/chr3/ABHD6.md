---
symbol: "ABHD6"
type: "gene"
col: 8754
ensembl_id: "ENSG00000163686"
name: "abhydrolase domain containing 6, acylglycerol lipase"
location: "3p14.3"
module: 10
arm: "-"
pooled_cpm: 10.13
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ABHD6

*abhydrolase domain containing 6, acylglycerol lipase* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.89× (z +18.4, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.478× (z -18.1, q 0e+00, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.66, fdr 1e-05), [[GNA12]] (+0.66, fdr 2e-05), [[LPCAT4]] (+0.65, fdr 1e-05); moves opposite to [[METTL6]] (-0.66, fdr 5e-05), [[EFCAB6]] (-0.66, fdr 2e-05), [[PBLD]] (-0.66, fdr 2e-05).
> It sits in the **-** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.89×** | +18.4 | 0e+00 | 41/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.88×** | +18.3 | 0e+00 | 43/46 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +17.1 | 0e+00 | 40/47 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +16.5 | 0e+00 | 42/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.47×** | +15.6 | 0e+00 | 42/47 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.17×** | +10.4 | 2e-23 | 35/46 (HEC-1-A, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.82×** | +10.3 | 4e-23 | 27/42 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +10.2 | 9e-23 | 30/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +9.1 | 5e-18 | 19/37 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.52×** | +7.2 | 3e-11 | 22/46 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.9 | 5e-05 | 12/47 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 6/44 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 7e-04 | 7/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 6/47 (SW 900, HCT15, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 4/47 (A-172, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 6/46 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.006 | 1/46 (HEC-1-A) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.478×** | -18.1 | 0e+00 | 32/43 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.421×** | -14.4 | 8e-45 | 31/45 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -8.0 | 3e-13 | 23/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.633×** | -7.9 | 3e-13 | 23/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.615×** | -7.8 | 5e-13 | 16/25 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -7.8 | 5e-13 | 18/38 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.684×** | -6.6 | 3e-09 | 19/32 (HS-578T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -5.6 | 2e-06 | 15/46 (HepG2/C3A, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.738×** | -5.3 | 9e-06 | 17/41 (LOX-IMVI, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 1e-05 | 14/45 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.617×** | -4.4 | 6e-04 | 19/46 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.3 | 8e-04 | 18/43 (SW1417, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.2 | 0.001 | 15/46 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.679×** | -3.5 | 0.018 | 8/17 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.820×** | -3.5 | 0.021 | 14/46 (RPMI-7951, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.833×** | -3.0 | 0.081 | 3/47 (SW480, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.6 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0764× (z -13.2) |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -20.0) |
| [[LoVo (line)]] | wt | 13.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -11.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.112× (z -11.9) |
| [[SW480 (line)]] | alt | 25.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 6.63 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -11.0) |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.6) |
| [[A498 (line)]] | wt | 5.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -13.8) |
| [[A549 (line)]] | wt | 5.02 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0242× (z -13.5) |
| [[C32 (line)]] | wt | 10.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.114× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0633× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0681× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0824× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -9.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 3.43 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.37× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 8.42 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.161× (z -8.9) |
| [[SW 900 (line)]] | alt | 8.67 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0760× (z -9.8) |
| [[A-172 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[GNA12]] | +0.66 | +0.56 / +0.47 | both halves | 2e-05 | pathway: Platelet activation, signaling and aggregation |
| [[LPCAT4]] | +0.65 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.63 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[MAST3]] | +0.63 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[RSAD1]] | +0.63 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[NR2C1]] | +0.62 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[MYPOP]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ANKS6]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ATRN]] | +0.61 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[BLVRA]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL6]] | -0.66 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[EFCAB6]] | -0.66 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PBLD]] | -0.66 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ATXN1L]] | -0.64 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.64 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.63 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.63 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PDCL3P4]] | -0.63 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[CCT6B]] | -0.63 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[PPP3CB-AS1]] | -0.63 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ARFGAP2]] | -0.62 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | -0.62 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.1, 5.7); signed map (-41.6, -5.6). **Vector** length 79.3, 14.9% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +16.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +10.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +15.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +18.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +17.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +10.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -18.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 6, acylglycerol lipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:58,237,532-58,295,693 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Abhydrolase domain containing; 2-arachidonoylglycerol hydrolases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 7 pathways, smallest: Arachidonate production from DAG; Effects of PIP2 hydrolysis; G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV23](https://www.uniprot.org/uniprotkb/Q9BV23) (Monoacylglycerol lipase ABHD6):

> Lipase that preferentially hydrolysis medium-chain saturated monoacylglycerols including 2-arachidonoylglycerol. Through 2-arachidonoylglycerol degradation may regulate endocannabinoid signaling pathways (By similarity). Also has a lysophosphatidyl lipase activity with a preference for lysophosphatidylglycerol among other lysophospholipids (By similarity). Also able to degrade bis(monoacylglycero)phosphate (BMP) and constitutes the major enzyme for BMP catabolism. BMP, also known as …

**Summary**, from NCBI Gene [57406](https://www.ncbi.nlm.nih.gov/gene/57406):

> Enables monoacylglycerol lipase activity. Involved in acylglycerol catabolic process. Predicted to be located in late endosome membrane and lysosomal membrane. Predicted to be part of AMPA glutamate receptor complex. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21398) · Entrez [57406](https://www.ncbi.nlm.nih.gov/gene/57406) · UniProt [Q9BV23](https://www.uniprot.org/uniprotkb/Q9BV23) · Ensembl [ENSG00000163686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163686)

## Data

Gene col 8754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8754); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8754]; `tensor/DDL_lfc|DDL_z.npy` [8754]; `embed/gene_vectors.npy` [8754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8754 or target_col == 8754). Every well: [[ABHD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
