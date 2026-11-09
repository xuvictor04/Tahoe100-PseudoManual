---
symbol: "HOXD10"
type: "gene"
col: 4916
ensembl_id: "ENSG00000128710"
name: "homeobox D10"
location: "2q31.1"
module: 46
arm: "+"
pooled_cpm: 12.11
n_lines_expressing: 17
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXD10

*homeobox D10* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +18.1, q 0e+00, up in 12 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.406× (z -8.9, q 3e-16, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXD11]] (+0.83, fdr 7e-06, ⚠ same locus), [[ZIC1]] (+0.63, fdr 1e-05), [[LINC02492]] (+0.59, fdr 5e-05), [[SHOX2]] (+0.58, fdr 3e-05); moves opposite to [[NDFIP2]] (-0.53, fdr 1e-04), [[NAPG]] (-0.49, fdr 4e-04), [[VTA1]] (-0.47, fdr 4e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[GRID2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +18.1 | 0e+00 | 12/13 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.2 | 8e-18 | 2/6 (SW480, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.4 | 1e-14 | 1/12 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +6.8 | 2e-09 | 8/14 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +6.6 | 3e-09 | 2/9 (SW480, HCT15) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.8 | 7e-07 | 2/11 (SK-MEL-2, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.1 | 2e-05 | 4/13 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +5.0 | 3e-05 | 1/14 (CHP-212) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +4.2 | 0.001 | 2/13 (SW480, HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.9 | 0.005 | 3/11 (NCI-H2030, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 4/14 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.6 | 0.014 | 0/13 | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.014 | 6/12 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.014 | 3/14 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.019 | 7/15 (HOP62, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.061 | 6/15 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.79×** | +3.0 | 0.083 | 2/10 (SHP-77, HOP62) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.406×** | -8.9 | 3e-16 | 12/15 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.555×** | -5.8 | 2e-06 | 12/15 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.603×** | -5.0 | 1e-04 | 13/15 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.691×** | -3.7 | 0.036 | 9/15 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.713×** | -3.4 | 0.088 | 2/15 (SW 1088, SHP-77) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.681× | -3.0 | 0.23 | 0/14 | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 148 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 29.2 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.0659× (z -17.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0974× (z -15.2) |
| [[A498 (line)]] | wt | 46.5 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 48.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.134× (z -16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.237× (z -11.5) |
| [[J82 (line)]] | alt | 34.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.238× (z -11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.323× (z -9.0) |
| [[SHP-77 (line)]] | alt | 67.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.215× (z -10.6) |
| [[A549 (line)]] | wt | 10.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +11.9) | [[Belinostat (drug)]] 5 µM 0.0811× (z -11.7) |
| [[A-427 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.942 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXD11]] | +0.83 | +0.78 / +0.76 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZIC1]] | +0.63 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LINC02492]] | +0.59 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[SHOX2]] | +0.58 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[RALYL]] | +0.56 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[KLRK1-AS1]] | +0.56 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[HOXB-AS1]] | +0.55 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[KCTD8]] | +0.55 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[FLRT2]] | +0.55 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[KCNMB2]] | +0.55 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[TYMSOS]] | +0.54 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[TSTD3]] | +0.54 | +0.33 / +0.34 | both halves | 1e-04 |  |
| [[LRRN2]] | +0.53 | +0.47 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDFIP2]] | -0.53 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[NAPG]] | -0.49 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[VTA1]] | -0.47 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[RSU1]] | -0.46 | -0.19 / -0.40 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HOXD10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers HOXD10's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[FAM13C]] | B | FAM13C activity raises HOXD10's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 2.89× lower at baseline in the lines without FAM13C | 0.096 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[HOXD11]] | C | HOXD11 activity raises HOXD10's level | lines that do not express HOXD11 (36) vs lines expressing it (14) | 11.99× lower at baseline in the lines without HOXD11 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXD10, TMEM52B, OLR1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRID2]] | B | HOXD10 activity raises GRID2's level | lines that do not express HOXD10 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without HOXD10 | 0.079 | ⚠ within organs, on part of the lines; also absent: HOXD11, TMEM52B, PHYHIPL |
| [[HOXD11]] | C | HOXD10 activity raises HOXD11's level | lines that do not express HOXD10 (33) vs lines expressing it (17) | 4.00× lower at baseline in the lines without HOXD10 | 6e-04 | ⚠ within organs, on part of the lines; also absent: HOXD11, TMEM52B, PHYHIPL; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (35.2, 25.3); signed map (44.1, 28.7). **Vector** length 42.0, 10.3% of its response variance represented; |z| ≥ 3 in 415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.9 | -5.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox D10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:176,108,790-176,119,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX4, HOX4D |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P28358](https://www.uniprot.org/uniprotkb/P28358) (Homeobox protein Hox-D10):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3236](https://www.ncbi.nlm.nih.gov/gene/3236):

> This gene is a member of the Abd-B homeobox family and encodes a protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox D genes located on chromosome 2. The encoded nuclear protein functions as a sequence-specific transcription factor that is expressed in the developing limb buds and is involved in differentiation and limb development. Mutations in this gene have been associated with Wilm's tumor and congenital vertical talus (also known as "rocker-bottom foot" …

**Accessions** — [HGNC:5133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5133) · Entrez [3236](https://www.ncbi.nlm.nih.gov/gene/3236) · UniProt [P28358](https://www.uniprot.org/uniprotkb/P28358) · Ensembl [ENSG00000128710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128710)

## Data

Gene col 4916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4916); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4916]; `tensor/DDL_lfc|DDL_z.npy` [4916]; `embed/gene_vectors.npy` [4916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4916 or target_col == 4916). Every well: [[HOXD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
