---
symbol: "LOXL4"
type: "gene"
col: 6130
ensembl_id: "ENSG00000138131"
name: "lysyl oxidase like 4"
location: "10q24.2"
module: 87
arm: "+"
pooled_cpm: 5.9
n_lines_expressing: 20
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 20
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# LOXL4

*lysyl oxidase like 4* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.04× (z +11.6, q 3e-28, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.95× (z +4.1, q 0.006, up in 0 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.454× (z -6.8, q 4e-09, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEF1-AS1]] (+0.63, fdr 1e-05), [[SHROOM4]] (+0.62, fdr 2e-05), [[AGMO]] (+0.62, fdr 1e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MILR1]] → it (grade B ⚠); 20 go from it, the strongest it → [[ITGB8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +11.6 | 3e-28 | 3/9 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +10.1 | 2e-21 | 3/9 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +7.4 | 3e-11 | 2/9 (SNU-423, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.95×** | +4.1 | 0.006 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +4.0 | 0.007 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.008 | 5/16 (NCI-H1792, C32, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +3.9 | 0.008 | 0/7 | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.37×** | +3.8 | 0.008 | 1/16 (HepG2/C3A) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +3.8 | 0.008 | 1/10 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.008 | 6/15 (BT-474, HT-29, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.8 | 0.008 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.066 | 5/16 (C32, Hs 766T, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.1 | 0.074 | 1/7 (SNU-423) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -6.8 | 4e-09 | 11/16 (Hs 766T, C32, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -5.1 | 9e-05 | 9/16 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.579×** | -4.7 | 4e-04 | 8/16 (Hs 766T, C32, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.581×** | -4.7 | 4e-04 | 11/16 (Hs 766T, C32, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.642×** | -3.8 | 0.014 | 14/16 (C32, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.650×** | -3.7 | 0.017 | 10/16 (SW480, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.450×** | -3.6 | 0.024 | 7/16 (C32, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.476×** | -3.4 | 0.055 | 4/16 (C32, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.689×** | -3.2 | 0.076 | 7/16 (Panc 03.27, C32, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.703× | -3.1 | 0.13 | 2/16 (SHP-77, AsPC-1) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 108 | 0 | 27 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0470× (z -22.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -15.3) |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0214× (z -19.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0816× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0568× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 23.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0562× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0816× (z -11.0) |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0331× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.0392× (z -8.6) |
| [[SW480 (line)]] | alt | 8.91 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.151× (z -9.8) |
| [[SNU-423 (line)]] | alt | 6.72 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0936× (z -8.6) |
| [[A-172 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEF1-AS1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SHROOM4]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 | **novel candidate** |
| [[AGMO]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[FKBP9P1-1]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[TRPV4]] | +0.60 | +0.61 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[C10orf90]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[OPRD1]] | +0.56 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[RAB17]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 | **novel candidate** |
| [[NTRK2]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[NYAP2]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[DUOX2]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[SAMMSON]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | MILR1 activity raises LOXL4's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without MILR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[HDAC6]] | B | HDAC6 activity raises LOXL4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LAPTM5]] | C | LAPTM5 activity raises LOXL4's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without LAPTM5 | 0.019 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[CFI]] | C | CFI activity raises LOXL4's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without CFI | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[AGMO]] | C | AGMO activity raises LOXL4's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without AGMO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises LOXL4's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without VSNL1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |
| [[ST18]] | C | ST18 activity raises LOXL4's level | lines that do not express ST18 (39) vs lines expressing it (11) | 1.21× lower at baseline in the lines without ST18 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises LOXL4's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without CEACAM1 | 0.072 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[RHOJ]] | C | RHOJ activity raises LOXL4's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without RHOJ | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 7, C 13. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | LOXL4 activity raises ITGB8's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without LOXL4 | 0.020 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[SLC44A5]] | B | LOXL4 activity raises SLC44A5's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.96× lower at baseline in the lines without LOXL4 | 0.023 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[LINC01239]] | B | LOXL4 activity raises LINC01239's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without LOXL4 | 0.032 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[LRMDA]] | B | LOXL4 activity raises LRMDA's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without LOXL4 | 0.072 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[PYROXD2]] | B | LOXL4 activity raises PYROXD2's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without LOXL4 | 0.073 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[NELL1]] | B | LOXL4 activity raises NELL1's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without LOXL4 | 0.097 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[PKHD1]] | B | LOXL4 activity raises PKHD1's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without LOXL4 | 0.098 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[PROX1]] | C | LOXL4 activity raises PROX1's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without LOXL4 | 0.006 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[TMEM163]] | C | LOXL4 activity raises TMEM163's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.51× lower at baseline in the lines without LOXL4 | 0.009 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[AGMO]] | C | LOXL4 activity raises AGMO's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.98× lower at baseline in the lines without LOXL4 | 0.014 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[CCL28]] | C | LOXL4 activity raises CCL28's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without LOXL4 | 0.021 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[PI15]] | C | LOXL4 activity raises PI15's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without LOXL4 | 0.024 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.9, 30.1); signed map (28.7, 37.5). **Vector** length 60.9, 18.0% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.4 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.3 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | lysyl oxidase like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:98,247,690-98,268,194 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21889, LOXC |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Lysyl oxidase family |
| Reactome | 5 pathways, smallest: Crosslinking of collagen fibrils; Elastic fibre formation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JB6](https://www.uniprot.org/uniprotkb/Q96JB6) (Lysyl oxidase homolog 4):

> Catalyzes the oxidative deamination of lysine and hydroxylysine residues in collagen and elastin, resulting in the formation of covalent cross-linkages, and the stabilization of collagen and elastin fibers.

**Summary**, from NCBI Gene [84171](https://www.ncbi.nlm.nih.gov/gene/84171):

> This gene encodes a member of the lysyl oxidase gene family. The prototypic member of the family is essential to the biogenesis of connective tissue, encoding an extracellular copper-dependent amine oxidase that catalyses the first step in the formation of crosslinks in collagens and elastin. A highly conserved amino acid sequence at the C-terminus end appears to be sufficient for amine oxidase activity, suggesting that each family member may retain this function. The N-terminus is poorly …

**Accessions** — [HGNC:17171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17171) · Entrez [84171](https://www.ncbi.nlm.nih.gov/gene/84171) · UniProt [Q96JB6](https://www.uniprot.org/uniprotkb/Q96JB6) · Ensembl [ENSG00000138131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138131)

## Data

Gene col 6130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6130); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6130]; `tensor/DDL_lfc|DDL_z.npy` [6130]; `embed/gene_vectors.npy` [6130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6130 or target_col == 6130). Every well: [[LOXL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LOXL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
