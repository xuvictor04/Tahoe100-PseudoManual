---
symbol: "PAX2"
type: "gene"
col: 1136
ensembl_id: "ENSG00000075891"
name: "paired box 2"
location: "10q24.31"
module: 128
arm: "+"
pooled_cpm: 8.9
n_lines_expressing: 17
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 29
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# PAX2

*paired box 2* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.97× (z +22.3, q 0e+00, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.646× (z -5.0, q 3e-04, down in 8 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 0.0720×, A498 0.223×, NCI-H2030 0.189×, A-427 0.133×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.142×, A498 0.322×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0674×, A498 0.221×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.342×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC4B]] (+0.65, fdr 2e-05), [[TUB]] (+0.59, fdr 4e-05), [[ADAMTS10]] (+0.58, fdr 2e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); 29 go from it, the strongest it → [[BRSK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.97×** | +22.3 | 0e+00 | 9/14 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +13.8 | 1e-40 | 6/14 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +13.6 | 1e-39 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +11.9 | 3e-30 | 1/9 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.42×** | +10.1 | 8e-22 | 4/14 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +6.4 | 1e-08 | 1/11 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +6.4 | 2e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.0 | 1e-07 | 5/13 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 0/14 | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 3e-04 | 0/13 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.1 | 0.002 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 3/13 (A498, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.004 | 0/14 | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.8 | 0.005 | 1/9 (A-427) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.8 | 0.005 | 0/13 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.009 | 1/14 (H4) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.013 | 0/14 | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.013 | 3/15 (NCI-H23, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.013 | 0/14 | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.014 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1136.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 0.0720×, A498 0.223×, NCI-H2030 0.189×, A-427 0.133×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.142×, A498 0.322×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0674×, A498 0.221×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.342×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -5.0 | 3e-04 | 8/15 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.742× | -3.3 | 0.27 | 0/14 | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.595× | -3.1 | 0.35 | 1/14 (MIA PaCa-2) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.1 | 1 | 8 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0674× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.2) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -23.8) |
| [[A-427 (line)]] | wt | 15.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0274× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.133× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -18.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.142× (z -15.7) |
| [[A549 (line)]] | wt | 3.82 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +12.2) | [[Digitoxin (drug)]] 0.5 µM 0.0341× (z -11.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[AN3 CA (line)]] | alt | 80.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.340× (z -9.8) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC4B]] | +0.65 | +0.63 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[TUB]] | +0.59 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[ADAMTS10]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[DUSP9]] | +0.55 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[LINC00466]] | +0.54 | +0.52 / +0.36 | both halves | 9e-05 |  |
| [[DPYSL5]] | +0.53 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[STOX2]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[LRIG3-DT]] | +0.53 | +0.23 / +0.55 | both halves | 5e-04 |  |
| [[LINC02384]] | +0.53 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[CYS1]] | +0.52 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[FAM184A]] | +0.52 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[LMX1B]] | +0.52 | +0.43 / +0.60 | both halves | 3e-05 | STRING 882 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises PAX2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without KIF26A | 0.026 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SAMD11]] | B | SAMD11 activity raises PAX2's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without SAMD11 | 0.086 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[ARHGAP44]] | B | ARHGAP44 activity raises PAX2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without ARHGAP44 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[LRRC4B]] | C | LRRC4B activity raises PAX2's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 3.00× lower at baseline in the lines without LRRC4B | 0.006 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent; co-absent with the target |
| [[RET]] | C | RET activity raises PAX2's level | lines that do not express RET (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without RET | 0.012 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[CECR2]] | C | CECR2 activity raises PAX2's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.38× lower at baseline in the lines without CECR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises PAX2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without PDZD4 | 0.022 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[GATA4]] | C | GATA4 activity raises PAX2's level | lines that do not express GATA4 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without GATA4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PIEZO2, TAFA5, ZNF667; co-absent with the target |
| [[ANKS1B]] | C | ANKS1B activity raises PAX2's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.34× lower at baseline in the lines without ANKS1B | 0.034 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3; co-absent with the target |
| [[GPC3]] | C | GPC3 activity raises PAX2's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 1.93× lower at baseline in the lines without GPC3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises PAX2's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without MYT1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises PAX2's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without LMX1B | 0.054 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 21, C 8. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK2]] | B | PAX2 activity raises BRSK2's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without PAX2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[GNAL]] | B | PAX2 activity raises GNAL's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without PAX2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[RHBDL3]] | B | PAX2 activity raises RHBDL3's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without PAX2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[MRAS]] | B | PAX2 activity raises MRAS's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.22× lower at baseline in the lines without PAX2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[KNDC1]] | B | PAX2 activity raises KNDC1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without PAX2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[AKAP7]] | B | PAX2 activity raises AKAP7's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.68× lower at baseline in the lines without PAX2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[SEPTIN3]] | B | PAX2 activity raises SEPTIN3's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without PAX2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[ADGRB2]] | B | PAX2 activity raises ADGRB2's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.78× lower at baseline in the lines without PAX2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[KIF26A]] | B | PAX2 activity raises KIF26A's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.02× lower at baseline in the lines without PAX2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[ARHGAP44]] | B | PAX2 activity raises ARHGAP44's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without PAX2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[CYS1]] | B | PAX2 activity raises CYS1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.92× lower at baseline in the lines without PAX2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[KNDC1]] | B | PAX2 activity strengthens KNDC1's drug response | lines that do not express PAX2 (26) vs lines expressing it (15) | the lines without PAX2 respond 0.63× as strongly (z diff +1.67); strongest at Homoharringtonine 5 µM: 0.41x vs 0.19x (z diff +4.6) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.1, 38.7); signed map (23.9, 28.5). **Vector** length 42.6, 10.9% of its response variance represented; |z| ≥ 3 in 378 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +22.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +10.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +13.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | -0.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.0 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -1.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | paired box 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,735,396-100,829,944 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAX-2 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes; Paired boxes |
| Reactome | 6 pathways, smallest: Formation of intermediate mesoderm; Nephron development; Formation of the nephric duct |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02962](https://www.uniprot.org/uniprotkb/Q02962) (Paired box protein Pax-2):

> Transcription factor that may have a role in kidney cell differentiation. Has a critical role in the development of the urogenital tract, the eyes, and the CNS.

**Summary**, from NCBI Gene [5076](https://www.ncbi.nlm.nih.gov/gene/5076):

> PAX2 encodes paired box gene 2, one of many human homologues of the Drosophila melanogaster gene prd. The central feature of this transcription factor gene family is the conserved DNA-binding paired box domain. PAX2 is believed to be a target of transcriptional supression by the tumor suppressor gene WT1. Mutations within PAX2 have been shown to result in optic nerve colobomas and renal hypoplasia. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:8616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8616) · Entrez [5076](https://www.ncbi.nlm.nih.gov/gene/5076) · UniProt [Q02962](https://www.uniprot.org/uniprotkb/Q02962) · Ensembl [ENSG00000075891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075891)

## Data

Gene col 1136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1136); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1136]; `tensor/DDL_lfc|DDL_z.npy` [1136]; `embed/gene_vectors.npy` [1136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1136 or target_col == 1136). Every well: [[PAX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
