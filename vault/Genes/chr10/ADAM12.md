---
symbol: "ADAM12"
type: "gene"
col: 7324
ensembl_id: "ENSG00000148848"
name: "ADAM metallopeptidase domain 12"
location: "10q26.2"
module: 13
arm: "+"
pooled_cpm: 45.46
n_lines_expressing: 23
n_dd_up: 20
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 49
direction_downstream: 80
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAM12

*ADAM metallopeptidase domain 12* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +14.9, q 0e+00, up in 2 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +9.7, q 5e-20, up in 2 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.577× (z -8.0, q 6e-13, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETBP1]] (+0.68, fdr 7e-06), [[FRMD4A]] (+0.68, fdr 7e-06), [[NAV1]] (+0.66, fdr 7e-06); moves opposite to [[DLEU1]] (-0.46, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 80 go from it, the strongest it → [[CEP85L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +14.9 | 0e+00 | 2/20 (A-172, hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +11.2 | 2e-26 | 2/16 (A-172, hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +10.5 | 2e-23 | 1/18 (hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.7 | 5e-20 | 2/21 (NCI-H460, H4) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.0 | 6e-05 | 4/21 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +5.0 | 7e-05 | 12/20 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.37×** | +4.7 | 2e-04 | 11/20 (SNU-423, NCI-H1573, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.7 | 2e-04 | 7/21 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.4 | 9e-04 | 3/21 (A-172, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.009 | 7/20 (SW 900, SNU-423, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.019 | 2/20 (NCI-H460, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.026 | 1/21 (hTERT-HPNE) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.026 | 4/20 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.030 | 4/21 (J82, HS-578T, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.038 | 7/17 (NCI-H460, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.047 | 3/21 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.053 | 3/21 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.053 | 3/20 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Acetohexamide (drug)]] 5 µM |  | 1.14× | +2.9 | 0.095 | 1/21 (RPMI-7951) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -8.0 | 6e-13 | 17/21 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.726×** | -6.9 | 2e-09 | 15/21 (LOX-IMVI, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -6.2 | 9e-08 | 15/21 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.668×** | -6.1 | 1e-07 | 16/21 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -5.8 | 7e-07 | 11/21 (HOP62, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.717×** | -5.0 | 4e-05 | 11/20 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -4.8 | 1e-04 | 15/20 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.730×** | -4.8 | 1e-04 | 14/21 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.737×** | -4.6 | 2e-04 | 11/21 (A498, SW 1271, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.591×** | -4.2 | 0.002 | 9/20 (CHP-212, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.761×** | -4.1 | 0.002 | 6/21 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.002 | 14/21 (SW 1088, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -4.0 | 0.003 | 13/21 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.775×** | -3.9 | 0.004 | 12/21 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.838× | -3.7 | 0.007 | 3/21 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.766×** | -3.7 | 0.007 | 3/21 (CHP-212, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 121 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -16.4) |
| [[HOP62 (line)]] | alt | 82.6 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.123× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -25.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -13.4) |
| [[HS-578T (line)]] | alt | 453 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 255 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -12.6) |
| [[SNU-423 (line)]] | alt | 314 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.3) |
| [[J82 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 166 | 0 | 2 (1 ⚠) | — | [[Triamcinolone (drug)]] 0.5 µM 0.274× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 26.5 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.271× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0410× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.36× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -9.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-427 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETBP1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[FRMD4A]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[NAV1]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[INSYN2B]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[APCDD1L]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MSC-AS1]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[GLIS3]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[LRAT]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[RARB]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTS12]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[APBB1IP]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | -0.46 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 5, C 44. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAM12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CPQ]] | B | CPQ activity raises ADAM12's level | lines that do not express CPQ (15) vs lines expressing it (35) | 3.35× lower at baseline in the lines without CPQ | 0.047 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity lowers ADAM12's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 7.44× higher at baseline in the lines without NOXA1 | 0.077 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers ADAM12's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[PATJ]] | B | PATJ activity lowers ADAM12's level | lines that do not express PATJ (9) vs lines expressing it (41) | 8.43× higher at baseline in the lines without PATJ | 0.092 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent |
| [[TRPA1]] | C | TRPA1 activity raises ADAM12's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 8.05× lower at baseline in the lines without TRPA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises ADAM12's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 7.60× lower at baseline in the lines without INSYN2B | 0.007 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[RARB]] | C | RARB activity raises ADAM12's level | lines that do not express RARB (28) vs lines expressing it (22) | 7.81× lower at baseline in the lines without RARB | 0.008 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises ADAM12's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 5.82× lower at baseline in the lines without ITGB3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises ADAM12's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 6.53× lower at baseline in the lines without FRMD4A | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises ADAM12's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 6.36× lower at baseline in the lines without BICC1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises ADAM12's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 6.92× lower at baseline in the lines without LINC01583 | 0.017 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |

### Downstream of this gene

*80 arrows, 80 of them with an alert ⚠; grade A 0, B 18, C 62. Shown: the 12 strongest; 68 more arrows (68 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP85L]] | B | ADAM12 activity raises CEP85L's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.20× lower at baseline in the lines without ADAM12 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Methylthiouracil (drug)]] 0.05 µM | B | ADAM12 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.83× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Mebendazole (drug)]] 5 µM | B | ADAM12 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.69× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[CCDC149]] | B | ADAM12 activity raises CCDC149's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without ADAM12 | 0.065 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | ADAM12 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.80× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[RAI14]] | B | ADAM12 activity raises RAI14's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 3.22× lower at baseline in the lines without ADAM12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | ADAM12 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.77× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[RNF217]] | B | ADAM12 activity raises RNF217's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without ADAM12 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | B | ADAM12 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.84× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 0.5 µM | B | ADAM12 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.86× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | B | ADAM12 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.77× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | ADAM12 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 1.16× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 17.8); signed map (26.0, 48.0). **Vector** length 87.6, 30.6% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.2 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +5.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.1 | -6.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:126,012,381-126,388,477 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCMPMltna, MLTN |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Invadopodia formation; Signaling by EGFR; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43184](https://www.uniprot.org/uniprotkb/O43184) (Disintegrin and metalloproteinase domain-containing protein 12):

> Involved in skeletal muscle regeneration, specifically at the onset of cell fusion. Also involved in macrophage-derived giant cells (MGC) and osteoclast formation from mononuclear precursors (By similarity).

**Summary**, from NCBI Gene [8038](https://www.ncbi.nlm.nih.gov/gene/8038):

> This gene encodes a member of a family of proteins that are structurally related to snake venom disintegrins and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. Expression of this gene has been used as a maternal serum marker for pre-natal development. Alternative splicing results in multiple transcript variants encoding different isoforms. Shorter isoforms are secreted, …

**Accessions** — [HGNC:190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:190) · Entrez [8038](https://www.ncbi.nlm.nih.gov/gene/8038) · UniProt [O43184](https://www.uniprot.org/uniprotkb/O43184) · Ensembl [ENSG00000148848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148848)

## Data

Gene col 7324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7324); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7324]; `tensor/DDL_lfc|DDL_z.npy` [7324]; `embed/gene_vectors.npy` [7324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7324 or target_col == 7324). Every well: [[ADAM12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
