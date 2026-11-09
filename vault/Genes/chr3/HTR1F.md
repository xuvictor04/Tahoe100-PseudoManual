---
symbol: "HTR1F"
type: "gene"
col: 10998
ensembl_id: "ENSG00000179097"
name: "5-hydroxytryptamine receptor 1F"
location: "3p12"
module: 13
arm: "+"
pooled_cpm: 5.2
n_lines_expressing: 16
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 21
direction_downstream: 44
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# HTR1F

*5-hydroxytryptamine receptor 1F* — 3p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.98× (z +14.6, q 3e-45, up in 3 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.0955×, HOP62 0.101×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0805×, NCI-H1792 0.133×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0854×; ⚠ cell-cycle shift, explains ~37% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.281×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1L]] (+0.69, fdr 7e-06), [[SLC14A2]] (+0.60, fdr 1e-05), [[SYNDIG1]] (+0.60, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 44 go from it, the strongest it → [[LDB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +14.6 | 3e-45 | 3/9 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +10.5 | 2e-23 | 2/7 (J82, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +8.2 | 6e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +6.8 | 2e-09 | 5/12 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +6.7 | 2e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.37×** | +6.4 | 1e-08 | 3/11 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 8e-04 | 5/11 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.0 | 0.004 | 1/8 (RPMI-7951) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.78×** | +4.0 | 0.004 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.007 | 0/12 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.3 | 0.047 | 0/6 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.050 | 0/8 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.083 | 0/10 | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.090 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.76×** | +3.0 | 0.098 | 0/11 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.0955×, HOP62 0.101×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0805×, NCI-H1792 0.133×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0854×; ⚠ cell-cycle shift, explains ~37% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.0 | 0.77 | 2/12 (HOP62, SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 74.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0805× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 76.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -15.9) |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -10.8) |
| [[A-172 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.831 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1L]] | +0.69 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLC14A2]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TENM4]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[CCDC190]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[APCDD1L-DT]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[COL5A1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[PDGFRB]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[EDNRA]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 | pathway: Class A/1 (Rhodopsin-like receptors) |
| [[ABCA13]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 1, C 20. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HTR1F's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TIMP3]] | C | TIMP3 activity raises HTR1F's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.10× lower at baseline in the lines without TIMP3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises HTR1F's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without LINC01411 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises HTR1F's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without COL5A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[APCDD1L-DT]] | C | APCDD1L-DT activity raises HTR1F's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without APCDD1L-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises HTR1F's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without HTRA3 | 0.027 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises HTR1F's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without APCDD1L | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises HTR1F's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without ITGA4 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[ANGPTL2]] | C | ANGPTL2 activity raises HTR1F's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.18× lower at baseline in the lines without ANGPTL2 | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises HTR1F's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.48× lower at baseline in the lines without CSPG4 | 0.031 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises HTR1F's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without PTGFR | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises HTR1F's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without BAALC | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 10, C 34. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDB2]] | B | HTR1F activity raises LDB2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.72× lower at baseline in the lines without HTR1F | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[LINC01500]] | B | HTR1F activity raises LINC01500's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.07× lower at baseline in the lines without HTR1F | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[CFAP20DC-DT]] | B | HTR1F activity raises CFAP20DC-DT's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without HTR1F | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[LTBP1]] | B | HTR1F activity raises LTBP1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without HTR1F | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[SETBP1]] | B | HTR1F activity raises SETBP1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 4.84× lower at baseline in the lines without HTR1F | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[LINC01119]] | B | HTR1F activity raises LINC01119's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 1.84× lower at baseline in the lines without HTR1F | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[SLC14A2]] | B | HTR1F activity raises SLC14A2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without HTR1F | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[FBLN7]] | B | HTR1F activity raises FBLN7's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without HTR1F | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| cells under [[Pitavastatin (Calcium) (drug)]] 5 µM | B | HTR1F activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express HTR1F (34) vs lines expressing it (14) | the lines without HTR1F: 1.26× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[DAB2]] | B | HTR1F activity raises DAB2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.48× lower at baseline in the lines without HTR1F | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[TIMP3]] | C | HTR1F activity raises TIMP3's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 14.51× lower at baseline in the lines without HTR1F | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[SEMA5A]] | C | HTR1F activity raises SEMA5A's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 7.18× lower at baseline in the lines without HTR1F | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.6, 17.4); signed map (25.4, 45.0). **Vector** length 36.2, 10.6% of its response variance represented; |z| ≥ 3 in 298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.7 | +0.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | 5-hydroxytryptamine receptor 1F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p12 — chr3:87,792,706-87,993,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HTR1EL, 5-HT1F |
| Gene groups (HGNC) | 5-hydroxytryptamine receptors, G protein-coupled |
| Reactome | 7 pathways, smallest: Serotonin receptors; Amine ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P30939](https://www.uniprot.org/uniprotkb/P30939) (5-hydroxytryptamine receptor 1F):

> G protein-coupled receptor for 5-hydroxytryptamine (serotonin). Also functions as a receptor for various alkaloids and psychoactive substances. Receptor for lasmiditan, a drug for the treatment of acute migraine. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. HTR1F is coupled to G(i)/G(o) G alpha proteins and mediates inhibitory …

**Summary**, from NCBI Gene [3355](https://www.ncbi.nlm.nih.gov/gene/3355):

> Enables Gi/o-coupled serotonin receptor activity and serotonin binding activity. Involved in adenylate cyclase-inhibiting serotonin receptor signaling pathway. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5292) · Entrez [3355](https://www.ncbi.nlm.nih.gov/gene/3355) · UniProt [P30939](https://www.uniprot.org/uniprotkb/P30939) · Ensembl [ENSG00000179097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179097)

## Data

Gene col 10998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10998); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10998]; `tensor/DDL_lfc|DDL_z.npy` [10998]; `embed/gene_vectors.npy` [10998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10998 or target_col == 10998). Every well: [[HTR1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTR1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
