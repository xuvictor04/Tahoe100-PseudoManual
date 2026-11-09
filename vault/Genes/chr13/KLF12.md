---
symbol: "KLF12"
type: "gene"
col: 4026
ensembl_id: "ENSG00000118922"
name: "KLF transcription factor 12"
location: "13q22.1"
module: 193
arm: "+"
pooled_cpm: 154.02
n_lines_expressing: 41
n_dd_up: 1
n_dd_down: 34
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# KLF12

*KLF transcription factor 12* — 13q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[BAY1125976 (drug)]] 5 µM: 1.72× (z +3.9, q 0.062, up in 27 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (SW1417 2.28×, LS 180 2.50×, NCI-H460 2.06×).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.386× (z -12.2, q 1e-31, down in 35 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.446× (z -11.0, q 7e-26, down in 34 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT3]] (+0.64, fdr 9e-06), [[STK10]] (+0.62, fdr 7e-06), [[MAMLD1]] (+0.57, fdr 1e-05); moves opposite to [[CWF19L1]] (-0.57, fdr 1e-05), [[PIGB]] (-0.56, fdr 1e-05), [[PICK1]] (-0.56, fdr 1e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[JAZF1]] → it (grade B ⚠); 6 go from it, the strongest it → [[LRRC8C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4026.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (SW1417 2.28×, LS 180 2.50×, NCI-H460 2.06×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.062 | 27/39 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.69 | 23/38 (SW48, C32, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.386×** | -12.2 | 1e-31 | 35/40 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -11.6 | 1e-28 | 34/36 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.446×** | -11.0 | 7e-26 | 34/39 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.443×** | -10.7 | 2e-24 | 37/38 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -9.6 | 1e-19 | 28/37 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.521×** | -8.9 | 6e-17 | 35/39 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -7.6 | 3e-12 | 37/39 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.592×** | -7.1 | 6e-11 | 33/39 (SW480, SNU-423, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.603×** | -6.9 | 3e-10 | 34/39 (PANC-1, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -6.4 | 8e-09 | 32/39 (SW480, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -6.3 | 1e-08 | 28/40 (A-172, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -6.2 | 3e-08 | 32/39 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -5.8 | 2e-07 | 27/39 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.660×** | -5.7 | 6e-07 | 29/39 (SW480, SNU-423, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.495×** | -5.0 | 2e-05 | 31/39 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -4.5 | 2e-04 | 24/39 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -4.2 | 9e-04 | 29/39 (LoVo, PANC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.563×** | -4.1 | 0.001 | 24/39 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.571×** | -4.0 | 0.002 | 28/39 (LoVo, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.574×** | -4.0 | 0.002 | 28/39 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.002 | 28/39 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.688×** | -3.6 | 0.007 | 23/39 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.718×** | -3.2 | 0.028 | 25/40 (A-172, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 393 | 0 | 14 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 295 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.302× (z -12.6) |
| [[PANC-1 (line)]] | alt | 121 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.361× (z -12.6) |
| [[A-172 (line)]] | wt | 186 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.172× (z -9.9) |
| [[Hs 766T (line)]] | wt | 240 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 82.7 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.354× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -14.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 319 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -10.7) |
| [[LoVo (line)]] | wt | 171 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.216× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 82.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -13.7) |
| [[A549 (line)]] | wt | 151 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 104 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.254× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 152 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.227× (z -15.2) |
| [[HS-578T (line)]] | alt | 231 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -11.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 310 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 68.9 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.50× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 209 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0789× (z -13.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -10.2) |
| [[A-427 (line)]] | wt | 180 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -14.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 301 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 84.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -13.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.399× (z -8.6) |
| [[HOP62 (line)]] | alt | 245 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.141× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.234× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -9.8) |
| [[SW 1271 (line)]] | alt | 261 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.215× (z -9.5) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 65.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.06× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.354× (z -9.5) ⚠ toxic |
| [[SW48 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 267 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT3]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[STK10]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MAMLD1]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PEAK1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CALM2]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[JAZF1]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 | same gene group |
| [[TIAM1]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[EPHB2]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CALM1]] | +0.53 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RAPGEF2]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWF19L1]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PIGB]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[PICK1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[METTL22]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[PAAF1]] | -0.54 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[CIAO3]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[DYNC2LI1]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ACOX3]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[APTX]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 | same gene group |
| [[MTO1]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[TMEM94]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TRMU]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAZF1]] | B | JAZF1 activity raises KLF12's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 3.06× lower at baseline in the lines without JAZF1 | 0.012 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[RASGRF2]] | B | RASGRF2 activity raises KLF12's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 1.77× lower at baseline in the lines without RASGRF2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[MAMLD1]] | B | MAMLD1 activity raises KLF12's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without MAMLD1 | 0.014 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[CD59]] | B | CD59 activity raises KLF12's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.94× lower at baseline in the lines without CD59 | 0.029 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[LRRC8C]] | B | LRRC8C activity raises KLF12's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.15× lower at baseline in the lines without LRRC8C | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[TGFB1]] | B | TGFB1 activity raises KLF12's level | lines that do not express TGFB1 (8) vs lines expressing it (42) | 2.94× lower at baseline in the lines without TGFB1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ZDHHC2, NUAK1, SLC22A4; maybe low, not absent |
| [[PRKCA]] | B | PRKCA activity raises KLF12's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without PRKCA | 0.099 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[TSPAN5]] | C | TSPAN5 activity raises KLF12's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 4.10× lower at baseline in the lines without TSPAN5 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLF12; co-absent with the target |
| [[SYNJ2]] | C | SYNJ2 activity raises KLF12's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 5.20× lower at baseline in the lines without SYNJ2 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8C]] | B | KLF12 activity raises LRRC8C's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without KLF12 | 0.039 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[JAZF1]] | B | KLF12 activity raises JAZF1's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 1.94× lower at baseline in the lines without KLF12 | 0.040 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[RGS17]] | B | KLF12 activity raises RGS17's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 4.24× lower at baseline in the lines without KLF12 | 0.064 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[CALM1]] | B | KLF12 activity raises CALM1's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without KLF12 | 0.074 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[CD59]] | B | KLF12 activity raises CD59's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without KLF12 | 0.079 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[TSPAN5]] | C | KLF12 activity raises TSPAN5's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 3.37× lower at baseline in the lines without KLF12 | 0.014 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, -1.4); signed map (-1.1, 34.3). **Vector** length 117, 40.4% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.1 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.1 | -8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -11.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -6.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.1 — chr13:73,686,089-74,134,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AP-2rep, HSPC122, AP2REP |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4X4](https://www.uniprot.org/uniprotkb/Q9Y4X4) (Krueppel-like factor 12):

> Confers strong transcriptional repression to the AP-2-alpha gene. Binds to a regulatory element (A32) in the AP-2-alpha gene promoter.

**Summary**, from NCBI Gene [11278](https://www.ncbi.nlm.nih.gov/gene/11278):

> Activator protein-2 alpha (AP-2 alpha) is a developmentally-regulated transcription factor and important regulator of gene expression during vertebrate development and carcinogenesis. The protein encoded by this gene is a member of the Kruppel-like zinc finger protein family and can repress expression of the AP-2 alpha gene by binding to a specific site in the AP-2 alpha gene promoter. Repression by the encoded protein requires binding with a corepressor, CtBP1. Two transcript variants encoding …

**Accessions** — [HGNC:6346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6346) · Entrez [11278](https://www.ncbi.nlm.nih.gov/gene/11278) · UniProt [Q9Y4X4](https://www.uniprot.org/uniprotkb/Q9Y4X4) · Ensembl [ENSG00000118922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118922)

## Data

Gene col 4026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4026); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4026]; `tensor/DDL_lfc|DDL_z.npy` [4026]; `embed/gene_vectors.npy` [4026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4026 or target_col == 4026). Every well: [[KLF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
