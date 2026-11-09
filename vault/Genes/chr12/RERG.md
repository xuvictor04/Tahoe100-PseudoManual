---
symbol: "RERG"
type: "gene"
col: 5574
ensembl_id: "ENSG00000134533"
name: "RAS like estrogen regulated growth inhibitor"
location: "12p12.3"
module: 150
arm: "+"
pooled_cpm: 4.35
n_lines_expressing: 26
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# RERG

*RAS like estrogen regulated growth inhibitor* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.32× (z +16.6, q 0e+00, up in 11 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM: 0.700× (z -4.1, q 0.025, down in 7 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0287×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.205×; ⚠ toxic; transcription drop); [[Talc (drug)]] 0.05 µM in 1 line (KATO III 0.0553×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01320]] (+0.64, fdr 2e-05), [[LINC02208]] (+0.63, fdr 7e-06), [[CNTN4]] (+0.61, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[F11-AS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[AGBL4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.32×** | +16.6 | 0e+00 | 11/18 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.84×** | +15.3 | 0e+00 | 8/18 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.19×** | +13.2 | 2e-37 | 21/23 (NCI-H23, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +9.9 | 6e-21 | 1/5 (BT-474) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +9.7 | 5e-20 | 2/6 (BT-474, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +9.1 | 6e-18 | 1/4 (BT-474) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +9.1 | 6e-18 | 9/20 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +8.7 | 3e-16 | 18/23 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.90×** | +8.5 | 8e-16 | 10/23 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +7.4 | 1e-11 | 5/23 (HS-578T, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.64×** | +7.2 | 3e-11 | 14/23 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +6.0 | 8e-08 | 10/21 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.4 | 3e-06 | 5/18 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +5.3 | 6e-06 | 2/15 (NCI-H1792, SW480) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.2 | 7e-06 | 4/20 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +4.9 | 3e-05 | 12/23 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +4.4 | 3e-04 | 14/23 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.3 | 5e-04 | 4/23 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5574.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0287×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.205×; ⚠ toxic; transcription drop); [[Talc (drug)]] 0.05 µM in 1 line (KATO III 0.0553×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.700×** | -4.1 | 0.025 | 7/23 (NCI-H1792, KATO III, …) | all doses, stronger at high dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.641×** | -3.6 | 0.090 | 3/23 (NCI-H2030, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 121 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 4.90 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0553× (z -8.5) |
| [[LoVo (line)]] | wt | 1.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 6.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0287× (z -11.4) |
| [[A-172 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01320]] | +0.64 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LINC02208]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CNTN4]] | +0.61 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[AGBL4]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC01695]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SNTG2]] | +0.60 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LINC02306]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ERC2]] | +0.60 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LINC00871]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[FAT3]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GABRA2]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[CHODL]] | +0.58 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11-AS1]] | B | F11-AS1 activity raises RERG's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without F11-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RERG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FUT9]] | C | FUT9 activity raises RERG's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without FUT9 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises RERG's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.75× lower at baseline in the lines without KCNH7 | 0.005 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises RERG's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.63× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC02484]] | C | LINC02484 activity raises RERG's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 4.59× lower at baseline in the lines without LINC02484 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises RERG's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.52× lower at baseline in the lines without GTSF1 | 0.071 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises RERG's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without CTNNA2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[FREM2]] | C | FREM2 activity raises RERG's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without FREM2 | 0.097 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGBL4]] | B | RERG activity raises AGBL4's level | lines that do not express RERG (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without RERG | 0.057 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent |
| [[SYNPO2]] | B | RERG activity raises SYNPO2's level | lines that do not express RERG (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without RERG | 0.066 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent |
| [[LINC01194]] | C | RERG activity raises LINC01194's level | lines that do not express RERG (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without RERG | 0.020 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent; co-absent with the target |
| [[FSTL5]] | C | RERG activity raises FSTL5's level | lines that do not express RERG (24) vs lines expressing it (26) | 2.52× lower at baseline in the lines without RERG | 0.094 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent; co-absent with the target |
| [[DISC1FP1]] | C | RERG activity raises DISC1FP1's level | lines that do not express RERG (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without RERG | 0.0999 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.4, 29.1); signed map (36.1, 16.4). **Vector** length 37.9, 6.67% of its response variance represented; |z| ≥ 3 in 575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RAS like estrogen regulated growth inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:15,107,783-15,348,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15754 |
| Gene groups (HGNC) | RAS type GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A58](https://www.uniprot.org/uniprotkb/Q96A58) (Ras-related and estrogen-regulated growth inhibitor):

> Binds GDP/GTP and possesses intrinsic GTPase activity. Has higher affinity for GDP than for GTP.

**Summary**, from NCBI Gene [85004](https://www.ncbi.nlm.nih.gov/gene/85004):

> RERG, a member of the RAS superfamily of GTPases, inhibits cell proliferation and tumor formation (Finlin et al., 2001 [PubMed 11533059]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:15980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15980) · Entrez [85004](https://www.ncbi.nlm.nih.gov/gene/85004) · UniProt [Q96A58](https://www.uniprot.org/uniprotkb/Q96A58) · Ensembl [ENSG00000134533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134533)

## Data

Gene col 5574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5574); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5574]; `tensor/DDL_lfc|DDL_z.npy` [5574]; `embed/gene_vectors.npy` [5574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5574 or target_col == 5574). Every well: [[RERG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RERG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
