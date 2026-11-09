---
symbol: "ENOX1"
type: "gene"
col: 4197
ensembl_id: "ENSG00000120658"
name: "ecto-NOX disulfide-thiol exchanger 1"
location: "13q14.11"
module: 98
arm: "+"
pooled_cpm: 37.55
n_lines_expressing: 38
n_dd_up: 18
n_dd_down: 25
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# ENOX1

*ecto-NOX disulfide-thiol exchanger 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.50× (z +12.8, q 5e-35, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.332× (z -15.4, q 0e+00, down in 34 of 36 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAOA]] (+0.54, fdr 1e-05), [[TMEFF2]] (+0.54, fdr 3e-05), [[LINC00607]] (+0.52, fdr 1e-05); moves opposite to [[TCP11L1]] (-0.42, fdr 8e-05), [[SLC66A3]] (-0.41, fdr 6e-05), [[STAG3L4]] (-0.41, fdr 1e-04, ⚠ STAG3L4 in the vector space only through flagged drug-doses), [[PHOSPHO2]] (-0.39, fdr 6e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01917]] → it (grade B ⚠); 10 go from it, the strongest it → [[ZC3H12A-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.50×** | +12.8 | 5e-35 | 28/36 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +11.8 | 1e-29 | 26/36 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +11.8 | 1e-29 | 29/36 (SW480, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +10.4 | 5e-23 | 24/36 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.8 | 2e-16 | 17/36 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.1 | 5e-14 | 18/35 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +7.8 | 7e-13 | 25/36 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.84×** | +5.8 | 5e-07 | 20/35 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 6e-07 | 19/36 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +5.7 | 8e-07 | 22/36 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 16/36 (A498, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.2 | 1e-05 | 22/36 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 12/36 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.009 | 16/36 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.017 | 15/36 (NCI-H460, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.332×** | -15.4 | 0e+00 | 34/36 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -14.6 | 1e-45 | 31/35 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.466×** | -10.6 | 3e-24 | 28/36 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -9.1 | 1e-17 | 30/36 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -7.3 | 4e-11 | 24/37 (COLO 205, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -7.0 | 3e-10 | 22/34 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -4.8 | 1e-04 | 19/36 (NCI-H1573, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.704×** | -4.7 | 2e-04 | 18/36 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -4.5 | 5e-04 | 16/35 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -4.3 | 0.001 | 18/36 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -4.2 | 0.001 | 15/35 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.561×** | -4.2 | 0.001 | 15/28 (HT-29, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **0.809×** | -4.2 | 0.001 | 13/36 (COLO 205, Hs 766T, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.568×** | -4.1 | 0.002 | 15/34 (COLO 205, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.749×** | -4.0 | 0.003 | 17/35 (hTERT-HPNE, C32, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.003 | 16/36 (SNU-1, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -3.9 | 0.003 | 11/36 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -3.6 | 0.009 | 16/36 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.5 | 0.015 | 11/36 (COLO 205, LoVo, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.016 | 15/36 (SNU-1, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 251 | 0 | 16 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0404× (z -30.5) |
| [[HT-29 (line)]] | alt | 44.7 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -19.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -13.0) |
| [[SNU-1 (line)]] | wt | 675 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -22.8) |
| [[A498 (line)]] | wt | 21.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.25× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 40.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -11.8) |
| [[J82 (line)]] | alt | 64.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.80× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.302× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 66.1 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -15.4) |
| [[A-172 (line)]] | wt | 10.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +20.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 14.3 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.26× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -11.6) |
| [[SW480 (line)]] | alt | 19.8 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.74× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -10.6) |
| [[BT-474 (line)]] | alt | 78.2 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +18.5) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.339× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.150× (z -10.1) |
| [[LoVo (line)]] | wt | 15.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.204× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 31.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.224× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 76.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -10.2) |
| [[C-33 A (line)]] | alt | 27.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.33× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 18.3 | 2 | 0 | [[Belinostat (drug)]] 5 µM 5.81× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.08× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAOA]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TMEFF2]] | +0.54 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[LINC00607]] | +0.52 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DAB1]] | +0.50 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LINC01917]] | +0.49 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[FRY]] | +0.49 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[ZMYND8]] | +0.48 | +0.26 / +0.49 | both halves | 4e-04 |  |
| [[ENPP2]] | +0.48 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[SAMSN1]] | +0.47 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[MAFB]] | +0.47 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SERPINA1]] | +0.47 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[STXBP5-AS1]] | +0.47 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP11L1]] | -0.42 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[SLC66A3]] | -0.41 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[STAG3L4]] ⚠ | -0.41 | -0.36 / -0.35 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PHOSPHO2]] | -0.39 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[NIPSNAP3A]] | -0.39 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[GALNT11]] | -0.39 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CYP27C1]] | -0.38 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[LOXL1-AS1]] | -0.38 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TCTN2]] | -0.38 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[UBE2Q2P1-1]] | -0.38 | -0.34 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01917]] | B | LINC01917 activity raises ENOX1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without LINC01917 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[MAFB]] | B | MAFB activity raises ENOX1's level | lines that do not express MAFB (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without MAFB | 0.073 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[MIR583HG]] | B | MIR583HG activity raises ENOX1's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.53× lower at baseline in the lines without MIR583HG | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[DIRC3]] | B | DIRC3 activity raises ENOX1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without DIRC3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ENOX1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12A-DT]] | B | ENOX1 activity raises ZC3H12A-DT's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without ENOX1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[LINC00607]] | B | ENOX1 activity raises LINC00607's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without ENOX1 | 0.045 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[SAMSN1]] | B | ENOX1 activity raises SAMSN1's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without ENOX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[UBA6-DT]] | B | ENOX1 activity raises UBA6-DT's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without ENOX1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[SQOR]] | B | ENOX1 activity raises SQOR's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 1.92× lower at baseline in the lines without ENOX1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[MIR583HG]] | B | ENOX1 activity raises MIR583HG's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.56× lower at baseline in the lines without ENOX1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | ENOX1 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express ENOX1 (12) vs lines expressing it (36) | the lines without ENOX1: 1.28× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[ITGA10]] | B | ENOX1 activity raises ITGA10's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without ENOX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[C1QTNF7-AS1]] | B | ENOX1 activity raises C1QTNF7-AS1's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without ENOX1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[PTPRM]] | B | ENOX1 activity raises PTPRM's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 3.48× lower at baseline in the lines without ENOX1 | 0.099 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, 20.3); signed map (21.4, 30.7). **Vector** length 83.0, 18.4% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +11.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.9 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +5.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -3.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.0 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.6 | -7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | +0.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | +0.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ecto-NOX disulfide-thiol exchanger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:43,213,130-43,786,972 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10094, PIG38, CNOX, cCNOX |
| Gene groups (HGNC) | RNA binding motif containing; Ecto-NOX disulfide-thiol exchanger family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC92](https://www.uniprot.org/uniprotkb/Q8TC92) (Ecto-NOX disulfide-thiol exchanger 1):

> Probably acts as a terminal oxidase of plasma electron transport from cytosolic NAD(P)H via hydroquinones to acceptors at the cell surface. Hydroquinone oxidase activity alternates with a protein disulfide-thiol interchange/oxidoreductase activity which may control physical membrane displacements associated with vesicle budding or cell enlargement. The activities oscillate with a period length of 24 minutes and play a role in control of the ultradian cellular biological clock.

**Summary**, from NCBI Gene [55068](https://www.ncbi.nlm.nih.gov/gene/55068):

> The protein encoded by this gene is involved in plasma membrane electron transport pathways. The encoded protein has both a hydroquinone (NADH) oxidase activity and a protein disulfide-thiol interchange activity. The two activities cycle with a periodicity of 24 minutes, with one activity being at its peak when the other is at its lowest. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:25474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25474) · Entrez [55068](https://www.ncbi.nlm.nih.gov/gene/55068) · UniProt [Q8TC92](https://www.uniprot.org/uniprotkb/Q8TC92) · Ensembl [ENSG00000120658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120658)

## Data

Gene col 4197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4197); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4197]; `tensor/DDL_lfc|DDL_z.npy` [4197]; `embed/gene_vectors.npy` [4197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4197 or target_col == 4197). Every well: [[ENOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
