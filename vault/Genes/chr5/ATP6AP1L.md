---
symbol: "ATP6AP1L"
type: "gene"
col: 12980
ensembl_id: "ENSG00000205464"
name: "ATPase H+ transporting accessory protein 1 like (pseudogene)"
location: "5q14.2"
module: 10
arm: "+"
pooled_cpm: 23.2
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 36
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ATP6AP1L

*ATPase H+ transporting accessory protein 1 like (pseudogene)* — 5q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.45× (z +6.5, q 5e-08, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~72% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.38× (z +4.0, q 0.019, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.207× (z -19.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSIP2-AS1]] (+0.66, fdr 7e-06), [[UBA6-DT]] (+0.54, fdr 7e-06), [[SUMF1]] (+0.53, fdr 3e-05); moves opposite to [[ARHGEF26]] (-0.46, fdr 1e-04), [[TLCD4]] (-0.42, fdr 1e-04), [[INTS8]] (-0.40, fdr 4e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GDAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.45×** | +6.5 | 5e-08 | 24/48 (AsPC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.019 | 18/47 (PANC-1, COLO 205, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.021 | 18/47 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.021 | 18/48 (HOP62, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.053 | 14/47 (LoVo, C-33 A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.061 | 13/48 (SW1417, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.061 | 18/47 (HEC-1-A, SW 900, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.061 | 13/47 (A-427, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +3.3 | 0.061 | 14/48 (SW1417, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.065 | 13/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.2 | 0.065 | 3/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.092 | 9/48 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.59× | +3.0 | 0.11 | 7/48 (NCI-H2347, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.207×** | -19.5 | 0e+00 | 48/48 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.226×** | -18.4 | 0e+00 | 45/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.258×** | -16.8 | 0e+00 | 45/48 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.330×** | -13.7 | 1e-40 | 44/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.499×** | -12.2 | 5e-32 | 35/47 (SNU-423, HepG2/C3A, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.391×** | -11.6 | 3e-29 | 41/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.383×** | -11.4 | 3e-28 | 38/48 (SW 900, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.434×** | -9.9 | 2e-21 | 36/45 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -7.6 | 3e-12 | 36/48 (HOP62, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -6.7 | 1e-09 | 34/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -6.6 | 2e-09 | 29/45 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.579×** | -6.4 | 8e-09 | 33/47 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.515×** | -6.2 | 2e-08 | 27/48 (PANC-1, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.412×** | -5.7 | 4e-07 | 28/46 (HEC-1-A, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.553×** | -5.6 | 1e-06 | 28/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.656×** | -5.2 | 7e-06 | 27/48 (HCT15, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -4.4 | 3e-04 | 23/47 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.777×** | -4.4 | 3e-04 | 19/48 (MIA PaCa-2, SW 1088, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.019 | 19/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.019 | 19/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.035 | 11/48 (RKO, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.042 | 16/47 (NCI-H460, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -15.6) |
| [[LoVo (line)]] | wt | 42.8 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0145× (z -39.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.173× (z -16.5) |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0520× (z -17.6) |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0912× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0861× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.188× (z -10.0) |
| [[A-427 (line)]] | wt | 13.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0892× (z -13.3) |
| [[HCT15 (line)]] | alt | 51.0 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -12.3) |
| [[HOP62 (line)]] | alt | 23.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.104× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 44.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0812× (z -17.4) |
| [[H4 (line)]] | wt | 26.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0565× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 87.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0404× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0639× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -12.2) |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 4 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0648× (z -13.9) ⚠ transcription drop; cell-cycle shift, explains ~89% of this change |
| [[A-172 (line)]] | wt | 22.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0918× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 30.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -11.5) |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0921× (z -14.1) |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0823× (z -13.0) |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0485× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -12.2) |
| [[SNU-423 (line)]] | alt | 47.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW480 (line)]] | alt | 36.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -10.8) ⚠ toxic |
| [[A549 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[C-33 A (line)]] | alt | 41.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.233× (z -9.0) |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0438× (z -11.9) |
| [[Hs 766T (line)]] | wt | 9.27 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0897× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~89% of this change |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0707× (z -10.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -9.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.198× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -9.5) |
| [[RKO (line)]] | wt | 14.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.167× (z -8.9) |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.229× (z -8.5) |
| [[A498 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSIP2-AS1]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[UBA6-DT]] | +0.54 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SUMF1]] | +0.53 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[LRGUK]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[KLHDC1]] | +0.52 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZNF717]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[FGGY]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TMEM232]] | +0.49 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[MFSD4B]] | +0.49 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[FAM172A]] | +0.48 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[MTERF1]] | +0.48 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[LINC02340]] | +0.48 | +0.54 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF26]] | -0.46 | -0.48 / -0.32 | both halves | 1e-04 |  |
| [[TLCD4]] | -0.42 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[INTS8]] | -0.40 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[FGD1]] | -0.40 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[EMSY]] | -0.40 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZYG11A]] | -0.40 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[ABHD3]] | -0.40 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[IFI27L1]] | -0.39 | -0.50 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDAP1]] | B | GDAP1 activity raises ATP6AP1L's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without GDAP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (12.9, 14.9); signed map (34.8, -12.7). **Vector** length 67.0, 14.2% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.8 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.2 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.4 | -6.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.5 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting accessory protein 1 like (pseudogene) |
| Locus type | pseudogene |
| Location | 5q14.2 — chr5:82,295,449-82,318,300 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ATP6AP1LP |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [Q52LC2](https://www.uniprot.org/uniprotkb/Q52LC2) carries no function annotation.

**Summary**, from NCBI Gene [92270](https://www.ncbi.nlm.nih.gov/gene/92270):

> Predicted to be located in bounding membrane of organelle; cytoplasmic vesicle membrane; and endomembrane system. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28091) · Entrez [92270](https://www.ncbi.nlm.nih.gov/gene/92270) · UniProt [Q52LC2](https://www.uniprot.org/uniprotkb/Q52LC2) · Ensembl [ENSG00000205464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205464)

## Data

Gene col 12980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12980); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12980]; `tensor/DDL_lfc|DDL_z.npy` [12980]; `embed/gene_vectors.npy` [12980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12980 or target_col == 12980). Every well: [[ATP6AP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6AP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
