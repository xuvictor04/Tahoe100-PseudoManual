---
symbol: "PAQR7"
type: "gene"
col: 11321
ensembl_id: "ENSG00000182749"
name: "progestin and adipoQ receptor family member 7"
location: "1p36.11"
module: 203
arm: "+"
pooled_cpm: 14.99
n_lines_expressing: 45
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# PAQR7

*progestin and adipoQ receptor family member 7* — 1p36.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.462× (z -13.3, q 2e-37, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLK2]] (+0.59, fdr 1e-05), [[ZNF593]] (+0.58, fdr 3e-04), [[LRFN4]] (+0.58, fdr 2e-04); moves opposite to [[LAMP2]] (-0.53, fdr 1e-04), [[TMEM123]] (-0.53, fdr 9e-05), [[GOLM2]] (-0.52, fdr 1e-04).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[POF1B]] → it (grade B ⚠); 5 go from it, the strongest it → [[PDZD8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.462×** | -13.3 | 2e-37 | 34/42 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -12.5 | 2e-33 | 37/43 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.397×** | -10.8 | 7e-25 | 34/42 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.426×** | -10.4 | 5e-23 | 34/43 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -10.3 | 8e-23 | 35/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.438×** | -10.0 | 1e-21 | 32/43 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.439×** | -10.0 | 1e-21 | 34/42 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -10.0 | 2e-21 | 35/42 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.262×** | -8.5 | 1e-15 | 34/43 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.515×** | -8.1 | 4e-14 | 31/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -7.0 | 2e-10 | 26/42 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.361×** | -6.5 | 5e-09 | 24/39 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -6.0 | 7e-08 | 24/37 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -5.0 | 3e-05 | 20/42 (A-427, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -4.8 | 5e-05 | 19/42 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -4.8 | 5e-05 | 22/43 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.683×** | -4.4 | 4e-04 | 18/41 (SNU-423, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 66.4 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.140× (z -12.6) |
| [[PANC-1 (line)]] | alt | 24.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.5) |
| [[A-427 (line)]] | wt | 36.5 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.6) |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 48.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -16.9) |
| [[J82 (line)]] | alt | 28.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.3) |
| [[RKO (line)]] | wt | 21.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0352× (z -18.5) |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 9.15 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.3) |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -10.5) |
| [[LoVo (line)]] | wt | 12.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -12.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 7.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0892× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.8) |
| [[H4 (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0918× (z -8.8) |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -9.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -10.6) |
| [[SNU-423 (line)]] | alt | 9.91 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.114× (z -10.2) |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -8.5) |
| [[SW480 (line)]] | alt | 9.49 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLK2]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.58 | +0.29 / +0.68 | both halves | 3e-04 |  |
| [[LRFN4]] | +0.58 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[NLRX1]] | +0.57 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[RPAP1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[NUDT22]] | +0.55 | +0.37 / +0.70 | both halves | 8e-05 |  |
| [[SYDE1]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[IMP3]] | +0.55 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[MTG2]] | +0.55 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[FBXO45]] | +0.55 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[BCL7A]] | +0.54 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[RILPL1]] | +0.54 | +0.38 / +0.61 | both halves | 7e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | -0.53 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[TMEM123]] | -0.53 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[GOLM2]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[SPTBN1]] | -0.51 | -0.26 / -0.62 | both halves | 3e-04 |  |
| [[STT3B]] | -0.50 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[NONO]] | -0.50 | -0.19 / -0.64 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LZTFL1]] | -0.50 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[SLC44A1]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[TMED10]] | -0.49 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[TMEM30A]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ADD3]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[FKBP9]] | -0.47 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[C1QTNF3]] | -0.47 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POF1B]] | B | POF1B activity lowers PAQR7's level | lines that do not express POF1B (34) vs lines expressing it (16) | 1.79× higher at baseline in the lines without POF1B | 0.011 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[BOK]] | B | BOK activity raises PAQR7's level | lines that do not express BOK (5) vs lines expressing it (45) | 2.48× lower at baseline in the lines without BOK | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |
| [[SLC44A1]] | B | SLC44A1 activity lowers PAQR7's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 2.24× higher at baseline in the lines without SLC44A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD8]] | B | PAQR7 activity lowers PDZD8's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.90× higher at baseline in the lines without PAQR7 | 0.040 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |
| [[LZTS2]] | B | PAQR7 activity raises LZTS2's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without PAQR7 | 0.058 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |
| [[FBXO45]] | B | PAQR7 activity raises FBXO45's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.11× lower at baseline in the lines without PAQR7 | 0.069 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |
| [[ALKBH4]] | B | PAQR7 activity raises ALKBH4's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without PAQR7 | 0.079 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |
| [[ENDOG]] | B | PAQR7 activity raises ENDOG's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without PAQR7 | 0.085 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-50.0, -3.7); signed map (-9.9, -6.6). **Vector** length 68.1, 12.8% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -6.2 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -6.0 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | progestin and adipoQ receptor family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,861,484-25,875,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mSR, MPRA, PGLP |
| Gene groups (HGNC) | Progestin and adipoQ receptor family; PAQR family membrane progesterone receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WK9](https://www.uniprot.org/uniprotkb/Q86WK9) (Membrane progestin receptor alpha):

> Plasma membrane progesterone (P4) receptor coupled to G proteins. Seems to act through a G(i) mediated pathway. May be involved in oocyte maturation. Involved in neurosteroid inhibition of apoptosis. Also binds dehydroepiandrosterone (DHEA), pregnanolone, pregnenolone and allopregnanolone.

**Summary**, from NCBI Gene [164091](https://www.ncbi.nlm.nih.gov/gene/164091):

> Predicted to enable nuclear steroid receptor activity and steroid binding activity. Predicted to be involved in response to steroid hormone. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23146) · Entrez [164091](https://www.ncbi.nlm.nih.gov/gene/164091) · UniProt [Q86WK9](https://www.uniprot.org/uniprotkb/Q86WK9) · Ensembl [ENSG00000182749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182749)

## Data

Gene col 11321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11321); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11321]; `tensor/DDL_lfc|DDL_z.npy` [11321]; `embed/gene_vectors.npy` [11321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11321 or target_col == 11321). Every well: [[PAQR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAQR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
