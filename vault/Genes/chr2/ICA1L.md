---
symbol: "ICA1L"
type: "gene"
col: 8723
ensembl_id: "ENSG00000163596"
name: "islet cell autoantigen 1 like"
location: "2q33.2"
module: 23
arm: "+"
pooled_cpm: 12.27
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ICA1L

*islet cell autoantigen 1 like* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +25.4, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.696× (z -6.8, q 7e-09, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (64 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 36 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM11]] (+0.70, fdr 2e-05), [[F8]] (+0.70, fdr 1e-04), [[SEPTIN7-DT]] (+0.69, fdr 9e-05); moves opposite to [[WRAP73]] (-0.57, fdr 4e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +25.4 | 0e+00 | 43/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +12.3 | 3e-32 | 28/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.9 | 7e-10 | 21/46 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.6 | 5e-09 | 15/37 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +6.2 | 9e-08 | 10/27 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.0 | 2e-07 | 8/21 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 7e-07 | 19/46 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +5.4 | 4e-06 | 15/47 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 3e-04 | 16/47 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 4e-04 | 15/47 (A-427, C-33 A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.4 | 6e-04 | 12/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 7e-04 | 13/46 (A498, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 15/45 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.5 | 0.020 | 12/48 (A498, NCI-H1573, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.20× | +3.4 | 0.024 | 10/45 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.024 | 12/47 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.051 | 8/46 (HS-578T, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -6.8 | 7e-09 | 22/45 (A-172, HS-578T, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -6.3 | 8e-08 | 17/47 (C-33 A, A549, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.718×** | -6.2 | 1e-07 | 16/47 (A-427, A549, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.748×** | -5.2 | 3e-05 | 17/43 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **0.759×** | -5.1 | 3e-05 | 15/42 (SNU-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -4.6 | 4e-04 | 14/47 (HEC-1-A, AN3 CA, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.627×** | -4.6 | 4e-04 | 11/47 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.801×** | -4.1 | 0.002 | 17/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.812×** | -3.9 | 0.007 | 14/47 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.838× | -3.3 | 0.056 | 5/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.831×** | -3.3 | 0.059 | 5/48 (SK-MEL-2, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.843× | -3.2 | 0.068 | 11/46 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.230× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 14.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +16.2) | — |
| [[SW480 (line)]] | alt | 9.73 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +14.5) | — |
| [[A-427 (line)]] | wt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[LJI308 (drug)]] 0.05 µM 0.200× (z -9.0) |
| [[A498 (line)]] | wt | 7.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0843× (z -10.1) |
| [[BT-474 (line)]] | alt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 8.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 6.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 8.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +8.5) | — |
| [[LoVo (line)]] | wt | 6.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 7.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +9.2) | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 36 of them with an alert (⚠; 36 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM11]] | +0.70 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[F8]] | +0.70 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | +0.69 | +0.66 / +0.37 | both halves | 9e-05 |  |
| [[LRRC37A3]] | +0.69 | +0.66 / +0.32 | both halves | 2e-04 |  |
| [[LRRC8C-DT]] | +0.68 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | +0.67 | +0.66 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[PCBP1-AS1]] | +0.66 | +0.61 / +0.22 | both halves | 6e-04 |  |
| [[PBLD]] | +0.65 | +0.58 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[MAD2L1-DT]] | +0.65 | +0.68 / +0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[PKN2-AS1]] | +0.65 | +0.67 / +0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[PPP1R12A-AS2]] | +0.65 | +0.66 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[ZCWPW1]] | +0.64 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[RAD9B]] | +0.64 | +0.61 / +0.27 | both halves | 3e-04 |  |
| [[TSTD3]] | +0.64 | +0.56 / +0.22 | both halves | 6e-04 |  |
| [[HOXB-AS1]] | +0.63 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[PJVK]] | +0.62 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[USP38-DT]] | +0.62 | +0.61 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.57 | -0.36 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers ICA1L's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.21× higher at baseline in the lines without ZNF341-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity raises ICA1L's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 1.79× lower at baseline in the lines without DCLK2 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[LINC03041]] | B | LINC03041 activity raises ICA1L's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 1.59× lower at baseline in the lines without LINC03041 | 0.042 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[MRAS]] | B | MRAS activity raises ICA1L's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without MRAS | 0.048 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[TOP2A]] | B | TOP2A activity lowers ICA1L's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.3, 15.8); signed map (27.0, -9.3). **Vector** length 75.7, 12.6% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +25.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.3 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.2 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -6.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -4.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | islet cell autoantigen 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:202,773,150-202,871,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ALS2CR15, ALS2CR14 |
| Gene groups (HGNC) | AH domain containing |
| Matched by | ensembl_id |

UniProt [Q8NDH6](https://www.uniprot.org/uniprotkb/Q8NDH6) carries no function annotation.

**Summary**, from NCBI Gene [130026](https://www.ncbi.nlm.nih.gov/gene/130026):

> Predicted to enable membrane curvature sensor activity. Predicted to be involved in membrane bending and regulation of secretion. Predicted to act upstream of or within spermatid development. Predicted to be located in acrosomal vesicle. Predicted to be active in secretory granule membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14442) · Entrez [130026](https://www.ncbi.nlm.nih.gov/gene/130026) · UniProt [Q8NDH6](https://www.uniprot.org/uniprotkb/Q8NDH6) · Ensembl [ENSG00000163596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163596)

## Data

Gene col 8723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8723); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8723]; `tensor/DDL_lfc|DDL_z.npy` [8723]; `embed/gene_vectors.npy` [8723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8723 or target_col == 8723). Every well: [[ICA1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICA1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
