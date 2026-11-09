---
symbol: "NOXRED1"
type: "gene"
col: 9144
ensembl_id: "ENSG00000165555"
name: "NADP dependent oxidoreductase domain containing 1"
location: "14q24.3"
module: 37
arm: "+"
pooled_cpm: 8.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# NOXRED1

*NADP dependent oxidoreductase domain containing 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +11.2, q 2e-26, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.254× (z -13.5, q 5e-39, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF547]] (+0.77, fdr 7e-06), [[C9orf24]] (+0.72, fdr 7e-06), [[ISY1-RAB43]] (+0.71, fdr 7e-06); moves opposite to [[SSX2IP]] (-0.69, fdr 9e-06), [[ICMT]] (-0.68, fdr 7e-06), [[MED14]] (-0.66, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF345]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +11.2 | 2e-26 | 41/44 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.5 | 2e-08 | 27/43 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +6.3 | 6e-08 | 29/45 (HOP62, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.2 | 8e-08 | 28/44 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 0.002 | 15/45 (SK-MEL-2, SW480, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.57×** | +4.2 | 0.002 | 16/43 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.023 | 10/46 (LS 180, A-172, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.029 | 5/47 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.095 | 12/47 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.38×** | +3.1 | 0.098 | 13/39 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 1.36× | +3.1 | 0.11 | 7/44 (LS 180, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.254×** | -13.5 | 5e-39 | 45/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.299×** | -11.9 | 2e-30 | 37/44 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.307×** | -11.2 | 5e-27 | 36/40 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.382×** | -9.5 | 3e-19 | 39/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.413×** | -8.7 | 3e-16 | 40/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.254×** | -7.1 | 1e-10 | 32/46 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.487×** | -6.8 | 7e-10 | 27/46 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.310×** | -6.1 | 1e-07 | 25/43 (COLO 205, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.554×** | -5.8 | 4e-07 | 28/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.608×** | -4.9 | 5e-05 | 23/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.006 | 17/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.684×** | -3.6 | 0.016 | 13/47 (A-172, HS-578T, …) | top dose only | plate-row cell shift |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.726×** | -3.1 | 0.074 | 11/47 (SW1417, H4, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.734×** | -3.0 | 0.095 | 19/46 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.556×** | -3.0 | 0.095 | 5/44 (SW48, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.98 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0361× (z -16.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -8.9) |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0350× (z -16.2) |
| [[SW480 (line)]] | alt | 9.72 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0960× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.166× (z -11.0) |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0341× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 6.73 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -11.7) |
| [[H4 (line)]] | wt | 11.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0607× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0632× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0770× (z -9.3) |
| [[HOP62 (line)]] | alt | 8.30 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -9.8) |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0722× (z -8.5) |
| [[KATO III (line)]] | alt | 8.76 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0383× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 7.04 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0372× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 9.64 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0463× (z -14.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0282× (z -8.8) |
| [[SNU-423 (line)]] | alt | 9.72 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0829× (z -12.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0889× (z -10.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 5.01 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0828× (z -8.5) |
| [[LoVo (line)]] | wt | 6.37 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0576× (z -11.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 9.71 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0896× (z -10.4) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0822× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.123× (z -8.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF547]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[C9orf24]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[UBE2CP5]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[TEX29]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SMBD1P]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.69 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PIN4]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[SPACDR]] | +0.68 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[FAM209A]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.69 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[ICMT]] | -0.68 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[MED14]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.64 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[LRRCC1]] | -0.62 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[VMA21]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[EFR3A]] | -0.62 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[ALDH3A2]] | -0.61 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[SIGMAR1]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MEST]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GUSB]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[THEM6]] | -0.60 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF345]] | B | ZNF345 activity raises NOXRED1's level | lines that do not express ZNF345 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without ZNF345 | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF790, DNAH14, ZNF606 |
| [[TOP2A]] | B | TOP2A activity lowers NOXRED1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOOK1]] | B | HOOK1 activity raises NOXRED1's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.10× lower at baseline in the lines without HOOK1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[ZNF529-AS1]] | B | ZNF529-AS1 activity raises NOXRED1's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without ZNF529-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[TNNI3K]] | C | TNNI3K activity raises NOXRED1's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without TNNI3K | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.1, -20.2); signed map (11.0, 8.8). **Vector** length 82.9, 17.6% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.2 | +6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.5 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.8 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | -5.1 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NADP dependent oxidoreductase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,394,021-77,423,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32809; previously C14orf148 |
| Gene groups (HGNC) | Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXP6](https://www.uniprot.org/uniprotkb/Q6NXP6) (NADP-dependent oxidoreductase domain-containing protein 1):

> Probable oxidoreductase.

**Summary**, from NCBI Gene [122945](https://www.ncbi.nlm.nih.gov/gene/122945):

> Predicted to enable pyrroline-5-carboxylate reductase activity. Predicted to be involved in L-proline biosynthetic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20487) · Entrez [122945](https://www.ncbi.nlm.nih.gov/gene/122945) · UniProt [Q6NXP6](https://www.uniprot.org/uniprotkb/Q6NXP6) · Ensembl [ENSG00000165555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165555)

## Data

Gene col 9144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9144); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9144]; `tensor/DDL_lfc|DDL_z.npy` [9144]; `embed/gene_vectors.npy` [9144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9144 or target_col == 9144). Every well: [[NOXRED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOXRED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
