---
symbol: "TAFA5"
type: "gene"
col: 13296
ensembl_id: "ENSG00000219438"
name: "TAFA chemokine like family member 5"
location: "22q13.32"
module: 9
arm: "+"
pooled_cpm: 6.69
n_lines_expressing: 21
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TAFA5

*TAFA chemokine like family member 5* — 22q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.37× (z +25.2, q 0e+00, up in 13 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[(S)-Crizotinib (drug)]] 0.05 µM: 0.656× (z -4.2, q 0.017, down in 1 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.160×, HepG2/C3A 0.292×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.143×, SHP-77 0.165×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.0879×, HepG2/C3A 0.144×; ⚠ toxic; cell-cycle shift, explains ~17% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02306]] (+0.60, fdr 1e-05), [[GRIK1]] (+0.58, fdr 2e-05), [[LINC00907]] (+0.58, fdr 1e-05); moves opposite to [[ANAPC4]] (-0.52, fdr 3e-05), [[SPATA7]] (-0.52, fdr 6e-05), [[NKTR]] (-0.48, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRHDE]] → it (grade B ⚠); 2 go from it, the strongest it → [[BCL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.37×** | +25.2 | 0e+00 | 13/18 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.71×** | +18.5 | 0e+00 | 15/18 (H4, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +14.4 | 1e-44 | 3/8 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +14.3 | 6e-44 | 8/17 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +14.0 | 1e-42 | 2/11 (A549, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +12.1 | 1e-31 | 1/9 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.85×** | +10.5 | 1e-23 | 12/17 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +7.7 | 9e-13 | 9/18 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +5.8 | 3e-07 | 10/18 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +4.6 | 2e-04 | 9/18 (C-33 A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.4 | 7e-04 | 2/9 (SHP-77, MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.002 | 4/16 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.003 | 5/18 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.003 | 1/15 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.9 | 0.003 | 3/15 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.011 | 6/17 (C-33 A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.016 | 6/17 (C-33 A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.016 | 0/18 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.024 | 0/17 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.041 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13296.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.160×, HepG2/C3A 0.292×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.143×, SHP-77 0.165×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.0879×, HepG2/C3A 0.144×; ⚠ toxic; cell-cycle shift, explains ~17% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.656×** | -4.2 | 0.017 | 1/18 (SW 900) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.5 | 0.11 | 6/19 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.809× | -3.2 | 0.24 | 4/18 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.737× | -3.0 | 0.36 | 1/18 (C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 97.4 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.110× (z -12.9) |
| [[SHP-77 (line)]] | alt | 50.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0620× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -12.3) |
| [[A-172 (line)]] | wt | 15.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +16.7) | — |
| [[H4 (line)]] | wt | 9.12 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.4× (z +15.0) | — |
| [[NCI-H460 (line)]] | wt | 20.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.52 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.3× (z +20.7) | — |
| [[NCI-H23 (line)]] | alt | 7.05 | 0 | 2 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0842× (z -9.9) |
| [[A549 (line)]] | wt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 16.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.45× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.95× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +10.2) | — |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02306]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GRIK1]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LINC00907]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC01287]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[COL21A1]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SALL1]] | +0.55 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[LINC01250]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ABCA13]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LRFN2]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ERC2]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GNG4]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[LINC01592]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC4]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SPATA7]] | -0.52 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[NKTR]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[GLT8D1]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRHDE]] | B | TRHDE activity lowers TAFA5's level | lines that do not express TRHDE (26) vs lines expressing it (24) | 1.66× higher at baseline in the lines without TRHDE | 0.068 | ⚠ within organs, on part of the lines; also absent: ZSCAN23, SAMD3, ITGA11; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2]] | B | TAFA5 activity raises BCL2's level | lines that do not express TAFA5 (29) vs lines expressing it (21) | 1.47× lower at baseline in the lines without TAFA5 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000260958, UNC5D, EPGN |
| [[GRID1]] | C | TAFA5 activity raises GRID1's level | lines that do not express TAFA5 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without TAFA5 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000260958, UNC5D, EPGN; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.3, 35.4); signed map (34.9, 27.7). **Vector** length 48.9, 11.9% of its response variance represented; |z| ≥ 3 in 470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +25.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.5 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TAFA chemokine like family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.32 — chr22:48,489,553-48,850,912 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAFA-5; previously FAM19A5 |
| Gene groups (HGNC) | TAFA chemokine like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5A7](https://www.uniprot.org/uniprotkb/Q7Z5A7) (Chemokine-like protein TAFA-5):

> Acts as a chemokine-like protein by regulating cell proliferation and migration through activation of G protein-coupled receptors (GPCRs), such as S1PR2 and FPR2 (By similarity). Stimulates chemotactic migration of macrophages mediated by the MAPK3/ERK1 and AKT1 pathway (By similarity). Blocks TNFSF11/RANKL-induced osteoclast formation from macrophages by inhibiting up-regulation of osteoclast fusogenic and differentiation genes (By similarity). Stimulation of macrophage migration and …

**Summary**, from NCBI Gene [25817](https://www.ncbi.nlm.nih.gov/gene/25817):

> This gene is a member of the TAFA family which is composed of five highly homologous genes that encode small secreted proteins. These proteins contain conserved cysteine residues at fixed positions, and are distantly related to MIP-1alpha, a member of the CC-chemokine family. The TAFA proteins are predominantly expressed in specific regions of the brain, and are postulated to function as brain-specific chemokines or neurokines that act as regulators of immune and nervous cells. [provided by …

**Accessions** — [HGNC:21592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21592) · Entrez [25817](https://www.ncbi.nlm.nih.gov/gene/25817) · UniProt [Q7Z5A7](https://www.uniprot.org/uniprotkb/Q7Z5A7) · Ensembl [ENSG00000219438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000219438)

## Data

Gene col 13296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13296); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13296]; `tensor/DDL_lfc|DDL_z.npy` [13296]; `embed/gene_vectors.npy` [13296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13296 or target_col == 13296). Every well: [[TAFA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAFA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
