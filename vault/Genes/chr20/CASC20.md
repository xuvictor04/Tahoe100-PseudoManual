---
symbol: "CASC20"
type: "gene"
col: 13719
ensembl_id: "ENSG00000229876"
name: "cancer susceptibility 20"
location: "20p12.3"
module: 90
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 30
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 19
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CASC20

*cancer susceptibility 20* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.23× (z +16.4, q 0e+00, up in 9 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.0738×, A498 0.195×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 2 lines (A498 0.150×, HEC-1-A 0.0734×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.118×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.287×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0731×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST8SIA1]] (+0.63, fdr 2e-05), [[LINC02208]] (+0.61, fdr 7e-05), [[LINC02763]] (+0.61, fdr 2e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 19 go from it, the strongest it → [[WDR49]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.23×** | +16.4 | 0e+00 | 9/14 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +10.2 | 8e-22 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.41×** | +9.8 | 1e-20 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +7.0 | 4e-10 | 5/14 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +6.8 | 9e-10 | 3/9 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +6.0 | 2e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +5.8 | 6e-07 | 3/15 (A-172, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +5.2 | 1e-05 | 2/18 (HOP62, LoVo) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.8 | 1e-04 | 3/8 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.7 | 2e-04 | 3/22 (A498, SW480, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.07×** | +4.2 | 0.002 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.66×** | +4.0 | 0.002 | 1/11 (SK-MEL-2) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.002 | 6/17 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.59×** | +4.0 | 0.003 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **2.50×** | +3.8 | 0.004 | 3/18 (HOP62, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.65×** | +3.7 | 0.008 | 1/8 (LoVo) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.008 | 3/9 (SHP-77, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.013 | 0/11 | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.023 | 0/9 | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.026 | 2/9 (SHP-77, A498) | inconsistent across doses |  |
| [[Methotrexate (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.037 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.042 | 2/13 (HEC-1-A, A-172) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13719.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.0738×, A498 0.195×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 2 lines (A498 0.150×, HEC-1-A 0.0734×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.118×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.287×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0731×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.645× | -3.4 | 0.43 | 5/14 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.6 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -10.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.150× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 4.18 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0734× (z -9.5) |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -15.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.674 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.650 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.603 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.609 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.617 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.628 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST8SIA1]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LINC02208]] | +0.61 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[LINC02763]] | +0.61 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CLVS1]] | +0.60 | +0.37 / +0.64 | both halves | 9e-05 |  |
| [[CNTNAP4]] | +0.60 | +0.36 / +0.69 | both halves | 1e-04 |  |
| [[LINC00861]] | +0.60 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[LINC01482]] | +0.60 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[DCC]] | +0.60 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CNBD1]] | +0.60 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[ANKRD7]] | +0.59 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[SLC13A4]] | +0.59 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[LINC01798]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASC20's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02360]] | C | LINC02360 activity raises CASC20's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 1.65× lower at baseline in the lines without LINC02360 | 0.058 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR49]] | B | CASC20 activity raises WDR49's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without CASC20 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[DISC1]] | B | CASC20 activity raises DISC1's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without CASC20 | 0.004 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[LVRN]] | B | CASC20 activity raises LVRN's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without CASC20 | 0.009 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[LINC01798]] | B | CASC20 activity raises LINC01798's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without CASC20 | 0.010 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[CPEB2-DT]] | B | CASC20 activity raises CPEB2-DT's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without CASC20 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[FAM184B]] | B | CASC20 activity raises FAM184B's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without CASC20 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[PKIA-AS1]] | B | CASC20 activity raises PKIA-AS1's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without CASC20 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[C1QTNF7]] | B | CASC20 activity raises C1QTNF7's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.31× lower at baseline in the lines without CASC20 | 0.013 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[MGC4859]] | B | CASC20 activity raises MGC4859's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without CASC20 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[TPTE2]] | B | CASC20 activity raises TPTE2's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.95× lower at baseline in the lines without CASC20 | 0.029 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[SNX31]] | B | CASC20 activity raises SNX31's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without CASC20 | 0.032 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[IQCJ]] | B | CASC20 activity raises IQCJ's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without CASC20 | 0.044 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, 23.7); signed map (28.6, 13.1). **Vector** length 25.7, 3.62% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -0.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -0.6 | -0.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.6 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 20 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p12.3 — chr20:6,446,723-6,528,459 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49477) · Entrez [101929244](https://www.ncbi.nlm.nih.gov/gene/101929244) · Ensembl [ENSG00000229876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229876)

## Data

Gene col 13719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13719); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13719]; `tensor/DDL_lfc|DDL_z.npy` [13719]; `embed/gene_vectors.npy` [13719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13719 or target_col == 13719). Every well: [[CASC20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
