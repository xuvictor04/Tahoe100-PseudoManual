---
symbol: "PRRC2A"
type: "gene"
col: 12877
ensembl_id: "ENSG00000204469"
name: "proline rich coiled-coil 2A"
location: "6p21.33"
module: 16
arm: "+"
pooled_cpm: 119.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PRRC2A

*proline rich coiled-coil 2A* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.42× (z +16.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.549× (z -11.5, q 1e-27, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGO]] (+0.75, fdr 7e-06), [[SRCAP]] (+0.73, fdr 7e-06), [[SF3B3]] (+0.72, fdr 7e-06); moves opposite to [[MACO1]] (-0.65, fdr 2e-05), [[SELENOK]] (-0.65, fdr 1e-05), [[RAB6A]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +16.7 | 0e+00 | 46/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +8.5 | 3e-15 | 42/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +8.5 | 3e-15 | 38/48 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +7.1 | 2e-10 | 43/49 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.0 | 2e-10 | 35/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +6.7 | 2e-09 | 46/48 (Hs 766T, HT-29, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +6.5 | 8e-09 | 42/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.2 | 4e-08 | 4/50 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.5 | 3e-06 | 36/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 8e-05 | 37/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 2e-04 | 34/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 4e-04 | 29/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **1.32×** | +3.6 | 0.012 | 32/48 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.5 | 0.019 | 29/47 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.094 | 23/48 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -11.5 | 1e-27 | 45/49 (CHP-212, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.721×** | -4.4 | 0.003 | 31/48 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.740×** | -4.1 | 0.008 | 30/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -3.9 | 0.014 | 30/48 (SK-MEL-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -3.8 | 0.019 | 28/48 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.770×** | -3.6 | 0.036 | 28/48 (NCI-H23, A-427, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.060 | 27/50 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.852× | -3.1 | 0.12 | 15/48 (H4, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.797× | -3.1 | 0.12 | 26/48 (SW 900, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.6 | 9 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.4) |
| [[A549 (line)]] | wt | 77.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 61.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 80.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.7) | — |
| [[NCI-H23 (line)]] | alt | 231 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.7) |
| [[HOP62 (line)]] | alt | 135 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +18.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.6) |
| [[HS-578T (line)]] | alt | 99.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +23.2) | — |
| [[KATO III (line)]] | alt | 109 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 162 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.8) |
| [[SW480 (line)]] | alt | 116 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.8) | — |
| [[A498 (line)]] | wt | 76.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +18.1) | — |
| [[C32 (line)]] | wt | 94.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 101 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.3) |
| [[H4 (line)]] | wt | 118 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 119 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.1) | — |
| [[LoVo (line)]] | wt | 73.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 193 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 207 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 192 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 131 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.5) |
| [[SW 900 (line)]] | alt | 93.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.3) | — |
| [[A-172 (line)]] | wt | 87.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 162 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.5) |
| [[CHP-212 (line)]] | wt | 142 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -15.4) |
| [[COLO 205 (line)]] | alt | 55.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.9) | — |
| [[HCT15 (line)]] | alt | 159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 79.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 48.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.6) | — |
| [[SW1417 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.3) | — |
| [[SW48 (line)]] | wt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.0) |
| [[A-427 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 188 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 168 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGO]] | +0.75 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | same gene group; STRING 477 |
| [[SF3B3]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | same gene group |
| [[PUF60]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[IRF2BP1]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[SAYSD1]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[HNRNPL]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TRIM28]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 | same gene group; STRING 485 |
| [[SF3B4]] | +0.66 | +0.64 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACO1]] | -0.65 | -0.48 / -0.71 | both halves | 2e-05 |  |
| [[SELENOK]] | -0.65 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.63 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[KLHL7]] | -0.63 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[IFT20]] | -0.63 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[MED31]] | -0.63 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[DPM1]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[MGST3]] | -0.61 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[RHOQ-AS1]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[ATP5MK]] | -0.60 | -0.45 / -0.62 | both halves | 3e-05 | same gene group |
| [[RNF181]] | -0.59 | -0.42 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises PRRC2A's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without SLC4A3 | 0.027 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[HDAC6]] | B | HDAC6 activity raises PRRC2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers PRRC2A's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without HLA-F-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[SLC9A3]] | C | SLC9A3 activity lowers PRRC2A's level | lines that do not express SLC9A3 (3) vs lines expressing it (47) | 1.62× higher at baseline in the lines without SLC9A3 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AIFM2, TESK2, HBEGF; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.1, -2.1); signed map (0.8, -32.9). **Vector** length 117, 37.8% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +16.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | +6.0 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | +6.0 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Artesunate (drug)]] 0.05 µM |  | +2.4 | +2.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.9 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.8 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | proline rich coiled-coil 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,620,715-31,637,771 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G2, D6S51E; previously BAT2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P48634](https://www.uniprot.org/uniprotkb/P48634) (Translational regulator PRRC2A):

> Recognizes and binds to N6-methyladenosine (m6A)-containing mRNAs (By similarity). Controls oligodendroglial specification and myelination by binding to oligodendrocyte transcription factor OLIG2 mRNA and promoting its stability (By similarity). Required for microglial maturation and proliferation by binding to and stabilizing essential developmental and functional transcripts of microglia (By similarity). Promotes leaky scanning, allowing ribosomes to bypass the translation start codons of …

**Summary**, from NCBI Gene [7916](https://www.ncbi.nlm.nih.gov/gene/7916):

> A cluster of genes, BAT1-BAT5, has been localized in the vicinity of the genes for TNF alpha and TNF beta. These genes are all within the human major histocompatibility complex class III region. This gene has microsatellite repeats which are associated with the age-at-onset of insulin-dependent diabetes mellitus (IDDM) and possibly thought to be involved with the inflammatory process of pancreatic beta-cell destruction during the development of IDDM. This gene is also a candidate gene for the …

**Accessions** — [HGNC:13918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13918) · Entrez [7916](https://www.ncbi.nlm.nih.gov/gene/7916) · UniProt [P48634](https://www.uniprot.org/uniprotkb/P48634) · Ensembl [ENSG00000204469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204469)

## Data

Gene col 12877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12877); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12877]; `tensor/DDL_lfc|DDL_z.npy` [12877]; `embed/gene_vectors.npy` [12877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12877 or target_col == 12877). Every well: [[PRRC2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRC2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
