---
symbol: "CACNA2D3"
type: "gene"
col: 8071
ensembl_id: "ENSG00000157445"
name: "calcium voltage-gated channel auxiliary subunit alpha2delta 3"
location: "3p21.1-p14.3"
module: 19
arm: "+"
pooled_cpm: 69.44
n_lines_expressing: 14
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 14
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CACNA2D3

*calcium voltage-gated channel auxiliary subunit alpha2delta 3* — 3p21.1-p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +12.8, q 1e-34, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.584× (z -6.8, q 8e-09, down in 9 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK4]] (+0.64, fdr 7e-06), [[GTF2I-AS1]] (+0.64, fdr 1e-05), [[DOK6]] (+0.62, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SUCNR1]] → it (grade C ⚠); 14 go from it, the strongest it → [[TMOD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +12.8 | 1e-34 | 2/12 (HS-578T, SW480) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +12.7 | 1e-34 | 8/12 (SW480, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +11.5 | 2e-28 | 2/12 (SW480, SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +9.6 | 9e-20 | 2/12 (SHP-77, SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.9 | 5e-17 | 1/11 (H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +7.4 | 1e-11 | 7/12 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.1 | 3e-05 | 7/12 (RPMI-7951, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 2e-04 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.016 | 2/12 (SW480, A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.030 | 1/12 (H4) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.040 | 0/12 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.061 | 2/12 (SW480, SW 900) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -6.8 | 8e-09 | 9/12 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.613×** | -6.2 | 2e-07 | 10/12 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -4.7 | 5e-04 | 10/12 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -4.5 | 8e-04 | 5/12 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.721×** | -4.1 | 0.004 | 8/12 (SW480, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -4.1 | 0.004 | 10/13 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -4.0 | 0.006 | 9/12 (RPMI-7951, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -3.9 | 0.007 | 3/12 (SW 900, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.744×** | -3.7 | 0.013 | 3/12 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.746×** | -3.5 | 0.022 | 10/12 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.756×** | -3.5 | 0.022 | 9/12 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.757×** | -3.5 | 0.022 | 7/12 (A498, SW 900, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.761×** | -3.4 | 0.027 | 3/12 (SW 900, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.770×** | -3.3 | 0.043 | 5/12 (A498, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.844× | -3.0 | 0.094 | 3/12 (HS-578T, NCI-H460, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 509 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -23.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0679× (z -17.6) |
| [[NCI-H1792 (line)]] | alt | 423 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 97.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.140× (z -14.9) |
| [[A498 (line)]] | wt | 96.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -22.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -12.5) |
| [[A-172 (line)]] | wt | 640 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -11.9) |
| [[SW 900 (line)]] | alt | 52.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.6) |
| [[SW480 (line)]] | alt | 29.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.30× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 30.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.85× (z +12.2) | — |
| [[J82 (line)]] | alt | 49.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK4]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[GTF2I-AS1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DOK6]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TDO2]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[CDH11]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[C5orf46]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[COL8A1]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[CNTN1]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SCUBE1]] | +0.55 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[GREM2]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[EPB41L3]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Neuronal System |
| [[BMPER]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCNR1]] | C | SUCNR1 activity raises CACNA2D3's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 8.39× lower at baseline in the lines without SUCNR1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises CACNA2D3's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.25× lower at baseline in the lines without C5orf46 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises CACNA2D3's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without ABI3BP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[CA12]] | C | CA12 activity raises CACNA2D3's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.81× lower at baseline in the lines without CA12 | 0.017 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises CACNA2D3's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 2.88× lower at baseline in the lines without LINC01885 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises CACNA2D3's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without LINC01583 | 0.031 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises CACNA2D3's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without COL8A1 | 0.071 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises CACNA2D3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.76× lower at baseline in the lines without LINC01411 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises CACNA2D3's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.97× lower at baseline in the lines without SIRLNT | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[DDIT4L]] | C | DDIT4L activity raises CACNA2D3's level | lines that do not express DDIT4L (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without DDIT4L | 0.077 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL1B, ARMCX2; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMOD1]] | B | CACNA2D3 activity raises TMOD1's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without CACNA2D3 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824 |
| [[LINC00922]] | B | CACNA2D3 activity raises LINC00922's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 1.83× lower at baseline in the lines without CACNA2D3 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824 |
| [[PSD3]] | B | CACNA2D3 activity raises PSD3's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without CACNA2D3 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824 |
| [[KCNMB2]] | B | CACNA2D3 activity raises KCNMB2's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without CACNA2D3 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824 |
| [[FRMPD4]] | C | CACNA2D3 activity raises FRMPD4's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.09× lower at baseline in the lines without CACNA2D3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[PDE7B]] | C | CACNA2D3 activity raises PDE7B's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without CACNA2D3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[LINC01411]] | C | CACNA2D3 activity raises LINC01411's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 4.00× lower at baseline in the lines without CACNA2D3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[TENM1]] | C | CACNA2D3 activity raises TENM1's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without CACNA2D3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[LINC01885]] | C | CACNA2D3 activity raises LINC01885's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.33× lower at baseline in the lines without CACNA2D3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[BMPER]] | C | CACNA2D3 activity raises BMPER's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.69× lower at baseline in the lines without CACNA2D3 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[COL8A1]] | C | CACNA2D3 activity raises COL8A1's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.95× lower at baseline in the lines without CACNA2D3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[ZMAT4]] | C | CACNA2D3 activity raises ZMAT4's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.94× lower at baseline in the lines without CACNA2D3 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, 34.3); signed map (40.9, 44.2). **Vector** length 58.7, 23.7% of its response variance represented; |z| ≥ 3 in 346 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.5 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit alpha2delta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1-p14.3 — chr3:54,122,552-55,074,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSA272268, alpha2delta-3 |
| Gene groups (HGNC) | Calcium voltage-gated channel auxiliary alpha2delta subunits |
| Reactome | 3 pathways, smallest: Presynaptic depolarization and calcium channel opening; Transmission across Chemical Synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZS8](https://www.uniprot.org/uniprotkb/Q8IZS8) (Voltage-dependent calcium channel subunit alpha-2/delta-3):

> The alpha-2/delta subunit of voltage-dependent calcium channels regulates calcium current density and activation/inactivation kinetics of the calcium channel. Acts as a regulatory subunit for P/Q-type calcium channel (CACNA1A), N-type (CACNA1B), L-type (CACNA1C OR CACNA1D) but not T-type (CACNA1G) (By similarity).

**Summary**, from NCBI Gene [55799](https://www.ncbi.nlm.nih.gov/gene/55799):

> This gene encodes a member of the alpha-2/delta subunit family, a protein in the voltage-dependent calcium channel complex. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization and consist of a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. Various versions of each of these subunits exist, either expressed from similar genes or the result of alternative splicing. Research on a highly similar protein in rabbit suggests the …

**Accessions** — [HGNC:15460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15460) · Entrez [55799](https://www.ncbi.nlm.nih.gov/gene/55799) · UniProt [Q8IZS8](https://www.uniprot.org/uniprotkb/Q8IZS8) · Ensembl [ENSG00000157445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157445)

## Data

Gene col 8071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8071); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8071]; `tensor/DDL_lfc|DDL_z.npy` [8071]; `embed/gene_vectors.npy` [8071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8071 or target_col == 8071). Every well: [[CACNA2D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA2D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
