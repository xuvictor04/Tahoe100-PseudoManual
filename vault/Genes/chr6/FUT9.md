---
symbol: "FUT9"
type: "gene"
col: 10258
ensembl_id: "ENSG00000172461"
name: "fucosyltransferase 9"
location: "6q16.1"
module: 9
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 10
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 44
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FUT9

*fucosyltransferase 9* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.59× (z +12.2, q 1e-31, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +11.3, q 5e-27, up in 0 of 5 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.607× (z -3.8, q 0.100, down in 0 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0647×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.362×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.483×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERBB4]] (+0.68, fdr 7e-06), [[PRLR]] (+0.65, fdr 1e-05), [[RUNX1T1]] (+0.64, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 44 go from it, the strongest it → [[KSR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.59×** | +12.2 | 1e-31 | 1/6 (CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +11.3 | 5e-27 | 0/5 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.09×** | +10.9 | 4e-25 | 1/4 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.91×** | +8.6 | 2e-15 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +7.4 | 2e-11 | 3/6 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.70×** | +7.4 | 2e-11 | 1/5 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +5.8 | 4e-07 | 4/6 (NCI-H1573, J82, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.63×** | +5.5 | 2e-06 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +5.4 | 5e-06 | 1/6 (SHP-77) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.0 | 3e-05 | 2/5 (J82, SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.22×** | +4.5 | 3e-04 | 0/6 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.21×** | +4.5 | 3e-04 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.83×** | +4.4 | 6e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.001 | 1/5 (J82) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.004 | 3/6 (SHP-77, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.010 | 4/6 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.011 | 1/6 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.011 | 1/6 (NCI-H1573) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.011 | 1/6 (J82) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.020 | 1/6 (J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.053 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.053 | 0/6 | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.0 | 0.068 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10258.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0647×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.362×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.483×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.607×** | -3.8 | 0.100 | 0/6 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.656× | -3.4 | 0.17 | 3/6 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.687× | -3.1 | 0.33 | 1/6 (NCI-H1573) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.689× | -3.0 | 0.33 | 1/6 (J82) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0647× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.5) |
| [[A-427 (line)]] | wt | 60.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.362× (z -10.4) |
| [[A-172 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.626 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERBB4]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PRLR]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RUNX1T1]] | +0.64 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PGR]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[ESRRG]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[KCNB2]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[KLHL13]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[KCNH7]] | +0.60 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[FREM2]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[KCTD8]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LIN28B]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CACNB2]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FUT9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNH7]] | C | KCNH7 activity raises FUT9's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 4.20× lower at baseline in the lines without KCNH7 | 0.008 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises FUT9's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.64× lower at baseline in the lines without BRINP3 | 0.027 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises FUT9's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.27× lower at baseline in the lines without GABRG2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises FUT9's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 2.15× lower at baseline in the lines without LINC02438 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises FUT9's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.65× lower at baseline in the lines without MGAT4C | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises FUT9's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 4.09× lower at baseline in the lines without LINC01456 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[GABRA2]] | C | GABRA2 activity raises FUT9's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without GABRA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[NPFFR2]] | C | NPFFR2 activity raises FUT9's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.95× lower at baseline in the lines without NPFFR2 | 0.047 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises FUT9's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without KCNH5 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises FUT9's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without CTNNA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises FUT9's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 1.77× lower at baseline in the lines without LINC02197 | 0.082 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 10, C 34. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KSR2]] | B | FUT9 activity raises KSR2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without FUT9 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[MID1]] | B | FUT9 activity raises MID1's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without FUT9 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| cells under [[Docetaxel (drug)]] 0.05 µM | B | FUT9 activity raises the cells' numbers under Docetaxel 0.05 µM (protects the cells) | lines that do not express FUT9 (40) vs lines expressing it (8) | the lines without FUT9: 0.83× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | B | FUT9 activity lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | lines that do not express FUT9 (40) vs lines expressing it (8) | the lines without FUT9: 1.16× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[MID1]] | B | FUT9 activity strengthens MID1's drug response | lines that do not express FUT9 (34) vs lines expressing it (10) | the lines without FUT9 respond 0.76× as strongly (z diff +1.81); strongest at Trametinib 5 µM: 1.33x vs 1.85x (z diff +3.2) | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; target measured in part of the lines; the reference differs; artifact flags |
| [[ADGRV1]] | B | FUT9 activity raises ADGRV1's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.00× lower at baseline in the lines without FUT9 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[RALYL]] | B | FUT9 activity raises RALYL's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.45× lower at baseline in the lines without FUT9 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | FUT9 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express FUT9 (40) vs lines expressing it (8) | the lines without FUT9: 0.86× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[SOBP]] | B | FUT9 activity raises SOBP's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.61× lower at baseline in the lines without FUT9 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[ONECUT2]] | B | FUT9 activity raises ONECUT2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.41× lower at baseline in the lines without FUT9 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[RERG]] | C | FUT9 activity raises RERG's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without FUT9 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[SLITRK6]] | C | FUT9 activity raises SLITRK6's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 5.88× lower at baseline in the lines without FUT9 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.5, 36.5); signed map (44.5, 32.1). **Vector** length 25.5, 9.89% of its response variance represented; |z| ≥ 3 in 161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +2.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | fucosyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:96,015,974-96,215,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Fuc-TIX |
| Gene groups (HGNC) | Fucosyltransferases |
| Reactome | 3 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y231](https://www.uniprot.org/uniprotkb/Q9Y231) (4-galactosyl-N-acetylglucosaminide 3-alpha-L-fucosyltransferase 9):

> Catalyzes alpha(1->3) linkage of fucosyl moiety transferred from GDP-beta-L-fucose to N-acetyl glucosamine (GlcNAc) within type 2 lactosamine (LacNAc, beta-D-Gal-(1->4)-beta-D-GlcNAc-) glycan attached to glycolipids and N- or O-linked glycoproteins. Fucosylates distal type 2 LacNAc and its fucosylated (H-type 2 LacNAc) and sialylated (sialyl-type 2 LacNAc) derivatives to form Lewis x (Lex) (CD15) and Lewis y (Ley) antigenic epitopes involved in cell adhesion and differentiation. Generates Lex …

**Summary**, from NCBI Gene [10690](https://www.ncbi.nlm.nih.gov/gene/10690):

> The protein encoded by this gene belongs to the glycosyltransferase family. It is localized to the golgi, and catalyzes the last step in the biosynthesis of Lewis X (LeX) antigen, the addition of a fucose to precursor polysaccharides. This protein is one of the few fucosyltransferases that synthesizes the LeX oligosaccharide (CD15) expressed in the organ buds progressing in mesenchyma during embryogenesis. It is also responsible for the expression of CD15 in mature granulocytes. A common …

**Accessions** — [HGNC:4020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4020) · Entrez [10690](https://www.ncbi.nlm.nih.gov/gene/10690) · UniProt [Q9Y231](https://www.uniprot.org/uniprotkb/Q9Y231) · Ensembl [ENSG00000172461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172461)

## Data

Gene col 10258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10258); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10258]; `tensor/DDL_lfc|DDL_z.npy` [10258]; `embed/gene_vectors.npy` [10258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10258 or target_col == 10258). Every well: [[FUT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
