---
symbol: "CYP2R1"
type: "gene"
col: 11777
ensembl_id: "ENSG00000186104"
name: "cytochrome P450 family 2 subfamily R member 1"
location: "11p15.2"
module: 63
arm: "+"
pooled_cpm: 14.01
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CYP2R1

*cytochrome P450 family 2 subfamily R member 1* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +9.0, q 2e-16, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.257× (z -18.2, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF222]] (+0.52, fdr 1e-05), [[TRIB3]] (+0.51, fdr 1e-04), [[HKDC1]] (+0.51, fdr 3e-05); moves opposite to [[SMIM4]] (-0.46, fdr 6e-04), [[CDK2AP1]] (-0.42, fdr 2e-04), [[SLC5A3]] (-0.42, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[KCTD21]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +9.0 | 2e-16 | 31/44 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +8.9 | 2e-16 | 35/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.3 | 3e-14 | 31/44 (SW1417, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +7.5 | 9e-12 | 27/44 (hTERT-HPNE, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 3e-09 | 24/42 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.1 | 8e-08 | 23/44 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 22/43 (LS 180, H4, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +4.6 | 3e-04 | 15/44 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.2 | 0.002 | 10/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.003 | 16/42 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.006 | 7/42 (hTERT-HPNE, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +3.3 | 0.043 | 7/44 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.046 | 6/43 (PANC-1, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.088 | 7/43 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.088 | 8/43 (SK-MEL-2, NCI-H23, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.257×** | -18.2 | 0e+00 | 40/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.305×** | -15.9 | 0e+00 | 35/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.336×** | -13.1 | 5e-37 | 38/44 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.384×** | -11.5 | 2e-28 | 39/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.577×** | -6.0 | 3e-07 | 21/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.653×** | -5.7 | 1e-06 | 26/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -5.1 | 2e-05 | 19/43 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -5.1 | 2e-05 | 21/40 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -4.9 | 5e-05 | 19/43 (RPMI-7951, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -4.9 | 5e-05 | 22/42 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.731×** | -3.9 | 0.005 | 14/28 (SW480, LS 180, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.744×** | -3.8 | 0.007 | 13/24 (SNU-423, SW480, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.609×** | -3.5 | 0.022 | 11/22 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0499× (z -28.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0917× (z -22.8) |
| [[SW480 (line)]] | alt | 18.9 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -16.3) |
| [[H4 (line)]] | wt | 26.4 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0829× (z -11.0) |
| [[KATO III (line)]] | alt | 24.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.106× (z -12.0) |
| [[J82 (line)]] | alt | 11.6 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0863× (z -12.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -9.1) |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0706× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -8.8) |
| [[HT-29 (line)]] | alt | 30.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -13.8) |
| [[LoVo (line)]] | wt | 13.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0697× (z -14.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -10.5) |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0464× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -10.1) |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -9.4) |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.134× (z -9.1) |
| [[A-427 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.59 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0448× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0474× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0952× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0790× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF222]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.51 | +0.33 / +0.40 | both halves | 1e-04 |  |
| [[HKDC1]] | +0.51 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ADM2]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ARHGEF2]] | +0.49 | +0.21 / +0.39 | both halves | 7e-04 |  |
| [[LINC01012]] | +0.48 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ZNF697]] | +0.47 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[PYROXD1]] | +0.46 | +0.39 / +0.28 | both halves | 3e-04 |  |
| [[EIF2S2]] | +0.45 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[TBC1D25]] | +0.45 | +0.11 / +0.42 | ⚠ not reproduced | 0.002 |  |
| [[NIBAN1]] | +0.44 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[EML5]] | +0.44 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CHAC1]] | +0.44 | +0.31 / +0.43 | both halves | 2e-04 | pathway: Biological oxidations |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM4]] | -0.46 | -0.22 / -0.25 | both halves | 6e-04 |  |
| [[CDK2AP1]] | -0.42 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[SLC5A3]] | -0.42 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[NUP133]] | -0.42 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[BMPR2]] | -0.41 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[LDB1]] | -0.40 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[IFI30]] | -0.39 | -0.29 / -0.25 | both halves | 4e-04 |  |
| [[ANKRD42]] | -0.39 | -0.17 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[GTF2I]] | -0.38 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[ARID1B]] | -0.37 | -0.19 / -0.36 | ⚠ not reproduced | 8e-04 |  |
| [[CD164]] | -0.37 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[GRK2]] | -0.37 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD21]] | C | CYP2R1 activity lowers KCTD21's level | lines that do not express CYP2R1 (3) vs lines expressing it (47) | 1.74× higher at baseline in the lines without CYP2R1 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: PIM2, CDCA7, NMRAL1; maybe low, not absent |
| [[MSL3P1]] | C | CYP2R1 activity raises MSL3P1's level | lines that do not express CYP2R1 (3) vs lines expressing it (47) | 3.47× lower at baseline in the lines without CYP2R1 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: PIM2, CDCA7, NMRAL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, 50.1); signed map (-11.6, 26.1). **Vector** length 55.3, 8.68% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +6.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.7 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.0 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -2.8 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 2 subfamily R member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:14,877,440-14,892,231 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome P450 family 2 |
| Reactome | 9 pathways, smallest: Vitamins; Vitamin D (calciferol) metabolism; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6VVX0](https://www.uniprot.org/uniprotkb/Q6VVX0) (Vitamin D 25-hydroxylase):

> A cytochrome P450 monooxygenase involved in activation of vitamin D precursors. Catalyzes hydroxylation at C-25 of both forms of vitamin D, vitamin D(2) and D(3) (calciol). Can metabolize vitamin D analogs/prodrugs 1alpha-hydroxyvitamin D(2) (doxercalciferol) and 1alpha-hydroxyvitamin D(3) (alfacalcidol) forming 25-hydroxy derivatives. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by …

**Summary**, from NCBI Gene [120227](https://www.ncbi.nlm.nih.gov/gene/120227):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This enzyme is a microsomal vitamin D hydroxylase that converts vitamin D into the active ligand for the vitamin D receptor. A mutation in this gene has been associated with selective 25-hydroxyvitamin D deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20580) · Entrez [120227](https://www.ncbi.nlm.nih.gov/gene/120227) · UniProt [Q6VVX0](https://www.uniprot.org/uniprotkb/Q6VVX0) · Ensembl [ENSG00000186104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186104)

## Data

Gene col 11777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11777); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11777]; `tensor/DDL_lfc|DDL_z.npy` [11777]; `embed/gene_vectors.npy` [11777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11777 or target_col == 11777). Every well: [[CYP2R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
