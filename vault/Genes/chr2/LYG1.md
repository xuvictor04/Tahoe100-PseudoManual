---
symbol: "LYG1"
type: "gene"
col: 6853
ensembl_id: "ENSG00000144214"
name: "lysozyme g1"
location: "2q11.2"
module: 39
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 45
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# LYG1

*lysozyme g1* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.13× (z +8.2, q 8e-14, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.601× (z -5.6, q 1e-05, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGAP5]] (+0.69, fdr 7e-06), [[RFPL3S]] (+0.66, fdr 1e-05), [[CDKL4]] (+0.66, fdr 7e-06); moves opposite to [[CYB5RL]] (-0.50, fdr 4e-04), [[ALG10B]] (-0.49, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[C9orf153]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.13×** | +8.2 | 8e-14 | 26/41 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.2 | 8e-14 | 22/35 (SW48, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.16×** | +7.9 | 5e-13 | 28/38 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.0 | 1e-04 | 12/24 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 2e-04 | 14/38 (A-172, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.4 | 0.001 | 6/17 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.001 | 14/32 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.001 | 11/35 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.001 | 11/42 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.002 | 8/41 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.68×** | +4.0 | 0.003 | 5/40 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.5 | 0.021 | 0/6 | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +3.4 | 0.034 | 9/42 (HEC-1-A, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -5.6 | 1e-05 | 21/42 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -4.9 | 2e-04 | 16/39 (NCI-H1573, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.676×** | -4.1 | 0.007 | 18/38 (NCI-H1792, A498, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.526×** | -3.7 | 0.034 | 10/26 (NCI-H2030, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.712×** | -3.6 | 0.035 | 10/41 (SW 900, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -3.6 | 0.035 | 18/33 (NCI-H1573, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.749× | -3.0 | 0.18 | 5/39 (HCT15, CHP-212, …) | top dose only |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.760× | -3.0 | 0.18 | 6/41 (A-172, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.54 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0846× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 12.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 9.35 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 6.06 | 0 | 2 | — | [[Verteporfin (drug)]] 0.05 µM 0.0688× (z -10.8) |
| [[A-172 (line)]] | wt | 3.96 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM 0.0753× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 3.55 | 0 | 1 | — | [[Captopril (drug)]] 5 µM 0.0779× (z -9.2) |
| [[HS-578T (line)]] | alt | 3.92 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0546× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 5.96 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0517× (z -15.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 0.995 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP5]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[CDKL4]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RAPSN]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SLC22A13]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[TMEM236]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[C9orf24]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5RL]] | -0.50 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[ALG10B]] | -0.49 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LYG1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02133]] | C | LINC02133 activity raises LYG1's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.82× lower at baseline in the lines without LINC02133 | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent; co-absent with the target |
| [[RBM44]] | C | RBM44 activity raises LYG1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.79× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C9orf153]] | B | LYG1 activity raises C9orf153's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 2.64× lower at baseline in the lines without LYG1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[CDRT4]] | B | LYG1 activity raises CDRT4's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 2.90× lower at baseline in the lines without LYG1 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[TEX29]] | B | LYG1 activity raises TEX29's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without LYG1 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[PLD5P1]] | B | LYG1 activity raises PLD5P1's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without LYG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[LINC02804]] | B | LYG1 activity raises LINC02804's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without LYG1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[MYOCOS]] | B | LYG1 activity raises MYOCOS's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without LYG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[RBM44]] | C | LYG1 activity raises RBM44's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without LYG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent; co-absent with the target |
| [[LINC02133]] | C | LYG1 activity raises LINC02133's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without LYG1 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.5, -19.2); signed map (11.9, 9.8). **Vector** length 63.8, 9.53% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +0.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.0 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | -2.0 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | lysozyme g1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,284,238-99,304,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SALW1939, LYGA1 |
| Gene groups (HGNC) | Lysozymes, g-type |
| Matched by | ensembl_id |

UniProt [Q8N1E2](https://www.uniprot.org/uniprotkb/Q8N1E2) carries no function annotation.

**Summary**, from NCBI Gene [129530](https://www.ncbi.nlm.nih.gov/gene/129530):

> Predicted to enable lysozyme activity. Predicted to be involved in defense response to Gram-positive bacterium. Predicted to be active in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27014) · Entrez [129530](https://www.ncbi.nlm.nih.gov/gene/129530) · UniProt [Q8N1E2](https://www.uniprot.org/uniprotkb/Q8N1E2) · Ensembl [ENSG00000144214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144214)

## Data

Gene col 6853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6853); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6853]; `tensor/DDL_lfc|DDL_z.npy` [6853]; `embed/gene_vectors.npy` [6853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6853 or target_col == 6853). Every well: [[LYG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
