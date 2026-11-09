---
symbol: "ULBP2"
type: "gene"
col: 5156
ensembl_id: "ENSG00000131015"
name: "UL16 binding protein 2"
location: "6q25.1"
module: 3
arm: "+"
pooled_cpm: 6.94
n_lines_expressing: 41
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ULBP2

*UL16 binding protein 2* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.42× (z +17.9, q 0e+00, up in 35 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (SNU-423 0.0723×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.164×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORMDL2]] (+0.65, fdr 3e-05), [[FKBP2]] (+0.61, fdr 7e-06, ⚠ FKBP2 in the vector space only through flagged drug-doses), [[RABGEF1]] (+0.59, fdr 3e-05), [[CIB1]] (+0.59, fdr 8e-05); moves opposite to [[SSRP1]] (-0.63, fdr 1e-05), [[BACE1-AS]] (-0.63, fdr 1e-04), [[MRRF]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CNBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.42×** | +17.9 | 0e+00 | 35/35 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.25×** | +9.8 | 2e-20 | 37/38 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.96×** | +9.4 | 2e-18 | 36/38 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.70×** | +8.5 | 2e-15 | 27/28 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **3.26×** | +8.0 | 1e-13 | 33/37 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.17×** | +7.8 | 4e-13 | 21/24 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.91×** | +7.0 | 2e-10 | 26/33 (SW480, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.03×** | +6.8 | 7e-10 | 26/38 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.74×** | +6.6 | 3e-09 | 13/14 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.51×** | +6.0 | 1e-07 | 29/35 (SW480, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +5.1 | 2e-05 | 28/35 (RKO, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +4.5 | 3e-04 | 27/38 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +4.1 | 0.002 | 20/35 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.003 | 18/36 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.003 | 15/38 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.025 | 13/38 (LS 180, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.47×** | +3.3 | 0.028 | 11/34 (LS 180, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.43×** | +3.3 | 0.032 | 16/32 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.34×** | +3.1 | 0.049 | 5/35 (LoVo, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.30×** | +3.1 | 0.057 | 9/36 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +2.9 | 0.096 | 11/36 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5156.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (SNU-423 0.0723×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.164×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.605× | -3.4 | 0.28 | 17/37 (A-172, Hs 766T, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.605× | -3.3 | 0.28 | 16/37 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | 0.722× | -3.2 | 0.28 | 13/38 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.90 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.0× (z +17.4) | — |
| [[LS 180 (line)]] | wt | 12.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 4.33 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 8.22 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.0) | [[Pimozide (drug)]] 0.05 µM 0.0723× (z -9.8) |
| [[A-172 (line)]] | wt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.2) | — |
| [[A498 (line)]] | wt | 6.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +9.9) | — |
| [[A549 (line)]] | wt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 5.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +9.7) | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.7) |
| [[HCT15 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 4.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.99× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 6.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 9.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +9.1) | — |
| [[J82 (line)]] | alt | 7.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +11.5) | — |
| [[LoVo (line)]] | wt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 4.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.41× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 9.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.14× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 8.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.35× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.5) | — |
| [[A-427 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORMDL2]] | +0.65 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[FKBP2]] ⚠ | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RABGEF1]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CIB1]] | +0.59 | +0.37 / +0.69 | both halves | 8e-05 |  |
| [[WDR44]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RABAC1]] | +0.58 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[RNF122]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TMEM134]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MORC3]] | +0.58 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[GLTP]] | +0.57 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[GUK1]] | +0.56 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[OST4]] | +0.56 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[SELENOK]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSRP1]] | -0.63 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[BACE1-AS]] | -0.63 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[MRRF]] | -0.56 | -0.36 / -0.64 | both halves | 1e-04 |  |
| [[PFAS]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[NONO]] | -0.55 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ATIC]] | -0.55 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[HNRNPR]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[AIFM1]] | -0.54 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[LAS1L]] | -0.53 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[MTHFD1]] | -0.53 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[U2SURP]] | -0.53 | -0.38 / -0.60 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ULBP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TPBG]] | B | TPBG activity raises ULBP2's level | lines that do not express TPBG (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without TPBG | 0.060 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNBP]] | B | ULBP2 activity lowers CNBP's level | lines that do not express ULBP2 (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without ULBP2 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM158]] | B | ULBP2 activity raises TMEM158's level | lines that do not express ULBP2 (9) vs lines expressing it (41) | 3.29× lower at baseline in the lines without ULBP2 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-29.5, -36.5); signed map (-16.5, 17.9). **Vector** length 66.7, 15.9% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.2 | +7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.9 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | UL16 binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,942,014-149,949,235 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAET1H |
| Gene groups (HGNC) | Retinoic acid early transcript 1 family |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZM5](https://www.uniprot.org/uniprotkb/Q9BZM5) (UL16-binding protein 2):

> Binds and activates the KLRK1/NKG2D receptor, mediating natural killer cell cytotoxicity.

**Summary**, from NCBI Gene [80328](https://www.ncbi.nlm.nih.gov/gene/80328):

> This gene encodes a major histocompatibility complex (MHC) class I-related molecule that binds to the NKG2D receptor on natural killer (NK) cells to trigger release of multiple cytokines and chemokines that in turn contribute to the recruitment and activation of NK cells. The encoded protein undergoes further processing to generate the mature protein that is either anchored to membrane via a glycosylphosphatidylinositol moiety, or secreted. Many malignant cells secrete the encoded protein to …

**Accessions** — [HGNC:14894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14894) · Entrez [80328](https://www.ncbi.nlm.nih.gov/gene/80328) · UniProt [Q9BZM5](https://www.uniprot.org/uniprotkb/Q9BZM5) · Ensembl [ENSG00000131015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131015)

## Data

Gene col 5156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5156); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5156]; `tensor/DDL_lfc|DDL_z.npy` [5156]; `embed/gene_vectors.npy` [5156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5156 or target_col == 5156). Every well: [[ULBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
