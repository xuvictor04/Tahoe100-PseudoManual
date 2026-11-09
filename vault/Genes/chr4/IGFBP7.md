---
symbol: "IGFBP7"
type: "gene"
col: 8692
ensembl_id: "ENSG00000163453"
name: "insulin like growth factor binding protein 7"
location: "4q12"
module: 13
arm: "+"
pooled_cpm: 64.09
n_lines_expressing: 23
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 41
direction_downstream: 36
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# IGFBP7

*insulin like growth factor binding protein 7* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.24× (z +15.7, q 0e+00, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +4.7, q 5e-04, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.548× (z -6.5, q 4e-08, down in 19 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTHRC1]] (+0.64, fdr 7e-06), [[COL1A2]] (+0.59, fdr 1e-05), [[ANGPTL2]] (+0.58, fdr 2e-05); moves opposite to [[ELMO3]] (-0.44, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 36 go from it, the strongest it → [[LAMC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.24×** | +15.7 | 0e+00 | 19/22 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +10.7 | 3e-24 | 18/20 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +9.2 | 9e-18 | 17/20 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.7 | 5e-04 | 10/21 (SW1417, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.5 | 1e-03 | 8/20 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.007 | 3/21 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.014 | 9/21 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.39×** | +3.6 | 0.021 | 5/21 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.024 | 9/21 (A498, A549, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.5 | 0.025 | 9/18 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.5 | 0.026 | 13/21 (HS-578T, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.030 | 3/23 (SW1417, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.044 | 0/21 | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.059 | 7/21 (A498, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -6.5 | 4e-08 | 19/21 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.628×** | -5.0 | 1e-04 | 18/21 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -5.0 | 1e-04 | 15/21 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -4.6 | 6e-04 | 14/21 (H4, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.679×** | -4.2 | 0.003 | 18/21 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 99.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 152 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.255× (z -10.5) |
| [[C32 (line)]] | wt | 303 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.5) |
| [[A-172 (line)]] | wt | 202 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -8.8) |
| [[A498 (line)]] | wt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -9.9) |
| [[HOP62 (line)]] | alt | 79.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -8.8) |
| [[HS-578T (line)]] | alt | 487 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.332× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 367 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.276× (z -8.9) |
| [[J82 (line)]] | alt | 131 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 311 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.306× (z -8.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW 1088 (line)]] | alt | 680 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.163× (z -8.7) |
| [[A-427 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTHRC1]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[COL1A2]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 | STRING 487 |
| [[ANGPTL2]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PRSS23]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 | pathway: Post-translational protein phosphorylation |
| [[ANTXR1]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[TRPA1]] | +0.57 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DOCK2]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[COL8A1]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.56 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SDC2]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 | pathway: Post-translational protein phosphorylation |
| [[ADAM12]] | +0.55 | +0.70 / +0.38 | both halves | 6e-05 | pathway: HALLMARK_MYOGENESIS |
| [[SPARC]] | +0.55 | +0.49 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MYOGENESIS; STRING 559 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMO3]] | -0.44 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 2, C 39. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IGFBP7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises IGFBP7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNG11]] | C | GNG11 activity raises IGFBP7's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 7.07× lower at baseline in the lines without GNG11 | 0.003 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[IL6]] | C | IL6 activity raises IGFBP7's level | lines that do not express IL6 (32) vs lines expressing it (18) | 7.87× lower at baseline in the lines without IL6 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises IGFBP7's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 7.64× lower at baseline in the lines without LINC01583 | 0.005 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises IGFBP7's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.70× lower at baseline in the lines without AEBP1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises IGFBP7's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 8.20× lower at baseline in the lines without COL8A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises IGFBP7's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 5.45× lower at baseline in the lines without ADAMTS9-AS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises IGFBP7's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 5.77× lower at baseline in the lines without BICC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises IGFBP7's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 7.48× lower at baseline in the lines without CTHRC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[CYGB]] | C | CYGB activity raises IGFBP7's level | lines that do not express CYGB (20) vs lines expressing it (30) | 4.19× lower at baseline in the lines without CYGB | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises IGFBP7's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 6.94× lower at baseline in the lines without TIMP3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 4, C 32. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC1]] | B | IGFBP7 activity raises LAMC1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without IGFBP7 | 0.031 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1 |
| [[TMSB4X]] | B | IGFBP7 activity raises TMSB4X's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without IGFBP7 | 0.063 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1 |
| [[LOXL3]] | B | IGFBP7 activity raises LOXL3's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without IGFBP7 | 0.066 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1 |
| [[EDIL3-DT]] | B | IGFBP7 activity strengthens EDIL3-DT's drug response | lines that do not express IGFBP7 (7) vs lines expressing it (15) | the lines without IGFBP7 respond 0.38× as strongly (z diff +1.73); strongest at Idarubicin (hydrochloride) 5 µM: 2.11x vs 7.18x (z diff +4.6) | 0.069 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; target measured in part of the lines; artifact flags |
| [[FN1]] | C | IGFBP7 activity raises FN1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 12.27× lower at baseline in the lines without IGFBP7 | 0.001 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[TGFBI]] | C | IGFBP7 activity raises TGFBI's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 7.36× lower at baseline in the lines without IGFBP7 | 0.003 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[MAF]] | C | IGFBP7 activity raises MAF's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 5.67× lower at baseline in the lines without IGFBP7 | 0.005 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[ADAMTS9-AS2]] | C | IGFBP7 activity raises ADAMTS9-AS2's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.94× lower at baseline in the lines without IGFBP7 | 0.011 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[COL8A1]] | C | IGFBP7 activity raises COL8A1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 4.91× lower at baseline in the lines without IGFBP7 | 0.019 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[AEBP1]] | C | IGFBP7 activity raises AEBP1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 2.33× lower at baseline in the lines without IGFBP7 | 0.020 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[CTHRC1]] | C | IGFBP7 activity raises CTHRC1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without IGFBP7 | 0.020 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[COL4A2]] | C | IGFBP7 activity raises COL4A2's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 5.80× lower at baseline in the lines without IGFBP7 | 0.022 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.8, 21.7); signed map (24.6, 42.9). **Vector** length 66.0, 22.1% of its response variance represented; |z| ≥ 3 in 460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +0.4 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.2 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:57,030,773-57,110,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAC25, IGFBP-7, PSF, FSTL2 |
| Gene groups (HGNC) | I-set domain containing |
| Hallmark sets | MYOGENESIS |
| Reactome | 6 pathways, smallest: Senescence-Associated Secretory Phenotype (SASP); Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16270](https://www.uniprot.org/uniprotkb/Q16270) (Insulin-like growth factor-binding protein 7):

> Binds IGF1 and IGF2 with a relatively low affinity. Stimulates prostacyclin (PGI2) production. Stimulates cell adhesion. Acts as a ligand for CD93 to play a role in angiogenesis.

**Summary**, from NCBI Gene [3490](https://www.ncbi.nlm.nih.gov/gene/3490):

> This gene encodes a member of the insulin-like growth factor (IGF)-binding protein (IGFBP) family. IGFBPs bind IGFs with high affinity, and regulate IGF availability in body fluids and tissues and modulate IGF binding to its receptors. This protein binds IGF-I and IGF-II with relatively low affinity, and belongs to a subfamily of low-affinity IGFBPs. It also stimulates prostacyclin production and cell adhesion. Alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:5476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5476) · Entrez [3490](https://www.ncbi.nlm.nih.gov/gene/3490) · UniProt [Q16270](https://www.uniprot.org/uniprotkb/Q16270) · Ensembl [ENSG00000163453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163453)

## Data

Gene col 8692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8692); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8692]; `tensor/DDL_lfc|DDL_z.npy` [8692]; `embed/gene_vectors.npy` [8692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8692 or target_col == 8692). Every well: [[IGFBP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
