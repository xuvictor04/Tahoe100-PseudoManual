---
symbol: "PRSS51"
type: "gene"
col: 14826
ensembl_id: "ENSG00000253649"
name: "serine protease 51"
location: "8p23.1"
module: 8
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 19
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PRSS51

*serine protease 51* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.12× (z +12.1, q 7e-31, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +5.6, q 3e-06, up in 0 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.0482×, CFPAC-1 0.0630×, COLO 205 0.113×); [[Harringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.120×, CFPAC-1 0.122×, COLO 205 0.177×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.106×, AsPC-1 0.0974×; ⚠ cell-cycle shift, explains ~52% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.214×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.137×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A1]] (+0.75, fdr 7e-06), [[SPATA6L]] (+0.67, fdr 8e-06), [[GABRP]] (+0.66, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CRACDL]] → it (grade B ⚠); 5 go from it, the strongest it → [[UNC5CL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.12×** | +12.1 | 7e-31 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.83×** | +9.6 | 3e-19 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +8.9 | 2e-16 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.6 | 3e-06 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.38×** | +4.8 | 2e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.7 | 3e-04 | 4/12 (AsPC-1, HCT15, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.3 | 0.001 | 1/11 (Hs 766T) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.1 | 0.003 | 0/10 | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.004 | 0/10 | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.9 | 0.005 | 0/10 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.005 | 0/11 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.8 | 0.008 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.62×** | +3.7 | 0.009 | 2/10 (HOP62, CFPAC-1) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.012 | 4/12 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.013 | 1/9 (Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.3 | 0.030 | 0/7 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.037 | 0/11 | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.2 | 0.038 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.039 | 1/10 (NCI-H2030) | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.040 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.040 | 1/13 (NCI-H2030) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.042 | 2/13 (AsPC-1, HCT15) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.0482×, CFPAC-1 0.0630×, COLO 205 0.113×); [[Harringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.120×, CFPAC-1 0.122×, COLO 205 0.177×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.106×, AsPC-1 0.0974×; ⚠ cell-cycle shift, explains ~52% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.214×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.137×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.643× | -3.4 | 0.34 | 11/14 (SHP-77, CFPAC-1, …) | top dose only | composition shift |
| [[Pimozide (drug)]] 5 µM |  | 0.672× | -3.1 | 0.57 | 2/12 (HOP62, AsPC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 77.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0630× (z -18.6) |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0675× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0482× (z -20.4) |
| [[A-172 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.924 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.775 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.754 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.824 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.571 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A1]] | +0.75 | +0.64 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SPATA6L]] | +0.67 | +0.58 / +0.62 | both halves | 8e-06 | **novel candidate** |
| [[GABRP]] | +0.66 | +0.62 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[SLC34A2]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CRACDL]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TTC22]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[PROM2]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RORC]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[IL17RE]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HHLA2]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SCNN1A]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[FAAH2]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACDL]] | B | CRACDL activity raises PRSS51's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without CRACDL | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[SPINT1]] | B | SPINT1 activity raises PRSS51's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 1.91× lower at baseline in the lines without SPINT1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[BCL2L15]] | B | BCL2L15 activity raises PRSS51's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without BCL2L15 | 0.079 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[FAAH2]] | B | FAAH2 activity raises PRSS51's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without FAAH2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[IGFBP1]] | C | IGFBP1 activity raises PRSS51's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.60× lower at baseline in the lines without IGFBP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[ADAM28]] | C | ADAM28 activity raises PRSS51's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.03× lower at baseline in the lines without ADAM28 | 0.011 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises PRSS51's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.59× lower at baseline in the lines without ITIH2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[FGA]] | C | FGA activity raises PRSS51's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.38× lower at baseline in the lines without FGA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises PRSS51's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.90× lower at baseline in the lines without DSCAML1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises PRSS51's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without F11-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises PRSS51's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.24× lower at baseline in the lines without SERPINA5 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises PRSS51's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.70× lower at baseline in the lines without SLC44A4 | 0.075 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5CL]] | B | PRSS51 activity raises UNC5CL's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 1.35× lower at baseline in the lines without PRSS51 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1 |
| [[SMIM2-AS1]] | C | PRSS51 activity raises SMIM2-AS1's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without PRSS51 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1; co-absent with the target |
| [[SNTG1]] | C | PRSS51 activity raises SNTG1's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 2.05× lower at baseline in the lines without PRSS51 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1; co-absent with the target |
| [[SERPINA5]] | C | PRSS51 activity raises SERPINA5's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without PRSS51 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1; co-absent with the target |
| [[TMC5]] | C | PRSS51 activity raises TMC5's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without PRSS51 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 54.9); signed map (60.8, 1.1). **Vector** length 35.7, 9.89% of its response variance represented; |z| ≥ 3 in 322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +1.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -2.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 51 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:10,482,878-10,547,624 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serine proteases |
| Matched by | ensembl_id |

UniProt [A0A1B0GVH4](https://www.uniprot.org/uniprotkb/A0A1B0GVH4) carries no function annotation.

**Summary**, from NCBI Gene [346702](https://www.ncbi.nlm.nih.gov/gene/346702):

> Predicted to enable serine-type peptidase activity. Predicted to be involved in protein processing. Predicted to be located in extracellular region. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37321) · Entrez [346702](https://www.ncbi.nlm.nih.gov/gene/346702) · UniProt [A0A1B0GVH4](https://www.uniprot.org/uniprotkb/A0A1B0GVH4) · Ensembl [ENSG00000253649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253649)

## Data

Gene col 14826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14826); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14826]; `tensor/DDL_lfc|DDL_z.npy` [14826]; `embed/gene_vectors.npy` [14826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14826 or target_col == 14826). Every well: [[PRSS51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
