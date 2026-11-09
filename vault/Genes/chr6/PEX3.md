---
symbol: "PEX3"
type: "gene"
col: 424
ensembl_id: "ENSG00000034693"
name: "peroxisomal biogenesis factor 3"
location: "6q24.2"
module: 164
arm: "+"
pooled_cpm: 46.48
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# PEX3

*peroxisomal biogenesis factor 3* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +12.8, q 6e-35, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.449× (z -13.4, q 5e-38, down in 33 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.712× (z -5.9, q 5e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPC3]] (+0.78, fdr 7e-06), [[SPATA7]] (+0.77, fdr 7e-06), [[VDAC3]] (+0.74, fdr 7e-06); moves opposite to [[RNF32-AS1]] (-0.67, fdr 7e-06), [[CFAP161]] (-0.65, fdr 7e-06), [[SSUH2]] (-0.63, fdr 9e-06).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +12.8 | 6e-35 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +12.2 | 2e-31 | 39/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +9.7 | 9e-20 | 33/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.81×** | +9.4 | 8e-19 | 37/49 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +5.9 | 4e-07 | 24/48 (NCI-H1792, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +5.2 | 2e-05 | 24/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.6 | 4e-04 | 24/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +4.4 | 1e-03 | 22/48 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +4.3 | 0.001 | 23/49 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 20/48 (SNU-423, A-172, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.24×** | +3.7 | 0.011 | 14/48 (NCI-H1792, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.015 | 17/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.028 | 12/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.028 | 13/47 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.044 | 11/48 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.044 | 11/48 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.055 | 15/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.059 | 11/47 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.14× | +2.9 | 0.097 | 11/48 (HT-29, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.449×** | -13.4 | 5e-38 | 33/39 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.449×** | -12.9 | 2e-35 | 37/44 (C32, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -11.4 | 9e-28 | 39/48 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -5.9 | 5e-07 | 27/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.715×** | -5.6 | 2e-06 | 27/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.6 | 3e-04 | 1/49 (AN3 CA) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.775×** | -4.4 | 8e-04 | 20/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.781×** | -4.3 | 0.001 | 26/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.783×** | -4.1 | 0.003 | 21/48 (C32, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.793×** | -3.9 | 0.006 | 22/48 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.025 | 20/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.819×** | -3.5 | 0.025 | 19/48 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.027 | 14/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.052 | 14/48 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.832×** | -3.2 | 0.053 | 13/49 (NCI-H661, NCI-H2030, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.833× | -3.2 | 0.055 | 8/48 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.060 | 15/47 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.075 | 12/48 (SW 1088, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 36.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 64.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -19.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 47.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 43.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.377× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 55.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -19.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +13.3) | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 53.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -14.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -15.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 93.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 28.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.75× (z +9.5) | — |
| [[KATO III (line)]] | alt | 31.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.13× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 79.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 48.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.339× (z -10.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 93.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 50.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -9.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.170× (z -9.9) |
| [[HOP62 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0805× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.147× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~4% of this change |
| [[NCI-H23 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -13.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC3]] | +0.78 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[SPATA7]] | +0.77 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[LNPK]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.74 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[PDK3]] | +0.74 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.73 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[USP37]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[HELZ]] | +0.71 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[ALG9]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MMS19]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF32-AS1]] | -0.67 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[CFAP161]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SSUH2]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[SFPQ]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[THOC6]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.61 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[FKRP]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[SLC2A9]] | -0.60 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[AVEN]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[DDX5]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SKIL]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises PEX3's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without GPR155 | 0.031 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises PEX3's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without KDM2B-DT | 0.064 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[LIX1L]] | B | LIX1L activity raises PEX3's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.61× lower at baseline in the lines without LIX1L | 0.066 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[ARAP2]] | B | ARAP2 activity lowers PEX3's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.48× higher at baseline in the lines without ARAP2 | 0.084 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[MPP2]] | B | MPP2 activity raises PEX3's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.74× lower at baseline in the lines without MPP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -17.8); signed map (-37.3, 22.8). **Vector** length 120, 34.6% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.6 | +12.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[NG25 (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +9.7 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.9 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,450,805-143,490,616 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Peroxins |
| Reactome | 5 pathways, smallest: ABC transporters in lipid homeostasis; Class I peroxisomal membrane protein import; ABC-family protein mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P56589](https://www.uniprot.org/uniprotkb/P56589) (Peroxisomal biogenesis factor 3):

> Involved in peroxisome biosynthesis and integrity. Assembles membrane vesicles before the matrix proteins are translocated. As a docking factor for PEX19, is necessary for the import of peroxisomal membrane proteins in the peroxisomes.

**Summary**, from NCBI Gene [8504](https://www.ncbi.nlm.nih.gov/gene/8504):

> The product of this gene is involved in peroxisome biosynthesis and integrity. It assembles membrane vesicles before the matrix proteins are translocated. Peroxins (PEXs) are proteins that are essential for the assembly of functional peroxisomes. The peroxisome biogenesis disorders (PBDs) are a group of genetically heterogeneous autosomal recessive, lethal diseases characterized by multiple defects in peroxisome function. The peroxisomal biogenesis disorders are a heterogeneous group with at …

**Accessions** — [HGNC:8858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8858) · Entrez [8504](https://www.ncbi.nlm.nih.gov/gene/8504) · UniProt [P56589](https://www.uniprot.org/uniprotkb/P56589) · Ensembl [ENSG00000034693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034693)

## Data

Gene col 424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 424); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 424]; `tensor/DDL_lfc|DDL_z.npy` [424]; `embed/gene_vectors.npy` [424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 424 or target_col == 424). Every well: [[PEX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
