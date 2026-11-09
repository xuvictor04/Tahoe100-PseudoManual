---
symbol: "ANKHD1-EIF4EBP3"
type: "gene"
col: 14907
ensembl_id: "ENSG00000254996"
name: "ANKHD1-EIF4EBP3 readthrough"
location: "5q31.3"
module: 23
arm: "+"
pooled_cpm: 11.08
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ANKHD1-EIF4EBP3

*ANKHD1-EIF4EBP3 readthrough* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +11.6, q 1e-28, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.544× (z -6.4, q 7e-08, down in 21 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.705× (z -4.0, q 0.013, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.110×, SNU-423 0.128×, NCI-H1573 0.136×, PANC-1 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.104×, PANC-1 0.170×, HOP62 0.115×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (KATO III 0.107×, NCI-H2030 0.0885×, NCI-H1573 0.174×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cilostazol (drug)]] 0.05 µM in 1 line (SW 900 0.0564×); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (SNU-1 0.0765×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (C32 0.0898×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4EBP3]] (+0.78, fdr 7e-06, ⚠ same locus), [[ASH1L]] (+0.76, fdr 7e-06), [[MED13]] (+0.74, fdr 3e-05), [[GTF2IRD2B]] (+0.73, fdr 8e-06); moves opposite to [[SDHAF3]] (-0.74, fdr 1e-05), [[ACTR5]] (-0.64, fdr 3e-05), [[ELP1]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +11.6 | 1e-28 | 33/46 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.6 | 1e-28 | 36/44 (AsPC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +9.9 | 1e-20 | 36/47 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +9.6 | 1e-19 | 34/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 2e-05 | 22/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.001 | 19/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.033 | 15/48 (A-172, A498, …) | rises with dose |  |
| [[Resveratrol (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.047 | 11/48 (HCT15, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14907.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.110×, SNU-423 0.128×, NCI-H1573 0.136×, PANC-1 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.104×, PANC-1 0.170×, HOP62 0.115×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (KATO III 0.107×, NCI-H2030 0.0885×, NCI-H1573 0.174×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cilostazol (drug)]] 0.05 µM in 1 line (SW 900 0.0564×); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (SNU-1 0.0765×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (C32 0.0898×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.544×** | -6.4 | 7e-08 | 21/28 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -4.0 | 0.013 | 21/45 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.706×** | -4.0 | 0.013 | 19/34 (KATO III, SNU-423, …) | all doses, flat | composition shift |
| [[Roxadustat (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.016 | 16/47 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.731×** | -3.6 | 0.039 | 17/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.736×** | -3.5 | 0.045 | 17/48 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.734×** | -3.4 | 0.055 | 18/39 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.738×** | -3.3 | 0.061 | 16/39 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | 0.760× | -3.0 | 0.16 | 14/22 (SNU-423, MIA PaCa-2, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 8.25 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.153× (z -9.5) |
| [[HOP62 (line)]] | alt | 10.2 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 17.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0853× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 9.98 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0898× (z -9.5) |
| [[HT-29 (line)]] | alt | 15.2 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +8.7) | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[NCI-H2030 (line)]] | alt | 9.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0974× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0878× (z -9.1) |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0765× (z -9.6) |
| [[SW 900 (line)]] | alt | 8.01 | 0 | 1 | — | [[Cilostazol (drug)]] 0.05 µM 0.0564× (z -10.4) |
| [[A-172 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4EBP3]] | +0.78 | +0.82 / +0.65 | both halves | 7e-06 | STRING 914; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ASH1L]] | +0.76 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MED13]] | +0.74 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | +0.73 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[LINC00571]] | +0.73 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[CREBBP]] | +0.73 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[AEBP2]] | +0.72 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | +0.72 | +0.79 / +0.41 | both halves | 4e-05 |  |
| [[RBBP6]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.81 / +0.39 | both halves | 6e-05 |  |
| [[CMYA5]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.71 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[KANSL1L]] | +0.71 | +0.70 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.74 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.64 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ELP1]] | -0.63 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[HLTF]] | -0.63 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[WASF3]] | -0.62 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[GTPBP3]] | -0.62 | -0.61 / -0.29 | both halves | 3e-04 |  |
| [[METAP1]] | -0.61 | -0.72 / -0.31 | both halves | 2e-04 |  |
| [[SSX2IP]] | -0.61 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PPP5C]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[GPD1L]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PIK3R2]] | -0.60 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[SKP2]] | -0.60 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKHD1-EIF4EBP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ANKHD1-EIF4EBP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers ANKHD1-EIF4EBP3's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.0, 10.4); signed map (21.5, -9.3). **Vector** length 97.1, 20.8% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +11.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.8 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -4.5 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ANKHD1-EIF4EBP3 readthrough |
| Locus type | readthrough (other) |
| Location | 5q31.3 — chr5:140,401,908-140,549,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MASK-BP3 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [404734](https://www.ncbi.nlm.nih.gov/gene/404734):

> The ANKHD1-EIF4EBP3 mRNA is an infrequent but naturally occurring readthrough transcript of the neighboring ANKHD1 and EIF4EBP3 genes. This readthrough transcript encodes a protein composed mostly of the multiple ankyrin repeats, single KH-domain protein, with its C-terminus encoded in a different reading frame from the shared portion of the EIF4EBP3 gene. The significance of this readthrough mRNA and the function of its protein product have not yet been determined. [provided by RefSeq, Nov …

**Accessions** — [HGNC:33530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33530) · Entrez [404734](https://www.ncbi.nlm.nih.gov/gene/404734) · Ensembl [ENSG00000254996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254996)

## Data

Gene col 14907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14907); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14907]; `tensor/DDL_lfc|DDL_z.npy` [14907]; `embed/gene_vectors.npy` [14907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14907 or target_col == 14907). Every well: [[ANKHD1-EIF4EBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKHD1-EIF4EBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
