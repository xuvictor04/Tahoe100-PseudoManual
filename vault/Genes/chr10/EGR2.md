---
symbol: "EGR2"
type: "gene"
col: 4383
ensembl_id: "ENSG00000122877"
name: "early growth response 2"
location: "10q21.3"
module: 109
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 43
n_dd_up: 17
n_dd_down: 38
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# EGR2

*early growth response 2* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.4× (z +20.2, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.144× (z -11.3, q 1e-26, down in 39 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR3]] (+0.92, fdr 7e-06), [[EGR1]] (+0.90, fdr 7e-06), [[IER2]] (+0.81, fdr 7e-06); moves opposite to [[FHIP2A]] (-0.63, fdr 7e-06), [[NAPB]] (-0.60, fdr 1e-05), [[ELMOD3]] (-0.57, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ADAM8]] → it (grade B ⚠); 9 go from it, the strongest it → [[SNX4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.4×** | +20.2 | 0e+00 | 31/34 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **7.84×** | +11.6 | 9e-29 | 33/36 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.60×** | +9.0 | 6e-17 | 21/34 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.19×** | +8.4 | 6e-15 | 33/39 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.65×** | +8.1 | 5e-14 | 32/40 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +8.1 | 6e-14 | 24/33 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.60×** | +7.5 | 4e-12 | 31/40 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.38×** | +5.1 | 2e-05 | 23/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.50×** | +5.0 | 4e-05 | 3/13 (HOP62, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.32×** | +5.0 | 4e-05 | 23/39 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.31×** | +4.9 | 4e-05 | 24/39 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **2.10×** | +4.4 | 5e-04 | 8/20 (NCI-H460, HOP62, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **2.12×** | +4.3 | 9e-04 | 1/11 (HOP62) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.80×** | +3.5 | 0.020 | 16/39 (NCI-H460, C32, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.026 | 13/40 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.031 | 8/40 (HT-29, SNU-423, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.053 | 12/40 (NCI-H1792, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.144×** | -11.3 | 1e-26 | 39/40 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.201×** | -9.3 | 3e-18 | 33/40 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.192×** | -9.2 | 5e-18 | 33/36 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.287×** | -9.0 | 2e-17 | 37/40 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.217×** | -8.9 | 6e-17 | 28/39 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.217×** | -8.2 | 2e-14 | 36/40 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.231×** | -8.2 | 2e-14 | 28/39 (SW1417, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.384×** | -7.8 | 5e-13 | 33/40 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.318×** | -6.7 | 2e-09 | 29/38 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.382×** | -6.4 | 1e-08 | 30/41 (SHP-77, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.325×** | -6.2 | 3e-08 | 26/37 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.520×** | -5.4 | 4e-06 | 25/40 (NCI-H1573, SW48, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.411×** | -5.2 | 1e-05 | 26/39 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.437×** | -4.8 | 6e-05 | 19/39 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.571×** | -4.6 | 2e-04 | 22/40 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.540×** | -4.4 | 4e-04 | 20/40 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.479×** | -4.3 | 7e-04 | 17/40 (H4, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 21.9 | 2 | 10 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.0530× (z -16.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0264× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 8.66 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 46.4× (z +19.7) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0552× (z -10.0) |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 6 (2 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0576× (z -10.8) |
| [[SW480 (line)]] | alt | 9.53 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +13.7) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0414× (z -11.7) |
| [[A498 (line)]] | wt | 5.07 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0394× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0460× (z -10.3) |
| [[HOP62 (line)]] | alt | 7.09 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 59.8× (z +17.4) | [[Trametinib (drug)]] 0.5 µM 0.0657× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 2.35 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 109× (z +16.8) | — |
| [[C32 (line)]] | wt | 6.73 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.3× (z +15.3) | — |
| [[CFPAC-1 (line)]] | alt | 5.14 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 55.1× (z +14.7) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0274× (z -9.3) |
| [[HS-578T (line)]] | alt | 7.71 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0318× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 20.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +13.2) | [[Ixazomib citrate (drug)]] 5 µM 0.0441× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0489× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 5.08 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0219× (z -9.8) |
| [[SNU-423 (line)]] | alt | 5.69 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 47.5× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0325× (z -8.8) |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0377× (z -11.1) |
| [[A549 (line)]] | wt | 4.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 9.80 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0499× (z -8.5) |
| [[Hs 766T (line)]] | wt | 3.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.0× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 7.55 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0176× (z -10.5) |
| [[SHP-77 (line)]] | alt | 4.07 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.0119× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 2.69 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 89.8× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 6.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.2× (z +12.8) | — |
| [[A-172 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | +0.92 | +0.91 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 987 |
| [[EGR1]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 980 |
| [[IER2]] | +0.81 | +0.85 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 582 |
| [[ASTL]] | +0.77 | +0.80 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MCL1]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[FOS]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 963 |
| [[DUSP6]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 | pathway: Nuclear Events (kinase and transcription factor activation); STRING 458 |
| [[BCL2L12]] | +0.71 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[ERCC1]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[TADA3]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[HIVEP3]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 | same gene group |
| [[PHLDA1]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | -0.63 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[NAPB]] | -0.60 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.57 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[ZNF148]] | -0.56 | -0.61 / -0.50 | both halves | 1e-05 | same gene group |
| [[SNX4]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RNPC3]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MAFIP]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[WWP1]] | -0.55 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[RFXAP]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity raises EGR2's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.51× lower at baseline in the lines without ADAM8 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[EGR3]] | B | EGR3 activity raises EGR2's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 2.24× lower at baseline in the lines without EGR3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[SYT5]] | B | SYT5 activity raises EGR2's level | lines that do not express SYT5 (10) vs lines expressing it (40) | 1.19× lower at baseline in the lines without SYT5 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ACVR2A; also absent: B4GALNT1, LARP6; maybe low, not absent |
| [[RASD1]] | B | RASD1 activity raises EGR2's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without RASD1 | 0.097 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX4]] | B | EGR2 activity lowers SNX4's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without EGR2 | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTPRN2]] | B | EGR2 activity raises PTPRN2's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without EGR2 | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EGR1]] | B | EGR2 activity raises EGR1's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 2.34× lower at baseline in the lines without EGR2 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LRRFIP2]] | B | EGR2 activity lowers LRRFIP2's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.39× higher at baseline in the lines without EGR2 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CTDSP1]] | B | EGR2 activity strengthens CTDSP1's drug response | lines that do not express EGR2 (7) vs lines expressing it (41) | the lines without EGR2 respond 0.67× as strongly (z diff +1.21); strongest at Panobinostat 5 µM: 0.34x vs 0.17x (z diff +2.4) | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FOSB]] | B | EGR2 activity raises FOSB's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without EGR2 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PHLDA1]] | B | EGR2 activity raises PHLDA1's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without EGR2 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR4A1]] | B | EGR2 activity raises NR4A1's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without EGR2 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ATP7A]] | B | EGR2 activity raises ATP7A's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without EGR2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.913). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, -0.6); signed map (6.1, 29.5). **Vector** length 126, 34.6% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +20.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +9.0 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.6 | -8.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.5 | -11.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.5 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.9 | -9.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -9.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.7 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | early growth response 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:62,811,996-62,819,167 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KROX20 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Early growth response family; Atypical E3 ubiquitin ligases |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 11 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation) |
| Matched by | ensembl_id |

**Function**, from UniProt [P11161](https://www.uniprot.org/uniprotkb/P11161) (E3 SUMO-protein ligase EGR2):

> Sequence-specific DNA-binding transcription factor. Plays a role in hindbrain segmentation by regulating the expression of a subset of homeobox containing genes and in Schwann cell myelination by regulating the expression of genes involved in the formation and maintenance of myelin (By similarity). Binds to two EGR2-consensus sites EGR2A (5'-CTGTAGGAG-3') and EGR2B (5'-ATGTAGGTG-3') in the HOXB3 enhancer and promotes HOXB3 transcriptional activation (By similarity). Binds to specific DNA sites …

**Summary**, from NCBI Gene [1959](https://www.ncbi.nlm.nih.gov/gene/1959):

> The protein encoded by this gene is a transcription factor with three tandem C2H2-type zinc fingers. Defects in this gene are associated with Charcot-Marie-Tooth disease type 1D (CMT1D), Charcot-Marie-Tooth disease type 4E (CMT4E), and with Dejerine-Sottas syndrome (DSS). Multiple transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:3239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3239) · Entrez [1959](https://www.ncbi.nlm.nih.gov/gene/1959) · UniProt [P11161](https://www.uniprot.org/uniprotkb/P11161) · Ensembl [ENSG00000122877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122877)

## Data

Gene col 4383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4383); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4383]; `tensor/DDL_lfc|DDL_z.npy` [4383]; `embed/gene_vectors.npy` [4383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4383 or target_col == 4383). Every well: [[EGR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
