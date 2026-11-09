---
symbol: "PLEKHG4B"
type: "gene"
col: 7720
ensembl_id: "ENSG00000153404"
name: "pleckstrin homology and RhoGEF domain containing G4B"
location: "5p15.33"
module: 13
arm: "+"
pooled_cpm: 20.94
n_lines_expressing: 23
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 11
direction_downstream: 20
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PLEKHG4B

*pleckstrin homology and RhoGEF domain containing G4B* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +10.2, q 8e-22, up in 1 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +4.3, q 0.003, up in 3 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.441× (z -10.6, q 1e-23, down in 16 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR493HG]] (+0.70, fdr 7e-06), [[EVC2]] (+0.68, fdr 7e-06), [[MEG3]] (+0.66, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SARDH]] → it (grade B ⚠); 20 go from it, the strongest it → [[LINC01237]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +10.2 | 8e-22 | 1/17 (SW 900) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.5 | 2e-08 | 2/16 (SW 900, A549) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.2 | 5e-05 | 0/13 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.003 | 3/21 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.051 | 7/19 (SW 900, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.071 | 3/18 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.441×** | -10.6 | 1e-23 | 16/20 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -9.6 | 2e-19 | 18/20 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.493×** | -9.2 | 7e-18 | 15/20 (HOP62, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.500×** | -9.0 | 3e-17 | 19/20 (BT-474, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -7.5 | 6e-12 | 15/20 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.711×** | -6.3 | 4e-08 | 15/20 (HOP62, BT-474, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.628×** | -6.0 | 1e-07 | 14/20 (H4, A-427, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -6.0 | 1e-07 | 16/19 (BT-474, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -5.4 | 4e-06 | 14/18 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -5.3 | 6e-06 | 9/20 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -5.1 | 1e-05 | 16/20 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.670×** | -5.1 | 2e-05 | 13/19 (H4, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.750×** | -3.7 | 0.009 | 16/18 (SW480, H4, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.743×** | -3.7 | 0.009 | 14/20 (HOP62, A-427, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.586×** | -3.6 | 0.011 | 13/19 (HOP62, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.014 | 14/18 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.016 | 3/21 (BT-474, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.771×** | -3.3 | 0.032 | 11/20 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.775×** | -3.2 | 0.038 | 3/20 (SW 900, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 85.0 | 0 | 23 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0481× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0663× (z -17.0) |
| [[HOP62 (line)]] | alt | 197 | 0 | 23 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0233× (z -36.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0152× (z -29.1) |
| [[SW480 (line)]] | alt | 42.9 | 0 | 15 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -14.9) |
| [[BT-474 (line)]] | alt | 230 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -20.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.163× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 46.2 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0363× (z -20.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0315× (z -15.1) |
| [[A-427 (line)]] | wt | 68.8 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0898× (z -17.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -16.1) |
| [[RPMI-7951 (line)]] | alt | 56.6 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0602× (z -15.1) |
| [[AN3 CA (line)]] | alt | 85.7 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.0) |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.209× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.206× (z -9.0) |
| [[A549 (line)]] | wt | 7.31 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0579× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0533× (z -14.9) |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR493HG]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[EVC2]] | +0.68 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MEG3]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SYNDIG1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ITGA11]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[APCDD1L]] | +0.65 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[MEG8]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[CSF1R]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[GPR68]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KCNK3]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SARDH]] | B | SARDH activity raises PLEKHG4B's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without SARDH | 0.025 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[DENND2A]] | B | DENND2A activity raises PLEKHG4B's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without DENND2A | 0.035 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[LOXL1]] | B | LOXL1 activity raises PLEKHG4B's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.56× lower at baseline in the lines without LOXL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[SHANK1]] | B | SHANK1 activity raises PLEKHG4B's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without SHANK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[CRMP1]] | C | CRMP1 activity raises PLEKHG4B's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 4.25× lower at baseline in the lines without CRMP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent; co-absent with the target |
| [[SFRP1]] | C | SFRP1 activity raises PLEKHG4B's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 3.34× lower at baseline in the lines without SFRP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[WT1-AS]] | C | WT1-AS activity raises PLEKHG4B's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 2.73× lower at baseline in the lines without WT1-AS | 0.033 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises PLEKHG4B's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.82× lower at baseline in the lines without NTNG2 | 0.041 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[TSHZ3]] | C | TSHZ3 activity raises PLEKHG4B's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 3.47× lower at baseline in the lines without TSHZ3 | 0.042 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises PLEKHG4B's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.77× lower at baseline in the lines without EVC2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[MME]] | C | MME activity raises PLEKHG4B's level | lines that do not express MME (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without MME | 0.092 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01237]] | B | PLEKHG4B activity raises LINC01237's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without PLEKHG4B | 0.031 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[EML1]] | B | PLEKHG4B activity raises EML1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without PLEKHG4B | 0.038 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[LOXL1]] | B | PLEKHG4B activity raises LOXL1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without PLEKHG4B | 0.050 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[SSC5D]] | B | PLEKHG4B activity raises SSC5D's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without PLEKHG4B | 0.064 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[TMEM145]] | B | PLEKHG4B activity raises TMEM145's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without PLEKHG4B | 0.079 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[HEYL]] | C | PLEKHG4B activity raises HEYL's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without PLEKHG4B | 0.003 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[JPH3]] | C | PLEKHG4B activity raises JPH3's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without PLEKHG4B | 0.005 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[EVC2]] | C | PLEKHG4B activity raises EVC2's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 4.04× lower at baseline in the lines without PLEKHG4B | 0.006 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[NTNG2]] | C | PLEKHG4B activity raises NTNG2's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.64× lower at baseline in the lines without PLEKHG4B | 0.007 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[TSHZ3]] | C | PLEKHG4B activity raises TSHZ3's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 4.79× lower at baseline in the lines without PLEKHG4B | 0.008 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[SFRP1]] | C | PLEKHG4B activity raises SFRP1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 4.26× lower at baseline in the lines without PLEKHG4B | 0.010 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[EDARADD]] | C | PLEKHG4B activity raises EDARADD's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without PLEKHG4B | 0.033 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.7, 15.8); signed map (22.9, 47.8). **Vector** length 82.1, 26.1% of its response variance represented; |z| ≥ 3 in 681 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen chain trimerization* (reactome, mean cos +0.50 to 7); *NCAM1 interactions* (reactome, mean cos +0.54 to 6); *Signaling by PDGF* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -9.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.4 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -6.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -6.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:92,168-189,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1909, ARHGEF48 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PX9](https://www.uniprot.org/uniprotkb/Q96PX9) (Pleckstrin homology domain-containing family G member 4B):

> Guanine nucleotide exchange factor (GEF) which specifically activates small GTPase CDC42 by exchanging bound GDP for free GTP. Plays a role in actin cytoskeletal remodeling in the late stage of cell-cell junction formation by regulating the contractility of actin filaments, which prompts the conversion from 'open' to 'closed' junctions.

**Summary**, from NCBI Gene [153478](https://www.ncbi.nlm.nih.gov/gene/153478):

> This gene encodes a large protein that contains a pleckstrin homology domain and may function as a guanine nucleotide exchange factor. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:29399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29399) · Entrez [153478](https://www.ncbi.nlm.nih.gov/gene/153478) · UniProt [Q96PX9](https://www.uniprot.org/uniprotkb/Q96PX9) · Ensembl [ENSG00000153404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153404)

## Data

Gene col 7720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7720); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7720]; `tensor/DDL_lfc|DDL_z.npy` [7720]; `embed/gene_vectors.npy` [7720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7720 or target_col == 7720). Every well: [[PLEKHG4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
