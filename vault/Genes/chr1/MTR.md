---
symbol: "MTR"
type: "gene"
col: 3861
ensembl_id: "ENSG00000116984"
name: "5-methyltetrahydrofolate-homocysteine methyltransferase"
location: "1q43"
module: 148
arm: "+"
pooled_cpm: 152.07
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# MTR

*5-methyltetrahydrofolate-homocysteine methyltransferase* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +10.4, q 2e-22, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.572× (z -11.5, q 8e-28, down in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.391× (z -10.5, q 2e-23, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT5]] (+0.60, fdr 1e-05), [[DMTF1]] (+0.58, fdr 1e-05), [[SERPINB6]] (+0.58, fdr 3e-05); moves opposite to [[LMTK2]] (-0.58, fdr 1e-05), [[HDHD3]] (-0.56, fdr 1e-05), [[TBC1D7]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +10.4 | 2e-22 | 35/49 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +7.7 | 5e-12 | 26/48 (SW48, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.2 | 1e-07 | 33/50 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.004 | 27/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.007 | 21/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.025 | 18/48 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -11.5 | 8e-28 | 36/47 (HepG2/C3A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -10.5 | 2e-23 | 45/49 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -9.6 | 2e-19 | 43/48 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -9.5 | 4e-19 | 43/48 (J82, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -9.4 | 6e-19 | 38/47 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.677×** | -8.3 | 7e-15 | 36/48 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.679×** | -7.8 | 4e-13 | 41/48 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.697×** | -7.7 | 8e-13 | 34/48 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -7.7 | 1e-12 | 35/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.710×** | -7.3 | 1e-11 | 36/48 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.527×** | -7.2 | 4e-11 | 38/48 (MIA PaCa-2, SNU-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.719×** | -7.1 | 8e-11 | 33/48 (HOP62, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.723×** | -6.9 | 2e-10 | 31/48 (SNU-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.9 | 1e-07 | 25/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.776×** | -5.4 | 2e-06 | 31/48 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.789×** | -5.0 | 2e-05 | 35/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.819×** | -4.2 | 6e-04 | 24/48 (C-33 A, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.816×** | -4.1 | 0.001 | 24/47 (HEC-1-A, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.828×** | -4.0 | 0.001 | 25/49 (Hs 766T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 291 | 9 (7 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +23.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -9.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.532× (z -9.7) |
| [[C32 (line)]] | wt | 208 | 0 | 13 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -14.9) |
| [[SNU-1 (line)]] | wt | 159 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -12.1) |
| [[SW480 (line)]] | alt | 127 | 11 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +23.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.610× (z -9.5) |
| [[HOP62 (line)]] | alt | 200 | 0 | 11 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -14.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.552× (z -11.8) |
| [[J82 (line)]] | alt | 151 | 0 | 8 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.404× (z -12.3) |
| [[A-172 (line)]] | wt | 297 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.383× (z -11.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 217 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.420× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 174 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.446× (z -10.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.462× (z -10.6) |
| [[SNU-423 (line)]] | alt | 197 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 126 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.253× (z -15.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 234 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.5) | [[TAK-901 (drug)]] 5 µM 0.194× (z -11.0) |
| [[PANC-1 (line)]] | alt | 172 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.445× (z -13.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.261× (z -12.0) |
| [[A549 (line)]] | wt | 147 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.277× (z -9.0) |
| [[C-33 A (line)]] | alt | 165 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -14.5) |
| [[HCT15 (line)]] | alt | 174 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.391× (z -9.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.418× (z -9.1) |
| [[LS 180 (line)]] | wt | 91.5 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.391× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 113 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.483× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.270× (z -9.5) |
| [[SW48 (line)]] | wt | 142 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +26.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.356× (z -9.9) |
| [[HS-578T (line)]] | alt | 92.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +13.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.460× (z -8.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.305× (z -14.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 72.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 147 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.474× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 143 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -8.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.130× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 62.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +18.6) | — |
| [[BT-474 (line)]] | alt | 92.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +14.4) | [[TAK-901 (drug)]] 0.05 µM 0.379× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 107 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.9) | [[Ixazomib citrate (drug)]] 5 µM 0.505× (z -8.6) |
| [[COLO 205 (line)]] | alt | 78.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 167 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.488× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 55.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +16.9) | — |
| [[RKO (line)]] | wt | 142 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.442× (z -10.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 77.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.5) | — |
| [[A-427 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 155 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.333× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 186 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.441× (z -8.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 54.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[LoVo (line)]] | wt | 108 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.497× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 286 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.3) | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT5]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DMTF1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SERPINB6]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MRPL30]] | +0.58 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[NEMP1]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[UBE3B]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SLC30A9]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MCPH1-AS1]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[CBR4]] | +0.53 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[DIPK2A]] | +0.53 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ANKRD26]] | +0.53 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[UBR5]] | +0.52 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK2]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[HDHD3]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TBC1D7]] | -0.55 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[GIPC1]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[KCTD21]] | -0.54 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ATG5]] | -0.53 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[MYPOP]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZNF444]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[IQSEC2]] | -0.51 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CSTPP1]] | -0.51 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[UBE2R2]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[IFNLR1]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MTR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SMAD9]] | B | SMAD9 activity raises MTR's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SMAD9 | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[LMTK3]] | B | LMTK3 activity lowers MTR's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.43× higher at baseline in the lines without LMTK3 | 0.096 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-22.4, 19.1); signed map (9.7, -14.9). **Vector** length 130, 42.0% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +0.6 |
|  | [[Roxadustat (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +2.2 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.3 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.2 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -9.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.6 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | 5-methyltetrahydrofolate-homocysteine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:236,795,260-236,921,278 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cblG |
| Gene groups (HGNC) | Homocysteine domain containing methyltransferases; Small molecule methyltransferases |
| Reactome | 16 pathways, smallest: Cobalamin (Cbl) metabolism; Methylation; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99707](https://www.uniprot.org/uniprotkb/Q99707) (Methionine synthase):

> Catalyzes the transfer of a methyl group from methylcob(III)alamin (MeCbl) to homocysteine, yielding enzyme-bound cob(I)alamin and methionine in the cytosol. MeCbl is an active form of cobalamin (vitamin B12) used as a cofactor for methionine biosynthesis. Cob(I)alamin form is regenerated to MeCbl by a transfer of a methyl group from 5-methyltetrahydrofolate. The processing of cobalamin in the cytosol occurs in a multiprotein complex composed of at least MMACHC, MMADHC, MTRR (methionine …

**Summary**, from NCBI Gene [4548](https://www.ncbi.nlm.nih.gov/gene/4548):

> This gene encodes the 5-methyltetrahydrofolate-homocysteine methyltransferase. This enzyme, also known as cobalamin-dependent methionine synthase, catalyzes the final step in methionine biosynthesis. Mutations in MTR have been identified as the underlying cause of methylcobalamin deficiency complementation group G. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:7468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7468) · Entrez [4548](https://www.ncbi.nlm.nih.gov/gene/4548) · UniProt [Q99707](https://www.uniprot.org/uniprotkb/Q99707) · Ensembl [ENSG00000116984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116984)

## Data

Gene col 3861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3861); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3861]; `tensor/DDL_lfc|DDL_z.npy` [3861]; `embed/gene_vectors.npy` [3861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3861 or target_col == 3861). Every well: [[MTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
