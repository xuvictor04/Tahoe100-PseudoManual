---
symbol: "KIRREL3"
type: "gene"
col: 7390
ensembl_id: "ENSG00000149571"
name: "kirre like nephrin family adhesion molecule 3"
location: "11q24.2"
module: 13
arm: "+"
pooled_cpm: 36.13
n_lines_expressing: 14
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 26
direction_downstream: 37
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# KIRREL3

*kirre like nephrin family adhesion molecule 3* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +12.9, q 3e-35, up in 1 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +12.6, q 1e-33, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.658× (z -4.9, q 4e-04, down in 8 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEGFC]] (+0.69, fdr 7e-06), [[ADAMTS16]] (+0.67, fdr 7e-06), [[LINC01411]] (+0.65, fdr 7e-06); moves opposite to [[ACSL1]] (-0.48, fdr 2e-05), [[KCNB1]] (-0.44, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 37 go from it, the strongest it → [[TPM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.9 | 3e-35 | 1/11 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +12.6 | 1e-33 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +12.1 | 1e-31 | 2/11 (RPMI-7951, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +10.3 | 1e-22 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.6 | 3e-09 | 1/12 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 4e-05 | 2/12 (RPMI-7951, NCI-H23) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.7 | 3e-04 | 2/12 (H4, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.46×** | +4.4 | 7e-04 | 0/12 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +4.3 | 0.001 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.64×** | +4.1 | 0.002 | 5/12 (A-172, H4, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.88×** | +3.9 | 0.006 | 5/12 (A-172, HS-578T, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.008 | 6/12 (H4, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.009 | 0/12 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Acetohexamide (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.015 | 2/12 (HOP62, RPMI-7951) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.658×** | -4.9 | 4e-04 | 8/12 (A498, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.658×** | -4.6 | 0.001 | 9/12 (A498, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.790×** | -3.9 | 0.012 | 8/12 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.720×** | -3.9 | 0.012 | 8/12 (A498, A549, …) | inconsistent across doses | position effect removed |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.706×** | -3.9 | 0.012 | 1/12 (NCI-H23) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.013 | 6/12 (A-172, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.030 | 6/12 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.812×** | -3.5 | 0.030 | 6/12 (SNU-423, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.746×** | -3.5 | 0.030 | 10/12 (A498, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.746×** | -3.5 | 0.030 | 8/12 (A498, A549, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.040 | 6/12 (HOP62, H4, …) | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.755×** | -3.3 | 0.041 | 7/12 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.762×** | -3.2 | 0.056 | 7/12 (A498, HS-578T, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.067 | 9/12 (A498, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.767×** | -3.0 | 0.096 | 7/12 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.760×** | -3.0 | 0.096 | 0/12 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 179 | 0 | 14 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -14.7) |
| [[A549 (line)]] | wt | 462 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -20.5) |
| [[HS-578T (line)]] | alt | 141 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -13.0) |
| [[SNU-423 (line)]] | alt | 165 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.218× (z -11.3) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -10.4) |
| [[A-172 (line)]] | wt | 57.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -11.2) |
| [[HOP62 (line)]] | alt | 99.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.4) |
| [[PANC-1 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEGFC]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS16]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[VSTM4]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[P3H2]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SLC8A1]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[INSYN2B]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[KCNMA1]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS6]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SIRLNT]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[AFF3]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[C12orf75-AS1]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | -0.48 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KCNB1]] | -0.44 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 1, C 25. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers KIRREL3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[ITIH5]] | C | ITIH5 activity raises KIRREL3's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 5.89× lower at baseline in the lines without ITIH5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises KIRREL3's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 5.54× lower at baseline in the lines without ADAMTS12 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises KIRREL3's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.13× lower at baseline in the lines without FRMD4A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises KIRREL3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 4.64× lower at baseline in the lines without SPOCK1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[MEG3]] | C | MEG3 activity raises KIRREL3's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 3.92× lower at baseline in the lines without MEG3 | 0.017 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises KIRREL3's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without INSYN2B | 0.024 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[STAC]] | C | STAC activity raises KIRREL3's level | lines that do not express STAC (25) vs lines expressing it (25) | 4.47× lower at baseline in the lines without STAC | 0.025 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises KIRREL3's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 4.35× lower at baseline in the lines without SLC8A1 | 0.028 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[LINC00842]] | C | LINC00842 activity raises KIRREL3's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 3.32× lower at baseline in the lines without LINC00842 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises KIRREL3's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 5.50× lower at baseline in the lines without SIRLNT | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[ADAMTS10]] | C | ADAMTS10 activity raises KIRREL3's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 4.43× lower at baseline in the lines without ADAMTS10 | 0.038 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 13, C 24. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPM1]] | B | KIRREL3 activity raises TPM1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 2.76× lower at baseline in the lines without KIRREL3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[EML1]] | B | KIRREL3 activity raises EML1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without KIRREL3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[EVC]] | B | KIRREL3 activity raises EVC's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without KIRREL3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[ATP13A3]] | B | KIRREL3 activity raises ATP13A3's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 1.74× lower at baseline in the lines without KIRREL3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[LRIG1]] | B | KIRREL3 activity raises LRIG1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 1.83× lower at baseline in the lines without KIRREL3 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[TPM1]] | B | KIRREL3 activity strengthens TPM1's drug response | lines that do not express KIRREL3 (33) vs lines expressing it (13) | the lines without KIRREL3 respond 0.72× as strongly (z diff +1.67); strongest at Ixazomib citrate 5 µM: 0.63x vs 0.37x (z diff +4.0) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; target measured in part of the lines; artifact flags |
| cells under [[Bendamustine (drug)]] 0.5 µM | B | KIRREL3 activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express KIRREL3 (36) vs lines expressing it (12) | the lines without KIRREL3: 1.32× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[DSE]] | B | KIRREL3 activity raises DSE's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 2.61× lower at baseline in the lines without KIRREL3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| cells under [[Fumaric acid (drug)]] 5 µM | B | KIRREL3 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express KIRREL3 (36) vs lines expressing it (12) | the lines without KIRREL3: 0.81× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[CD44]] | B | KIRREL3 activity raises CD44's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without KIRREL3 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | B | KIRREL3 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express KIRREL3 (36) vs lines expressing it (12) | the lines without KIRREL3: 1.42× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[ARL4C]] | B | KIRREL3 activity strengthens ARL4C's drug response | lines that do not express KIRREL3 (24) vs lines expressing it (11) | the lines without KIRREL3 respond 0.61× as strongly (z diff +1.95); strongest at Homoharringtonine 5 µM: 0.72x vs 0.51x (z diff +3.3) | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 16.7); signed map (22.6, 49.3). **Vector** length 72.3, 30.9% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +12.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +4.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.3 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | kirre like nephrin family adhesion molecule 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,423,358-127,003,460 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NEPH2, KIAA1867, KIRRE |
| Gene groups (HGNC) | C2-set domain containing; I-set domain containing; MicroRNA protein coding host genes; Kirre like nephrin family adhesion molecules |
| Reactome | 2 pathways, smallest: Nephrin family interactions; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZU9](https://www.uniprot.org/uniprotkb/Q8IZU9) (Kin of IRRE-like protein 3):

> Synaptic adhesion molecule required for the formation of target-specific synapses. Required for formation of target-specific synapses at hippocampal mossy fiber synapses. Required for formation of mossy fiber filopodia, the synaptic structures connecting dentate granule and GABA neurons. Probably acts as a homophilic adhesion molecule that promotes trans-cellular interactions and stabilize mossy fiber filipodia contact and subsequent synapse formation. Required for the coalescence of …

**Summary**, from NCBI Gene [84623](https://www.ncbi.nlm.nih.gov/gene/84623):

> The protein encoded by this gene is a member of the nephrin-like protein family. These proteins are expressed in fetal and adult brain, and also in podocytes of kidney glomeruli. The cytoplasmic domains of these proteins interact with the C-terminus of podocin, also expressed in the podocytes, cells involved in ensuring size- and charge-selective ultrafiltration. The protein encoded by this gene is a synaptic cell adhesion molecule with multiple extracellular immunoglobulin-like domains and a …

**Accessions** — [HGNC:23204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23204) · Entrez [84623](https://www.ncbi.nlm.nih.gov/gene/84623) · UniProt [Q8IZU9](https://www.uniprot.org/uniprotkb/Q8IZU9) · Ensembl [ENSG00000149571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149571)

## Data

Gene col 7390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7390); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7390]; `tensor/DDL_lfc|DDL_z.npy` [7390]; `embed/gene_vectors.npy` [7390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7390 or target_col == 7390). Every well: [[KIRREL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIRREL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
