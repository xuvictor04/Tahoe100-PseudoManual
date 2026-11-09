---
symbol: "PHEX"
type: "gene"
col: 2222
ensembl_id: "ENSG00000102174"
name: "phosphate regulating endopeptidase X-linked"
location: "Xp22.11"
module: 39
arm: "+"
pooled_cpm: 11.49
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# PHEX

*phosphate regulating endopeptidase X-linked* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.67× (z +19.1, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.532× (z -6.9, q 2e-09, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP4]] (+0.79, fdr 7e-06), [[SCUBE2]] (+0.78, fdr 7e-06), [[ALDH8A1]] (+0.76, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SCUBE2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.67×** | +19.1 | 0e+00 | 45/46 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +11.3 | 6e-27 | 32/44 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +9.9 | 9e-21 | 35/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +7.7 | 2e-12 | 12/22 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.4 | 2e-11 | 22/42 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +7.2 | 7e-11 | 11/26 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **2.83×** | +6.0 | 2e-07 | 21/46 (C32, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.8 | 4e-07 | 16/34 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.63×** | +5.4 | 4e-06 | 24/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 22/47 (A498, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 1e-05 | 23/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.51×** | +4.3 | 9e-04 | 15/47 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.88×** | +3.6 | 0.012 | 10/42 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.022 | 12/43 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Naproxen (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.022 | 8/42 (A498, RKO, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.80×** | +3.4 | 0.026 | 6/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.042 | 16/47 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.052 | 19/47 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.532×** | -6.9 | 2e-09 | 25/48 (H4, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -5.6 | 6e-06 | 24/42 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.644×** | -4.8 | 2e-04 | 19/43 (RKO, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[NG25 (drug)]] 5 µM |  | **0.441×** | -4.7 | 3e-04 | 16/39 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.740×** | -4.7 | 3e-04 | 19/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.727×** | -3.5 | 0.044 | 17/47 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.068 | 14/47 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.3 | 2 | 1 | [[Auranofin (drug)]] 5 µM 45.4× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0924× (z -9.2) |
| [[HOP62 (line)]] | alt | 16.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.08× (z +11.3) | [[Docetaxel (drug)]] 0.05 µM 0.164× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +17.3) | — |
| [[COLO 205 (line)]] | alt | 5.15 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +11.2) | [[Cyclosporin A (drug)]] 0.05 µM 0.0444× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 8.34 | 1 | 1 | [[Auranofin (drug)]] 5 µM 15.6× (z +10.9) | [[Ferulic acid (drug)]] 0.05 µM 0.0694× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 5.08 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.73× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.61× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 26.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.66× (z +12.9) | — |
| [[SW480 (line)]] | alt | 8.76 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.74× (z +10.1) | — |
| [[A-427 (line)]] | wt | 5.08 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.3× (z +8.8) | — |
| [[A498 (line)]] | wt | 5.03 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.06× (z +9.2) | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 5.95 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.0× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.50× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.91 | 1 | 0 | [[Auranofin (drug)]] 5 µM 76.9× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0773× (z -10.4) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP4]] | +0.79 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.76 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.74 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[DPYS]] | +0.73 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.73 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCUBE2]] | B | SCUBE2 activity raises PHEX's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without SCUBE2 | 0.059 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[DPYS]] | B | DPYS activity raises PHEX's level | lines that do not express DPYS (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without DPYS | 0.090 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity raises PHEX's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.86× lower at baseline in the lines without DDR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[LINC00702]] | B | LINC00702 activity raises PHEX's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without LINC00702 | 0.097 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[MMP25]] | C | MMP25 activity raises PHEX's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.6, -12.3); signed map (19.1, 8.5). **Vector** length 103, 23.1% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.7 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +7.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphate regulating endopeptidase X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:22,032,325-22,494,713 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEX, HPDR1, HYP1, XLH; previously HYP, HPDR |
| Gene groups (HGNC) | M13 metallopeptidases |
| Hallmark sets | COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [P78562](https://www.uniprot.org/uniprotkb/P78562) (Phosphate-regulating neutral endopeptidase PHEX):

> Peptidase that cleaves SIBLING (small integrin-binding ligand, N-linked glycoprotein)-derived ASARM peptides, thus regulating their biological activity. Cleaves ASARM peptides between Ser and Glu or Asp residues. Regulates osteogenic cell differentiation and bone mineralization through the cleavage of the MEPE-derived ASARM peptide. Promotes dentin mineralization and renal phosphate reabsorption by cleaving DMP1- and MEPE-derived ASARM peptides. Inhibits the cleavage of MEPE by CTSB/cathepsin B …

**Summary**, from NCBI Gene [5251](https://www.ncbi.nlm.nih.gov/gene/5251):

> The protein encoded by this gene is a transmembrane endopeptidase that belongs to the type II integral membrane zinc-dependent endopeptidase family. The protein is thought to be involved in bone and dentin mineralization and renal phosphate reabsorption. Mutations in this gene cause X-linked hypophosphatemic rickets. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:8918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8918) · Entrez [5251](https://www.ncbi.nlm.nih.gov/gene/5251) · UniProt [P78562](https://www.uniprot.org/uniprotkb/P78562) · Ensembl [ENSG00000102174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102174)

## Data

Gene col 2222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2222); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2222]; `tensor/DDL_lfc|DDL_z.npy` [2222]; `embed/gene_vectors.npy` [2222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2222 or target_col == 2222). Every well: [[PHEX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHEX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
