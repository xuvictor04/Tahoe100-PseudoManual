---
symbol: "FAM20C"
type: "gene"
col: 10857
ensembl_id: "ENSG00000177706"
name: "FAM20C golgi associated secretory pathway kinase"
location: "7p22.3"
module: 13
arm: "+"
pooled_cpm: 69.8
n_lines_expressing: 31
n_dd_up: 0
n_dd_down: 42
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 25
direction_downstream: 22
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FAM20C

*FAM20C golgi associated secretory pathway kinase* — 7p22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.350× (z -17.4, q 0e+00, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAV1]] (+0.64, fdr 7e-06), [[DENND2A]] (+0.64, fdr 7e-06), [[ITGB3]] (+0.63, fdr 7e-06); moves opposite to [[LINC02253]] (-0.53, fdr 3e-05), [[LINC01748]] (-0.49, fdr 3e-05), [[DLEU1]] (-0.49, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[HTRA3]] → it (grade B ⚠); 22 go from it, the strongest it → [[ITPR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.7 | 0.12 | 1/30 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.350×** | -17.4 | 0e+00 | 25/28 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.260×** | -15.8 | 0e+00 | 26/29 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.143×** | -14.9 | 0e+00 | 29/29 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.294×** | -14.4 | 1e-44 | 26/29 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.306×** | -13.9 | 8e-42 | 27/29 (RPMI-7951, NCI-H1792, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.312×** | -13.7 | 2e-40 | 25/28 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.312×** | -13.6 | 2e-40 | 28/29 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.331×** | -13.0 | 1e-36 | 26/29 (H4, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.344×** | -12.5 | 5e-34 | 24/29 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.379×** | -11.4 | 3e-28 | 26/29 (NCI-H1792, H4, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.382×** | -11.3 | 7e-28 | 26/29 (RPMI-7951, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -11.1 | 6e-27 | 21/29 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.622×** | -7.9 | 2e-13 | 19/29 (C32, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.513×** | -7.8 | 2e-13 | 24/29 (H4, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.523×** | -7.2 | 3e-11 | 21/29 (H4, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.590×** | -6.2 | 2e-08 | 17/29 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.466×** | -4.7 | 8e-05 | 17/29 (RPMI-7951, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.682×** | -4.5 | 2e-04 | 16/29 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 736 | 0 | 20 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0673× (z -27.9) |
| [[SW 900 (line)]] | alt | 190 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -20.4) |
| [[C32 (line)]] | wt | 80.9 | 0 | 19 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -19.1) |
| [[H4 (line)]] | wt | 257 | 0 | 19 (9 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0453× (z -20.0) |
| [[HOP62 (line)]] | alt | 121 | 0 | 18 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 673 | 0 | 18 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0800× (z -30.3) |
| [[J82 (line)]] | alt | 66.4 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -22.8) |
| [[SNU-423 (line)]] | alt | 297 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0718× (z -23.0) |
| [[A-172 (line)]] | wt | 81.1 | 0 | 11 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0803× (z -17.4) |
| [[A498 (line)]] | wt | 157 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.3) |
| [[HS-578T (line)]] | alt | 187 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0713× (z -19.0) |
| [[Panc 03.27 (line)]] | alt | 58.3 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -13.0) |
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -23.4) |
| [[A-427 (line)]] | wt | 24.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0483× (z -20.4) |
| [[A549 (line)]] | wt | 25.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -15.7) |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.7) |
| [[SW 1088 (line)]] | alt | 366 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0382× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.117× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -13.5) |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -10.6) |
| [[CHP-212 (line)]] | wt | 42.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -13.1) |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0859× (z -8.6) |
| [[LoVo (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -8.6) |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.5) |
| [[SW48 (line)]] | wt | 32.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.101× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAV1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DENND2A]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ITGB3]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LOXL2]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[VSTM4]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MRC2]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ADAM12]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[KCNK3]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02253]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LINC01748]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[DLEU1]] | -0.49 | -0.50 / -0.49 | both halves | 2e-05 |  |
| [[ADCY4]] | -0.49 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[ABO]] | -0.48 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[SYK]] | -0.47 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[POF1B]] | -0.47 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[MIR4307HG]] | -0.47 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[TMC4]] | -0.47 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[LINC02058]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[TMEM45B]] | -0.46 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[TOX3]] | -0.46 | -0.47 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 10, C 15. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTRA3]] | B | HTRA3 activity raises FAM20C's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.56× lower at baseline in the lines without HTRA3 | 0.022 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[COL7A1]] | B | COL7A1 activity raises FAM20C's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.90× lower at baseline in the lines without COL7A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[GPR173]] | B | GPR173 activity raises FAM20C's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without GPR173 | 0.048 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |
| [[GPR173]] | B | GPR173 activity strengthens FAM20C's drug response | lines that do not express GPR173 (16) vs lines expressing it (13) | the lines without GPR173 respond 0.75× as strongly (z diff +2.02); strongest at Ixazomib citrate 5 µM: 0.44x vs 0.21x (z diff +3.6) | 0.056 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; target measured in part of the lines; artifact flags |
| [[PATJ]] | B | PATJ activity lowers FAM20C's level | lines that do not express PATJ (9) vs lines expressing it (41) | 2.35× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[FRMD4A]] | B | FRMD4A activity raises FAM20C's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.44× lower at baseline in the lines without FRMD4A | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[SPOCD1]] | B | SPOCD1 activity strengthens FAM20C's drug response | lines that do not express SPOCD1 (13) vs lines expressing it (16) | the lines without SPOCD1 respond 0.64× as strongly (z diff +2.23); strongest at Ixazomib citrate 5 µM: 0.53x vs 0.21x (z diff +4.0) | 0.069 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; target measured in part of the lines; artifact flags |
| [[LINC02813]] | B | LINC02813 activity raises FAM20C's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without LINC02813 | 0.072 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[LOX]] | B | LOX activity raises FAM20C's level | lines that do not express LOX (31) vs lines expressing it (19) | 5.05× lower at baseline in the lines without LOX | 0.082 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity raises FAM20C's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.57× lower at baseline in the lines without ADAMTS9-AS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[COL5A1]] | C | COL5A1 activity raises FAM20C's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.44× lower at baseline in the lines without COL5A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises FAM20C's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 8.30× lower at baseline in the lines without LINC01411 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 12, C 10. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR1]] | B | FAM20C activity raises ITPR1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.39× lower at baseline in the lines without FAM20C | 0.013 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[NPAS1]] | B | FAM20C activity raises NPAS1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without FAM20C | 0.015 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[ZCCHC24]] | B | FAM20C activity raises ZCCHC24's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without FAM20C | 0.039 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[SYK]] | B | FAM20C activity lowers SYK's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.88× higher at baseline in the lines without FAM20C | 0.045 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[SSH1]] | B | FAM20C activity raises SSH1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without FAM20C | 0.047 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[LOXL2]] | B | FAM20C activity raises LOXL2's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.89× lower at baseline in the lines without FAM20C | 0.048 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[LINC03040]] | B | FAM20C activity lowers LINC03040's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.73× higher at baseline in the lines without FAM20C | 0.079 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[WIPF1]] | B | FAM20C activity raises WIPF1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.14× lower at baseline in the lines without FAM20C | 0.079 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[BSPRY]] | B | FAM20C activity lowers BSPRY's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.20× higher at baseline in the lines without FAM20C | 0.089 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[MPZL2]] | B | FAM20C activity lowers MPZL2's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 4.23× higher at baseline in the lines without FAM20C | 0.089 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[GHRLOS]] | B | FAM20C activity raises GHRLOS's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without FAM20C | 0.090 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[TMEM45B]] | B | FAM20C activity lowers TMEM45B's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 4.55× higher at baseline in the lines without FAM20C | 0.099 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.7, 17.1); signed map (24.9, 47.8). **Vector** length 100, 29.6% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +1.1 | -17.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.1 | -15.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.0 | -0.1 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Ritonavir (drug)]] 5 µM |  | +0.9 | +0.3 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +0.9 | +1.7 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +0.9 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -13.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -7.9 |
|  | [[NG25 (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -14.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -11.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | FAM20C golgi associated secretory pathway kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:192,571-260,772 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMAGE:4942737, DKFZp547D065, DMP4, G-CK |
| Gene groups (HGNC) | Golgi associated kinase family |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXL6](https://www.uniprot.org/uniprotkb/Q8IXL6) (Extracellular serine/threonine protein kinase FAM20C):

> Golgi serine/threonine protein kinase that phosphorylates secretory pathway proteins within Ser-x-Glu/pSer motifs and plays a key role in biomineralization of bones and teeth. Constitutes the main protein kinase for extracellular proteins, generating the majority of the extracellular phosphoproteome. Mainly phosphorylates proteins within the Ser-x-Glu/pSer motif, but also displays a broader substrate specificity. Phosphorylates ERO1A, enhancing its activity which is required to maintain …

**Summary**, from NCBI Gene [56975](https://www.ncbi.nlm.nih.gov/gene/56975):

> This gene encodes a member of the family of secreted protein kinases. The encoded protein binds calcium and phosphorylates proteins involved in bone mineralization. Mutations in this gene are associated with the autosomal recessive disorder Raine syndrome. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:22140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22140) · Entrez [56975](https://www.ncbi.nlm.nih.gov/gene/56975) · UniProt [Q8IXL6](https://www.uniprot.org/uniprotkb/Q8IXL6) · Ensembl [ENSG00000177706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177706)

## Data

Gene col 10857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10857); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10857]; `tensor/DDL_lfc|DDL_z.npy` [10857]; `embed/gene_vectors.npy` [10857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10857 or target_col == 10857). Every well: [[FAM20C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM20C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
