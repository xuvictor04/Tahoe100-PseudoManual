---
symbol: "EPAS1"
type: "gene"
col: 3751
ensembl_id: "ENSG00000116016"
name: "endothelial PAS domain protein 1"
location: "2p21"
module: 113
arm: "+"
pooled_cpm: 170.7
n_lines_expressing: 41
n_dd_up: 4
n_dd_down: 31
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 18
direction_downstream: 17
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# EPAS1

*endothelial PAS domain protein 1* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +8.6, q 6e-15, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.578× (z -12.8, q 1e-34, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERRFI1]] (+0.61, fdr 1e-05), [[ELL2]] (+0.60, fdr 1e-05), [[TCIM]] (+0.60, fdr 1e-05); moves opposite to [[TRAPPC13]] (-0.48, fdr 7e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); 17 go from it, the strongest it → [[TBC1D8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +8.6 | 6e-15 | 32/39 (J82, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +7.4 | 4e-11 | 31/40 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.1 | 8e-05 | 24/39 (J82, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.081 | 17/39 (HOP62, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -12.8 | 1e-34 | 30/40 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -11.2 | 7e-27 | 36/38 (HepG2/C3A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.624×** | -7.8 | 1e-12 | 31/39 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -7.5 | 9e-12 | 25/39 (H4, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.618×** | -7.3 | 3e-11 | 23/36 (A-172, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -7.3 | 3e-11 | 28/39 (NCI-H23, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.641×** | -7.0 | 2e-10 | 25/38 (BT-474, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -5.8 | 4e-07 | 24/41 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.716×** | -5.5 | 3e-06 | 23/40 (SHP-77, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.737×** | -5.0 | 3e-05 | 26/38 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.735×** | -4.9 | 6e-05 | 20/36 (A-172, NCI-H1573, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.746×** | -4.8 | 7e-05 | 23/39 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -4.8 | 8e-05 | 23/39 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -4.7 | 1e-04 | 23/39 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.765×** | -4.4 | 4e-04 | 20/39 (COLO 205, NCI-H23, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 5e-04 | 24/39 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.769×** | -4.3 | 5e-04 | 22/38 (LOX-IMVI, NCI-H23, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -4.1 | 0.001 | 19/39 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.624×** | -4.1 | 0.001 | 19/39 (NCI-H1573, SHP-77, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.845× | -3.9 | 0.003 | 19/40 (NCI-H1792, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 240 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 418 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.524× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 219 | 0 | 10 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.170× (z -14.8) |
| [[SHP-77 (line)]] | alt | 150 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.279× (z -10.3) |
| [[BT-474 (line)]] | alt | 234 | 0 | 9 (6 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 723 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -16.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.395× (z -10.7) |
| [[A549 (line)]] | wt | 571 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 298 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.367× (z -9.5) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.403× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 321 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 250 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -15.7) |
| [[SNU-423 (line)]] | alt | 422 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -17.8) |
| [[PANC-1 (line)]] | alt | 257 | 1 | 3 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.39× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -13.4) |
| [[CHP-212 (line)]] | wt | 238 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.119× (z -11.2) |
| [[H4 (line)]] | wt | 167 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.159× (z -13.7) |
| [[HOP62 (line)]] | alt | 238 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 203 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -11.2) |
| [[SW1417 (line)]] | alt | 114 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.69× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 133 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -17.6) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.53× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.239× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 132 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.87× (z +10.3) | — |
| [[SW480 (line)]] | alt | 68.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -13.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.348× (z -9.8) |
| [[A498 (line)]] | wt | 263 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.3) |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0998× (z -9.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 152 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.64× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 112 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.15× (z +10.5) | — |
| [[KATO III (line)]] | alt | 105 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.65× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.418× (z -9.2) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 281 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 29.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 137 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERRFI1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ELL2]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TCIM]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RASD1]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TREM1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SGK1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LINC00540]] | +0.57 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[MT1A]] | +0.56 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[NCOA3]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 | same gene group |
| [[TGM2]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[BCL6]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TIPARP]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 13, C 5. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises EPAS1's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.82× lower at baseline in the lines without TBC1D8 | 0.017 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[LINC02015]] | B | LINC02015 activity raises EPAS1's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without LINC02015 | 0.017 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[RHCG]] | B | RHCG activity raises EPAS1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without RHCG | 0.019 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[IL1RAP]] | B | IL1RAP activity raises EPAS1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 4.49× lower at baseline in the lines without IL1RAP | 0.020 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[MARCHF3]] | B | MARCHF3 activity raises EPAS1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.45× lower at baseline in the lines without MARCHF3 | 0.020 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[SIPA1L2]] | B | SIPA1L2 activity raises EPAS1's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without SIPA1L2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[RGS17]] | B | RGS17 activity raises EPAS1's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without RGS17 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EPAS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PTGES]] | B | PTGES activity raises EPAS1's level | lines that do not express PTGES (17) vs lines expressing it (33) | 3.29× lower at baseline in the lines without PTGES | 0.047 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[ZC3H12A]] | B | ZC3H12A activity raises EPAS1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 4.99× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SMOX]] | B | SMOX activity raises EPAS1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.49× lower at baseline in the lines without SMOX | 0.069 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises EPAS1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without MYO1E | 0.069 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | EPAS1 activity raises TBC1D8's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.48× lower at baseline in the lines without EPAS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[PC]] | B | EPAS1 activity raises PC's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.86× lower at baseline in the lines without EPAS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[TPCN1]] | B | EPAS1 activity raises TPCN1's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without EPAS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[ZC3H12A]] | B | EPAS1 activity raises ZC3H12A's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without EPAS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[RGS17]] | B | EPAS1 activity raises RGS17's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 4.19× lower at baseline in the lines without EPAS1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[AKAP13]] | B | EPAS1 activity raises AKAP13's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without EPAS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[IL1RAP]] | B | EPAS1 activity raises IL1RAP's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 3.26× lower at baseline in the lines without EPAS1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[MAP3K5]] | B | EPAS1 activity raises MAP3K5's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without EPAS1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[MARCHF3]] | B | EPAS1 activity raises MARCHF3's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without EPAS1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[NCOA3]] | B | EPAS1 activity raises NCOA3's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without EPAS1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[TPCN1]] | B | EPAS1 activity strengthens TPCN1's drug response | lines that do not express EPAS1 (9) vs lines expressing it (40) | the lines without EPAS1 respond 0.63× as strongly (z diff +1.64); strongest at Topotecan (hydrochloride) 5 µM: 0.81x vs 0.54x (z diff +3.6) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS; target measured in part of the lines; artifact flags |
| [[RHCG]] | B | EPAS1 activity raises RHCG's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without EPAS1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 10.2); signed map (11.2, 31.1). **Vector** length 134, 42.6% of its response variance represented; |z| ≥ 3 in 1,549 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +7.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.3 | +1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[Econazole (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.6 | -0.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -7.3 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | endothelial PAS domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,293,667-46,386,697 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP2, PASD2, HIF2A, HLF, bHLHe73 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing; Hypoxia inducible factor subunits |
| Reactome | 19 pathways, smallest: PTK6 Expression; Regulation of gene expression by Hypoxia-inducible Factor; Pexophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99814](https://www.uniprot.org/uniprotkb/Q99814) (Endothelial PAS domain-containing protein 1):

> Transcription factor involved in the induction of oxygen regulated genes. Heterodimerizes with ARNT; heterodimer binds to core DNA sequence 5'-TACGTG-3' within the hypoxia response element (HRE) of target gene promoters (By similarity). Regulates the vascular endothelial growth factor (VEGF) expression and seems to be implicated in the development of blood vessels and the tubular system of lung. May also play a role in the formation of the endothelium that gives rise to the blood brain barrier. …

**Summary**, from NCBI Gene [2034](https://www.ncbi.nlm.nih.gov/gene/2034):

> This gene encodes a transcription factor involved in the induction of genes regulated by oxygen, which is induced as oxygen levels fall. The encoded protein contains a basic-helix-loop-helix domain protein dimerization domain as well as a domain found in proteins in signal transduction pathways which respond to oxygen levels. Mutations in this gene are associated with erythrocytosis familial type 4. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:3374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3374) · Entrez [2034](https://www.ncbi.nlm.nih.gov/gene/2034) · UniProt [Q99814](https://www.uniprot.org/uniprotkb/Q99814) · Ensembl [ENSG00000116016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116016)

## Data

Gene col 3751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3751); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3751]; `tensor/DDL_lfc|DDL_z.npy` [3751]; `embed/gene_vectors.npy` [3751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3751 or target_col == 3751). Every well: [[EPAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
