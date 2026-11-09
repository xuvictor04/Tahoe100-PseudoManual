---
symbol: "RHCG"
type: "gene"
col: 6422
ensembl_id: "ENSG00000140519"
name: "Rh family C glycoprotein"
location: "15q26.1"
module: 167
arm: "+"
pooled_cpm: 11.02
n_lines_expressing: 17
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 27
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# RHCG

*Rh family C glycoprotein* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.53× (z +10.2, q 8e-22, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.06× (z +6.3, q 3e-08, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.492× (z -6.3, q 2e-07, down in 13 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.171×, NCI-H1792 0.0912×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (A549 0.0710×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.380×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCIM]] (+0.65, fdr 1e-05), [[LINC02015]] (+0.61, fdr 1e-05), [[CD38]] (+0.58, fdr 2e-05); moves opposite to [[CMTM7]] (-0.45, fdr 2e-04), [[DENND11]] (-0.44, fdr 1e-04), [[IVD]] (-0.42, fdr 9e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[C1QTNF1-AS1]] → it (grade B ⚠); 27 go from it, the strongest it → [[CEBPB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.53×** | +10.2 | 8e-22 | 2/7 (NCI-H460, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.96×** | +10.0 | 6e-21 | 4/10 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.19×** | +8.2 | 3e-14 | 1/9 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +6.3 | 3e-08 | 7/15 (NCI-H1792, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +4.9 | 7e-05 | 13/14 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.28×** | +4.9 | 7e-05 | 8/14 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.8 | 1e-04 | 5/12 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.4 | 8e-04 | 5/15 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +4.1 | 0.003 | 2/13 (NCI-H460, AsPC-1) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.6 | 0.019 | 2/10 (NCI-H460, NCI-H2030) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.052 | 3/14 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.2 | 0.059 | 0/12 | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.088 | 4/14 (HOP62, J82, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.64×** | +3.1 | 0.088 | 4/15 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6422.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.171×, NCI-H1792 0.0912×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (A549 0.0710×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.380×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.492×** | -6.3 | 2e-07 | 13/14 (NCI-H23, A549, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -3.7 | 0.073 | 10/15 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.566× | -3.3 | 0.15 | 1/14 (AsPC-1) | inconsistent across doses | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.594× | -3.3 | 0.15 | 6/14 (RPMI-7951, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.599× | -3.2 | 0.15 | 14/15 (NCI-H1792, hTERT-HPNE, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 267 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0710× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 24.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 21.1× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.380× (z -10.4) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.798 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCIM]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[LINC02015]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CD38]] | +0.58 | +0.64 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[PHLDB2]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SOD2]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SGK1]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[KYNU]] | +0.53 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[CP]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[MAFB]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[IL1R1]] | +0.50 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ACKR3]] | +0.50 | +0.50 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM7]] | -0.45 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[DENND11]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[IVD]] | -0.42 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[WNT7A]] | -0.41 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[ZFP64]] | -0.39 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QTNF1-AS1]] | B | C1QTNF1-AS1 activity raises RHCG's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without C1QTNF1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[EPAS1]] | B | EPAS1 activity raises RHCG's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without EPAS1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[CCL20]] | B | CCL20 activity raises RHCG's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without CCL20 | 0.088 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[C1QTNF1]] | B | C1QTNF1 activity raises RHCG's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without C1QTNF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[PTGES]] | B | PTGES activity raises RHCG's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without PTGES | 0.096 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[IL1R1]] | C | IL1R1 activity raises RHCG's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.71× lower at baseline in the lines without IL1R1 | 0.023 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises RHCG's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.33× lower at baseline in the lines without PAPPA | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises RHCG's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without KYNU | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |
| [[CD38]] | C | CD38 activity raises RHCG's level | lines that do not express CD38 (35) vs lines expressing it (15) | 3.64× lower at baseline in the lines without CD38 | 0.061 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent; co-absent with the target |
| [[LINC02015]] | C | LINC02015 activity raises RHCG's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without LINC02015 | 0.094 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 18, C 9. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEBPB]] | B | RHCG activity raises CEBPB's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without RHCG | 0.004 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[NFIL3]] | B | RHCG activity raises NFIL3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.85× lower at baseline in the lines without RHCG | 0.008 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[SOD2]] | B | RHCG activity raises SOD2's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without RHCG | 0.008 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[ATP2B1]] | B | RHCG activity raises ATP2B1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without RHCG | 0.009 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[ZC3H12A]] | B | RHCG activity raises ZC3H12A's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without RHCG | 0.015 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[EPAS1]] | B | RHCG activity raises EPAS1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without RHCG | 0.019 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[C1QTNF1]] | B | RHCG activity raises C1QTNF1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without RHCG | 0.020 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[OSMR]] | B | RHCG activity raises OSMR's level | lines that do not express RHCG (33) vs lines expressing it (17) | 4.37× lower at baseline in the lines without RHCG | 0.026 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[TNFAIP3]] | B | RHCG activity raises TNFAIP3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without RHCG | 0.038 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[PTGES]] | B | RHCG activity raises PTGES's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.75× lower at baseline in the lines without RHCG | 0.041 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[C11orf96]] | B | RHCG activity raises C11orf96's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.17× lower at baseline in the lines without RHCG | 0.042 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[ADPRHL1]] | B | RHCG activity raises ADPRHL1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.51× lower at baseline in the lines without RHCG | 0.056 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 21.5); signed map (50.9, 24.9). **Vector** length 53.6, 18.0% of its response variance represented; |z| ≥ 3 in 415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.4 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Rh family C glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,471,398-89,496,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RHGK, PDRC2, SLC42A3; previously C15orf6 |
| Gene groups (HGNC) | Solute carrier family 42 |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBD6](https://www.uniprot.org/uniprotkb/Q9UBD6) (Ammonium transporter Rh type C):

> Ammonium transporter involved in the maintenance of acid-base homeostasis. Transports ammonium and its related derivative methylammonium across the plasma membrane of epithelial cells likely contributing to renal transepithelial ammonia transport and ammonia metabolism. Postulated to primarily mediate an electroneutral bidirectional transport of NH3 ammonia species according to a mechanism that implies interaction of an NH4(+) ion with acidic residues of the pore entry followed by dissociation …

**Summary**, from NCBI Gene [51458](https://www.ncbi.nlm.nih.gov/gene/51458):

> Enables ankyrin binding activity; identical protein binding activity; and transmembrane transporter activity. Involved in ammonium transmembrane transport; intracellular monoatomic ion homeostasis; and transepithelial ammonium transport. Located in apical plasma membrane and basolateral plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18140) · Entrez [51458](https://www.ncbi.nlm.nih.gov/gene/51458) · UniProt [Q9UBD6](https://www.uniprot.org/uniprotkb/Q9UBD6) · Ensembl [ENSG00000140519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140519)

## Data

Gene col 6422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6422); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6422]; `tensor/DDL_lfc|DDL_z.npy` [6422]; `embed/gene_vectors.npy` [6422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6422 or target_col == 6422). Every well: [[RHCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
