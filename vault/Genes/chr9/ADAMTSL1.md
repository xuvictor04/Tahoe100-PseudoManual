---
symbol: "ADAMTSL1"
type: "gene"
col: 10888
ensembl_id: "ENSG00000178031"
name: "ADAMTS like 1"
location: "9p22.2-p22.1"
module: 61
arm: "+"
pooled_cpm: 11.46
n_lines_expressing: 32
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 8
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ADAMTSL1

*ADAMTS like 1* — 9p22.2-p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.82× (z +29.8, q 0e+00, up in 20 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Betamethasone dipropionate (drug)]] 0.05 µM: 0.581× (z -6.0, q 1e-06, down in 13 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01592]] (+0.76, fdr 7e-06), [[ABCA13]] (+0.74, fdr 7e-06), [[OFCC1]] (+0.69, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[ROBO4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.82×** | +29.8 | 0e+00 | 20/25 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.53×** | +25.6 | 0e+00 | 15/26 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.06×** | +16.8 | 0e+00 | 11/19 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +16.3 | 0e+00 | 5/10 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +14.2 | 8e-44 | 18/27 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.95×** | +12.5 | 1e-33 | 17/26 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +11.1 | 8e-27 | 10/16 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.20×** | +9.4 | 3e-19 | 14/27 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +8.7 | 3e-16 | 18/23 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.2 | 2e-14 | 13/28 (J82, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +7.6 | 1e-12 | 12/26 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.9 | 2e-10 | 9/25 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.3 | 1e-08 | 8/25 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 5/26 (LoVo, HCT15, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.5 | 0.016 | 2/11 (SNU-423, HS-578T) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.581×** | -6.0 | 1e-06 | 13/25 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.692×** | -4.4 | 0.003 | 13/25 (H4, SNU-423, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.704×** | -4.2 | 0.005 | 12/27 (H4, SNU-423, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.711×** | -4.1 | 0.006 | 9/26 (H4, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.746×** | -3.5 | 0.050 | 10/25 (Hs 766T, H4, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.078 | 8/25 (H4, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.080 | 10/27 (H4, Hs 766T, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.774× | -3.1 | 0.13 | 9/27 (SHP-77, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.774× | -3.1 | 0.13 | 9/27 (RKO, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 69.9 | 0 | 11 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.161× (z -14.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.6) |
| [[H4 (line)]] | wt | 86.5 | 0 | 8 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.117× (z -10.5) |
| [[A498 (line)]] | wt | 3.62 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 103× (z +23.9) | — |
| [[LoVo (line)]] | wt | 8.40 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.4× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 9.67× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 3.89 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +14.8) | — |
| [[A-172 (line)]] | wt | 11.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.6× (z +16.7) | — |
| [[A-427 (line)]] | wt | 57.7 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0870× (z -13.4) |
| [[HOP62 (line)]] | alt | 3.86 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +16.4) | — |
| [[J82 (line)]] | alt | 3.60 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 78.8× (z +17.2) | — |
| [[SK-MEL-2 (line)]] | alt | 9.11 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.0× (z +17.9) | — |
| [[A549 (line)]] | wt | 3.19 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +10.2) | — |
| [[C32 (line)]] | wt | 5.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 10.3× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 4.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.2× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 42.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +17.6) | — |
| [[HCT15 (line)]] | alt | 4.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.140× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 6.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.8× (z +17.2) | — |
| [[AN3 CA (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01592]] | +0.76 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ABCA13]] | +0.74 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[OFCC1]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[LDB2]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[BAALC]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[LINC01060]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CACNA1A]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PCSK2]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[DGKI]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[KCNN2]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[RERGL]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FGF1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAMTSL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HGF]] | B | HGF activity raises ADAMTSL1's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.05× lower at baseline in the lines without HGF | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[SCN3A]] | B | SCN3A activity raises ADAMTSL1's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without SCN3A | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865 |
| [[LINC00702]] | B | LINC00702 activity raises ADAMTSL1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without LINC00702 | 0.071 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[ROBO4]] | B | ROBO4 activity raises ADAMTSL1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.79× lower at baseline in the lines without ROBO4 | 0.084 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[FMN2]] | B | FMN2 activity raises ADAMTSL1's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without FMN2 | 0.084 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[CDH6]] | B | CDH6 activity raises ADAMTSL1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without CDH6 | 0.085 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[ADAMTS1]] | B | ADAMTS1 activity raises ADAMTSL1's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 2.41× lower at baseline in the lines without ADAMTS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12 |
| [[NR3C1]] | B | NR3C1 activity lowers ADAMTSL1's level | compounds that target NR3C1: 2 of 3 lower it (Betamethasone dipropionate, Dexamethasone) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises ADAMTSL1's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without APCDD1L-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[LINC01592]] | C | LINC01592 activity raises ADAMTSL1's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.66× lower at baseline in the lines without LINC01592 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises ADAMTSL1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 3.10× lower at baseline in the lines without BAALC | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO4]] | B | ADAMTSL1 activity raises ROBO4's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without ADAMTSL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[INHBA]] | B | ADAMTSL1 activity raises INHBA's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 3.77× lower at baseline in the lines without ADAMTSL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[MIR4300HG]] | B | ADAMTSL1 activity raises MIR4300HG's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without ADAMTSL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[PLXNA4]] | B | ADAMTSL1 activity raises PLXNA4's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without ADAMTSL1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[RGS4]] | C | ADAMTSL1 activity raises RGS4's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 3.20× lower at baseline in the lines without ADAMTSL1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent; co-absent with the target |
| [[LINC01592]] | C | ADAMTSL1 activity raises LINC01592's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without ADAMTSL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent; co-absent with the target |
| [[EML1]] | C | ADAMTSL1 activity raises EML1's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 3.37× lower at baseline in the lines without ADAMTSL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent; co-absent with the target |
| [[FZD8]] | C | ADAMTSL1 activity raises FZD8's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without ADAMTSL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, 20.8); signed map (33.6, 27.5). **Vector** length 84.4, 22.1% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +29.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.3 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +25.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | -0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -4.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | ADAMTS like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.2-p22.1 — chr9:17,906,563-18,910,950 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADAMTSR1, FLJ35283; previously C9orf94 |
| Gene groups (HGNC) | I-set domain containing; ADAMTS like; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [Q8N6G6](https://www.uniprot.org/uniprotkb/Q8N6G6) carries no function annotation.

**Summary**, from NCBI Gene [92949](https://www.ncbi.nlm.nih.gov/gene/92949):

> This gene encodes a secreted protein and member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motif) family. This protein lacks the metalloproteinase and disintegrin-like domains, which are typical of the ADAMTS family, but contains other ADAMTS domains, including the thrombospondin type 1 motif. This protein may have important functions in the extracellular matrix. Alternative splicing results in multiple transcript variants encoding distinct proteins. [provided by …

**Accessions** — [HGNC:14632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14632) · Entrez [92949](https://www.ncbi.nlm.nih.gov/gene/92949) · UniProt [Q8N6G6](https://www.uniprot.org/uniprotkb/Q8N6G6) · Ensembl [ENSG00000178031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178031)

## Data

Gene col 10888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10888); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10888]; `tensor/DDL_lfc|DDL_z.npy` [10888]; `embed/gene_vectors.npy` [10888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10888 or target_col == 10888). Every well: [[ADAMTSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
