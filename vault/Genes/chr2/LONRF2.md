---
symbol: "LONRF2"
type: "gene"
col: 9964
ensembl_id: "ENSG00000170500"
name: "LON peptidase N-terminal domain and ring finger 2"
location: "2q11.2"
module: 25
arm: "+"
pooled_cpm: 8.94
n_lines_expressing: 29
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# LONRF2

*LON peptidase N-terminal domain and ring finger 2* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.66× (z +19.9, q 0e+00, up in 16 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.14× (z +13.9, q 7e-42, up in 20 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.159×, PANC-1 0.285×, SNU-1 0.330×, NCI-H460 0.413×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.303×, CHP-212 0.254×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0592×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.204×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.60, fdr 1e-05), [[KLHL13]] (+0.57, fdr 2e-05), [[FECH]] (+0.57, fdr 3e-05); moves opposite to [[ZNF324]] (-0.47, fdr 4e-04), [[PSEN1]] (-0.45, fdr 5e-05), [[DZANK1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAXC]] → it (grade B ⚠); 2 go from it, the strongest it → [[HACD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.66×** | +19.9 | 0e+00 | 16/20 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.69×** | +19.3 | 0e+00 | 11/13 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +13.9 | 7e-42 | 20/26 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +10.8 | 3e-25 | 10/16 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +10.0 | 1e-21 | 7/23 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +9.3 | 2e-18 | 16/24 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +8.3 | 9e-15 | 10/24 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +7.3 | 2e-11 | 15/25 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +6.5 | 4e-09 | 9/22 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.5 | 4e-09 | 11/24 (SHP-77, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.2 | 2e-08 | 14/26 (C32, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +6.0 | 1e-07 | 8/22 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.7 | 6e-07 | 9/26 (CHP-212, CFPAC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +5.1 | 1e-05 | 12/26 (A-172, SW 900, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 10/26 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 4e-04 | 11/25 (BT-474, A-427, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.2 | 9e-04 | 10/25 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.004 | 9/25 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.004 | 9/21 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.012 | 9/26 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.013 | 9/26 (NCI-H2030, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.159×, PANC-1 0.285×, SNU-1 0.330×, NCI-H460 0.413×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.303×, CHP-212 0.254×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0592×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -4.0 | 0.043 | 3/27 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.764× | -3.5 | 0.14 | 7/25 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.625× | -3.2 | 0.27 | 10/23 (SNU-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 119 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.1) |
| [[A-427 (line)]] | wt | 25.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.9) |
| [[PANC-1 (line)]] | alt | 12.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 14.0 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -8.7) |
| [[SW 900 (line)]] | alt | 11.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.0× (z +10.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -20.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.5) |
| [[A-172 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.819 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[KLHL13]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FECH]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[FAM110B]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[TNPO1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SNCA]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RNF2]] | +0.54 | +0.36 / +0.56 | both halves | 9e-05 | same gene group |
| [[GNAL]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GPR63]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SLC47A1]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TMEM64]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RAVER2]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF324]] | -0.47 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[PSEN1]] | -0.45 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DZANK1]] | -0.44 | -0.34 / -0.33 | both halves | 1e-04 | STRING 404 |
| [[PPP1R13L]] | -0.44 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[BLZF1]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DYNC2I1]] | -0.42 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXC]] | B | FAXC activity raises LONRF2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without FAXC | 0.094 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[KLHL13]] | C | KLHL13 activity raises LONRF2's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.43× lower at baseline in the lines without KLHL13 | 0.078 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACD2]] | B | LONRF2 activity lowers HACD2's level | lines that do not express LONRF2 (21) vs lines expressing it (29) | 1.02× higher at baseline in the lines without LONRF2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ADCY1 |
| [[SHTN1]] | B | LONRF2 activity raises SHTN1's level | lines that do not express LONRF2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without LONRF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ADCY1 |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.333). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.0, 44.3); signed map (10.6, -0.2). **Vector** length 60.7, 13.3% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +19.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +19.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -0.5 |
|  | [[Thymol (drug)]] 5 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | LON peptidase N-terminal domain and ring finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:100,271,875-100,322,501 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45273, RNF192 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q1L5Z9](https://www.uniprot.org/uniprotkb/Q1L5Z9) carries no function annotation.

**Summary**, from NCBI Gene [164832](https://www.ncbi.nlm.nih.gov/gene/164832):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in neuron apoptotic process; neuron projection development; and protein quality control for misfolded or incompletely synthesized proteins. Predicted to act upstream of or within several processes, including motor behavior; negative regulation of neuron apoptotic process; and spinal cord motor neuron differentiation. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24788) · Entrez [164832](https://www.ncbi.nlm.nih.gov/gene/164832) · UniProt [Q1L5Z9](https://www.uniprot.org/uniprotkb/Q1L5Z9) · Ensembl [ENSG00000170500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170500)

## Data

Gene col 9964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9964); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9964]; `tensor/DDL_lfc|DDL_z.npy` [9964]; `embed/gene_vectors.npy` [9964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9964 or target_col == 9964). Every well: [[LONRF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LONRF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
