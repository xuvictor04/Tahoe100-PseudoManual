---
symbol: "FENDRR"
type: "gene"
col: 15598
ensembl_id: "ENSG00000268388"
name: "FOXF1 adjacent non-coding developmental regulatory RNA"
location: "16q24.1"
module: 19
arm: "+"
pooled_cpm: 6.49
n_lines_expressing: 11
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 19
direction_downstream: 24
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# FENDRR

*FOXF1 adjacent non-coding developmental regulatory RNA* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.77× (z +10.0, q 1e-20, up in 2 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.426× (z -5.7, q 9e-06, down in 5 of 8 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GREM2]] (+0.85, fdr 7e-06), [[KCNK2]] (+0.84, fdr 7e-06), [[SCARA5]] (+0.77, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 24 go from it, the strongest it → [[LINC00922]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +10.0 | 1e-20 | 2/9 (HOP62, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +8.3 | 4e-14 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +8.0 | 3e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +5.6 | 3e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.35×** | +4.2 | 0.003 | 1/6 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.9 | 0.010 | 2/8 (SNU-423, SW 900) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.12×** | +3.7 | 0.016 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.65×** | +3.5 | 0.028 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +3.5 | 0.030 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Megestrol (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.088 | 0/8 | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.088 | 1/6 (H4) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.86×** | +3.1 | 0.096 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.426×** | -5.7 | 9e-06 | 5/8 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -4.8 | 4e-04 | 5/8 (NCI-H460, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -4.4 | 0.002 | 6/8 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -3.9 | 0.010 | 7/8 (CHP-212, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -3.9 | 0.010 | 5/8 (CHP-212, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.596×** | -3.4 | 0.056 | 3/9 (SNU-423, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -3.4 | 0.056 | 4/8 (SNU-1, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.603×** | -3.2 | 0.092 | 2/8 (NCI-H460, SNU-1) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -3.1 | 0.11 | 0/9 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.636× | -3.1 | 0.11 | 0/8 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.639× | -3.1 | 0.11 | 5/8 (NCI-H460, SNU-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.0 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0468× (z -16.9) |
| [[SNU-1 (line)]] | wt | 365 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -27.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.9) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0429× (z -16.2) |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0218× (z -15.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0661× (z -10.0) |
| [[H4 (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0359× (z -11.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0384× (z -10.8) |
| [[A-172 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.715 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.620 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GREM2]] | +0.85 | +0.82 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.84 | +0.73 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[LINC01257]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.76 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.74 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DPP10]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[PLAC4]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FENDRR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CTNND2]] | C | CTNND2 activity raises FENDRR's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without CTNND2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises FENDRR's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without C5orf46 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises FENDRR's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.53× lower at baseline in the lines without KCNE4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises FENDRR's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.49× lower at baseline in the lines without DPP10 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises FENDRR's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.45× lower at baseline in the lines without GTF2I-AS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises FENDRR's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.31× lower at baseline in the lines without SCARA5 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises FENDRR's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 5.84× lower at baseline in the lines without LINC03000 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises FENDRR's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 2.46× lower at baseline in the lines without TENM2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises FENDRR's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 3.73× lower at baseline in the lines without GREM2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[CDH11]] | C | CDH11 activity raises FENDRR's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.39× lower at baseline in the lines without CDH11 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises FENDRR's level | lines that do not express TBXT (47) vs lines expressing it (3) | 4.81× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 5, C 19. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00922]] | B | FENDRR activity raises LINC00922's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.60× lower at baseline in the lines without FENDRR | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[RBFOX1]] | B | FENDRR activity raises RBFOX1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.86× lower at baseline in the lines without FENDRR | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[APLN]] | B | FENDRR activity raises APLN's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 1.85× lower at baseline in the lines without FENDRR | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[PLAC4]] | B | FENDRR activity raises PLAC4's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without FENDRR | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[AQP4-AS1]] | B | FENDRR activity raises AQP4-AS1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.13× lower at baseline in the lines without FENDRR | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[CDH11]] | C | FENDRR activity raises CDH11's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 4.77× lower at baseline in the lines without FENDRR | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[BMPER]] | C | FENDRR activity raises BMPER's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.58× lower at baseline in the lines without FENDRR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[PAK3]] | C | FENDRR activity raises PAK3's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.74× lower at baseline in the lines without FENDRR | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[STEAP1B-AS1]] | C | FENDRR activity raises STEAP1B-AS1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.95× lower at baseline in the lines without FENDRR | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[PDE7B]] | C | FENDRR activity raises PDE7B's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.67× lower at baseline in the lines without FENDRR | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[SCUBE1]] | C | FENDRR activity raises SCUBE1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.34× lower at baseline in the lines without FENDRR | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[SCARA5]] | C | FENDRR activity raises SCARA5's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.36× lower at baseline in the lines without FENDRR | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 35.9); signed map (42.5, 44.1). **Vector** length 49.2, 21.7% of its response variance represented; |z| ≥ 3 in 271 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +0.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.7 | +2.8 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | FOXF1 adjacent non-coding developmental regulatory RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q24.1 — chr16:86,474,529-86,509,099 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lincFOXF1, onco-lncRNA-21; previously FOXF1-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [400550](https://www.ncbi.nlm.nih.gov/gene/400550):

> This gene produces a spliced long non-coding RNA transcribed bidirectionally with FOXF1 on the opposite strand. A similar gene in mouse is essential for normal development of the heart and body wall. The encoded transcript is thought to act by binding to polycomb repressive complex 2 (PRC2) and/or TrxG/MLL complexes to promote the methylation of the promoters of target genes, thus reducing their expression. It has been suggested that this transcript may play a role in the progression of gastric …

**Accessions** — [HGNC:43894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43894) · Entrez [400550](https://www.ncbi.nlm.nih.gov/gene/400550) · Ensembl [ENSG00000268388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268388)

## Data

Gene col 15598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15598); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15598]; `tensor/DDL_lfc|DDL_z.npy` [15598]; `embed/gene_vectors.npy` [15598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15598 or target_col == 15598). Every well: [[FENDRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FENDRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
