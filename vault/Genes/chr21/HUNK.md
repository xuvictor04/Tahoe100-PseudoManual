---
symbol: "HUNK"
type: "gene"
col: 6597
ensembl_id: "ENSG00000142149"
name: "hormonally up-regulated Neu-associated kinase"
location: "21q22.11"
module: 27
arm: "+"
pooled_cpm: 14.58
n_lines_expressing: 29
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 5
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# HUNK

*hormonally up-regulated Neu-associated kinase* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +22.1, q 0e+00, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.533× (z -9.3, q 6e-18, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHDH]] (+0.64, fdr 1e-05), [[LINC02058]] (+0.62, fdr 7e-06), [[ADAMTS19]] (+0.61, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[FGD5]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +22.1 | 0e+00 | 18/26 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +8.6 | 2e-15 | 17/26 (A-427, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +7.5 | 1e-11 | 12/26 (A498, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.60×** | +7.4 | 3e-11 | 10/17 (LoVo, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +7.2 | 5e-11 | 14/26 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +6.9 | 4e-10 | 11/26 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.8 | 1e-09 | 1/11 (HS-578T) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.86×** | +6.5 | 5e-09 | 8/27 (A498, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.6 | 2e-06 | 8/20 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 9/26 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.6 | 2e-04 | 3/18 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 8/23 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 7/25 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.002 | 7/25 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 6/27 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.021 | 4/24 (SW1417, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.026 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.026 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.054 | 6/26 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.533×** | -9.3 | 6e-18 | 16/26 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.637×** | -6.7 | 7e-09 | 15/27 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -6.1 | 2e-07 | 15/27 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.748×** | -4.3 | 0.002 | 10/27 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.007 | 8/27 (A-427, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.754×** | -3.9 | 0.010 | 4/26 (COLO 205, C32, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.854× | -3.3 | 0.063 | 3/27 (HS-578T, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.063 | 13/27 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.858× | -3.2 | 0.071 | 4/27 (SW480, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.071 | 10/26 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.071 | 13/27 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.814× | -3.1 | 0.10 | 12/27 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 110 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -31.7) |
| [[COLO 205 (line)]] | alt | 103 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0777× (z -25.1) |
| [[A-172 (line)]] | wt | 24.6 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0772× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.137× (z -12.8) |
| [[LS 180 (line)]] | wt | 65.0 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0918× (z -16.7) |
| [[A498 (line)]] | wt | 6.55 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +13.1) | — |
| [[A-427 (line)]] | wt | 20.4 | 1 | 2 | [[Auranofin (drug)]] 5 µM 5.42× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -10.8) |
| [[LoVo (line)]] | wt | 13.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.8) |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.7) |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Apalutamide (drug)]] 0.05 µM 0.0735× (z -9.7) |
| [[RKO (line)]] | wt | 13.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.100× (z -11.7) |
| [[A549 (line)]] | wt | 9.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 4.93 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.134× (z -8.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHDH]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTS19]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[SLC30A10]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[VWA2]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[IL17RB]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ENTREP2]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ADGRG5]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.59 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[NKD1]] | +0.58 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[LINC02981]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD5]] | B | FGD5 activity raises HUNK's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without FGD5 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[APCDD1]] | B | APCDD1 activity raises HUNK's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 3.61× lower at baseline in the lines without APCDD1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[VSNL1]] | B | VSNL1 activity raises HUNK's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without VSNL1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[EPHX4]] | B | EPHX4 activity raises HUNK's level | lines that do not express EPHX4 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without EPHX4 | 0.061 | ⚠ within organs, on part of the lines; also absent: GALNT6, NOD2 |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises HUNK's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.17× lower at baseline in the lines without ZNF503-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[TFF3]] | B | TFF3 activity raises HUNK's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.62× lower at baseline in the lines without TFF3 | 0.080 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[HDAC6]] | B | HDAC6 activity raises HUNK's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C9orf152]] | B | C9orf152 activity raises HUNK's level | lines that do not express C9orf152 (32) vs lines expressing it (18) | 2.01× lower at baseline in the lines without C9orf152 | 0.084 | ⚠ within organs, on part of the lines; also absent: AGR3, MYO7B, KRT17; maybe low, not absent |
| [[NCALD]] | B | NCALD activity raises HUNK's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without NCALD | 0.094 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[BMP7]] | B | BMP7 activity raises HUNK's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 2.06× lower at baseline in the lines without BMP7 | 0.097 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[NKD1]] | C | NKD1 activity raises HUNK's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without NKD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Docetaxel (Trihydrate) (drug)]] 0.5 µM | B | HUNK activity lowers the cells' numbers under Docetaxel (Trihydrate) 0.5 µM (makes them more sensitive) | lines that do not express HUNK (21) vs lines expressing it (27) | the lines without HUNK: 1.16× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| cells under [[Pimozide (drug)]] 0.5 µM | B | HUNK activity lowers the cells' numbers under Pimozide 0.5 µM (makes them more sensitive) | lines that do not express HUNK (21) vs lines expressing it (27) | the lines without HUNK: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| [[CACNA1E]] | B | HUNK activity raises CACNA1E's level | lines that do not express HUNK (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without HUNK | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| cells under [[Osimertinib (mesylate) (drug)]] 5 µM | B | HUNK activity lowers the cells' numbers under Osimertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express HUNK (21) vs lines expressing it (27) | the lines without HUNK: 1.14× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| [[NCALD]] | B | HUNK activity raises NCALD's level | lines that do not express HUNK (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without HUNK | 0.098 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 44.3); signed map (62.2, 14.5). **Vector** length 74.2, 18.0% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +22.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | hormonally up-regulated Neu-associated kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:31,873,020-32,044,633 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | HUNK family kinases |
| Matched by | ensembl_id |

UniProt [P57058](https://www.uniprot.org/uniprotkb/P57058) carries no function annotation.

**Summary**, from NCBI Gene [30811](https://www.ncbi.nlm.nih.gov/gene/30811):

> Predicted to enable protein serine/threonine kinase activity. Predicted to be involved in intracellular signal transduction. Predicted to act upstream of or within protein phosphorylation. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13326) · Entrez [30811](https://www.ncbi.nlm.nih.gov/gene/30811) · UniProt [P57058](https://www.uniprot.org/uniprotkb/P57058) · Ensembl [ENSG00000142149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142149)

## Data

Gene col 6597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6597); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6597]; `tensor/DDL_lfc|DDL_z.npy` [6597]; `embed/gene_vectors.npy` [6597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6597 or target_col == 6597). Every well: [[HUNK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HUNK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
