---
symbol: "ITIH2"
type: "gene"
col: 7546
ensembl_id: "ENSG00000151655"
name: "inter-alpha-trypsin inhibitor heavy chain 2"
location: "10p14"
module: 8
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 8
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 20
direction_downstream: 37
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ITIH2

*inter-alpha-trypsin inhibitor heavy chain 2* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.87× (z +14.2, q 3e-43, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.37× (z +11.8, q 5e-30, up in 1 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.262×, A549 0.0309×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.134×; ⚠ cell-cycle shift, explains ~69% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFBP1]] (+0.82, fdr 1e-05), [[CYP24A1]] (+0.64, fdr 3e-05), [[DSCAML1]] (+0.62, fdr 1e-05); moves opposite to [[SMG9]] (-0.37, fdr 0.003, ⚠ not reproduced), [[LINC02099]] (-0.36, fdr 6e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TNFSF14]] → it (grade C ⚠); 37 go from it, the strongest it → [[ETNK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.87×** | +14.2 | 3e-43 | 3/3 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.12×** | +13.0 | 2e-36 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +11.8 | 5e-30 | 1/4 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.83×** | +11.3 | 3e-27 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +7.1 | 2e-10 | 1/2 (HepG2/C3A) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +6.8 | 1e-09 | 0/3 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.6 | 2e-06 | 2/4 (HepG2/C3A, COLO 205) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.51×** | +5.4 | 4e-06 | 1/2 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +4.6 | 2e-04 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.010 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.86×** | +3.7 | 0.013 | 0/3 | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.5 | 0.024 | 0/4 | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.067 | 0/4 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.00×** | +3.1 | 0.067 | 0/3 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.067 | 0/3 | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.99×** | +3.1 | 0.067 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.068 | 1/5 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7546.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.262×, A549 0.0309×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.134×; ⚠ cell-cycle shift, explains ~69% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Monocrotaline (drug)]] 5 µM |  | 0.585× | -3.6 | 0.19 | 1/4 (CFPAC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 392 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -20.8) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.196× (z -11.5) |
| [[A549 (line)]] | wt | 3.61 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0309× (z -9.5) |
| [[A-172 (line)]] | wt | 0.796 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.664 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP1]] | +0.82 | +0.82 / +0.51 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 489 |
| [[CYP24A1]] | +0.64 | +0.70 / +0.43 | both halves | 3e-05 | **novel candidate** |
| [[DSCAML1]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[CP]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 669 |
| [[FGA]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 811 |
| [[PON3]] | +0.60 | +0.48 / +0.39 | both halves | 6e-05 | **novel candidate** |
| [[AFP]] | +0.59 | +0.51 / +0.71 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 582 |
| [[CD38]] | +0.59 | +0.52 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[TIMD4]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[TARID]] | +0.58 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[HAVCR1]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[FXYD2]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG9]] | -0.37 | -0.35 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[LINC02099]] | -0.36 | -0.22 / -0.28 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF14]] | C | TNFSF14 activity raises ITIH2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.91× lower at baseline in the lines without TNFSF14 | 0.014 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent; co-absent with the target |
| [[APOL1]] | C | APOL1 activity raises ITIH2's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 1.46× lower at baseline in the lines without APOL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises ITIH2's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.24× lower at baseline in the lines without HLA-DRB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises ITIH2's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.49× lower at baseline in the lines without IGFBP1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises ITIH2's level | lines that do not express PIGR (45) vs lines expressing it (5) | 1.71× lower at baseline in the lines without PIGR | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[LINC00278]] | C | LINC00278 activity raises ITIH2's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.69× lower at baseline in the lines without LINC00278 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1; co-absent with the target |
| [[C3]] | C | C3 activity raises ITIH2's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without C3 | 0.045 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[ARSL]] | C | ARSL activity raises ITIH2's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without ARSL | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises ITIH2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.01× lower at baseline in the lines without SERPINA5 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[CP]] | C | CP activity raises ITIH2's level | lines that do not express CP (39) vs lines expressing it (11) | 2.44× lower at baseline in the lines without CP | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |
| [[BMP10]] | C | BMP10 activity raises ITIH2's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 2.26× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[GPR141]] | C | GPR141 activity raises ITIH2's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 1.26× lower at baseline in the lines without GPR141 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 12, C 25. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETNK1]] | B | ITIH2 activity weakens ETNK1's drug response | lines that do not express ITIH2 (42) vs lines expressing it (7) | the lines without ITIH2 respond 3.34× as strongly (z diff -2.39); strongest at Homoharringtonine 5 µM: 1.66x vs 1.04x (z diff -6.9) | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; target measured in part of the lines; artifact flags |
| [[PDZD8]] | B | ITIH2 activity raises PDZD8's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 1.68× lower at baseline in the lines without ITIH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[ODF3B]] | B | ITIH2 activity raises ODF3B's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 1.89× lower at baseline in the lines without ITIH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[PDZD8]] | B | ITIH2 activity weakens PDZD8's drug response | lines that do not express ITIH2 (42) vs lines expressing it (7) | the lines without ITIH2 respond 16.14× as strongly (z diff -3.21); strongest at Homoharringtonine 5 µM: 1.25x vs 0.88x (z diff -6.1) | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; target measured in part of the lines; artifact flags |
| [[SEC16B]] | B | ITIH2 activity raises SEC16B's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.24× lower at baseline in the lines without ITIH2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[IGSF11]] | B | ITIH2 activity raises IGSF11's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.13× lower at baseline in the lines without ITIH2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[SQOR]] | B | ITIH2 activity raises SQOR's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.63× lower at baseline in the lines without ITIH2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[SQOR]] | B | ITIH2 activity strengthens SQOR's drug response | lines that do not express ITIH2 (35) vs lines expressing it (7) | the lines without ITIH2 respond 0.83× as strongly (z diff +1.49); strongest at Topotecan (hydrochloride) 5 µM: 0.72x vs 0.41x (z diff +4.9) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; target measured in part of the lines; artifact flags |
| [[EPCAM-DT]] | B | ITIH2 activity raises EPCAM-DT's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.60× lower at baseline in the lines without ITIH2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[PON3]] | B | ITIH2 activity raises PON3's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without ITIH2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[SLC16A4]] | B | ITIH2 activity raises SLC16A4's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.22× lower at baseline in the lines without ITIH2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[XDH]] | B | ITIH2 activity raises XDH's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.70× lower at baseline in the lines without ITIH2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.360). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.4, 44.7); signed map (52.5, 26.8). **Vector** length 13.8, 4.62% of its response variance represented; |z| ≥ 3 in 89 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +5.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.3 | +3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.3 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.4 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.3 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | inter-alpha-trypsin inhibitor heavy chain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:7,703,316-7,749,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H2P |
| Gene groups (HGNC) | Gla domain containing; Inter-alpha-trypsin inhibitor heavy chains |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P19823](https://www.uniprot.org/uniprotkb/P19823) (Inter-alpha-trypsin inhibitor heavy chain H2):

> May act as a carrier of hyaluronan in serum or as a binding protein between hyaluronan and other matrix protein, including those on cell surfaces in tissues to regulate the localization, synthesis and degradation of hyaluronan which are essential to cells undergoing biological processes.

**Summary**, from NCBI Gene [3698](https://www.ncbi.nlm.nih.gov/gene/3698):

> The inter-alpha-trypsin inhibitors (ITI) are a family of structurally related plasma serine protease inhibitors involved in extracellular matrix stabilization and in prevention of tumor metastasis. The ITI family contains multiple proteins made up of a light chain (see MIM 176870) and a variable number of heavy chains (Salier et al., 1987 [PubMed 2446322]; Himmelfarb et al., 2004 [PubMed 14744536]).[supplied by OMIM, Nov 2009]

**Accessions** — [HGNC:6167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6167) · Entrez [3698](https://www.ncbi.nlm.nih.gov/gene/3698) · UniProt [P19823](https://www.uniprot.org/uniprotkb/P19823) · Ensembl [ENSG00000151655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151655)

## Data

Gene col 7546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7546); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7546]; `tensor/DDL_lfc|DDL_z.npy` [7546]; `embed/gene_vectors.npy` [7546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7546 or target_col == 7546). Every well: [[ITIH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITIH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
