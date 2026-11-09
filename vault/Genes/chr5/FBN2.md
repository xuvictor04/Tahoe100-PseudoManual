---
symbol: "FBN2"
type: "gene"
col: 6249
ensembl_id: "ENSG00000138829"
name: "fibrillin 2"
location: "5q23.3"
module: 121
arm: "+"
pooled_cpm: 16.4
n_lines_expressing: 19
n_dd_up: 27
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 14
direction_downstream: 17
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# FBN2

*fibrillin 2* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.65× (z +32.1, q 0e+00, up in 12 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.704× (z -5.2, q 1e-04, down in 4 of 16 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01776]] (+0.56, fdr 1e-05), [[PHACTR1]] (+0.56, fdr 1e-05), [[MYOSLID]] (+0.53, fdr 5e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TENM3-AS1]] → it (grade B ⚠); 17 go from it, the strongest it → [[TENM3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.65×** | +32.1 | 0e+00 | 12/14 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +25.6 | 0e+00 | 10/14 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +15.0 | 0e+00 | 4/13 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.70×** | +14.7 | 0e+00 | 11/15 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +14.2 | 2e-43 | 1/10 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +12.7 | 1e-34 | 11/16 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +9.0 | 2e-17 | 10/15 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +8.9 | 5e-17 | 4/11 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +8.8 | 6e-17 | 7/17 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.9 | 1e-13 | 5/14 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.6 | 1e-12 | 8/16 (A549, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.2 | 3e-11 | 2/14 (A549, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +6.4 | 6e-09 | 7/15 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.40×** | +5.0 | 2e-05 | 2/14 (A-172, CHP-212) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +4.5 | 3e-04 | 6/14 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.3 | 6e-04 | 9/17 (A549, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.033 | 5/16 (A-172, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.033 | 1/15 (SW48) | two highest doses | position effect removed |
| [[Acetohexamide (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.033 | 0/15 | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.035 | 0/15 | inconsistent across doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.039 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.704×** | -5.2 | 1e-04 | 4/16 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.709×** | -5.1 | 1e-04 | 1/16 (NCI-H1792) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.744×** | -4.4 | 0.002 | 0/17 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.741×** | -4.1 | 0.005 | 2/14 (hTERT-HPNE, NCI-H1792) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.822×** | -4.1 | 0.005 | 3/17 (SW48, A549, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.5 | 0.047 | 0/17 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.053 | 0/17 | rises with dose |  |
| [[Verapamil (drug)]] 0.05 µM |  | **0.786×** | -3.3 | 0.071 | 1/16 (SNU-423) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 90.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0897× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +14.4) | — |
| [[A549 (line)]] | wt | 42.7 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +9.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.37× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 5.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.1× (z +20.2) | — |
| [[J82 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -9.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 12.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +14.0) | — |
| [[A-172 (line)]] | wt | 68.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.5) | — |
| [[H4 (line)]] | wt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 52.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +8.7) | — |
| [[SW48 (line)]] | wt | 4.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.8× (z +11.7) | — |
| [[A-427 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 155 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01776]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PHACTR1]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MYOSLID]] | +0.53 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[COL12A1]] | +0.52 | +0.52 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 471 |
| [[LINC00993]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[FLG-AS1]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MYLK]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 503 |
| [[NETO1]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[BNC1]] | +0.51 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[S1PR3]] | +0.50 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CLCN4]] | +0.50 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[CALD1]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 3, C 11. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises FBN2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without TENM3-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FBN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TRPM2]] | B | TRPM2 activity raises FBN2's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without TRPM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[ALPK2]] | C | ALPK2 activity raises FBN2's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 4.04× lower at baseline in the lines without ALPK2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises FBN2's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 3.66× lower at baseline in the lines without ADAMTS12 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises FBN2's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 3.31× lower at baseline in the lines without FMN2 | 0.022 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises FBN2's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.41× lower at baseline in the lines without PSG5 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises FBN2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.86× lower at baseline in the lines without NLGN4Y | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[NALF1]] | C | NALF1 activity raises FBN2's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 3.17× lower at baseline in the lines without NALF1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[LINC02241]] | C | LINC02241 activity raises FBN2's level | lines that do not express LINC02241 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without LINC02241 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259560, LINC02616, LINC02476; maybe low, not absent; co-absent with the target |
| [[COL4A1]] | C | COL4A1 activity raises FBN2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 3.24× lower at baseline in the lines without COL4A1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises FBN2's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.25× lower at baseline in the lines without PDCD1LG2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3-AS1]] | B | FBN2 activity raises TENM3-AS1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without FBN2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[HDAC2-AS2]] | B | FBN2 activity raises HDAC2-AS2's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without FBN2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[ZFPM2]] | B | FBN2 activity raises ZFPM2's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without FBN2 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[SCHIP1]] | B | FBN2 activity raises SCHIP1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 2.02× lower at baseline in the lines without FBN2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[LINC01687]] | C | FBN2 activity raises LINC01687's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without FBN2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[ALPK2]] | C | FBN2 activity raises ALPK2's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 3.09× lower at baseline in the lines without FBN2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[NALF1]] | C | FBN2 activity raises NALF1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 5.29× lower at baseline in the lines without FBN2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[WNT5B]] | C | FBN2 activity raises WNT5B's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 3.87× lower at baseline in the lines without FBN2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[ADAMTS12]] | C | FBN2 activity raises ADAMTS12's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 4.07× lower at baseline in the lines without FBN2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[NLGN4Y]] | C | FBN2 activity raises NLGN4Y's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 3.57× lower at baseline in the lines without FBN2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[COL12A1]] | C | FBN2 activity raises COL12A1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 5.08× lower at baseline in the lines without FBN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[CACNA2D1]] | C | FBN2 activity raises CACNA2D1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 4.45× lower at baseline in the lines without FBN2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.7, 24.3); signed map (40.2, 26.6). **Vector** length 50.8, 14.5% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +25.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +32.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fibrillin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:128,257,909-128,659,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DA9; previously CCA |
| Gene groups (HGNC) | Fibrillin family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Degradation of the extracellular matrix |
| Matched by | ensembl_id |

**Function**, from UniProt [P35556](https://www.uniprot.org/uniprotkb/P35556) (Fibrillin-2):

> [Fibrillin-2]: Fibrillins are structural components of 10-12 nm extracellular calcium-binding microfibrils, which occur either in association with elastin or in elastin-free bundles. Fibrillin-2-containing microfibrils regulate the early process of elastic fiber assembly. Regulates osteoblast maturation by controlling TGF-beta bioavailability and calibrating TGF-beta and BMP levels, respectively.; [Placensin]: Hormone secreted by trophoblasts that promotes trophoblast invasiveness. Has …

**Summary**, from NCBI Gene [2201](https://www.ncbi.nlm.nih.gov/gene/2201):

> The protein encoded by this gene is a component of connective tissue microfibrils and may be involved in elastic fiber assembly. Mutations in this gene cause congenital contractural arachnodactyly. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3604) · Entrez [2201](https://www.ncbi.nlm.nih.gov/gene/2201) · UniProt [P35556](https://www.uniprot.org/uniprotkb/P35556) · Ensembl [ENSG00000138829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138829)

## Data

Gene col 6249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6249); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6249]; `tensor/DDL_lfc|DDL_z.npy` [6249]; `embed/gene_vectors.npy` [6249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6249 or target_col == 6249). Every well: [[FBN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
