---
symbol: "STRA6"
type: "gene"
col: 6086
ensembl_id: "ENSG00000137868"
name: "signaling receptor and transporter of retinol STRA6"
location: "15q24.1"
module: 13
arm: "+"
pooled_cpm: 12.03
n_lines_expressing: 24
n_dd_up: 7
n_dd_down: 39
n_dd_up_clean: 6
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 18
direction_downstream: 11
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# STRA6

*signaling receptor and transporter of retinol STRA6* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 5 µM: 1.78× (z +7.4, q 7e-11, up in 16 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.399× (z -8.2, q 1e-13, down in 20 of 21 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC33]] (+0.78, fdr 7e-06, ⚠ same locus), [[ADAMTS14]] (+0.61, fdr 1e-05), [[MILR1]] (+0.56, fdr 3e-05), [[SYNDIG1]] (+0.54, fdr 3e-05); moves opposite to [[SLC49A4]] (-0.42, fdr 7e-05), [[VSIG10]] (-0.41, fdr 1e-04), [[BEND7]] (-0.40, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[GPR173]] → it (grade B ⚠); 11 go from it, the strongest it → [[THEMIS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **1.78×** | +7.4 | 7e-11 | 16/21 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +6.8 | 2e-09 | 0/13 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +6.5 | 1e-08 | 7/21 (HEC-1-A, BT-474, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.92×** | +5.9 | 5e-07 | 13/20 (A549, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 0.001 | 10/20 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.008 | 9/21 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.038 | 6/20 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.43× | +3.1 | 0.13 | 11/20 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 2 with an alert ⚠; shown: the 15 strongest. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.399×** | -8.2 | 1e-13 | 20/21 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.423×** | -7.7 | 4e-12 | 18/20 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.435×** | -7.4 | 2e-11 | 19/20 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.569×** | -7.1 | 2e-10 | 17/21 (CFPAC-1, CHP-212, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.484×** | -6.5 | 1e-08 | 17/20 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -6.1 | 8e-08 | 16/21 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -5.7 | 1e-06 | 19/20 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.538×** | -5.5 | 2e-06 | 16/20 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.547×** | -5.4 | 5e-06 | 12/20 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.664×** | -5.2 | 1e-05 | 14/21 (H4, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.591×** | -4.7 | 1e-04 | 10/20 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -4.4 | 4e-04 | 15/20 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -4.4 | 5e-04 | 12/20 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.625×** | -4.2 | 0.001 | 11/20 (A-172, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.411×** | -4.2 | 0.001 | 14/21 (HOP62, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 53.9 | 0 | 20 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0469× (z -16.3) |
| [[SW480 (line)]] | alt | 54.5 | 0 | 14 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -21.2) |
| [[A-172 (line)]] | wt | 36.1 | 0 | 11 | — | [[Panobinostat (drug)]] 0.5 µM 0.0340× (z -14.0) |
| [[HOP62 (line)]] | alt | 45.1 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 76.9 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0662× (z -24.7) |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -14.5) |
| [[A549 (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0929× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 8.16 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.131× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0928× (z -19.7) |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.112× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.6) |
| [[A-427 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC33]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ADAMTS14]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MILR1]] | +0.56 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[SYNDIG1]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TMEM163]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ARMCX2]] | +0.54 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[KCNK3]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[PDGFB]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SARDH]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[LINC02813]] | +0.53 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[PDLIM4]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TREM1]] | +0.52 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[ADGRE2]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC49A4]] | -0.42 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[VSIG10]] | -0.41 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[BEND7]] | -0.40 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[ARHGEF28]] | -0.40 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR173]] | B | GPR173 activity strengthens STRA6's drug response | lines that do not express GPR173 (9) vs lines expressing it (13) | the lines without GPR173 respond 0.64× as strongly (z diff +1.35); strongest at Homoharringtonine 5 µM: 0.76x vs 0.29x (z diff +4.9) | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; target measured in part of the lines; artifact flags |
| [[PDGFB]] | B | PDGFB activity raises STRA6's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without PDGFB | 0.039 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[MILR1]] | B | MILR1 activity raises STRA6's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without MILR1 | 0.045 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[TNS1]] | B | TNS1 activity raises STRA6's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without TNS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[LMO2]] | B | LMO2 activity raises STRA6's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without LMO2 | 0.074 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[CCDC33]] | C | CCDC33 activity raises STRA6's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 4.94× lower at baseline in the lines without CCDC33 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8; co-absent with the target |
| [[EVA1A-AS]] | C | EVA1A-AS activity raises STRA6's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 3.08× lower at baseline in the lines without EVA1A-AS | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises STRA6's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.58× lower at baseline in the lines without GPR173 | 0.016 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises STRA6's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.33× lower at baseline in the lines without RFX8 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises STRA6's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without COL7A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises STRA6's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without NAV1 | 0.038 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[CA12]] | C | CA12 activity raises STRA6's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without CA12 | 0.048 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THEMIS2]] | B | STRA6 activity raises THEMIS2's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 2.28× lower at baseline in the lines without STRA6 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |
| [[PORCN]] | B | STRA6 activity raises PORCN's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without STRA6 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |
| [[IQSEC1]] | B | STRA6 activity raises IQSEC1's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without STRA6 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |
| [[MANCR]] | B | STRA6 activity raises MANCR's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without STRA6 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |
| [[CCDC33]] | C | STRA6 activity raises CCDC33's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 3.63× lower at baseline in the lines without STRA6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[ADGRE2]] | C | STRA6 activity raises ADGRE2's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 3.00× lower at baseline in the lines without STRA6 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[PWWP3B]] | C | STRA6 activity raises PWWP3B's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without STRA6 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[TMEM163]] | C | STRA6 activity raises TMEM163's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without STRA6 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[EVA1A-AS]] | C | STRA6 activity raises EVA1A-AS's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without STRA6 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[LAPTM5]] | C | STRA6 activity raises LAPTM5's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without STRA6 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[SYNDIG1]] | C | STRA6 activity raises SYNDIG1's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without STRA6 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.9, 16.4); signed map (24.2, 48.0). **Vector** length 70.2, 19.7% of its response variance represented; |z| ≥ 3 in 698 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.8 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.3 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | signaling receptor and transporter of retinol STRA6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,179,466-74,212,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC69A1, FLJ12541 |
| Gene groups (HGNC) | Solute carrier family 69 |
| Reactome | 6 pathways, smallest: Diseases associated with visual transduction; Diseases of the neuronal system; Retinoid cycle disease events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX79](https://www.uniprot.org/uniprotkb/Q9BX79) (Receptor for retinol uptake STRA6):

> Functions as a retinol transporter. Accepts all-trans retinol from the extracellular retinol-binding protein RBP4, facilitates retinol transport across the cell membrane, and then transfers retinol to the cytoplasmic retinol-binding protein RBP1. Retinol uptake is enhanced by LRAT, an enzyme that converts retinol to all-trans retinyl esters, the storage forms of vitamin A. Contributes to the activation of a signaling cascade that depends on retinol transport and LRAT-dependent generation of …

**Summary**, from NCBI Gene [64220](https://www.ncbi.nlm.nih.gov/gene/64220):

> The protein encoded by this gene is a membrane protein involved in the metabolism of retinol. The encoded protein acts as a receptor for retinol/retinol binding protein complexes. This protein removes the retinol from the complex and transports it across the cell membrane. Defects in this gene are a cause of syndromic microphthalmia type 9 (MCOPS9). Several transcript variants encoding a few different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:30650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30650) · Entrez [64220](https://www.ncbi.nlm.nih.gov/gene/64220) · UniProt [Q9BX79](https://www.uniprot.org/uniprotkb/Q9BX79) · Ensembl [ENSG00000137868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137868)

## Data

Gene col 6086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6086); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6086]; `tensor/DDL_lfc|DDL_z.npy` [6086]; `embed/gene_vectors.npy` [6086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6086 or target_col == 6086). Every well: [[STRA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
