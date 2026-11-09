---
symbol: "MAP3K5"
type: "gene"
col: 12398
ensembl_id: "ENSG00000197442"
name: "mitogen-activated protein kinase kinase kinase 5"
location: "6q23.3"
module: 174
arm: "+"
pooled_cpm: 134.17
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 63
n_dd_up_clean: 5
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 16
direction_downstream: 17
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# MAP3K5

*mitogen-activated protein kinase kinase kinase 5* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[BAY1125976 (drug)]] 5 µM: 1.68× (z +4.8, q 7e-04, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.434× (z -23.3, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST3B1]] (+0.64, fdr 1e-05), [[EFNA5]] (+0.62, fdr 1e-05), [[DOCK5]] (+0.61, fdr 7e-06); moves opposite to [[SH3BGR]] (-0.50, fdr 3e-05), [[PDCD6IP]] (-0.45, fdr 6e-05), [[DUSP3]] (-0.44, fdr 1e-04).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[IL7]] → it (grade B ⚠); 17 go from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **1.68×** | +4.8 | 7e-04 | 27/45 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.029 | 20/46 (LoVo, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.029 | 24/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.062 | 17/45 (A-172, HOP62, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.062 | 16/45 (LoVo, COLO 205, …) | two highest doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.083 | 18/46 (HOP62, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.2 | 0.11 | 12/45 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 1.11× | +3.0 | 0.18 | 2/45 (MIA PaCa-2, SW 1088) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 78 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.434×** | -23.3 | 0e+00 | 37/45 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.377×** | -19.2 | 0e+00 | 41/45 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -18.3 | 0e+00 | 39/46 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.401×** | -17.3 | 0e+00 | 32/39 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.428×** | -16.7 | 0e+00 | 38/46 (SW 900, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.446×** | -15.9 | 0e+00 | 40/45 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.448×** | -14.6 | 0e+00 | 31/42 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -14.2 | 1e-43 | 39/45 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -13.4 | 5e-39 | 36/44 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.533×** | -12.4 | 2e-33 | 39/45 (SW 900, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -11.6 | 1e-29 | 29/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.554×** | -11.6 | 1e-29 | 36/45 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.589×** | -10.4 | 9e-24 | 38/45 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.579×** | -10.2 | 1e-22 | 37/45 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.607×** | -9.8 | 3e-21 | 34/46 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -9.6 | 3e-20 | 36/45 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.603×** | -9.6 | 3e-20 | 36/45 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -9.2 | 1e-18 | 35/47 (SW 900, BT-474, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -9.2 | 1e-18 | 32/45 (SNU-423, BT-474, …) | top dose only | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 138 | 0 | 26 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -21.2) |
| [[LoVo (line)]] | wt | 188 | 0 | 23 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -32.4) |
| [[NCI-H1573 (line)]] | alt | 220 | 0 | 23 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -32.5) |
| [[NCI-H2030 (line)]] | alt | 383 | 0 | 22 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -34.6) |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 21 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 211 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -19.5) |
| [[SW 900 (line)]] | alt | 355 | 0 | 16 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -26.0) |
| [[RKO (line)]] | wt | 115 | 0 | 15 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 239 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -24.6) |
| [[NCI-H1792 (line)]] | alt | 275 | 0 | 14 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0924× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.225× (z -21.3) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -31.9) |
| [[NCI-H460 (line)]] | wt | 106 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -30.6) |
| [[PANC-1 (line)]] | alt | 114 | 0 | 13 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -17.8) |
| [[A498 (line)]] | wt | 92.8 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -15.9) |
| [[A-172 (line)]] | wt | 80.7 | 1 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.180× (z -14.7) |
| [[COLO 205 (line)]] | alt | 475 | 1 (1 ⚠) | 8 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.26× (z +8.8) ⚠ cell-cycle shift, explains ~59% of this change | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -24.2) |
| [[HS-578T (line)]] | alt | 179 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 72.6 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +21.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 137 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -17.2) |
| [[SNU-423 (line)]] | alt | 266 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -18.5) |
| [[SW48 (line)]] | wt | 126 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.1) |
| [[A549 (line)]] | wt | 114 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 203 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.0) |
| [[LS 180 (line)]] | wt | 161 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.3) |
| [[SHP-77 (line)]] | alt | 188 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -14.7) |
| [[SW 1271 (line)]] | alt | 335 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -14.6) |
| [[C32 (line)]] | wt | 51.7 | 0 | 6 | — | [[Cobimetinib (drug)]] 5 µM 0.248× (z -9.7) |
| [[KATO III (line)]] | alt | 124 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.2) |
| [[SW480 (line)]] | alt | 74.2 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -17.8) |
| [[J82 (line)]] | alt | 65.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 82.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.6) |
| [[HOP62 (line)]] | alt | 95.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.2) |
| [[HT-29 (line)]] | alt | 128 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.290× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.460× (z -17.4) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.6) |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 60.9 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.51× (z +10.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.6× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 54.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.5) |
| [[SW1417 (line)]] | alt | 77.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 48.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.5) |
| [[A-427 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST3B1]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[EFNA5]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[DOCK5]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RGS17]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DUSP4]] | +0.59 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[MCTP1]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TBC1D8]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TNFRSF6B]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ITGB5]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ADGRE2]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PTPN12]] | +0.55 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGR]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PDCD6IP]] | -0.45 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[DUSP3]] | -0.44 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[CLCC1]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[NRBP1]] | -0.44 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL7]] | B | IL7 activity raises MAP3K5's level | lines that do not express IL7 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without IL7 | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[MET]] | B | MET activity raises MAP3K5's level | lines that do not express MET (9) vs lines expressing it (41) | 2.45× lower at baseline in the lines without MET | 0.019 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[RGS17]] | B | RGS17 activity raises MAP3K5's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without RGS17 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[ABHD17C]] | B | ABHD17C activity raises MAP3K5's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without ABHD17C | 0.029 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[TGFBR2]] | B | TGFBR2 activity raises MAP3K5's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.73× lower at baseline in the lines without TGFBR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises MAP3K5's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without TNFRSF6B | 0.044 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[EPAS1]] | B | EPAS1 activity raises MAP3K5's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without EPAS1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[ADAM28]] | B | ADAM28 activity raises MAP3K5's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without ADAM28 | 0.058 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[MTOR]] | B | MTOR activity lowers MAP3K5's level | compounds that target MTOR: 3 of 8 raise it (AZD-8055, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.4% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[SERPINE2]] | B | SERPINE2 activity raises MAP3K5's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without SERPINE2 | 0.067 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[CEMIP]] | B | CEMIP activity raises MAP3K5's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CEMIP | 0.067 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[NRG2]] | B | NRG2 activity weakens MAP3K5's drug response | lines that do not express NRG2 (14) vs lines expressing it (32) | the lines without NRG2 respond 1.34× as strongly (z diff -1.59); strongest at Dinaciclib 0.05 µM: 0.35x vs 0.57x (z diff -4.5) | 0.067 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B; target measured in part of the lines; artifact flags |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | MAP3K5 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.68× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Filgotinib (drug)]] 0.05 µM | C | MAP3K5 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 1.48× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | C | MAP3K5 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 1.99× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | C | MAP3K5 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 1.40× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | C | MAP3K5 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.74× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[MK-3903 (drug)]] 0.05 µM | C | MAP3K5 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.73× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Arbutin (drug)]] 5 µM | C | MAP3K5 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.70× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Tirabrutinib (drug)]] 0.5 µM | C | MAP3K5 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 1.34× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | C | MAP3K5 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.72× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | MAP3K5 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.76× the cells of the other lines | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | MAP3K5 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.82× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| cells under [[Pralsetinib (drug)]] 0.05 µM | C | MAP3K5 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 1.44× the cells of the other lines | 0.077 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, 6.1); signed map (8.3, 49.0). **Vector** length 123, 42.7% of its response variance represented; |z| ≥ 3 in 2,195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | -11.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | -1.7 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +3.3 | +3.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.8 | -8.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.3 | -8.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.1 | -9.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.4 | -9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.2 | -6.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.0 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:136,557,046-136,793,097 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAPKKK5, ASK1; previously MEKK5 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |
| Reactome | 4 pathways, smallest: Oxidative Stress Induced Senescence; Cellular Senescence; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99683](https://www.uniprot.org/uniprotkb/Q99683) (Mitogen-activated protein kinase kinase kinase 5):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. Plays an important role in the cascades of cellular responses evoked by changes in the environment. Mediates signaling for determination of cell fate such as differentiation and survival. Plays a crucial role in the apoptosis signal transduction pathway through mitochondria-dependent caspase activation. MAP3K5/ASK1 is required for the innate immune response, which is essential for host …

**Summary**, from NCBI Gene [4217](https://www.ncbi.nlm.nih.gov/gene/4217):

> Mitogen-activated protein kinase (MAPK) signaling cascades include MAPK or extracellular signal-regulated kinase (ERK), MAPK kinase (MKK or MEK), and MAPK kinase kinase (MAPKKK or MEKK). MAPKK kinase/MEKK phosphorylates and activates its downstream protein kinase, MAPK kinase/MEK, which in turn activates MAPK. The kinases of these signaling cascades are highly conserved, and homologs exist in yeast, Drosophila, and mammalian cells. MAPKKK5 contains 1,374 amino acids with all 11 kinase …

**Accessions** — [HGNC:6857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6857) · Entrez [4217](https://www.ncbi.nlm.nih.gov/gene/4217) · UniProt [Q99683](https://www.uniprot.org/uniprotkb/Q99683) · Ensembl [ENSG00000197442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197442)

## Data

Gene col 12398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12398); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12398]; `tensor/DDL_lfc|DDL_z.npy` [12398]; `embed/gene_vectors.npy` [12398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12398 or target_col == 12398). Every well: [[MAP3K5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
