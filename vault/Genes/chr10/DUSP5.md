---
symbol: "DUSP5"
type: "gene"
col: 6137
ensembl_id: "ENSG00000138166"
name: "dual specificity phosphatase 5"
location: "10q25.2"
module: 141
arm: "+"
pooled_cpm: 100.56
n_lines_expressing: 43
n_dd_up: 13
n_dd_down: 41
n_dd_up_clean: 11
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 20
direction_downstream: 10
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# DUSP5

*dual specificity phosphatase 5* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.81× (z +7.3, q 1e-10, up in 28 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.11× (z +7.0, q 5e-10, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.397× (z -10.8, q 1e-24, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB1]] (+0.68, fdr 7e-06), [[PLK3]] (+0.68, fdr 7e-06), [[PLAUR]] (+0.68, fdr 7e-06); moves opposite to [[NNT]] (-0.61, fdr 2e-05), [[RAB11FIP2]] (-0.60, fdr 2e-05), [[PAIP1]] (-0.58, fdr 2e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[MICAL2]] → it (grade B ⚠); 10 go from it, the strongest it → [[SMOX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.3 | 1e-10 | 28/40 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.11×** | +7.0 | 5e-10 | 33/42 (Hs 766T, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.3 | 7e-08 | 27/41 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +4.9 | 1e-04 | 23/41 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +4.9 | 1e-04 | 21/41 (NCI-H2030, HCT15, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 5e-04 | 27/42 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.022 | 21/41 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.047 | 17/41 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.047 | 20/41 (NCI-H23, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.057 | 11/42 (A549, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +3.2 | 0.058 | 16/41 (NCI-H2030, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.11×** | +3.2 | 0.058 | 16/41 (CFPAC-1, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +3.1 | 0.076 | 16/40 (NCI-H2347, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.397×** | -10.8 | 1e-24 | 39/41 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -10.1 | 2e-21 | 28/34 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.454×** | -10.0 | 3e-21 | 35/41 (HCT15, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.576×** | -9.8 | 1e-20 | 36/41 (A549, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.490×** | -8.7 | 4e-16 | 36/40 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.455×** | -8.6 | 6e-16 | 35/43 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.614×** | -8.6 | 7e-16 | 36/41 (HepG2/C3A, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.578×** | -8.6 | 7e-16 | 36/41 (NCI-H1573, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.498×** | -8.5 | 1e-15 | 34/41 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.528×** | -8.1 | 3e-14 | 35/42 (LoVo, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.530×** | -8.0 | 5e-14 | 37/40 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.603×** | -7.8 | 3e-13 | 35/41 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.693×** | -6.5 | 3e-09 | 27/41 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.701×** | -6.2 | 3e-08 | 27/42 (SW480, SW48, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.0 | 1e-07 | 27/41 (Hs 766T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.597×** | -5.9 | 1e-07 | 31/42 (SK-MEL-2, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.627×** | -5.6 | 8e-07 | 27/41 (SW48, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 189 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 171 | 1 (1 ⚠) | 9 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.93× (z +9.1) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.0490× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.251× (z -11.6) |
| [[A549 (line)]] | wt | 330 | 2 (1 ⚠) | 6 (2 ⚠) | [[Harringtonine (drug)]] 0.05 µM 2.74× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -19.9) |
| [[HOP62 (line)]] | alt | 55.4 | 1 (1 ⚠) | 7 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.65× (z +8.8) ⚠ cell-cycle shift, explains ~72% of this change | [[Adagrasib (drug)]] 0.05 µM 0.503× (z -16.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.342× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 8 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.493× (z -16.2) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.136× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 1 (1 ⚠) | 7 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.01× (z +8.8) ⚠ toxic | [[Cobimetinib (drug)]] 0.5 µM 0.167× (z -11.7) |
| [[SW480 (line)]] | alt | 59.1 | 0 | 8 | — | [[Trametinib (drug)]] 0.05 µM 0.281× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 240 | 1 (1 ⚠) | 6 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.68× (z +8.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.187× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 146 | 0 | 7 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.543× (z -16.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.5) |
| [[Hs 766T (line)]] | wt | 211 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 19.0× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.0) |
| [[RKO (line)]] | wt | 60.8 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.214× (z -10.4) |
| [[SW 900 (line)]] | alt | 209 | 1 (1 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.38× (z +9.3) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.0747× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 216 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.8) |
| [[A498 (line)]] | wt | 136 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.1) |
| [[HCT15 (line)]] | alt | 72.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.9) |
| [[PANC-1 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 130 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.66× (z +9.1) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 149 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.227× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 97.5 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.63× (z +11.4) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 69.1 | 0 | 2 | — | [[Radotinib (drug)]] 5 µM 0.385× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.08× (z +10.0) | [[Adagrasib (drug)]] 0.05 µM 0.510× (z -12.8) ⚠ position not correctable |
| [[SNU-423 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 50.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.5) |
| [[C32 (line)]] | wt | 57.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.176× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 1 | — | [[Trametinib (drug)]] 0.05 µM 0.206× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 75.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.617× (z -10.2) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 207 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -8.6) |
| [[SW1417 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB1]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 436 |
| [[PLK3]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 | STRING 568 |
| [[PLAUR]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[DUSP6]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_COMPLEMENT |
| [[SHB]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RDH13]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[MAP2K3]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EGR2]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 421 |
| [[EHD1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[EGR3]] | +0.65 | +0.58 / +0.68 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 447 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.61 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PAIP1]] | -0.58 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[PHC3]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CDC23]] | -0.56 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[VBP1]] | -0.56 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ZFR]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[C5orf15]] | -0.55 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICAL2]] | B | MICAL2 activity raises DUSP5's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without MICAL2 | 0.022 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[FAM107B]] | B | FAM107B activity raises DUSP5's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.11× lower at baseline in the lines without FAM107B | 0.024 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[MYO1E]] | B | MYO1E activity raises DUSP5's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without MYO1E | 0.024 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity raises DUSP5's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.87× lower at baseline in the lines without WNT7B | 0.025 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[MAP2K1]] | B | MAP2K1 activity raises DUSP5's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[TOR4A]] | B | TOR4A activity raises DUSP5's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without TOR4A | 0.031 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[SERPINB1]] | B | SERPINB1 activity raises DUSP5's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without SERPINB1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[ST3GAL1]] | B | ST3GAL1 activity raises DUSP5's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without ST3GAL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[TSPAN5]] | B | TSPAN5 activity raises DUSP5's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.32× lower at baseline in the lines without TSPAN5 | 0.037 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[RGS17]] | B | RGS17 activity raises DUSP5's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without RGS17 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[ADRB2]] | B | ADRB2 activity raises DUSP5's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without ADRB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |
| [[SMOX]] | B | SMOX activity raises DUSP5's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.19× lower at baseline in the lines without SMOX | 0.048 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMOX]] | B | DUSP5 activity raises SMOX's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without DUSP5 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[STX1A]] | B | DUSP5 activity raises STX1A's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without DUSP5 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[STK17A]] | B | DUSP5 activity raises STK17A's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without DUSP5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[PHC2]] | B | DUSP5 activity raises PHC2's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.36× lower at baseline in the lines without DUSP5 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[BCAN-AS1]] | B | DUSP5 activity raises BCAN-AS1's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.39× lower at baseline in the lines without DUSP5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[ITPRIP]] | B | DUSP5 activity raises ITPRIP's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.79× lower at baseline in the lines without DUSP5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[TIMP1]] | B | DUSP5 activity raises TIMP1's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.66× lower at baseline in the lines without DUSP5 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[DOCK4]] | B | DUSP5 activity raises DOCK4's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 3.32× lower at baseline in the lines without DUSP5 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | DUSP5 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DUSP5 (7) vs lines expressing it (41) | the lines without DUSP5: 1.22× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[SHB]] | C | DUSP5 activity raises SHB's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without DUSP5 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.3, 2.7); signed map (2.7, 44.4). **Vector** length 140, 45.5% of its response variance represented; |z| ≥ 3 in 1,379 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.7 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.3 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.9 | +4.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.0 | -9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.8 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -10.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.7 | -8.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.5 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.4 | -8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.3 | -10.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.2 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,497,907-110,511,533 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HVH3 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Hallmark sets | COMPLEMENT, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: RAF-independent MAPK1/3 activation; Negative regulation of MAPK pathway; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16690](https://www.uniprot.org/uniprotkb/Q16690) (Dual specificity protein phosphatase 5):

> Dual specificity protein phosphatase; active with phosphotyrosine, phosphoserine and phosphothreonine residues. The highest relative activity is toward ERK1.

**Summary**, from NCBI Gene [1847](https://www.ncbi.nlm.nih.gov/gene/1847):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3071) · Entrez [1847](https://www.ncbi.nlm.nih.gov/gene/1847) · UniProt [Q16690](https://www.uniprot.org/uniprotkb/Q16690) · Ensembl [ENSG00000138166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138166)

## Data

Gene col 6137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6137); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6137]; `tensor/DDL_lfc|DDL_z.npy` [6137]; `embed/gene_vectors.npy` [6137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6137 or target_col == 6137). Every well: [[DUSP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
