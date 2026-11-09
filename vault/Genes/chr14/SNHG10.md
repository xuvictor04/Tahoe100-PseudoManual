---
symbol: "SNHG10"
type: "gene"
col: 14480
ensembl_id: "ENSG00000247092"
name: "small nucleolar RNA host gene 10"
location: "14q32.13"
module: 15
arm: "+"
pooled_cpm: 6.63
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SNHG10

*small nucleolar RNA host gene 10* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.04× (z +21.0, q 0e+00, up in 42 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Alpelisib (drug)]] 0.05 µM in 1 line (SHP-77 0.0686×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTTN-DT]] (+0.73, fdr 1e-05), [[GTF3C2-AS2]] (+0.70, fdr 1e-05), [[FAM184B]] (+0.68, fdr 1e-05); moves opposite to [[WDR7]] (-0.52, fdr 4e-04), [[ISCA2]] (-0.52, fdr 1e-04), [[ALAS1]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.04×** | +21.0 | 0e+00 | 42/43 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.86×** | +13.3 | 6e-38 | 17/17 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.17×** | +11.8 | 5e-30 | 28/35 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.8 | 5e-30 | 26/30 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +10.8 | 4e-25 | 28/41 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +8.7 | 4e-16 | 23/38 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.23×** | +8.2 | 2e-14 | 7/11 (HOP62, PANC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +8.1 | 4e-14 | 29/46 (SW480, SK-MEL-2, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.7 | 9e-13 | 27/44 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.89×** | +6.7 | 9e-10 | 28/47 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +6.6 | 2e-09 | 19/46 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.2 | 3e-08 | 22/36 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +5.8 | 3e-07 | 24/47 (SW1417, SW480, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +5.8 | 3e-07 | 22/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.8 | 3e-07 | 24/42 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +5.3 | 4e-06 | 19/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.51×** | +5.1 | 1e-05 | 19/44 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.7 | 9e-05 | 17/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +4.2 | 5e-04 | 10/39 (PANC-1, RPMI-7951, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.49×** | +4.2 | 6e-04 | 14/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.002 | 17/41 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.048 | 6/44 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +2.9 | 0.062 | 5/36 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14480.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Alpelisib (drug)]] 0.05 µM in 1 line (SHP-77 0.0686×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.717× | -3.6 | 0.19 | 4/47 (NCI-H460, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.04 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 5.51 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.15× (z +12.6) | — |
| [[A498 (line)]] | wt | 5.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +8.5) | — |
| [[A549 (line)]] | wt | 6.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 5.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 5.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.43× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 7.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 5.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.54× (z +11.6) | — |
| [[KATO III (line)]] | alt | 7.36 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 9.71× (z +8.9) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 4.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 6.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0686× (z -11.4) |
| [[SW 900 (line)]] | alt | 8.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 6.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +12.0) | — |
| [[SW480 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTN-DT]] | +0.73 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.70 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.68 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | +0.67 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZNF213-AS1]] | +0.66 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SLC16A4-AS1]] | +0.65 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[NIPBL-DT]] | +0.64 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[LINC00115]] | +0.63 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[SPATA1]] | +0.62 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[DIDO1]] | +0.62 | +0.25 / +0.57 | both halves | 4e-04 |  |
| [[GLIPR1-AS1]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[CNPY2-AS1]] | +0.62 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.52 | -0.24 / -0.38 | both halves | 4e-04 |  |
| [[ISCA2]] | -0.52 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.52 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[TTBK2]] | -0.51 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[GPATCH11]] | -0.51 | -0.29 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNHG10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.1, 22.8); signed map (32.0, -17.8). **Vector** length 62.6, 9.58% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +21.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.6 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.9 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.7 | +3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 10 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q32.13 — chr14:95,521,943-95,534,889 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ40557, NCRNA00063, LINC00063, TP53LC16; previously C14orf62 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [283596](https://www.ncbi.nlm.nih.gov/gene/283596):

> This gene is small nucleolar RNA host gene 10 and represents a non-protein coding RNA. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:27510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27510) · Entrez [283596](https://www.ncbi.nlm.nih.gov/gene/283596) · Ensembl [ENSG00000247092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247092)

## Data

Gene col 14480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14480); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14480]; `tensor/DDL_lfc|DDL_z.npy` [14480]; `embed/gene_vectors.npy` [14480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14480 or target_col == 14480). Every well: [[SNHG10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
