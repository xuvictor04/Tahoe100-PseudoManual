---
symbol: "KRT23"
type: "gene"
col: 2927
ensembl_id: "ENSG00000108244"
name: "keratin 23"
location: "17q21.2"
module: 8
arm: "+"
pooled_cpm: 11.63
n_lines_expressing: 10
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 67
direction_downstream: 91
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# KRT23

*keratin 23* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.03× (z +11.6, q 1e-28, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.74× (z +5.7, q 2e-06, up in 5 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.678× (z -3.9, q 0.041, down in 1 of 8 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACSTD2]] (+0.72, fdr 7e-06), [[MPZL2]] (+0.72, fdr 7e-06), [[CCR3]] (+0.68, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 91 go from it, the strongest it → [[BCL2L15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.03×** | +11.6 | 1e-28 | 3/7 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.56×** | +10.5 | 2e-23 | 2/4 (SW480, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +7.4 | 2e-11 | 2/4 (SW480, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +5.7 | 2e-06 | 5/8 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.74×** | +4.0 | 0.007 | 4/8 (COLO 205, SW1417, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.6 | 0.027 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.033 | 3/8 (SW1417, HepG2/C3A, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.033 | 0/8 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.5 | 0.033 | 1/7 (SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.041 | 5/8 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.05×** | +3.2 | 0.084 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | **0.678×** | -3.9 | 0.041 | 1/8 (CFPAC-1) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -3.8 | 0.041 | 6/8 (COLO 205, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -3.7 | 0.043 | 6/8 (HepG2/C3A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -3.5 | 0.063 | 5/8 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.636× | -3.2 | 0.14 | 2/8 (HepG2/C3A, COLO 205) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.631× | -3.0 | 0.19 | 2/8 (BT-474, HepG2/C3A) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.653× | -3.0 | 0.19 | 0/8 | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 204 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0354× (z -22.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0586× (z -13.2) |
| [[SW480 (line)]] | alt | 62.8 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 68.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -9.8) |
| [[COLO 205 (line)]] | alt | 78.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0380× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0382× (z -11.8) |
| [[A-172 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.893 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACSTD2]] | +0.72 | +0.58 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MPZL2]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CCR3]] | +0.68 | +0.65 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[TMEM45B]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[FGD5]] | +0.65 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[SLC6A14]] | +0.63 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[IL1RN]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ITGB6]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[HPGD]] | +0.58 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[SPTSSB]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[FLRT3]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 2, C 65. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KRT23's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAPGEF5]] | B | RAPGEF5 activity raises KRT23's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.19× lower at baseline in the lines without RAPGEF5 | 0.089 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[WFDC2]] | C | WFDC2 activity raises KRT23's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 4.58× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises KRT23's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 6.64× lower at baseline in the lines without PROM1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises KRT23's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 6.57× lower at baseline in the lines without GJB1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises KRT23's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.06× lower at baseline in the lines without ARHGEF38 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises KRT23's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 3.07× lower at baseline in the lines without TSHZ2 | 0.005 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises KRT23's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 3.75× lower at baseline in the lines without DSCAML1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises KRT23's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 5.29× lower at baseline in the lines without ITIH2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[S100A9]] | C | S100A9 activity raises KRT23's level | lines that do not express S100A9 (42) vs lines expressing it (8) | 3.58× lower at baseline in the lines without S100A9 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, GSDMC, KRT20; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises KRT23's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 2.46× lower at baseline in the lines without HLA-DRB1 | 0.007 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |
| [[C3]] | C | C3 activity raises KRT23's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.51× lower at baseline in the lines without C3 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |

### Downstream of this gene

*91 arrows, 91 of them with an alert ⚠; grade A 0, B 17, C 74. Shown: the 12 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L15]] | B | KRT23 activity raises BCL2L15's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.36× lower at baseline in the lines without KRT23 | 0.002 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[FHDC1]] | B | KRT23 activity raises FHDC1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without KRT23 | 0.003 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[STS]] | B | KRT23 activity raises STS's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.73× lower at baseline in the lines without KRT23 | 0.005 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[MUC20]] | B | KRT23 activity raises MUC20's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 4.20× lower at baseline in the lines without KRT23 | 0.006 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[FAM83E]] | B | KRT23 activity raises FAM83E's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.95× lower at baseline in the lines without KRT23 | 0.007 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[CHST15]] | B | KRT23 activity raises CHST15's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.77× lower at baseline in the lines without KRT23 | 0.011 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[LGALS9]] | B | KRT23 activity raises LGALS9's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.56× lower at baseline in the lines without KRT23 | 0.014 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[ELF3-AS1]] | B | KRT23 activity raises ELF3-AS1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.76× lower at baseline in the lines without KRT23 | 0.019 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[TMEM51-AS1]] | B | KRT23 activity raises TMEM51-AS1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.64× lower at baseline in the lines without KRT23 | 0.029 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[PPL]] | B | KRT23 activity raises PPL's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 4.33× lower at baseline in the lines without KRT23 | 0.032 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[PDE11A]] | B | KRT23 activity raises PDE11A's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without KRT23 | 0.033 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[LINC01348]] | B | KRT23 activity raises LINC01348's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.50× lower at baseline in the lines without KRT23 | 0.035 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 56.8); signed map (60.0, 8.3). **Vector** length 48.3, 22.9% of its response variance represented; |z| ≥ 3 in 250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.9 | +4.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +0.9 | +0.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | keratin 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,922,700-40,937,646 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K23, DKFZP434G032, HAIK1, CK23, MGC26158 |
| Gene groups (HGNC) | Keratins, type I |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

UniProt [Q9C075](https://www.uniprot.org/uniprotkb/Q9C075) carries no function annotation.

**Summary**, from NCBI Gene [25984](https://www.ncbi.nlm.nih.gov/gene/25984):

> The protein encoded by this gene is a member of the keratin family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. The type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. The type I cytokeratin genes are clustered in a region of chromosome 17q12-q21. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:6438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6438) · Entrez [25984](https://www.ncbi.nlm.nih.gov/gene/25984) · UniProt [Q9C075](https://www.uniprot.org/uniprotkb/Q9C075) · Ensembl [ENSG00000108244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108244)

## Data

Gene col 2927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2927); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2927]; `tensor/DDL_lfc|DDL_z.npy` [2927]; `embed/gene_vectors.npy` [2927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2927 or target_col == 2927). Every well: [[KRT23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
