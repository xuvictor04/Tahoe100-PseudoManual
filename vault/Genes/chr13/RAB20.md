---
symbol: "RAB20"
type: "gene"
col: 6348
ensembl_id: "ENSG00000139832"
name: "RAB20, member RAS oncogene family"
location: "13q34"
module: 164
arm: "+"
pooled_cpm: 28.85
n_lines_expressing: 42
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 23
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# RAB20

*RAB20, member RAS oncogene family* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 6.56× (z +13.1, q 3e-36, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.491× (z -13.3, q 2e-37, down in 31 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPC3]] (+0.70, fdr 1e-05), [[WDR45B]] (+0.68, fdr 1e-05), [[CNOT8]] (+0.67, fdr 7e-06); moves opposite to [[AVEN]] (-0.63, fdr 3e-05), [[ACYP2]] (-0.59, fdr 4e-05), [[PRDM11]] (-0.58, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CA9]] → it (grade B ⚠); 23 go from it, the strongest it → [[CHMP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.56×** | +13.1 | 3e-36 | 39/40 (SW480, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +4.6 | 8e-04 | 20/38 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.46×** | +4.6 | 8e-04 | 20/39 (J82, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +4.5 | 0.001 | 17/40 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.010 | 15/39 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.028 | 15/40 (COLO 205, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.031 | 12/40 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.30× | +3.2 | 0.10 | 10/39 (J82, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.0 | 0.16 | 8/40 (RKO, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.491×** | -13.3 | 2e-37 | 31/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.357×** | -12.3 | 2e-32 | 34/39 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.438×** | -10.9 | 2e-25 | 29/35 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -8.7 | 3e-16 | 28/37 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.507×** | -8.1 | 7e-14 | 27/37 (C32, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -7.6 | 2e-12 | 26/39 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -7.5 | 4e-12 | 22/29 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -6.6 | 3e-09 | 27/40 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.601×** | -6.2 | 3e-08 | 26/31 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.652×** | -5.6 | 1e-06 | 26/39 (NCI-H460, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -5.6 | 1e-06 | 21/40 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -4.5 | 3e-04 | 20/39 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -4.4 | 4e-04 | 17/39 (NCI-H460, KATO III, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.740×** | -4.0 | 0.003 | 15/40 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.010 | 19/40 (A-172, C32, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.738×** | -3.6 | 0.011 | 17/40 (CHP-212, SHP-77, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.017 | 15/39 (NCI-H460, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.776×** | -3.0 | 0.084 | 13/39 (A498, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.799×** | -2.9 | 0.095 | 16/39 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.0 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -29.2) |
| [[A498 (line)]] | wt | 59.0 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0941× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -13.6) |
| [[C32 (line)]] | wt | 53.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0530× (z -26.3) |
| [[HT-29 (line)]] | alt | 107 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.341× (z -10.8) |
| [[KATO III (line)]] | alt | 97.5 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -13.1) |
| [[COLO 205 (line)]] | alt | 52.8 | 2 | 2 | [[PH-797804 (drug)]] 5 µM 12.8× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 41.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.3) |
| [[SNU-423 (line)]] | alt | 27.0 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 21.5× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.100× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.5× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0907× (z -15.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -8.6) |
| [[LS 180 (line)]] | wt | 35.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.1) |
| [[SW480 (line)]] | alt | 49.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.42× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0804× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0879× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 13.5 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0787× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.159× (z -8.9) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.9) |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 26.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.2× (z +11.0) | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -9.0) |
| [[HOP62 (line)]] | alt | 21.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 36.2× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -9.1) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 36.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.57× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -8.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -10.1) |
| [[SW1417 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.9) |
| [[A-427 (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC3]] | +0.70 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.68 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ARL6]] | +0.67 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[HDHD5]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PDK3]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.64 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ATG4C]] | +0.64 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[HERC3]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHA2]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.63 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ACYP2]] | -0.59 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[PRDM11]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[BRPF3]] | -0.57 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[CHMP3]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PPP3CB-AS1]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | -0.56 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[FKRP]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NEK10]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ATXN10]] | -0.55 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[DESI1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[N4BP2]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | CA9 activity raises RAB20's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CA9 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[GLRX]] | B | GLRX activity raises RAB20's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without GLRX | 0.051 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[PPP1R3C]] | B | PPP1R3C activity raises RAB20's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.17× lower at baseline in the lines without PPP1R3C | 0.067 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[HDAC6]] | B | HDAC6 activity lowers RAB20's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MLLT3]] | B | MLLT3 activity raises RAB20's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without MLLT3 | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHMP3]] | B | RAB20 activity lowers CHMP3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.38× higher at baseline in the lines without RAB20 | 0.004 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[FAM13A]] | B | RAB20 activity raises FAM13A's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.69× lower at baseline in the lines without RAB20 | 0.011 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[WDR89]] | B | RAB20 activity lowers WDR89's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.72× higher at baseline in the lines without RAB20 | 0.013 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[HERC3]] | B | RAB20 activity raises HERC3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.27× lower at baseline in the lines without RAB20 | 0.014 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[LRRC57]] | B | RAB20 activity lowers LRRC57's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without RAB20 | 0.020 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[MSRB3]] | B | RAB20 activity lowers MSRB3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 5.49× higher at baseline in the lines without RAB20 | 0.022 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[INSIG2]] | B | RAB20 activity raises INSIG2's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without RAB20 | 0.032 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[NRN1]] | B | RAB20 activity raises NRN1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without RAB20 | 0.034 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[SPICE1]] | B | RAB20 activity strengthens SPICE1's drug response | lines that do not express RAB20 (8) vs lines expressing it (41) | the lines without RAB20 respond 0.82× as strongly (z diff +0.56); strongest at Homoharringtonine 5 µM: 0.87x vs 0.46x (z diff +4.4) | 0.034 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MXI1]] | B | RAB20 activity raises MXI1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without RAB20 | 0.034 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[PTPN21]] | B | RAB20 activity lowers PTPN21's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without RAB20 | 0.036 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[PFKFB4]] | B | RAB20 activity raises PFKFB4's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without RAB20 | 0.055 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -15.9); signed map (-36.4, 22.7). **Vector** length 116, 30.6% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +13.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.0 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -10.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB20, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,523,066-110,561,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20429 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX57](https://www.uniprot.org/uniprotkb/Q9NX57) (Ras-related protein Rab-20):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB20 plays a role in apical endocytosis/recycling. Plays a role in the maturation and acidification of …

**Summary**, from NCBI Gene [55647](https://www.ncbi.nlm.nih.gov/gene/55647):

> Predicted to enable GTPase activity. Involved in phagosome acidification and phagosome-lysosome fusion. Located in Golgi apparatus and phagocytic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18260) · Entrez [55647](https://www.ncbi.nlm.nih.gov/gene/55647) · UniProt [Q9NX57](https://www.uniprot.org/uniprotkb/Q9NX57) · Ensembl [ENSG00000139832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139832)

## Data

Gene col 6348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6348); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6348]; `tensor/DDL_lfc|DDL_z.npy` [6348]; `embed/gene_vectors.npy` [6348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6348 or target_col == 6348). Every well: [[RAB20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
