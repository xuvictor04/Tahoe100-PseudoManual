---
symbol: "BMPER"
type: "gene"
col: 8973
ensembl_id: "ENSG00000164619"
name: "BMP binding endothelial regulator"
location: "7p14.3"
module: 19
arm: "+"
pooled_cpm: 17.58
n_lines_expressing: 29
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 50
direction_downstream: 58
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# BMPER

*BMP binding endothelial regulator* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.92× (z +7.4, q 1e-10, up in 5 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +6.3, q 8e-08, up in 7 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.444× (z -9.5, q 1e-18, down in 17 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS6]] (+0.72, fdr 7e-06), [[C5orf46]] (+0.69, fdr 7e-06), [[GJA1]] (+0.68, fdr 7e-06); moves opposite to [[PLEKHA7]] (-0.49, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[FGD4]] → it (grade B ⚠); 58 go from it, the strongest it → [[GNG11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +7.4 | 1e-10 | 5/18 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.3 | 8e-08 | 7/27 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.33×** | +5.0 | 1e-04 | 6/27 (A498, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.8 | 3e-04 | 3/19 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.7 | 3e-04 | 2/16 (NCI-H2030, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.002 | 6/27 (RPMI-7951, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.006 | 8/27 (A-172, SW 900, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.012 | 9/26 (HOP62, SHP-77, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.054 | 3/27 (A-172, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Nafamostat (mesylate) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.11 | 2/26 (NCI-H1792, SW48) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 1/27 (A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.444×** | -9.5 | 1e-18 | 17/26 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.581×** | -6.6 | 1e-08 | 16/27 (NCI-H460, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -6.5 | 2e-08 | 16/26 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.589×** | -6.5 | 2e-08 | 14/27 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.696×** | -6.2 | 5e-08 | 18/25 (NCI-H460, RPMI-7951, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.609×** | -6.0 | 2e-07 | 18/27 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.617×** | -5.9 | 4e-07 | 16/22 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.623×** | -5.7 | 6e-07 | 15/26 (NCI-H460, J82, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.649×** | -5.3 | 9e-06 | 15/27 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.661×** | -5.0 | 3e-05 | 13/25 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.660×** | -4.9 | 6e-05 | 14/26 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.688×** | -4.5 | 3e-04 | 17/26 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.710×** | -4.2 | 0.001 | 10/27 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -3.6 | 0.011 | 16/26 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.742×** | -3.6 | 0.011 | 10/26 (SNU-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.012 | 7/27 (COLO 205, NCI-H23, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.019 | 5/27 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.696×** | -3.1 | 0.050 | 3/27 (AN3 CA, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.772×** | -3.0 | 0.065 | 6/25 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.839× | -3.0 | 0.065 | 7/27 (J82, A549, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.068 | 10/25 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.068 | 11/27 (Hs 766T, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 0 | 44 (17 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -29.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0618× (z -24.3) |
| [[J82 (line)]] | alt | 128 | 0 | 16 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.209× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 47.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0666× (z -16.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 46.9 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.3 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.177× (z -8.7) |
| [[C32 (line)]] | wt | 7.08 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0732× (z -8.7) |
| [[H4 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 6.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -11.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0931× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.39 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.122× (z -9.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0550× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0980× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0304× (z -10.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW 900 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.92× (z +12.4) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[A-427 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS6]] | +0.72 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[C5orf46]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GJA1]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[VEGFC]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[NCKAP5]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SPOCK1]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FRMPD4]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CDH11]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SIRLNT]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ABI3BP]] | +0.61 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[PDE3A]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA7]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 18, C 32. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | FGD4 activity lowers BMPER's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.25× higher at baseline in the lines without FGD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[LINC00922]] | B | LINC00922 activity raises BMPER's level | lines that do not express LINC00922 (9) vs lines expressing it (41) | 2.13× lower at baseline in the lines without LINC00922 | 0.028 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[NLGN4Y]] | B | NLGN4Y activity raises BMPER's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without NLGN4Y | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9 |
| [[SEMA5A]] | B | SEMA5A activity raises BMPER's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without SEMA5A | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[CDH13]] | B | CDH13 activity raises BMPER's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without CDH13 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[INHBA]] | B | INHBA activity raises BMPER's level | lines that do not express INHBA (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without INHBA | 0.042 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[GLIS3]] | B | GLIS3 activity raises BMPER's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.14× lower at baseline in the lines without GLIS3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[PDE3A]] | B | PDE3A activity raises BMPER's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without PDE3A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[RBFOX1]] | B | RBFOX1 activity raises BMPER's level | lines that do not express RBFOX1 (6) vs lines expressing it (44) | 3.54× lower at baseline in the lines without RBFOX1 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02932, ZNF474, DNAH6; maybe low, not absent |
| [[COL4A6]] | B | COL4A6 activity raises BMPER's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without COL4A6 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035 |
| [[PAPPA2]] | B | PAPPA2 activity raises BMPER's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without PAPPA2 | 0.071 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[TENM2]] | B | TENM2 activity raises BMPER's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without TENM2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1 |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 38, C 20. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNG11]] | B | BMPER activity raises GNG11's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.68× lower at baseline in the lines without BMPER | 0.014 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | BMPER activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[P4HA3]] | B | BMPER activity raises P4HA3's level | lines that do not express BMPER (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without BMPER | 0.027 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | BMPER activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.48× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[GLIS3]] | B | BMPER activity raises GLIS3's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.99× lower at baseline in the lines without BMPER | 0.031 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[ADAMTS6]] | B | BMPER activity raises ADAMTS6's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.26× lower at baseline in the lines without BMPER | 0.034 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[PRSS23]] | B | BMPER activity raises PRSS23's level | lines that do not express BMPER (21) vs lines expressing it (29) | 2.57× lower at baseline in the lines without BMPER | 0.035 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| cells under [[Sunitinib (drug)]] 5 µM | B | BMPER activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.24× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| cells under [[Pemetrexed (drug)]] 5 µM | B | BMPER activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.23× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | BMPER activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.16× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| cells under [[Mebendazole (drug)]] 0.5 µM | B | BMPER activity lowers the cells' numbers under Mebendazole 0.5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.12× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[FGD4]] | B | BMPER activity lowers FGD4's level | lines that do not express BMPER (21) vs lines expressing it (29) | 2.22× higher at baseline in the lines without BMPER | 0.049 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.5, 16.5); signed map (39.2, 44.3). **Vector** length 75.6, 17.6% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.0 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | BMP binding endothelial regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:33,904,308-34,156,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cv2, CRIM3 |
| Gene groups (HGNC) | Cysteine rich transmembrane BMP regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8U9](https://www.uniprot.org/uniprotkb/Q8N8U9) (BMP-binding endothelial regulator protein):

> Inhibitor of bone morphogenetic protein (BMP) function, it may regulate BMP responsiveness of osteoblasts and chondrocytes.

**Summary**, from NCBI Gene [168667](https://www.ncbi.nlm.nih.gov/gene/168667):

> This gene encodes a secreted protein that interacts with, and inhibits bone morphogenetic protein (BMP) function. It has been shown to inhibit BMP2- and BMP4-dependent osteoblast differentiation and BMP-dependent differentiation of the chondrogenic cells. Mutations in this gene are associated with a lethal skeletal disorder, diaphanospondylodysostosis. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:24154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24154) · Entrez [168667](https://www.ncbi.nlm.nih.gov/gene/168667) · UniProt [Q8N8U9](https://www.uniprot.org/uniprotkb/Q8N8U9) · Ensembl [ENSG00000164619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164619)

## Data

Gene col 8973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8973); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8973]; `tensor/DDL_lfc|DDL_z.npy` [8973]; `embed/gene_vectors.npy` [8973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8973 or target_col == 8973). Every well: [[BMPER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMPER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
