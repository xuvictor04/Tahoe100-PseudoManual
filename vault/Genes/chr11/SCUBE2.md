---
symbol: "SCUBE2"
type: "gene"
col: 10602
ensembl_id: "ENSG00000175356"
name: "signal peptide, CUB domain and EGF like domain containing 2"
location: "11p15.4"
module: 39
arm: "+"
pooled_cpm: 11.06
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 16
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SCUBE2

*signal peptide, CUB domain and EGF like domain containing 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.64× (z +15.2, q 0e+00, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.348× (z -8.8, q 7e-16, down in 29 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.388× (z -7.9, q 8e-13, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.82, fdr 7e-06), [[SLC22A1]] (+0.82, fdr 7e-06), [[MYOCOS]] (+0.81, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NEK10]] → it (grade B ⚠); 16 go from it, the strongest it → [[LINC01355]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.64×** | +15.2 | 0e+00 | 32/39 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.86×** | +11.2 | 1e-26 | 27/38 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.63×** | +8.0 | 2e-13 | 30/39 (A-172, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.52×** | +7.2 | 7e-11 | 31/39 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.02×** | +5.8 | 7e-07 | 29/41 (PANC-1, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.6 | 5e-04 | 10/41 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.003 | 21/40 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.004 | 17/40 (J82, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.005 | 18/40 (AN3 CA, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 18/39 (NCI-H1792, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +3.7 | 0.010 | 16/38 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.036 | 16/38 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.08×** | +3.2 | 0.065 | 11/37 (SNU-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.066 | 13/40 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.01×** | +3.0 | 0.095 | 6/41 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.348×** | -8.8 | 7e-16 | 29/38 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.388×** | -7.9 | 8e-13 | 27/40 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -6.8 | 2e-09 | 28/39 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.484×** | -6.1 | 2e-07 | 26/40 (LOX-IMVI, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -4.9 | 1e-04 | 22/34 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.587×** | -4.2 | 0.002 | 21/37 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **0.427×** | -3.7 | 0.017 | 17/35 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.676× | -3.2 | 0.10 | 15/39 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.687× | -3.2 | 0.10 | 13/40 (COLO 205, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.680× | -3.1 | 0.10 | 15/41 (H4, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 21.4 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +8.9) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0945× (z -9.5) |
| [[C-33 A (line)]] | alt | 28.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0836× (z -10.8) |
| [[LoVo (line)]] | wt | 4.35 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.148× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 13.4× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0505× (z -12.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 19.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +12.4) | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.99 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +13.1) | [[Imiquimod (maleate) (drug)]] 5 µM 0.0769× (z -9.8) |
| [[SW480 (line)]] | alt | 5.25 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +15.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0610× (z -13.4) ⚠ toxic |
| [[HOP62 (line)]] | alt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0355× (z -15.0) ⚠ toxic |
| [[J82 (line)]] | alt | 19.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0853× (z -11.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.131× (z -9.1) |
| [[SNU-423 (line)]] | alt | 20.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -9.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +10.1) | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0647× (z -10.3) |
| [[COLO 205 (line)]] | alt | 6.05 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0592× (z -9.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 5.90 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0776× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0784× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 8.78 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0459× (z -8.9) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0613× (z -11.9) |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0813× (z -9.4) |
| [[A498 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.82 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.82 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.81 | +0.85 / +0.72 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[DPYS]] | +0.81 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.80 | +0.83 / +0.68 | both halves | 7e-06 |  |
| [[OIT3]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.80 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[MPP4]] | +0.79 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.79 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.78 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK10]] | B | NEK10 activity raises SCUBE2's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 3.51× lower at baseline in the lines without NEK10 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[CD226]] | B | CD226 activity raises SCUBE2's level | lines that do not express CD226 (7) vs lines expressing it (43) | 2.75× lower at baseline in the lines without CD226 | 0.061 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[CFAP161]] | B | CFAP161 activity raises SCUBE2's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without CFAP161 | 0.074 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent |
| [[ACOT12]] | B | ACOT12 activity raises SCUBE2's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 2.88× lower at baseline in the lines without ACOT12 | 0.098 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises SCUBE2's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 3.30× lower at baseline in the lines without ITPR2-AS1 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01355]] | B | SCUBE2 activity raises LINC01355's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without SCUBE2 | 0.008 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[ALPK3]] | B | SCUBE2 activity lowers ALPK3's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.56× higher at baseline in the lines without SCUBE2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[ITPR2-AS1]] | B | SCUBE2 activity raises ITPR2-AS1's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without SCUBE2 | 0.021 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[SFXN5]] | B | SCUBE2 activity raises SFXN5's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without SCUBE2 | 0.039 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[ANKAR]] | B | SCUBE2 activity raises ANKAR's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without SCUBE2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[MYH3]] | B | SCUBE2 activity raises MYH3's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without SCUBE2 | 0.051 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[PHEX]] | B | SCUBE2 activity raises PHEX's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without SCUBE2 | 0.059 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[MPP4]] | B | SCUBE2 activity raises MPP4's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.20× lower at baseline in the lines without SCUBE2 | 0.063 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[CAVIN4]] | B | SCUBE2 activity raises CAVIN4's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.54× lower at baseline in the lines without SCUBE2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[HPN]] | B | SCUBE2 activity lowers HPN's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.12× higher at baseline in the lines without SCUBE2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| cells under [[Balsalazide (sodium hydrate) (drug)]] 5 µM | B | SCUBE2 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express SCUBE2 (7) vs lines expressing it (41) | the lines without SCUBE2: 0.87× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[TIAM2]] | B | SCUBE2 activity raises TIAM2's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without SCUBE2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.855). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, -13.1); signed map (18.6, 8.5). **Vector** length 112, 27.3% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.2 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.2 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.6 | +7.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.7 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -8.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.4 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | signal peptide, CUB domain and EGF like domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,019,476-9,138,114 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cegf1, Cegb1, FLJ16792 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 3 pathways, smallest: Release of Hh-Np from the secreting cell; Hedgehog ligand biogenesis; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ36](https://www.uniprot.org/uniprotkb/Q9NQ36) (Signal peptide, CUB and EGF-like domain-containing protein 2):

> Lipid-binding protein carrier required for sonic hedgehog (SHH) long-range signaling: binds to the dually lipid-modified Sonic hedgehog protein N-product (ShhN) and promotes its release from producing cells, allowing it to act as a morphogen for distant signaling. ShhN is then transferred to the CDON-BOC heterodimer and GAS1 coreceptors to reach its target, the patched receptor (PTCH1 or PTCH2), followed by activation of the smoothened signaling pathway. May also enhance the proteolytic …

**Summary**, from NCBI Gene [57758](https://www.ncbi.nlm.nih.gov/gene/57758):

> Predicted to enable hedgehog family protein binding activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within several processes, including positive regulation of chondrocyte proliferation; positive regulation of osteoblast differentiation; and positive regulation of smoothened signaling pathway. Predicted to be located in extracellular region. Predicted to be active in cell surface and obsolete extracellular space. [provided by Alliance of Genome …

**Accessions** — [HGNC:30425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30425) · Entrez [57758](https://www.ncbi.nlm.nih.gov/gene/57758) · UniProt [Q9NQ36](https://www.uniprot.org/uniprotkb/Q9NQ36) · Ensembl [ENSG00000175356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175356)

## Data

Gene col 10602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10602); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10602]; `tensor/DDL_lfc|DDL_z.npy` [10602]; `embed/gene_vectors.npy` [10602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10602 or target_col == 10602). Every well: [[SCUBE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCUBE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
