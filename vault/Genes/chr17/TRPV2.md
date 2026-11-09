---
symbol: "TRPV2"
type: "gene"
col: 11936
ensembl_id: "ENSG00000187688"
name: "transient receptor potential cation channel subfamily V member 2"
location: "17p11.2"
module: 78
arm: "+"
pooled_cpm: 3.54
n_lines_expressing: 22
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# TRPV2

*transient receptor potential cation channel subfamily V member 2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.81× (z +13.6, q 3e-39, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +10.9, q 2e-25, up in 0 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 0.164×, CFPAC-1 0.209×, SHP-77 0.120×, KATO III 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clonidine (hydrochloride) (drug)]] 5 µM in 1 line (SW 1271 0.142×); [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0665×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANGPTL2]] (+0.56, fdr 1e-05), [[NES]] (+0.55, fdr 3e-05), [[SHC3]] (+0.52, fdr 3e-05); moves opposite to [[MAP2K5]] (-0.51, fdr 4e-05), [[BABAM2]] (-0.44, fdr 8e-05), [[PHLPP1]] (-0.44, fdr 1e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HS3ST3A1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[LINC01169]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +13.6 | 3e-39 | 4/9 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +12.2 | 7e-32 | 3/10 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +10.9 | 2e-25 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +10.1 | 1e-21 | 1/9 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +5.5 | 4e-06 | 3/15 (SW480, NCI-H460, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.27×** | +5.2 | 1e-05 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.1 | 4e-05 | 2/14 (Hs 766T, LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.3 | 1e-03 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.58×** | +4.1 | 0.003 | 0/15 | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.9 | 0.005 | 0/6 | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.006 | 1/17 (C32) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.8 | 0.007 | 1/14 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.7 | 0.009 | 3/15 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.6 | 0.012 | 2/13 (A-427, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.015 | 1/16 (C32) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.015 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.055 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.078 | 2/16 (CFPAC-1, C32) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.084 | 3/15 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11936.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 0.164×, CFPAC-1 0.209×, SHP-77 0.120×, KATO III 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clonidine (hydrochloride) (drug)]] 5 µM in 1 line (SW 1271 0.142×); [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0665×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 0.662× | -3.7 | 0.10 | 11/17 (hTERT-HPNE, SNU-1, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | 0.723× | -3.3 | 0.31 | 6/18 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 4.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 4.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 3.59 | 0 | 1 (1 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM 0.0665× (z -8.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 1 | — | [[Clonidine (hydrochloride) (drug)]] 5 µM 0.142× (z -11.1) |
| [[A-172 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGPTL2]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NES]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SHC3]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[NMNAT2]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[PCDHGC3]] | +0.51 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[LINC02813]] | +0.51 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[CACNA2D4]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CDC42EP2]] | +0.50 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[GMIP]] | +0.49 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[MILR1]] | +0.49 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[PAEP]] | +0.49 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[CNIH3]] | +0.49 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K5]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[BABAM2]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[PHLPP1]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[YY1]] | -0.40 | -0.42 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises TRPV2's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without HS3ST3A1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[NES]] | C | NES activity raises TRPV2's level | lines that do not express NES (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without NES | 0.056 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[STK32B]] | C | STK32B activity raises TRPV2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without STK32B | 0.091 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[SCUBE1]] | C | SCUBE1 activity raises TRPV2's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 1.67× lower at baseline in the lines without SCUBE1 | 0.091 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01169]] | C | TRPV2 activity raises LINC01169's level | lines that do not express TRPV2 (28) vs lines expressing it (22) | 1.45× lower at baseline in the lines without TRPV2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02941, ENSG00000239268, ENSG00000267284; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.6, 10.1); signed map (10.3, 50.9). **Vector** length 32.1, 6.61% of its response variance represented; |z| ≥ 3 in 312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily V member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:16,415,571-16,437,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VRL, VRL-1, VRL1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily V |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5S1](https://www.uniprot.org/uniprotkb/Q9Y5S1) (Transient receptor potential cation channel subfamily V member 2):

> Calcium-permeable, non-selective cation channel. Seems to be regulated, at least in part, by growth factors, such as IGF1, PDGF and morphogenetic neuropeptide/head activator. May transduce physical stimuli in mast cells (By similarity).

**Summary**, from NCBI Gene [51393](https://www.ncbi.nlm.nih.gov/gene/51393):

> This gene encodes an ion channel that is activated by high temperatures above 52 degrees Celsius. The protein may be involved in transduction of high-temperature heat responses in sensory ganglia. It is thought that in other tissues the channel may be activated by stimuli other than heat. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18082) · Entrez [51393](https://www.ncbi.nlm.nih.gov/gene/51393) · UniProt [Q9Y5S1](https://www.uniprot.org/uniprotkb/Q9Y5S1) · Ensembl [ENSG00000187688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187688)

## Data

Gene col 11936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11936); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11936]; `tensor/DDL_lfc|DDL_z.npy` [11936]; `embed/gene_vectors.npy` [11936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11936 or target_col == 11936). Every well: [[TRPV2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPV2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
