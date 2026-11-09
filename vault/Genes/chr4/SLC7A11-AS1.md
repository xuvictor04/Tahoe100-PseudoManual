---
symbol: "SLC7A11-AS1"
type: "gene"
col: 14657
ensembl_id: "ENSG00000250033"
name: "SLC7A11 antisense RNA 1"
location: "4q28.3"
module: 165
arm: "+"
pooled_cpm: 17.19
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# SLC7A11-AS1

*SLC7A11 antisense RNA 1* — 4q28.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.99× (z +11.9, q 7e-30, up in 14 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +11.7, q 6e-29, up in 22 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.196×, LOX-IMVI 0.341×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.111×); [[Neratinib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0912×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OPCML]] (+0.59, fdr 1e-05), [[LRRC4C]] (+0.58, fdr 1e-05), [[LINC02511]] (+0.58, fdr 2e-05); moves opposite to [[CPD]] (-0.60, fdr 1e-05), [[COPS8]] (-0.47, fdr 7e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GDPD4]] → it (grade B ⚠); 5 go from it, the strongest it → [[XKR4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +11.9 | 7e-30 | 14/23 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +11.7 | 6e-29 | 22/31 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +9.1 | 2e-17 | 24/35 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +8.6 | 8e-16 | 4/11 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +6.7 | 3e-09 | 18/31 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.5 | 9e-09 | 15/33 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.3 | 3e-08 | 7/14 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.0 | 1e-07 | 14/28 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +5.5 | 3e-06 | 10/26 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.8 | 8e-05 | 10/31 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.5 | 4e-04 | 15/37 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +4.3 | 9e-04 | 9/34 (SK-MEL-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +4.2 | 0.001 | 4/11 (SNU-423, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 3/31 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.005 | 10/35 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.7 | 0.007 | 2/27 (SW 900, NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.013 | 10/34 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.055 | 8/35 (CFPAC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.099 | 9/37 (J82, HOP62, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.196×, LOX-IMVI 0.341×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.111×); [[Neratinib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0912×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 67.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 4.87 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +11.1) | [[Neratinib (drug)]] 0.05 µM 0.0912× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +15.5) | — |
| [[HOP62 (line)]] | alt | 4.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 419 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.1) |
| [[SNU-423 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +9.0) | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPCML]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[XKR4]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[RERGL]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[LINC00616]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ATP8A2]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[L3MBTL2-AS1]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 | same gene group |
| [[SLC8A1-AS1]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 | same gene group |
| [[SYT16]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPD]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[COPS8]] | -0.47 | -0.37 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDPD4]] | B | GDPD4 activity raises SLC7A11-AS1's level | lines that do not express GDPD4 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without GDPD4 | 0.092 | ⚠ within organs, on part of the lines; also absent: STEAP4, ENSG00000275016, DDX43; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR4]] | B | SLC7A11-AS1 activity lowers XKR4's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without SLC7A11-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |
| [[ERC2]] | B | SLC7A11-AS1 activity lowers ERC2's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.98× higher at baseline in the lines without SLC7A11-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |
| [[LINC00616]] | B | SLC7A11-AS1 activity raises LINC00616's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without SLC7A11-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |
| [[FLRT1]] | B | SLC7A11-AS1 activity lowers FLRT1's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.30× higher at baseline in the lines without SLC7A11-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |
| [[B4GALT1]] | B | SLC7A11-AS1 activity raises B4GALT1's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without SLC7A11-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.6, 30.5); signed map (32.2, 17.1). **Vector** length 51.4, 7.89% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SLC7A11 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q28.3 — chr4:138,057,464-138,178,177 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000512786 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44064) · Entrez [641364](https://www.ncbi.nlm.nih.gov/gene/641364) · Ensembl [ENSG00000250033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250033)

## Data

Gene col 14657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14657); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14657]; `tensor/DDL_lfc|DDL_z.npy` [14657]; `embed/gene_vectors.npy` [14657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14657 or target_col == 14657). Every well: [[SLC7A11-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A11-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
