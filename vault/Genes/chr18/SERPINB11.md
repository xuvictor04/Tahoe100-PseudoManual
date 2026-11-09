---
symbol: "SERPINB11"
type: "gene"
col: 13030
ensembl_id: "ENSG00000206072"
name: "serpin family B member 11"
location: "18q21.33"
module: 19
arm: "+"
pooled_cpm: 6.67
n_lines_expressing: 7
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 19
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SERPINB11

*serpin family B member 11* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.55× (z +10.0, q 1e-20, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +5.2, q 2e-05, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0329×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0236×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.102×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0478×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP10]] (+0.88, fdr 7e-06), [[SCARA5]] (+0.80, fdr 7e-06), [[LINC03000]] (+0.80, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[GTF2I-AS1]] → it (grade C ⚠); 19 go from it, the strongest it → [[PLAC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.55×** | +10.0 | 1e-20 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.25×** | +9.3 | 6e-18 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.82×** | +7.2 | 1e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.2 | 2e-05 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.78×** | +3.8 | 0.015 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.6 | 0.028 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.95×** | +3.3 | 0.074 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.3 | 0.074 | 0/3 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.2 | 0.074 | 0/3 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.70× | +3.1 | 0.11 | 0/3 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.70× | +3.1 | 0.11 | 0/4 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0329×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0236×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.102×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0478×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.554× | -3.4 | 0.15 | 3/4 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.557× | -3.4 | 0.15 | 3/4 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.535× | -3.4 | 0.15 | 2/4 (NCI-H460, BT-474) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.587× | -3.1 | 0.27 | 0/4 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.568× | -3.0 | 0.27 | 0/4 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 117 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0329× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0236× (z -17.7) |
| [[A-172 (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.993 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.660 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP10]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.80 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[GREM2]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[RHOH]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.77 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.76 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.76 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.75 | +0.62 / +0.83 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[PLAC4]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises SERPINB11's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.32× lower at baseline in the lines without GTF2I-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC00824]] | C | LINC00824 activity raises SERPINB11's level | lines that do not express LINC00824 (46) vs lines expressing it (4) | 7.79× lower at baseline in the lines without LINC00824 | 0.013 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SUCNR1, ENSG00000289530; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises SERPINB11's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.46× lower at baseline in the lines without LINC03000 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises SERPINB11's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.76× lower at baseline in the lines without SCARA5 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[LINC01967]] | C | LINC01967 activity raises SERPINB11's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 2.01× lower at baseline in the lines without LINC01967 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises SERPINB11's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.45× lower at baseline in the lines without CHL1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises SERPINB11's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.37× lower at baseline in the lines without SLC15A5 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises SERPINB11's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.30× lower at baseline in the lines without CTNND2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises SERPINB11's level | lines that do not express TBXT (47) vs lines expressing it (3) | 9.48× lower at baseline in the lines without TBXT | 0.089 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[C5orf46]] | C | C5orf46 activity raises SERPINB11's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without C5orf46 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises SERPINB11's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.13× lower at baseline in the lines without GREM2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[GDA]] | C | GDA activity raises SERPINB11's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without GDA | 0.092 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | SERPINB11 activity raises PLAC4's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 3.39× lower at baseline in the lines without SERPINB11 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[SPDYE10]] | B | SERPINB11 activity raises SPDYE10's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 1.92× lower at baseline in the lines without SERPINB11 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[RGS2]] | B | SERPINB11 activity raises RGS2's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.98× lower at baseline in the lines without SERPINB11 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[PART1]] | B | SERPINB11 activity raises PART1's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 1.85× lower at baseline in the lines without SERPINB11 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[TMEM154]] | C | SERPINB11 activity raises TMEM154's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 4.41× lower at baseline in the lines without SERPINB11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[LINC00824]] | C | SERPINB11 activity raises LINC00824's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 6.69× lower at baseline in the lines without SERPINB11 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[SHC4]] | C | SERPINB11 activity raises SHC4's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 3.96× lower at baseline in the lines without SERPINB11 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[LINC02742]] | C | SERPINB11 activity raises LINC02742's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 4.49× lower at baseline in the lines without SERPINB11 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[LINC01967]] | C | SERPINB11 activity raises LINC01967's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.74× lower at baseline in the lines without SERPINB11 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[LAMB4]] | C | SERPINB11 activity raises LAMB4's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.28× lower at baseline in the lines without SERPINB11 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[SCARA5]] | C | SERPINB11 activity raises SCARA5's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 3.02× lower at baseline in the lines without SERPINB11 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[DDIT4L]] | C | SERPINB11 activity raises DDIT4L's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.57× lower at baseline in the lines without SERPINB11 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 36.2); signed map (42.9, 44.3). **Vector** length 36.9, 26.7% of its response variance represented; |z| ≥ 3 in 137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,647,579-63,726,432 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P15](https://www.uniprot.org/uniprotkb/Q96P15) (Serpin B11):

> Has no serine protease inhibitory activity, probably due to variants in the scaffold impairing conformational change.

**Summary**, from NCBI Gene [89778](https://www.ncbi.nlm.nih.gov/gene/89778):

> Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to be located in cytoplasm. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14221) · Entrez [89778](https://www.ncbi.nlm.nih.gov/gene/89778) · UniProt [Q96P15](https://www.uniprot.org/uniprotkb/Q96P15) · Ensembl [ENSG00000206072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206072)

## Data

Gene col 13030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13030); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13030]; `tensor/DDL_lfc|DDL_z.npy` [13030]; `embed/gene_vectors.npy` [13030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13030 or target_col == 13030). Every well: [[SERPINB11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
