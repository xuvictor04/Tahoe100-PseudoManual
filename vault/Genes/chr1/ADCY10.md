---
symbol: "ADCY10"
type: "gene"
col: 6697
ensembl_id: "ENSG00000143199"
name: "adenylate cyclase 10"
location: "1q24.2"
module: 37
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 10
n_dd_up_clean: 30
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ADCY10

*adenylate cyclase 10* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.62× (z +24.1, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Berbamine (drug)]] 0.05 µM: 0.566× (z -5.0, q 3e-04, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRD1]] (+0.78, fdr 7e-06), [[SNX31]] (+0.77, fdr 7e-06), [[CD247]] (+0.77, fdr 7e-06); moves opposite to [[EIF2B3]] (-0.59, fdr 4e-05), [[RAD54L2]] (-0.59, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CFAP45]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.62×** | +24.1 | 0e+00 | 37/37 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.57×** | +17.2 | 0e+00 | 38/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.53×** | +15.8 | 0e+00 | 28/37 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.06×** | +13.7 | 2e-40 | 31/37 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.40×** | +10.7 | 7e-25 | 35/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +10.5 | 9e-24 | 27/38 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +9.1 | 9e-18 | 27/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +8.3 | 1e-14 | 33/46 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +8.1 | 4e-14 | 18/28 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +8.0 | 8e-14 | 6/14 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.1 | 8e-11 | 28/47 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.9 | 2e-10 | 22/47 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +6.4 | 5e-09 | 18/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **3.96×** | +6.3 | 1e-08 | 25/44 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.00×** | +6.1 | 5e-08 | 23/44 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +5.3 | 4e-06 | 23/45 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +4.9 | 3e-05 | 20/44 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +4.9 | 4e-05 | 18/46 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 0.05 µM |  | **0.566×** | -5.0 | 3e-04 | 17/45 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.608×** | -4.2 | 0.007 | 17/42 (NCI-H1573, HCT15, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.632×** | -4.0 | 0.008 | 17/47 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.633×** | -4.0 | 0.008 | 19/45 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.645×** | -3.9 | 0.013 | 10/46 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.672×** | -3.5 | 0.045 | 11/45 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.679×** | -3.4 | 0.054 | 11/47 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.691×** | -3.3 | 0.082 | 9/47 (COLO 205, HOP62, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -3.1 | 0.098 | 8/48 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.700×** | -3.1 | 0.098 | 9/47 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.703× | -3.1 | 0.10 | 14/45 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.705× | -3.1 | 0.10 | 9/46 (CFPAC-1, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.87 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +12.0) | — |
| [[SW480 (line)]] | alt | 3.41 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.0) | — |
| [[A498 (line)]] | wt | 9.52 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 8.20 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.5) | — |
| [[LoVo (line)]] | wt | 2.70 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 19.3× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.80× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 5.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 8.74 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 10.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.02× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.1× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 1.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +11.7) | — |
| [[A549 (line)]] | wt | 4.39 | 0 | 1 | — | [[Baicalin (drug)]] 0.5 µM 0.0641× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 1.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.6× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 4.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 4.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 6.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.82× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 5.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.76× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.3× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 4.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +9.0) | — |
| [[A-427 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRD1]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SNX31]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[CD247]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[WDR49]] | +0.75 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[UPP2]] | +0.74 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.74 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CASS4]] | +0.72 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[EFCAB12]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.71 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | -0.59 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RAD54L2]] | -0.59 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP45]] | B | CFAP45 activity raises ADCY10's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without CFAP45 | 0.050 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ADCY10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, -17.8); signed map (10.9, 4.7). **Vector** length 75.5, 14.7% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +24.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.9 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -5.0 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:167,809,386-167,914,215 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAC, Sacy, SACI, HCA2, RP1-313L4.2 |
| Gene groups (HGNC) | Adenylate cyclases |
| Reactome | 2 pathways, smallest: Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PN6](https://www.uniprot.org/uniprotkb/Q96PN6) (Adenylate cyclase type 10):

> Catalyzes the formation of the signaling molecule cAMP. May function as sensor that mediates responses to changes in cellular bicarbonate and CO(2) levels. Has a critical role in mammalian spermatogenesis by producing the cAMP which regulates cAMP-responsive nuclear factors indispensable for sperm maturation in the epididymis. Induces capacitation, the maturational process that sperm undergo prior to fertilization (By similarity). Involved in ciliary beat regulation.

**Summary**, from NCBI Gene [55811](https://www.ncbi.nlm.nih.gov/gene/55811):

> The protein encoded by this gene belongs to a distinct class of adenylyl cyclases that is soluble and insensitive to G protein or forskolin regulation. Activity of this protein is regulated by bicarbonate. Variation at this gene has been observed in patients with absorptive hypercalciuria. Alternatively spliced transcript variants encoding different isoforms have been observed. There is a pseudogene of this gene on chromosome 6. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:21285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21285) · Entrez [55811](https://www.ncbi.nlm.nih.gov/gene/55811) · UniProt [Q96PN6](https://www.uniprot.org/uniprotkb/Q96PN6) · Ensembl [ENSG00000143199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143199)

## Data

Gene col 6697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6697); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6697]; `tensor/DDL_lfc|DDL_z.npy` [6697]; `embed/gene_vectors.npy` [6697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6697 or target_col == 6697). Every well: [[ADCY10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
