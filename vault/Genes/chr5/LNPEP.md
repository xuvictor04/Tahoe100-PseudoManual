---
symbol: "LNPEP"
type: "gene"
col: 3463
ensembl_id: "ENSG00000113441"
name: "leucyl and cystinyl aminopeptidase"
location: "5q15"
module: 32
arm: "+"
pooled_cpm: 149.74
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LNPEP

*leucyl and cystinyl aminopeptidase* — 5q15

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.05×, NCI-H460 1.68×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.496× (z -14.0, q 6e-42, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAP1]] (+0.61, fdr 2e-05), [[ERAP1]] (+0.60, fdr 1e-05), [[DTX3L]] (+0.58, fdr 5e-05); moves opposite to [[ZNF559-ZNF177]] (-0.56, fdr 3e-05), [[RBAK-RBAKDN]] (-0.56, fdr 7e-05), [[TNNT1]] (-0.52, fdr 2e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3463.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.05×, NCI-H460 1.68×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.014 | 0/50 | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.17 | 17/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 1.12× | +3.3 | 0.19 | 3/48 (Hs 766T, CHP-212, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.23 | 14/47 (SW480, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.496×** | -14.0 | 6e-42 | 46/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.612×** | -13.9 | 1e-41 | 40/48 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.515×** | -13.3 | 5e-38 | 46/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -9.1 | 2e-17 | 39/49 (SNU-1, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -8.7 | 3e-16 | 41/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -7.8 | 5e-13 | 41/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -7.5 | 7e-12 | 37/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -7.4 | 7e-12 | 39/47 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -6.9 | 2e-10 | 38/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -6.3 | 1e-08 | 36/48 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.807×** | -6.1 | 6e-08 | 29/48 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.748×** | -5.8 | 3e-07 | 28/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.752×** | -5.7 | 5e-07 | 28/49 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.751×** | -5.5 | 1e-06 | 33/47 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.598×** | -5.4 | 3e-06 | 32/48 (RKO, SNU-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -5.0 | 2e-05 | 21/49 (CFPAC-1, H4, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.781×** | -5.0 | 2e-05 | 33/48 (HepG2/C3A, SNU-1, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.795×** | -4.6 | 1e-04 | 28/48 (RPMI-7951, NCI-H1792, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 113 | 1 (1 ⚠) | 14 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.402× (z -14.2) |
| [[A-172 (line)]] | wt | 244 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.427× (z -11.4) |
| [[KATO III (line)]] | alt | 154 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -14.4) |
| [[RKO (line)]] | wt | 182 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -15.7) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.163× (z -11.0) |
| [[Hs 766T (line)]] | wt | 394 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.268× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 182 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.437× (z -10.3) |
| [[SNU-423 (line)]] | alt | 188 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -14.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.333× (z -13.4) |
| [[A549 (line)]] | wt | 154 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.5) |
| [[HS-578T (line)]] | alt | 179 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -16.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -12.6) |
| [[SW480 (line)]] | alt | 154 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -18.8) |
| [[COLO 205 (line)]] | alt | 202 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -11.8) |
| [[HCT15 (line)]] | alt | 144 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -9.6) |
| [[LoVo (line)]] | wt | 109 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.483× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.282× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 285 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.465× (z -10.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.497× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 198 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -11.5) |
| [[A498 (line)]] | wt | 170 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -20.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.524× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 70.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 77.1 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.317× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -9.1) |
| [[LS 180 (line)]] | wt | 139 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.406× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.377× (z -10.1) |
| [[SHP-77 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 140 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0981× (z -11.4) |
| [[SW 900 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -11.6) |
| [[A-427 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[CFPAC-1 (line)]] | alt | 165 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.469× (z -9.0) |
| [[H4 (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.205× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 88.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.101× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAP1]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 | pathway: Antigen processing-Cross presentation |
| [[ERAP1]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 | same gene group |
| [[DTX3L]] | +0.58 | +0.39 / +0.61 | both halves | 5e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MBNL3]] | +0.57 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[ERAP2]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 | same gene group; ⚠ same locus (15.7 kb, same strand: neighbours can correlate without regulation) |
| [[MOB1A]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[DECR1]] | +0.57 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[ZHX1]] | +0.57 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[CD164]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CHRAC1]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ADAR]] | +0.55 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[OAS3]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[PARP14]] | +0.54 | +0.31 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF559-ZNF177]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | -0.56 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[TNNT1]] | -0.52 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[SYP]] | -0.52 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[EXO5-DT]] | -0.51 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[RAPGEFL1]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[FAM131A]] | -0.50 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[SAMD4B]] | -0.50 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[GPSM1]] | -0.50 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[CARMIL2]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[CHST12]] | -0.50 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ZNF212]] | -0.50 | -0.47 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.461). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 3.3); signed map (14.1, -13.9). **Vector** length 108, 33.8% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +3.4 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.6 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.5 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -7.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | leucyl and cystinyl aminopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:96,935,394-97,037,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP, PLAP, P-LAP, IRAP |
| Gene groups (HGNC) | Aminopeptidases; M1 metallopeptidases |
| Reactome | 8 pathways, smallest: Endosomal/Vacuolar pathway; Translocation of SLC2A4 (GLUT4) to the plasma membrane; Antigen processing-Cross presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIQ6](https://www.uniprot.org/uniprotkb/Q9UIQ6) (Leucyl-cystinyl aminopeptidase):

> Release of an N-terminal amino acid, cleaves before cysteine, leucine as well as other amino acids. Degrades peptide hormones such as oxytocin, vasopressin and angiotensin III, and plays a role in maintaining homeostasis during pregnancy. May be involved in the inactivation of neuronal peptides in the brain. Cleaves Met-enkephalin and dynorphin. Binds angiotensin IV and may be the angiotensin IV receptor in the brain.

**Summary**, from NCBI Gene [4012](https://www.ncbi.nlm.nih.gov/gene/4012):

> This gene encodes a zinc-dependent aminopeptidase that cleaves vasopressin, oxytocin, lys-bradykinin, met-enkephalin, dynorphin A and other peptide hormones. The protein can be secreted in maternal serum, reside in intracellular vesicles with the insulin-responsive glucose transporter GLUT4, or form a type II integral membrane glycoprotein. The protein catalyzes the final step in the conversion of angiotensinogen to angiotensin IV (AT4) and is also a receptor for AT4. Alternative splicing …

**Accessions** — [HGNC:6656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6656) · Entrez [4012](https://www.ncbi.nlm.nih.gov/gene/4012) · UniProt [Q9UIQ6](https://www.uniprot.org/uniprotkb/Q9UIQ6) · Ensembl [ENSG00000113441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113441)

## Data

Gene col 3463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3463); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3463]; `tensor/DDL_lfc|DDL_z.npy` [3463]; `embed/gene_vectors.npy` [3463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3463 or target_col == 3463). Every well: [[LNPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
