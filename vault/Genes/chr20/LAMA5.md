---
symbol: "LAMA5"
type: "gene"
col: 5099
ensembl_id: "ENSG00000130702"
name: "laminin subunit alpha 5"
location: "20q13.33"
module: 2
arm: "+"
pooled_cpm: 73.46
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LAMA5

*laminin subunit alpha 5* — 20q13.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.409× (z -11.4, q 4e-27, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF16]] (+0.66, fdr 7e-06), [[NCOR2]] (+0.63, fdr 7e-06), [[FOXP4]] (+0.60, fdr 1e-05); moves opposite to [[PCF11-AS1]] (-0.53, fdr 3e-05), [[PIGBOS1]] (-0.44, fdr 2e-05), [[FAAP24]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TNS4]] → it (grade B ⚠); 11 go from it, the strongest it → [[RPS6KA4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.32× | +3.5 | 0.22 | 22/38 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.28× | +3.2 | 0.42 | 13/38 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.409×** | -11.4 | 4e-27 | 28/37 (A549, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -10.6 | 5e-24 | 29/38 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.495×** | -8.9 | 9e-17 | 26/37 (A549, Hs 766T, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -8.9 | 1e-16 | 26/36 (NCI-H2030, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -8.7 | 5e-16 | 31/36 (A549, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.516×** | -8.4 | 4e-15 | 29/37 (A549, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.598×** | -6.3 | 3e-08 | 24/36 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.671×** | -5.1 | 3e-05 | 22/37 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.764×** | -4.8 | 9e-05 | 24/37 (SW1417, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.765×** | -4.8 | 9e-05 | 23/36 (NCI-H2030, A549, …) | two highest doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.677×** | -4.8 | 1e-04 | 24/39 (SW480, J82, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -4.4 | 5e-04 | 23/37 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -3.8 | 0.007 | 19/38 (KATO III, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.738×** | -3.7 | 0.008 | 18/37 (NCI-H460, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.012 | 21/37 (Hs 766T, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.018 | 19/37 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.067 | 18/38 (CFPAC-1, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 146 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -14.0) |
| [[A549 (line)]] | wt | 170 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -17.5) |
| [[SW480 (line)]] | alt | 81.6 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -14.9) |
| [[Hs 766T (line)]] | wt | 342 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -14.6) |
| [[HT-29 (line)]] | alt | 118 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -13.4) |
| [[LoVo (line)]] | wt | 39.5 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.287× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -12.3) |
| [[A-172 (line)]] | wt | 92.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.310× (z -8.6) |
| [[LS 180 (line)]] | wt | 49.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -11.4) |
| [[PANC-1 (line)]] | alt | 86.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -9.5) |
| [[SW1417 (line)]] | alt | 50.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.8) |
| [[A-427 (line)]] | wt | 35.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.240× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 139 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -10.9) |
| [[HCT15 (line)]] | alt | 73.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.7) |
| [[J82 (line)]] | alt | 59.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.8) |
| [[KATO III (line)]] | alt | 101 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -14.1) |
| [[HS-578T (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.3) |
| [[A498 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 91.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF16]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[NCOR2]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FOXP4]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 | same gene group |
| [[INF2]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[IGSF9]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[P2RY2]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MPRIP]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RPH3AL]] | +0.53 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ITPK1]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HR]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MAPK11]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCF11-AS1]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PIGBOS1]] | -0.44 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[FAAP24]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[GTF2IRD2B]] | -0.44 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PIGP]] | -0.43 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CNPY2]] | -0.43 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SCAND1]] | -0.42 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[FDX2]] | -0.42 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ATP6V1F]] | -0.42 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MRPS36]] ⚠ | -0.42 | -0.38 / -0.46 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS4]] | B | TNS4 activity raises LAMA5's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.58× lower at baseline in the lines without TNS4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[P2RY2]] | B | P2RY2 activity raises LAMA5's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without P2RY2 | 0.023 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[MMP15]] | B | MMP15 activity raises LAMA5's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 3.67× lower at baseline in the lines without MMP15 | 0.036 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[EPPK1]] | B | EPPK1 activity raises LAMA5's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without EPPK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[ITGB4]] | B | ITGB4 activity raises LAMA5's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without ITGB4 | 0.057 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[CCDC9B]] | B | CCDC9B activity raises LAMA5's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without CCDC9B | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |
| [[BCAM]] | B | BCAM activity raises LAMA5's level | lines that do not express BCAM (8) vs lines expressing it (42) | 3.23× lower at baseline in the lines without BCAM | 0.068 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[TNS4]] | B | TNS4 activity strengthens LAMA5's drug response | lines that do not express TNS4 (22) vs lines expressing it (16) | the lines without TNS4 respond 0.54× as strongly (z diff +2.41); strongest at Idarubicin (hydrochloride) 5 µM: 0.67x vs 0.45x (z diff +3.7) | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6; target measured in part of the lines; artifact flags |
| [[MAPK11]] | C | MAPK11 activity raises LAMA5's level | lines that do not express MAPK11 (3) vs lines expressing it (47) | 5.80× lower at baseline in the lines without MAPK11 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: ADCY7, DBN1, LAMC1; maybe low, not absent |
| [[PLEC]] | C | PLEC activity raises LAMA5's level | lines that do not express PLEC (3) vs lines expressing it (47) | 3.34× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6KA4]] | B | LAMA5 activity raises RPS6KA4's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without LAMA5 | 0.020 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[MMP15]] | B | LAMA5 activity raises MMP15's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without LAMA5 | 0.026 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[SEMA3F]] | B | LAMA5 activity raises SEMA3F's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without LAMA5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[LMNB2]] | B | LAMA5 activity raises LMNB2's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without LAMA5 | 0.049 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[PLCB3]] | B | LAMA5 activity raises PLCB3's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without LAMA5 | 0.052 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[MYO18A]] | B | LAMA5 activity raises MYO18A's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without LAMA5 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[SLCO4A1]] | B | LAMA5 activity raises SLCO4A1's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without LAMA5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[SLC4A11]] | B | LAMA5 activity raises SLC4A11's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without LAMA5 | 0.067 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[PCNX3]] | B | LAMA5 activity raises PCNX3's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without LAMA5 | 0.079 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[ABCA2]] | B | LAMA5 activity raises ABCA2's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without LAMA5 | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[NBEAL2]] | B | LAMA5 activity raises NBEAL2's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without LAMA5 | 0.097 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (15.0, -5.3); signed map (-11.0, 30.2). **Vector** length 96.7, 27.0% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.6 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -1.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Altretamine (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.7 | -4.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -10.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit alpha 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,307,955-62,367,312 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Laminin subunits; MicroRNA protein coding host genes |
| Reactome | 22 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O15230](https://www.uniprot.org/uniprotkb/O15230) (Laminin subunit alpha-5):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components. Plays a role in the regulation of skeletogenesis, through a mechanism that involves integrin-mediated signaling and PTK2B/PYK2.

**Summary**, from NCBI Gene [3911](https://www.ncbi.nlm.nih.gov/gene/3911):

> This gene encodes one of the vertebrate laminin alpha chains. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively) and they form a cruciform …

**Accessions** — [HGNC:6485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6485) · Entrez [3911](https://www.ncbi.nlm.nih.gov/gene/3911) · UniProt [O15230](https://www.uniprot.org/uniprotkb/O15230) · Ensembl [ENSG00000130702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130702)

## Data

Gene col 5099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5099); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5099]; `tensor/DDL_lfc|DDL_z.npy` [5099]; `embed/gene_vectors.npy` [5099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5099 or target_col == 5099). Every well: [[LAMA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
