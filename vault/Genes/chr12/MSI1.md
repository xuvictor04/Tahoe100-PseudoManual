---
symbol: "MSI1"
type: "gene"
col: 5652
ensembl_id: "ENSG00000135097"
name: "musashi RNA binding protein 1"
location: "12q24.31"
module: 102
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 24
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 46
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# MSI1

*musashi RNA binding protein 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.39× (z +12.6, q 2e-33, up in 0 of 0 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +8.5, q 3e-15, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.642× (z -3.9, q 0.024, down in 13 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBPMS2]] (+0.67, fdr 1e-05), [[SMO]] (+0.66, fdr 1e-05), [[TBKBP1]] (+0.66, fdr 1e-05); moves opposite to [[KIAA0319L]] (-0.47, fdr 1e-04), [[PKN2]] (-0.46, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RASGEF1C]] → it (grade B ⚠); 46 go from it, the strongest it → [[RASGEF1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +12.6 | 2e-33 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +9.8 | 3e-20 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +8.5 | 3e-15 | 7/15 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.27×** | +7.2 | 6e-11 | 9/18 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +7.2 | 6e-11 | 1/8 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +6.6 | 4e-09 | 2/19 (LoVo, BT-474) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +6.3 | 2e-08 | 2/11 (A-172, SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.71×** | +6.3 | 2e-08 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +6.1 | 8e-08 | 7/18 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.47×** | +5.7 | 5e-07 | 3/8 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.31×** | +5.3 | 7e-06 | 2/14 (A-427, MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.5 | 3e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.2 | 0.001 | 1/15 (NCI-H23) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.2 | 0.001 | 2/11 (LoVo, PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +4.2 | 0.001 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.001 | 9/20 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 5/20 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +3.9 | 0.003 | 4/17 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.011 | 2/15 (A-427, PANC-1) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.014 | 0/18 | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.023 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.037 | 1/14 (RKO) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.065 | 1/19 (A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.642×** | -3.9 | 0.024 | 13/20 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.632×** | -3.9 | 0.024 | 8/18 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.650×** | -3.8 | 0.024 | 4/20 (CHP-212, SW480, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -3.6 | 0.043 | 7/15 (RKO, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 23.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -12.2) |
| [[LoVo (line)]] | wt | 6.76 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0827× (z -13.1) |
| [[A-172 (line)]] | wt | 3.90 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0708× (z -9.5) |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0799× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0974× (z -11.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.103× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 4.65 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0849× (z -8.5) |
| [[A-427 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.748 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.795 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPMS2]] | +0.67 | +0.56 / +0.56 | both halves | 1e-05 | same gene group |
| [[SMO]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TBKBP1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[LRRN2]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PKN3]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[GRID1]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[TYRO3]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SCD5]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FAXC]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[BRSK2]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NKAIN1]] | +0.60 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0319L]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[PKN2]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1C]] | B | RASGEF1C activity raises MSI1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without RASGEF1C | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises MSI1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without FAXC | 0.044 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[EBF4]] | B | EBF4 activity raises MSI1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without EBF4 | 0.093 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[LRRC4B]] | C | LRRC4B activity raises MSI1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without LRRC4B | 0.056 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent; co-absent with the target |
| [[PALM]] | C | PALM activity raises MSI1's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without PALM | 0.057 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[TBX1]] | C | TBX1 activity raises MSI1's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.46× lower at baseline in the lines without TBX1 | 0.075 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1; co-absent with the target |
| [[KCND3]] | C | KCND3 activity raises MSI1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without KCND3 | 0.091 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 36, C 10. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1C]] | B | MSI1 activity raises RASGEF1C's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without MSI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[RHBDL3]] | B | MSI1 activity raises RHBDL3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without MSI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[LINC00937]] | B | MSI1 activity raises LINC00937's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without MSI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[PKN3]] | B | MSI1 activity raises PKN3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.67× lower at baseline in the lines without MSI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[KMT2D]] | B | MSI1 activity raises KMT2D's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.33× lower at baseline in the lines without MSI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[TLE2]] | B | MSI1 activity raises TLE2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without MSI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[GNAL]] | B | MSI1 activity raises GNAL's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without MSI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[LINC01357]] | B | MSI1 activity raises LINC01357's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.80× lower at baseline in the lines without MSI1 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[ADCY3]] | B | MSI1 activity raises ADCY3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without MSI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[BRSK2]] | B | MSI1 activity raises BRSK2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without MSI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[DBNDD1]] | B | MSI1 activity raises DBNDD1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without MSI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[SMO]] | B | MSI1 activity raises SMO's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without MSI1 | 0.021 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.4, 35.7); signed map (26.5, 24.6). **Vector** length 34.3, 5.82% of its response variance represented; |z| ≥ 3 in 442 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +9.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.4 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | musashi RNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,341,330-120,369,164 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing; Musashi RNA binding protein family |
| Reactome | 4 pathways, smallest: Regulation of expression of SLITs and ROBOs; Signaling by ROBO receptors; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O43347](https://www.uniprot.org/uniprotkb/O43347) (RNA-binding protein Musashi homolog 1):

> RNA binding protein that regulates the expression of target mRNAs at the translation level. Regulates expression of the NOTCH1 antagonist NUMB. Binds RNA containing the sequence 5'-GUUAGUUAGUUAGUU-3' and other sequences containing the pattern 5'-[GA]U(1-3)AGU-3'. May play a role in the proliferation and maintenance of stem cells in the central nervous system (By similarity).

**Summary**, from NCBI Gene [4440](https://www.ncbi.nlm.nih.gov/gene/4440):

> This gene encodes a protein containing two conserved tandem RNA recognition motifs. Similar proteins in other species function as RNA-binding proteins and play central roles in posttranscriptional gene regulation. Expression of this gene has been correlated with the grade of the malignancy and proliferative activity in gliomas and melanomas. A pseudogene for this gene is located on chromosome 11q13. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7330) · Entrez [4440](https://www.ncbi.nlm.nih.gov/gene/4440) · UniProt [O43347](https://www.uniprot.org/uniprotkb/O43347) · Ensembl [ENSG00000135097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135097)

## Data

Gene col 5652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5652); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5652]; `tensor/DDL_lfc|DDL_z.npy` [5652]; `embed/gene_vectors.npy` [5652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5652 or target_col == 5652). Every well: [[MSI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
