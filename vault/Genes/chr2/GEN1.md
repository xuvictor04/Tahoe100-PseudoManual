---
symbol: "GEN1"
type: "gene"
col: 10914
ensembl_id: "ENSG00000178295"
name: "GEN1 structure-specific endonuclease"
location: "2p24.2"
module: 91
arm: "+"
pooled_cpm: 42.03
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# GEN1

*GEN1 structure-specific endonuclease* — 2p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +8.0, q 8e-13, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.632× (z -6.3, q 1e-07, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESCO2]] (+0.82, fdr 7e-06), [[CIP2A]] (+0.82, fdr 7e-06), [[BRCA2]] (+0.81, fdr 7e-06); moves opposite to [[PLD3]] (-0.64, fdr 1e-05), [[PIGH]] (-0.64, fdr 2e-05), [[STX7]] (-0.63, fdr 9e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.0 | 8e-13 | 36/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.9 | 8e-13 | 32/47 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +6.9 | 9e-10 | 34/48 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +6.7 | 2e-09 | 25/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.3 | 1e-05 | 32/48 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.46×** | +4.9 | 7e-05 | 28/48 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.40×** | +4.5 | 7e-04 | 20/40 (CFPAC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +4.4 | 9e-04 | 24/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.064 | 14/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.064 | 16/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +3.1 | 0.090 | 17/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.0 | 0.090 | 11/48 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.090 | 7/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.090 | 12/48 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.090 | 9/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.090 | 11/48 (CFPAC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -6.3 | 1e-07 | 29/48 (SHP-77, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.726×** | -6.2 | 1e-07 | 30/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -5.1 | 6e-05 | 24/48 (HT-29, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.693×** | -5.0 | 6e-05 | 33/48 (A-427, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -5.0 | 6e-05 | 26/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -5.0 | 6e-05 | 30/48 (hTERT-HPNE, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.715×** | -4.6 | 3e-04 | 23/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.720×** | -4.5 | 5e-04 | 26/48 (CHP-212, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.645×** | -4.3 | 0.001 | 21/48 (LOX-IMVI, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.813×** | -4.0 | 0.003 | 22/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.008 | 25/48 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.012 | 21/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.750×** | -3.6 | 0.012 | 20/48 (A-427, NCI-H2030, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -3.6 | 0.015 | 22/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.777×** | -3.5 | 0.021 | 20/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.048 | 17/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.048 | 16/48 (A-427, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.4) | [[Digitoxin (drug)]] 5 µM 0.297× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 80.5 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.285× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 22.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +15.2) | — |
| [[RKO (line)]] | wt | 51.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 23.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.9) | — |
| [[A-427 (line)]] | wt | 73.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.467× (z -9.2) |
| [[A549 (line)]] | wt | 52.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.2) | — |
| [[C32 (line)]] | wt | 40.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +8.5) | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.135× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 51.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.373× (z -8.8) |
| [[LS 180 (line)]] | wt | 37.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.409× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 24.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.72× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 75.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW1417 (line)]] | alt | 46.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.6) | — |
| [[A-172 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESCO2]] | +0.82 | +0.85 / +0.79 | both halves | 7e-06 | STRING 415 |
| [[CIP2A]] | +0.82 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.81 | +0.86 / +0.79 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 796 |
| [[HASPIN]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[TMPO]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[LRR1]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ESPL1]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.73 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[CENPH]] | +0.73 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[ZNF724]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[CENPN]] | +0.73 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[SPDL1]] | +0.73 | +0.77 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLD3]] | -0.64 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[PIGH]] | -0.64 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[STX7]] | -0.63 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[FBXO44]] | -0.62 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[VPS37D]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[RBIS]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GEN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TP53]] | C | TP53 activity weakens GEN1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.15× as strongly (z diff -0.58); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.53x vs 1.01x (z diff -3.5) | 0.112 over the table, 0.003 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-40.9, -48.0); signed map (-44.0, -47.5). **Vector** length 140, 43.3% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.5 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.6 | +3.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.3 | +2.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.3 | +3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.2 | +3.3 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.1 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -6.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | GEN1 structure-specific endonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.2 — chr2:17,753,858-17,788,946 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40869, Gen |
| Gene groups (HGNC) | Rad2/XPG endonuclease family |
| Reactome | 7 pathways, smallest: Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures; HDR through Homologous Recombination (HRR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RS7](https://www.uniprot.org/uniprotkb/Q17RS7) (Flap endonuclease GEN homolog 1):

> Endonuclease which resolves Holliday junctions (HJs) by the introduction of symmetrically related cuts across the junction point, to produce nicked duplex products in which the nicks can be readily ligated. Four-way DNA intermediates, also known as Holliday junctions, are formed during homologous recombination and DNA repair, and their resolution is necessary for proper chromosome segregation. Cleaves HJs by a nick and counter-nick mechanism involving dual coordinated incisions that lead to the …

**Summary**, from NCBI Gene [348654](https://www.ncbi.nlm.nih.gov/gene/348654):

> This gene encodes a member of the Rad2/xeroderma pigmentosum group G nuclease family, whose members are characterized by N-terminal and internal xeroderma pigmentosum group G nuclease domains followed by helix-hairpin-helix domains and disordered C-terminal domains. The protein encoded by this gene is involved in resolution of Holliday junctions, which are intermediate four-way structures that covalently link DNA during homologous recombination and double-strand break repair. The protein …

**Accessions** — [HGNC:26881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26881) · Entrez [348654](https://www.ncbi.nlm.nih.gov/gene/348654) · UniProt [Q17RS7](https://www.uniprot.org/uniprotkb/Q17RS7) · Ensembl [ENSG00000178295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178295)

## Data

Gene col 10914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10914); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10914]; `tensor/DDL_lfc|DDL_z.npy` [10914]; `embed/gene_vectors.npy` [10914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10914 or target_col == 10914). Every well: [[GEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
