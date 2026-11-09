---
symbol: "FOXO3B"
type: "gene"
col: 14236
ensembl_id: "ENSG00000240445"
name: "forkhead box O3B"
location: "17p11.2"
module: 33
arm: "+"
pooled_cpm: 4.31
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# FOXO3B

*forkhead box O3B* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.75× (z +7.3, q 1e-10, up in 9 of 21 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.43× (z +6.7, q 7e-09, up in 12 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.628× (z -6.4, q 1e-07, down in 11 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -5.7, q 3e-06, down in 14 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF286A]] (+0.75, fdr 7e-06), [[NOB1]] (+0.63, fdr 1e-05), [[ZNF74]] (+0.61, fdr 1e-05); moves opposite to [[GPAA1]] (-0.57, fdr 3e-05), [[PRKCA]] (-0.52, fdr 4e-05), [[CFL1]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.3 | 1e-10 | 9/21 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +6.7 | 7e-09 | 12/45 (NCI-H460, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +6.1 | 3e-07 | 12/45 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.8 | 9e-07 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +5.7 | 1e-06 | 16/41 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +5.6 | 2e-06 | 11/38 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +5.1 | 3e-05 | 3/12 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.6 | 3e-04 | 4/41 (NCI-H460, HCT15, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.6 | 3e-04 | 4/46 (HOP62, C-33 A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.5 | 4e-04 | 13/45 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +3.9 | 0.005 | 5/41 (H4, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.009 | 3/45 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.010 | 5/44 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.010 | 7/44 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.6 | 0.010 | 2/21 (A-172, NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.015 | 3/23 (NCI-H2030, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.021 | 2/44 (RKO, hTERT-HPNE) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.032 | 4/29 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.043 | 6/38 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.055 | 6/44 (PANC-1, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.092 | 5/37 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +2.9 | 0.095 | 7/44 (NCI-H460, LS 180, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.628×** | -6.4 | 1e-07 | 11/19 (NCI-H460, SW480, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -5.7 | 3e-06 | 14/36 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -4.5 | 0.001 | 12/45 (Panc 03.27, SW480, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.790×** | -4.5 | 0.001 | 10/44 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.744×** | -4.1 | 0.005 | 8/44 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -4.0 | 0.005 | 10/37 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.828×** | -3.6 | 0.029 | 11/39 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.776×** | -3.5 | 0.034 | 11/43 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.777×** | -3.5 | 0.034 | 11/45 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 0.843× | -3.3 | 0.064 | 5/45 (HCT15, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 16.1 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0880× (z -12.2) |
| [[A-172 (line)]] | wt | 5.47 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -9.0) |
| [[A549 (line)]] | wt | 4.59 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0600× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.14 | 0 | 1 | — | [[LJI308 (drug)]] 0.5 µM 0.0649× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 4.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -8.6) |
| [[SW480 (line)]] | alt | 3.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF286A]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[NOB1]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF286B]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF615]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[C3orf33]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZNF133]] | +0.57 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ZNF571]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RABGGTB]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ZNF227]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ZNF566]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZFP37]] | +0.56 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[ZNF692]] | +0.55 | +0.38 / +0.63 | both halves | 7e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPAA1]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[PRKCA]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CFL1]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[HMGB1]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[CMTM6]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SKA2]] | -0.48 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PDLIM5]] | -0.47 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[BMPR2]] | -0.46 | -0.39 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FOXO3B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BRSK1]] | B | BRSK1 activity raises FOXO3B's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without BRSK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[PRKCA]] | B | PRKCA activity lowers FOXO3B's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without PRKCA | 0.011 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises FOXO3B's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without ANK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity lowers FOXO3B's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.96× higher at baseline in the lines without SMAD3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-39.3, 15.2); signed map (-16.1, -23.8). **Vector** length 47.0, 5.46% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.7 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +2.8 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.3 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -4.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box O3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,667,629-18,682,314 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FKHRL1P1 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A2Z4LIS9](https://www.uniprot.org/uniprotkb/A0A2Z4LIS9) (Forkhead box protein O3B):

> Transcription factor.

**Summary**, from NCBI Gene [2310](https://www.ncbi.nlm.nih.gov/gene/2310):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II and response to starvation. Predicted to be located in mitochondrial matrix. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3822) · Entrez [2310](https://www.ncbi.nlm.nih.gov/gene/2310) · UniProt [A0A2Z4LIS9](https://www.uniprot.org/uniprotkb/A0A2Z4LIS9) · Ensembl [ENSG00000240445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240445)

## Data

Gene col 14236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14236); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14236]; `tensor/DDL_lfc|DDL_z.npy` [14236]; `embed/gene_vectors.npy` [14236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14236 or target_col == 14236). Every well: [[FOXO3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXO3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
