---
symbol: "DOCK1"
type: "gene"
col: 7458
ensembl_id: "ENSG00000150760"
name: "dedicator of cytokinesis 1"
location: "10q26.2"
module: 5
arm: "+"
pooled_cpm: 213.09
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DOCK1

*dedicator of cytokinesis 1* — 10q26.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.249× (z -21.7, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENOX2]] (+0.70, fdr 7e-06), [[MAPKAP1]] (+0.68, fdr 1e-05), [[GNL3L]] (+0.68, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.65, fdr 7e-06), [[VPS37D]] (-0.63, fdr 1e-05), [[FAM229B]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RANBP17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | 1.55× | +3.6 | 0.18 | 33/47 (AsPC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.25× | +3.3 | 0.24 | 25/47 (AsPC-1, A-427, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.21× | +3.0 | 0.45 | 23/47 (CFPAC-1, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.249×** | -21.7 | 0e+00 | 47/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.265×** | -20.7 | 0e+00 | 47/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.287×** | -19.5 | 0e+00 | 47/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.488×** | -15.8 | 0e+00 | 44/48 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.543×** | -13.5 | 3e-39 | 37/47 (C32, HEC-1-A, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.448×** | -12.0 | 2e-31 | 43/46 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.479×** | -11.0 | 2e-26 | 44/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.303×** | -9.8 | 1e-20 | 47/48 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -9.6 | 5e-20 | 37/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.581×** | -8.5 | 1e-15 | 36/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.616×** | -7.6 | 2e-12 | 34/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.626×** | -7.3 | 1e-11 | 44/47 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.424×** | -7.0 | 1e-10 | 39/47 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -6.2 | 2e-08 | 35/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.667×** | -6.1 | 5e-08 | 34/49 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.681×** | -6.0 | 8e-08 | 38/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -5.5 | 1e-06 | 30/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.575×** | -4.5 | 2e-04 | 38/48 (HepG2/C3A, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 4e-04 | 29/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -4.0 | 0.001 | 23/47 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.771×** | -4.0 | 0.001 | 31/47 (A549, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 175 | 0 | 17 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -19.1) |
| [[RKO (line)]] | wt | 319 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -28.4) |
| [[NCI-H23 (line)]] | alt | 277 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -19.1) |
| [[PANC-1 (line)]] | alt | 333 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 370 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -19.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -18.9) |
| [[C32 (line)]] | wt | 212 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -23.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -15.4) |
| [[J82 (line)]] | alt | 150 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -20.5) |
| [[LOX-IMVI (line)]] | wt | 327 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -22.4) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -18.5) |
| [[SNU-423 (line)]] | alt | 214 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -21.5) |
| [[LS 180 (line)]] | wt | 170 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 304 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -23.8) |
| [[NCI-H1573 (line)]] | alt | 435 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -16.0) |
| [[SW48 (line)]] | wt | 256 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -14.1) |
| [[SW480 (line)]] | alt | 168 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -23.5) |
| [[A-427 (line)]] | wt | 288 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -15.9) |
| [[C-33 A (line)]] | alt | 197 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -13.7) |
| [[HT-29 (line)]] | alt | 191 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -21.4) |
| [[hTERT-HPNE (line)]] | wt | 230 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -11.9) |
| [[LoVo (line)]] | wt | 148 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -21.7) |
| [[NCI-H1792 (line)]] | alt | 166 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -17.6) |
| [[SNU-1 (line)]] | wt | 324 | 0 | 8 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -13.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -13.3) |
| [[SW 900 (line)]] | alt | 206 | 0 | 8 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -13.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.362× (z -12.1) |
| [[A-172 (line)]] | wt | 116 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -16.5) |
| [[A498 (line)]] | wt | 208 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -17.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.306× (z -13.4) |
| [[A549 (line)]] | wt | 238 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -22.2) |
| [[NCI-H2030 (line)]] | alt | 264 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -15.0) |
| [[SW1417 (line)]] | alt | 138 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.240× (z -14.8) |
| [[COLO 205 (line)]] | alt | 337 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0978× (z -22.6) |
| [[HOP62 (line)]] | alt | 179 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -20.7) |
| [[HS-578T (line)]] | alt | 139 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -18.2) |
| [[KATO III (line)]] | alt | 134 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.105× (z -22.4) |
| [[Panc 03.27 (line)]] | alt | 262 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.196× (z -17.4) |
| [[AN3 CA (line)]] | alt | 341 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -11.4) |
| [[H4 (line)]] | wt | 219 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -11.7) |
| [[HCT15 (line)]] | alt | 253 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 208 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 193 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 170 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.393× (z -10.7) |
| [[Hs 766T (line)]] | wt | 98.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.241× (z -11.7) |
| [[BT-474 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -12.6) |
| [[SW 1088 (line)]] | alt | 203 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0894× (z -10.7) |
| [[SW 1271 (line)]] | alt | 186 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.161× (z -10.8) ⚠ transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -9.4) |
| [[CHP-212 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MAPKAP1]] | +0.68 | +0.49 / +0.77 | both halves | 1e-05 | pathway: Signaling by VEGF |
| [[GNL3L]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.67 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DIAPH2]] | +0.66 | +0.69 / +0.66 | both halves | 7e-06 | same gene group |
| [[CTPS1]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[UGGT2]] | +0.65 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ASAP1]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 | same gene group |
| [[RANBP17]] | +0.64 | +0.68 / +0.58 | both halves | 8e-06 | same gene group |
| [[HLCS]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.65 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[VPS37D]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[FAM229B]] | -0.63 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[THAP8]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[USP30]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ANG]] | -0.60 | -0.51 / -0.52 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[SAP30-DT]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.59 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[PEX13]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 | same gene group |
| [[IST1]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RANBP17]] | B | RANBP17 activity raises DOCK1's level | lines that do not express RANBP17 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without RANBP17 | 0.026 | ⚠ within organs, on part of the lines |
| [[RIN3]] | B | RIN3 activity raises DOCK1's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.87× lower at baseline in the lines without RIN3 | 0.051 | ⚠ within organs, on part of the lines |
| [[DIAPH2]] | B | DIAPH2 activity raises DOCK1's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 1.74× lower at baseline in the lines without DIAPH2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |
| [[DHRS3]] | C | DHRS3 activity weakens DOCK1's drug response | lines that do not express DHRS3 (13) vs lines expressing it (35) | the lines without DHRS3 respond 1.02× as strongly (z diff -1.43); strongest at Homoharringtonine 5 µM: 0.50x vs 0.58x (z diff -2.6) | 0.020 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.8, -34.4); signed map (3.2, -51.0). **Vector** length 104, 44.4% of its response variance represented; |z| ≥ 3 in 1,403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.6 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:126,905,409-127,452,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DOCK180, ced5 |
| Gene groups (HGNC) | Armadillo like helical domain containing; DOCK family Rho GEFs; SH3 domain containing |
| Reactome | 32 pathways, smallest: DCC mediated attractive signaling; PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14185](https://www.uniprot.org/uniprotkb/Q14185) (Dedicator of cytokinesis protein 1):

> Involved in cytoskeletal rearrangements required for phagocytosis of apoptotic cells and cell motility. Along with DOCK1, mediates CRK/CRKL regulation of epithelial and endothelial cell spreading and migration on type IV collagen. Functions as a guanine nucleotide exchange factor (GEF), which activates Rac Rho small GTPases by exchanging bound GDP for free GTP. Its GEF activity may be enhanced by ELMO1.

**Summary**, from NCBI Gene [1793](https://www.ncbi.nlm.nih.gov/gene/1793):

> This gene encodes a member of the dedicator of cytokinesis protein family. Dedicator of cytokinesis proteins act as guanine nucleotide exchange factors for small Rho family G proteins. The encoded protein regulates the small GTPase Rac, thereby influencing several biological processes, including phagocytosis and cell migration. Overexpression of this gene has also been associated with certain cancers. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:2987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2987) · Entrez [1793](https://www.ncbi.nlm.nih.gov/gene/1793) · UniProt [Q14185](https://www.uniprot.org/uniprotkb/Q14185) · Ensembl [ENSG00000150760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150760)

## Data

Gene col 7458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7458); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7458]; `tensor/DDL_lfc|DDL_z.npy` [7458]; `embed/gene_vectors.npy` [7458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7458 or target_col == 7458). Every well: [[DOCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
