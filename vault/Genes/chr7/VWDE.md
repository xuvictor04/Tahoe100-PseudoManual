---
symbol: "VWDE"
type: "gene"
col: 7101
ensembl_id: "ENSG00000146530"
name: "von Willebrand factor D and EGF domains"
location: "7p21.3"
module: 17
arm: "+"
pooled_cpm: 36.47
n_lines_expressing: 28
n_dd_up: 4
n_dd_down: 36
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# VWDE

*von Willebrand factor D and EGF domains* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +9.4, q 5e-18, up in 19 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.308× (z -17.8, q 0e+00, down in 23 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.440× (z -17.6, q 0e+00, down in 23 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRRS1]] (+0.59, fdr 1e-05), [[SFMBT2]] (+0.57, fdr 1e-05), [[WDR17]] (+0.55, fdr 1e-04); moves opposite to [[QRICH2]] (-0.55, fdr 4e-05), [[ZFTRAF1]] (-0.50, fdr 5e-05), [[SLC26A7]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 3 go from it, the strongest it → [[SFMBT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.4 | 5e-18 | 19/26 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +8.8 | 4e-16 | 22/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +4.8 | 4e-04 | 14/27 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.019 | 11/26 (LoVo, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.28 | 5/27 (A549, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.308×** | -17.8 | 0e+00 | 23/26 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -17.6 | 0e+00 | 23/25 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.406×** | -13.7 | 3e-40 | 23/26 (SW480, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.447×** | -11.7 | 1e-29 | 19/22 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.488×** | -10.0 | 1e-21 | 18/23 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.548×** | -9.1 | 8e-18 | 18/26 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.577×** | -8.3 | 8e-15 | 21/25 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -8.3 | 1e-14 | 23/25 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -8.1 | 2e-14 | 20/26 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.695×** | -7.7 | 5e-13 | 20/26 (A498, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.602×** | -7.7 | 9e-13 | 20/26 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -7.5 | 4e-12 | 18/26 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.708×** | -7.4 | 8e-12 | 16/26 (NCI-H1792, H4, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -7.0 | 8e-11 | 21/27 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.652×** | -6.5 | 4e-09 | 17/26 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -5.9 | 1e-07 | 20/26 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.482×** | -5.8 | 2e-07 | 15/27 (HCT15, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.684×** | -5.4 | 2e-06 | 18/26 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.702×** | -5.1 | 8e-06 | 16/26 (NCI-H1792, J82, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.651×** | -4.3 | 4e-04 | 12/25 (NCI-H1792, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.772×** | -3.9 | 0.002 | 13/26 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.780×** | -3.6 | 0.007 | 12/26 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -3.1 | 0.039 | 4/25 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 77.6 | 0 | 13 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 123 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0712× (z -32.7) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.7) |
| [[SW480 (line)]] | alt | 89.3 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0642× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.168× (z -19.1) |
| [[A498 (line)]] | wt | 57.8 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -18.2) |
| [[SW 900 (line)]] | alt | 72.4 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 25.4 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.177× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -12.1) |
| [[H4 (line)]] | wt | 47.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -20.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -12.7) |
| [[A549 (line)]] | wt | 28.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.7) |
| [[HCT15 (line)]] | alt | 86.1 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.137× (z -14.3) |
| [[LoVo (line)]] | wt | 55.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -8.8) |
| [[J82 (line)]] | alt | 34.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 86.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.8) |
| [[LS 180 (line)]] | wt | 42.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 53.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -12.2) |
| [[SHP-77 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.390× (z -8.6) |
| [[A-427 (line)]] | wt | 61.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.519× (z -8.5) |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 36.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 49.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.131× (z -16.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.307× (z -8.6) |
| [[A-172 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRRS1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SFMBT2]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[WDR17]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[MRPS31P4]] | +0.53 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[ZC4H2]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[L2HGDH]] | +0.52 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[RADX]] | +0.51 | +0.26 / +0.50 | both halves | 4e-04 |  |
| [[ATG4C]] | +0.50 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[POT1]] | +0.50 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[BCHE]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CSRNP3]] | +0.49 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[FBXO16]] | +0.49 | +0.33 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH2]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ZFTRAF1]] | -0.50 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SLC26A7]] | -0.50 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[CPEB2-DT]] | -0.49 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[ATXN7L3-AS1]] | -0.49 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[LINC00393]] | -0.48 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[ATXN1L]] | -0.48 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[WDR45]] | -0.47 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[PHF2]] | -0.47 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[MCF2]] | -0.47 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[AVEN]] | -0.47 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[MYLK4]] | -0.47 | -0.37 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers VWDE's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TOP2A]] | B | TOP2A activity raises VWDE's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASAL1]] | B | RASAL1 activity raises VWDE's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.84× lower at baseline in the lines without RASAL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFMBT2]] | B | VWDE activity raises SFMBT2's level | lines that do not express VWDE (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without VWDE | 0.021 | ⚠ within organs, on part of the lines; also absent: RBM11, L3MBTL4, RPS6KA6 |
| [[WDR17]] | B | VWDE activity raises WDR17's level | lines that do not express VWDE (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without VWDE | 0.068 | ⚠ within organs, on part of the lines; also absent: RBM11, L3MBTL4, RPS6KA6 |
| [[FBXO16]] | B | VWDE activity raises FBXO16's level | lines that do not express VWDE (22) vs lines expressing it (28) | 1.64× lower at baseline in the lines without VWDE | 0.091 | ⚠ within organs, on part of the lines; also absent: RBM11, L3MBTL4, RPS6KA6 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (33.0, 30.5); signed map (39.0, 39.1). **Vector** length 79.6, 21.9% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.7 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.7 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | von Willebrand factor D and EGF domains |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:12,330,885-12,403,941 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14712 |
| Matched by | ensembl_id |

UniProt [Q8N2E2](https://www.uniprot.org/uniprotkb/Q8N2E2) carries no function annotation.

**Summary**, from NCBI Gene [221806](https://www.ncbi.nlm.nih.gov/gene/221806):

> Predicted to enable signaling receptor binding activity. Predicted to be active in cell surface and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21897) · Entrez [221806](https://www.ncbi.nlm.nih.gov/gene/221806) · UniProt [Q8N2E2](https://www.uniprot.org/uniprotkb/Q8N2E2) · Ensembl [ENSG00000146530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146530)

## Data

Gene col 7101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7101); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7101]; `tensor/DDL_lfc|DDL_z.npy` [7101]; `embed/gene_vectors.npy` [7101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7101 or target_col == 7101). Every well: [[VWDE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VWDE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
