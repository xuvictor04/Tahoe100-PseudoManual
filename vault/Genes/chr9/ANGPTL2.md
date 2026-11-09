---
symbol: "ANGPTL2"
type: "gene"
col: 5920
ensembl_id: "ENSG00000136859"
name: "angiopoietin like 2"
location: "9q33.3"
module: 13
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 21
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 14
direction_downstream: 34
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ANGPTL2

*angiopoietin like 2* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.44× (z +9.8, q 1e-19, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.63× (z +4.0, q 0.007, up in 2 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -6.8, q 5e-09, down in 13 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA11]] (+0.67, fdr 7e-06), [[COL15A1]] (+0.66, fdr 1e-05), [[CTHRC1]] (+0.66, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[STING1]] → it (grade B ⚠); 34 go from it, the strongest it → [[PECAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +9.8 | 1e-19 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +9.2 | 9e-18 | 2/10 (SHP-77, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +8.3 | 3e-14 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.12×** | +4.4 | 0.002 | 1/8 (SHP-77) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.007 | 2/16 (H4, HepG2/C3A) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.015 | 1/15 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.015 | 4/17 (HOP62, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.028 | 2/13 (SW480, A-172) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.028 | 2/12 (hTERT-HPNE, Hs 766T) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +3.4 | 0.036 | 0/2 | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.3 | 0.046 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.2 | 0.060 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.080 | 0/14 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.1 | 0.080 | 0/3 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -6.8 | 5e-09 | 13/18 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.588×** | -4.4 | 0.003 | 8/15 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.621×** | -3.9 | 0.014 | 6/18 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.617×** | -3.8 | 0.014 | 3/15 (RPMI-7951, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -3.8 | 0.014 | 12/16 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.642×** | -3.7 | 0.024 | 7/17 (RPMI-7951, hTERT-HPNE, …) | two highest doses |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.648×** | -3.6 | 0.025 | 4/17 (RPMI-7951, HepG2/C3A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -3.6 | 0.025 | 7/17 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -3.5 | 0.033 | 10/15 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.747×** | -3.4 | 0.038 | 4/16 (SW 900, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.678×** | -3.2 | 0.070 | 5/14 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 0.5 µM |  | **0.686×** | -3.1 | 0.090 | 3/17 (SW480, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 68.5 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0325× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -9.4) |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.124× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 4.76 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0498× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0861× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0483× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA11]] | +0.67 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[COL15A1]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[CTHRC1]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[BAALC]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[MANCR]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[FRMPD4]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GPR68]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[EVA1A]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LINC02813]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SAMD3]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STING1]] | B | STING1 activity raises ANGPTL2's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without STING1 | 0.075 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[EVA1A]] | B | EVA1A activity raises ANGPTL2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without EVA1A | 0.099 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[CARMN]] | C | CARMN activity raises ANGPTL2's level | lines that do not express CARMN (40) vs lines expressing it (10) | 4.36× lower at baseline in the lines without CARMN | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[TNS1]] | C | TNS1 activity raises ANGPTL2's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.46× lower at baseline in the lines without TNS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises ANGPTL2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without ITGA11 | 0.026 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises ANGPTL2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without HTR1F | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises ANGPTL2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.30× lower at baseline in the lines without RFX8 | 0.027 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[MANCR]] | C | MANCR activity raises ANGPTL2's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without MANCR | 0.032 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises ANGPTL2's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.27× lower at baseline in the lines without TIMP3 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[SLC24A3]] | C | SLC24A3 activity raises ANGPTL2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without SLC24A3 | 0.048 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises ANGPTL2's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.98× lower at baseline in the lines without GDNF | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[IL33]] | C | IL33 activity raises ANGPTL2's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without IL33 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 6, C 28. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PECAM1]] | B | ANGPTL2 activity raises PECAM1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.01× lower at baseline in the lines without ANGPTL2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[SHC3]] | B | ANGPTL2 activity raises SHC3's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without ANGPTL2 | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[NMNAT2]] | B | ANGPTL2 activity weakens NMNAT2's drug response | lines that do not express ANGPTL2 (17) vs lines expressing it (12) | the lines without ANGPTL2 respond 2.71× as strongly (z diff -2.34); strongest at Idarubicin (hydrochloride) 5 µM: 1.41x vs 0.63x (z diff -4.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SETBP1]] | B | ANGPTL2 activity raises SETBP1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 3.13× lower at baseline in the lines without ANGPTL2 | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[DOCK2]] | B | ANGPTL2 activity raises DOCK2's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without ANGPTL2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[LRIG1]] | B | ANGPTL2 activity raises LRIG1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without ANGPTL2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[CDH13]] | C | ANGPTL2 activity raises CDH13's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 5.86× lower at baseline in the lines without ANGPTL2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[PAK3]] | C | ANGPTL2 activity raises PAK3's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 3.43× lower at baseline in the lines without ANGPTL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[SHISAL1]] | C | ANGPTL2 activity raises SHISAL1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without ANGPTL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[SLC16A6]] | C | ANGPTL2 activity raises SLC16A6's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.91× lower at baseline in the lines without ANGPTL2 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[ITGA11]] | C | ANGPTL2 activity raises ITGA11's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 4.12× lower at baseline in the lines without ANGPTL2 | 0.017 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[TENM4]] | C | ANGPTL2 activity raises TENM4's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without ANGPTL2 | 0.017 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.5, 16.5); signed map (22.4, 46.0). **Vector** length 52.7, 14.1% of its response variance represented; |z| ≥ 3 in 573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | angiopoietin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:127,087,348-127,122,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARP2, HARP |
| Gene groups (HGNC) | Fibrinogen C domain containing; Angiopoietin like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKU9](https://www.uniprot.org/uniprotkb/Q9UKU9) (Angiopoietin-related protein 2):

> Induces sprouting in endothelial cells through an autocrine and paracrine action.

**Summary**, from NCBI Gene [23452](https://www.ncbi.nlm.nih.gov/gene/23452):

> Angiopoietins are members of the vascular endothelial growth factor family and the only known growth factors largely specific for vascular endothelium. Angiopoietin-1, angiopoietin-2, and angiopoietin-4 participate in the formation of blood vessels. ANGPTL2 protein is a secreted glycoprotein with homology to the angiopoietins and may exert a function on endothelial cells through autocrine or paracrine action. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:490) · Entrez [23452](https://www.ncbi.nlm.nih.gov/gene/23452) · UniProt [Q9UKU9](https://www.uniprot.org/uniprotkb/Q9UKU9) · Ensembl [ENSG00000136859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136859)

## Data

Gene col 5920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5920); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5920]; `tensor/DDL_lfc|DDL_z.npy` [5920]; `embed/gene_vectors.npy` [5920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5920 or target_col == 5920). Every well: [[ANGPTL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANGPTL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
