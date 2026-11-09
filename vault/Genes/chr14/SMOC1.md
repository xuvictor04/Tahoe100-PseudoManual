---
symbol: "SMOC1"
type: "gene"
col: 12659
ensembl_id: "ENSG00000198732"
name: "SPARC related modular calcium binding 1"
location: "14q24.1"
module: 19
arm: "+"
pooled_cpm: 75.67
n_lines_expressing: 16
n_dd_up: 11
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SMOC1

*SPARC related modular calcium binding 1* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +13.2, q 6e-37, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.681× (z -5.7, q 9e-06, down in 2 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EYA2]] (+0.75, fdr 7e-06), [[UNC5D]] (+0.73, fdr 1e-05), [[RSPO3]] (+0.69, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[LXN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +13.2 | 6e-37 | 3/15 (HepG2/C3A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.9 | 2e-16 | 2/15 (NCI-H1573, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.3 | 2e-14 | 5/14 (LS 180, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +7.3 | 5e-11 | 3/16 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.9 | 5e-10 | 7/14 (HepG2/C3A, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.7 | 2e-04 | 1/12 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.6 | 3e-04 | 2/14 (HOP62, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +3.3 | 0.062 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.081 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.081 | 4/14 (HOP62, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.23×** | +3.1 | 0.085 | 1/14 (SW1417) | top dose only | composition shift |
| [[Arbutin (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.12 | 4/14 (hTERT-HPNE, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.681×** | -5.7 | 9e-06 | 2/14 (NCI-H460, LS 180) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.609×** | -5.3 | 3e-05 | 10/14 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.615×** | -5.2 | 4e-05 | 8/14 (SW 900, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -4.5 | 9e-04 | 9/14 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.3 | 0.002 | 11/14 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.673×** | -4.2 | 0.002 | 7/14 (A549, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.652×** | -4.2 | 0.002 | 2/14 (NCI-H460, LS 180) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.684×** | -4.1 | 0.003 | 5/14 (SHP-77, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.685×** | -4.0 | 0.003 | 8/14 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.488×** | -4.0 | 0.003 | 7/14 (NCI-H460, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.673×** | -3.9 | 0.005 | 8/14 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.690×** | -3.8 | 0.008 | 0/14 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -3.7 | 0.011 | 9/14 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.526×** | -3.6 | 0.013 | 9/14 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.724×** | -3.5 | 0.021 | 7/14 (SW 900, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.022 | 6/14 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 533 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.7) |
| [[SHP-77 (line)]] | alt | 822 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -17.3) |
| [[NCI-H2030 (line)]] | alt | 565 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -16.1) |
| [[SW 900 (line)]] | alt | 67.9 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.128× (z -10.2) |
| [[A549 (line)]] | wt | 96.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0778× (z -11.9) |
| [[HOP62 (line)]] | alt | 38.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 7.98× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 6.76× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 92.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0998× (z -11.4) |
| [[A-427 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -11.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.118× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.1) |
| [[SW1417 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +9.3) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[A-172 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.52 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.65 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EYA2]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[UNC5D]] | +0.73 | +0.56 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[RSPO3]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PAK3]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CRLF2]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GRAMD1B]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[PDE7B]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GPRIN3]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SLITRK4]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CYP24A1]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CDH11]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMOC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LXN]] | B | LXN activity raises SMOC1's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without LXN | 0.020 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[NCKAP5]] | B | NCKAP5 activity raises SMOC1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without NCKAP5 | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers SMOC1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[DOCK4]] | B | DOCK4 activity raises SMOC1's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without DOCK4 | 0.099 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[GPRIN3]] | C | GPRIN3 activity raises SMOC1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.93× lower at baseline in the lines without GPRIN3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises SMOC1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.01× lower at baseline in the lines without DPP10 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises SMOC1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without COL22A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises SMOC1's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without LIN7A | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[TARID]] | C | TARID activity raises SMOC1's level | lines that do not express TARID (29) vs lines expressing it (21) | 4.11× lower at baseline in the lines without TARID | 0.083 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1; co-absent with the target |
| [[ADGRD1]] | C | ADGRD1 activity raises SMOC1's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without ADGRD1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[EYA2]] | C | EYA2 activity raises SMOC1's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 4.39× lower at baseline in the lines without EYA2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LXN]] | B | SMOC1 activity raises LXN's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 1.70× lower at baseline in the lines without SMOC1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1 |
| [[GPRIN3]] | C | SMOC1 activity raises GPRIN3's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 3.61× lower at baseline in the lines without SMOC1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[LIN7A]] | C | SMOC1 activity raises LIN7A's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without SMOC1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[TESC]] | C | SMOC1 activity raises TESC's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without SMOC1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[EYA2]] | C | SMOC1 activity raises EYA2's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 3.54× lower at baseline in the lines without SMOC1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 33.1); signed map (39.2, 46.1). **Vector** length 75.7, 28.6% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | SPARC related modular calcium binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,854,131-70,032,366 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SPARC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4F8](https://www.uniprot.org/uniprotkb/Q9H4F8) (SPARC-related modular calcium-binding protein 1):

> Plays essential roles in both eye and limb development. Probable regulator of osteoblast differentiation.

**Summary**, from NCBI Gene [64093](https://www.ncbi.nlm.nih.gov/gene/64093):

> This gene encodes a multi-domain secreted protein that may have a critical role in ocular and limb development. Mutations in this gene are associated with microphthalmia and limb anomalies. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:20318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20318) · Entrez [64093](https://www.ncbi.nlm.nih.gov/gene/64093) · UniProt [Q9H4F8](https://www.uniprot.org/uniprotkb/Q9H4F8) · Ensembl [ENSG00000198732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198732)

## Data

Gene col 12659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12659); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12659]; `tensor/DDL_lfc|DDL_z.npy` [12659]; `embed/gene_vectors.npy` [12659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12659 or target_col == 12659). Every well: [[SMOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
