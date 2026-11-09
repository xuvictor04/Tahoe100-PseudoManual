---
symbol: "KIFC3"
type: "gene"
col: 6458
ensembl_id: "ENSG00000140859"
name: "kinesin family member C3"
location: "16q21"
module: 193
arm: "+"
pooled_cpm: 53.63
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 6
direction_downstream: 13
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# KIFC3

*kinesin family member C3* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +7.5, q 5e-11, up in 24 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.55× (z +6.1, q 4e-07, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.434× (z -16.2, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK4]] (+0.67, fdr 7e-06), [[SRGAP1]] (+0.62, fdr 7e-06), [[ADGRL4]] (+0.59, fdr 1e-05); moves opposite to [[DERL1]] (-0.52, fdr 3e-05), [[IDH1]] (-0.47, fdr 3e-05), [[VPS35]] (-0.47, fdr 9e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BCAR3]] → it (grade B ⚠); 13 go from it, the strongest it → [[MIR1915HG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.5 | 5e-11 | 24/45 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +6.1 | 4e-07 | 27/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.8 | 3e-04 | 18/37 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.7 | 3e-04 | 19/45 (H4, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.5 | 9e-04 | 22/44 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.014 | 7/45 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.016 | 12/45 (A498, SNU-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.019 | 8/45 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.026 | 19/45 (BT-474, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.026 | 8/45 (J82, CFPAC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +3.4 | 0.038 | 6/45 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.20×** | +3.1 | 0.074 | 17/40 (Hs 766T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.074 | 10/46 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.17× | +3.1 | 0.075 | 8/44 (BT-474, CFPAC-1, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.096 | 7/44 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.434×** | -16.2 | 0e+00 | 43/45 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.484×** | -14.1 | 7e-43 | 34/45 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -10.5 | 2e-23 | 32/45 (NCI-H23, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.618×** | -9.3 | 1e-18 | 34/45 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.662×** | -8.5 | 3e-15 | 27/46 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -7.7 | 1e-12 | 24/45 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.677×** | -7.3 | 3e-11 | 24/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.751×** | -7.3 | 3e-11 | 28/45 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.735×** | -7.3 | 3e-11 | 25/45 (NCI-H460, SHP-77, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.442×** | -7.1 | 7e-11 | 24/44 (NCI-H23, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.704×** | -6.8 | 5e-10 | 30/46 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.479×** | -6.4 | 8e-09 | 20/40 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.480×** | -6.4 | 8e-09 | 20/45 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.716×** | -6.2 | 2e-08 | 24/44 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -6.0 | 9e-08 | 26/45 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.722×** | -6.0 | 9e-08 | 25/45 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 121 | 0 | 23 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 95.4 | 0 | 21 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.8) |
| [[NCI-H2030 (line)]] | alt | 183 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -26.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.327× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -13.5) |
| [[A549 (line)]] | wt | 175 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 157 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.5) |
| [[HOP62 (line)]] | alt | 70.8 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.393× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 58.9 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -11.9) |
| [[A498 (line)]] | wt | 94.5 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.391× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 39.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.285× (z -10.9) |
| [[Hs 766T (line)]] | wt | 55.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -11.1) |
| [[LoVo (line)]] | wt | 30.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.8) |
| [[RKO (line)]] | wt | 78.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.8) |
| [[SNU-423 (line)]] | alt | 66.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.6) |
| [[A-172 (line)]] | wt | 36.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -10.1) |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.520× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 44.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK4]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SRGAP1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ADGRL4]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LINC00472]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF28]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MYL12A]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SHANK2]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[MBP]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TMEM156]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[BCAR3]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DERL1]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[IDH1]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[VPS35]] | -0.47 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[VDAC2]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[LNPK]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[EPRS1]] | -0.45 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[EIF2AK1]] | -0.45 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[TTLL7]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CANX]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3]] | B | BCAR3 activity raises KIFC3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.62× lower at baseline in the lines without BCAR3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises KIFC3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP5-DT]] | B | DUSP5-DT activity raises KIFC3's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without DUSP5-DT | 0.047 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[TMEM156]] | B | TMEM156 activity raises KIFC3's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without TMEM156 | 0.078 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ESM1]] | B | ESM1 activity raises KIFC3's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without ESM1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[PHLDA2]] | B | PHLDA2 activity raises KIFC3's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.50× lower at baseline in the lines without PHLDA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | C | KIFC3 activity lowers MIR1915HG's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 7.17× higher at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[DUSP4]] | C | KIFC3 activity raises DUSP4's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 5.39× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent |
| [[STAMBPL1]] | C | KIFC3 activity raises STAMBPL1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 5.15× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; co-absent with the target; its own permutation p |
| [[WTIP]] | C | KIFC3 activity lowers WTIP's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 5.04× higher at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[MBP]] | C | KIFC3 activity raises MBP's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 4.21× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[BCAR3]] | C | KIFC3 activity raises BCAR3's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 3.14× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent |
| [[PMEPA1]] | C | KIFC3 activity raises PMEPA1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 3.14× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[DUSP5-DT]] | C | KIFC3 activity raises DUSP5-DT's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[SVIL]] | C | KIFC3 activity raises SVIL's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent |
| [[ITGB5]] | C | KIFC3 activity raises ITGB5's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[MCL1]] | C | KIFC3 activity raises MCL1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |
| [[IDH1]] | C | KIFC3 activity lowers IDH1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 1.47× higher at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.6, 10.9); signed map (12.4, 43.0). **Vector** length 117, 32.4% of its response variance represented; |z| ≥ 3 in 1,273 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +4.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -6.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.8 | -8.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -6.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member C3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,758,217-57,863,053 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kinesins; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVG8](https://www.uniprot.org/uniprotkb/Q9BVG8) (Kinesin-like protein KIFC3):

> Minus-end microtubule-dependent motor protein. Involved in apically targeted transport (By similarity). Required for zonula adherens maintenance.

**Summary**, from NCBI Gene [3801](https://www.ncbi.nlm.nih.gov/gene/3801):

> This gene encodes a member of the kinesin-14 family of microtubule motors. Members of this family play a role in the formation, maintenance and remodeling of the bipolar mitotic spindle. The protein encoded by this gene has cytoplasmic functions in the interphase cells. It may also be involved in the final stages of cytokinesis. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:6326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6326) · Entrez [3801](https://www.ncbi.nlm.nih.gov/gene/3801) · UniProt [Q9BVG8](https://www.uniprot.org/uniprotkb/Q9BVG8) · Ensembl [ENSG00000140859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140859)

## Data

Gene col 6458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6458); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6458]; `tensor/DDL_lfc|DDL_z.npy` [6458]; `embed/gene_vectors.npy` [6458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6458 or target_col == 6458). Every well: [[KIFC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIFC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
