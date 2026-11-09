---
symbol: "KCNMB2"
type: "gene"
col: 12424
ensembl_id: "ENSG00000197584"
name: "potassium calcium-activated channel subfamily M regulatory beta subunit 2"
location: "3q26.32"
module: 19
arm: "+"
pooled_cpm: 16.77
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 25
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# KCNMB2

*potassium calcium-activated channel subfamily M regulatory beta subunit 2* — 3q26.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.79× (z +26.3, q 0e+00, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.678× (z -4.2, q 0.018, down in 12 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0734×, NCI-H460 0.0656×, RPMI-7951 0.119×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SHP-77 0.158×, NCI-H460 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.0688×, NCI-H460 0.173×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.215×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.148×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCM]] (+0.82, fdr 7e-06), [[PCDH15]] (+0.77, fdr 7e-06), [[LINC00461]] (+0.71, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[PCSK1]] → it (grade B ⚠); 7 go from it, the strongest it → [[STEAP1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.79×** | +26.3 | 0e+00 | 18/24 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +14.4 | 2e-44 | 4/7 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +10.5 | 1e-23 | 11/18 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.57×** | +10.0 | 3e-21 | 15/27 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +8.4 | 6e-15 | 7/14 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.2 | 5e-08 | 7/24 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.9 | 8e-05 | 7/22 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.6 | 3e-04 | 10/28 (RKO, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.3 | 1e-03 | 9/29 (A498, SK-MEL-2, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.49×** | +4.2 | 0.001 | 3/21 (SW 900, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.071 | 8/27 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.073 | 11/26 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.098 | 4/19 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12424.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0734×, NCI-H460 0.0656×, RPMI-7951 0.119×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SHP-77 0.158×, NCI-H460 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.0688×, NCI-H460 0.173×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.215×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -4.2 | 0.018 | 12/28 (RPMI-7951, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.702×** | -3.8 | 0.045 | 10/27 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.683×** | -3.5 | 0.082 | 8/30 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.719× | -3.3 | 0.16 | 1/27 (HepG2/C3A) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.748× | -3.1 | 0.21 | 11/28 (SHP-77, HepG2/C3A, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.719× | -3.0 | 0.21 | 6/28 (LOX-IMVI, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 499 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -24.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 52.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0656× (z -20.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.148× (z -9.9) |
| [[A498 (line)]] | wt | 4.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 7.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 5.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 4.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 4.98 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0612× (z -9.3) |
| [[LoVo (line)]] | wt | 4.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.87× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 4.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 5.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0688× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +12.0) | — |
| [[A-172 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCM]] | +0.82 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PCDH15]] | +0.77 | +0.63 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LINC00461]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NKAIN2]] | +0.71 | +0.57 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[KCNJ6]] | +0.70 | +0.55 / +0.76 | both halves | 1e-05 | pathway: Neuronal System |
| [[LINC01035]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[AGBL1]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ANO3]] | +0.68 | +0.58 / +0.66 | both halves | 8e-06 | **novel candidate** |
| [[GRIK1]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | pathway: Neuronal System |
| [[DOK6]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[ADGRD1]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[LSAMP]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK1]] | B | PCSK1 activity raises KCNMB2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.54× lower at baseline in the lines without PCSK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[TOP2A]] | B | TOP2A activity lowers KCNMB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CALCA]] | B | CALCA activity raises KCNMB2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.17× lower at baseline in the lines without CALCA | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[SCARA5]] | B | SCARA5 activity raises KCNMB2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.06× lower at baseline in the lines without SCARA5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[LINC01456]] | B | LINC01456 activity raises KCNMB2's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.91× lower at baseline in the lines without LINC01456 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8 |
| [[DPP10]] | B | DPP10 activity raises KCNMB2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.38× lower at baseline in the lines without DPP10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[LINC01508]] | B | LINC01508 activity raises KCNMB2's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.60× lower at baseline in the lines without LINC01508 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX |
| [[CGA]] | B | CGA activity raises KCNMB2's level | lines that do not express CGA (44) vs lines expressing it (6) | 6.01× lower at baseline in the lines without CGA | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[SYT4]] | B | SYT4 activity raises KCNMB2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.11× lower at baseline in the lines without SYT4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[ADGRD1]] | B | ADGRD1 activity raises KCNMB2's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 2.97× lower at baseline in the lines without ADGRD1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5 |
| [[KCNE4]] | B | KCNE4 activity raises KCNMB2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without KCNE4 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[KCNB2]] | B | KCNB2 activity raises KCNMB2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.85× lower at baseline in the lines without KCNB2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1B]] | B | KCNMB2 activity raises STEAP1B's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without KCNMB2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[SLCO1C1]] | B | KCNMB2 activity raises SLCO1C1's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without KCNMB2 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[ENPEP]] | B | KCNMB2 activity raises ENPEP's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.17× lower at baseline in the lines without KCNMB2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[PDE3A]] | B | KCNMB2 activity raises PDE3A's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without KCNMB2 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[STEAP1B]] | B | KCNMB2 activity weakens STEAP1B's drug response | lines that do not express KCNMB2 (17) vs lines expressing it (30) | the lines without KCNMB2 respond 1.33× as strongly (z diff -0.44); strongest at Idarubicin (hydrochloride) 5 µM: 2.34x vs 1.52x (z diff -3.0) | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[KCNE4]] | B | KCNMB2 activity raises KCNE4's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without KCNMB2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[CPS1]] | B | KCNMB2 activity raises CPS1's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without KCNMB2 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.7, 34.8); signed map (42.9, 39.5). **Vector** length 56.9, 12.0% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +26.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.0 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily M regulatory beta subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.32 — chr3:178,272,932-178,844,429 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Potassium calcium-activated channel subfamily M regulatory beta subunits |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 7 pathways, smallest: Ca2+ activated K+ channels; cGMP effects; Nitric oxide stimulates guanylate cyclase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y691](https://www.uniprot.org/uniprotkb/Q9Y691) (Calcium-activated potassium channel subunit beta-2):

> Regulatory subunit of the calcium activated potassium KCNMA1 (maxiK) channel. Modulates the calcium sensitivity and gating kinetics of KCNMA1, thereby contributing to KCNMA1 channel diversity. Acts as a negative regulator that confers rapid and complete inactivation of KCNMA1 channel complex. May participate in KCNMA1 inactivation in chromaffin cells of the adrenal gland or in hippocampal CA1 neurons.

**Summary**, from NCBI Gene [10242](https://www.ncbi.nlm.nih.gov/gene/10242):

> MaxiK channels are large conductance, voltage and calcium-sensitive potassium channels which are fundamental to the control of smooth muscle tone and neuronal excitability. MaxiK channels can be formed by 2 subunits: the pore-forming alpha subunit and the modulatory beta subunit. The protein encoded by this gene is an auxiliary beta subunit which decreases the activation time of MaxiK alpha subunit currents. Alternative splicing results in multiple transcript variants of this gene. Additional …

**Accessions** — [HGNC:6286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6286) · Entrez [10242](https://www.ncbi.nlm.nih.gov/gene/10242) · UniProt [Q9Y691](https://www.uniprot.org/uniprotkb/Q9Y691) · Ensembl [ENSG00000197584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197584)

## Data

Gene col 12424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12424); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12424]; `tensor/DDL_lfc|DDL_z.npy` [12424]; `embed/gene_vectors.npy` [12424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12424 or target_col == 12424). Every well: [[KCNMB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNMB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
