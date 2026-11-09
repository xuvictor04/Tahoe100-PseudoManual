---
symbol: "CENPO"
type: "gene"
col: 6124
ensembl_id: "ENSG00000138092"
name: "centromere protein O"
location: "2p23.3"
module: 71
arm: "+"
pooled_cpm: 23.11
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# CENPO

*centromere protein O* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +8.7, q 1e-15, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.38× (z +5.5, q 5e-06, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.695× (z -8.0, q 7e-13, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA5]] (+0.88, fdr 7e-06), [[SPC25]] (+0.87, fdr 7e-06), [[DTL]] (+0.85, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.67×** | +8.7 | 1e-15 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.60×** | +8.1 | 2e-13 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.41×** | +7.6 | 6e-12 | 25/47 (PANC-1, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.52×** | +7.1 | 1e-10 | 26/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.5 | 5e-06 | 22/48 (NCI-H23, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.98×** | +5.4 | 5e-06 | 18/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.36×** | +5.3 | 1e-05 | 17/47 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.36×** | +5.3 | 1e-05 | 19/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +5.0 | 3e-05 | 19/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.31×** | +4.7 | 2e-04 | 19/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.0 | 0.003 | 20/47 (SW480, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +4.0 | 0.004 | 13/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +3.8 | 0.005 | 14/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.19× | +3.7 | 0.008 | 11/48 (LoVo, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.6 | 0.012 | 17/48 (A549, LoVo, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.019 | 8/48 (SW480, KATO III, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.695×** | -8.0 | 7e-13 | 24/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -7.9 | 7e-13 | 27/47 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.651×** | -7.3 | 4e-11 | 31/48 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -7.0 | 4e-10 | 24/48 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -5.3 | 1e-05 | 22/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.792×** | -5.3 | 1e-05 | 23/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.765×** | -4.6 | 4e-04 | 18/48 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.776×** | -4.4 | 9e-04 | 17/48 (SHP-77, RPMI-7951, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.597×** | -4.1 | 0.002 | 13/46 (SW480, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.790×** | -4.0 | 0.003 | 18/48 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.796×** | -3.9 | 0.005 | 19/45 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.837× | -3.8 | 0.007 | 11/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.814×** | -3.5 | 0.019 | 9/48 (SW 1088, A-427, …) | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.650×** | -3.4 | 0.024 | 12/46 (SW480, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.048 | 15/48 (A-427, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.059 | 10/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.059 | 8/47 (SW 900, SK-MEL-2, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.831×** | -3.0 | 0.059 | 13/47 (A-427, HOP62, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.876× | -2.9 | 0.082 | 8/48 (NCI-H661, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.1 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.240× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -9.8) |
| [[SW480 (line)]] | alt | 47.6 | 2 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.5) ⚠ cell-cycle shift, explains ~51% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.3) |
| [[A-427 (line)]] | wt | 58.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -13.0) |
| [[PANC-1 (line)]] | alt | 21.9 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +11.7) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HOP62 (line)]] | alt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 40.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.3) |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0874× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.2) |
| [[H4 (line)]] | wt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.2) |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 9.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.383× (z -9.4) ⚠ cell-cycle shift, explains ~65% of this change |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.243× (z -8.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA5]] | +0.88 | +0.87 / +0.90 | both halves | 7e-06 | pathway: Mitotic Anaphase; STRING 455 |
| [[SPC25]] | +0.87 | +0.88 / +0.87 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[DTL]] | +0.85 | +0.90 / +0.84 | both halves | 7e-06 |  |
| [[POLQ]] | +0.85 | +0.87 / +0.89 | both halves | 7e-06 |  |
| [[MELK]] | +0.84 | +0.89 / +0.86 | both halves | 7e-06 |  |
| [[GINS1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.84 | +0.87 / +0.82 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.84 | +0.87 / +0.83 | both halves | 7e-06 |  |
| [[WDR62]] | +0.83 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[RFWD3]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.83 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[MCM8]] | +0.82 | +0.84 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity lowers CENPO's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.916). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.7, -47.6); signed map (-40.8, -44.0). **Vector** length 119, 31.3% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metabolism of non-coding RNA* (reactome, mean cos +0.57 to 5); *snRNP Assembly* (reactome, mean cos +0.57 to 5); *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.5 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.4 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.4 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -8.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.3 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,793,136-24,822,376 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11266, CENP-O |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BU64](https://www.uniprot.org/uniprotkb/Q9BU64) (Centromere protein O):

> Component of the CENPA-CAD (nucleosome distal) complex, a complex recruited to centromeres which is involved in assembly of kinetochore proteins, mitotic progression and chromosome segregation. May be involved in incorporation of newly synthesized CENPA into centromeres via its interaction with the CENPA-NAC complex. Modulates the kinetochore-bound levels of NDC80 complex.

**Summary**, from NCBI Gene [79172](https://www.ncbi.nlm.nih.gov/gene/79172):

> This gene encodes a component of the interphase centromere complex. The encoded protein is localized to the centromere throughout the cell cycle and is required for bipolar spindle assembly, chromosome segregation and checkpoint signaling during mitosis. Alternatively spliced transcript variants encoding multiple protein isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:28152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28152) · Entrez [79172](https://www.ncbi.nlm.nih.gov/gene/79172) · UniProt [Q9BU64](https://www.uniprot.org/uniprotkb/Q9BU64) · Ensembl [ENSG00000138092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138092)

## Data

Gene col 6124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6124); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6124]; `tensor/DDL_lfc|DDL_z.npy` [6124]; `embed/gene_vectors.npy` [6124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6124 or target_col == 6124). Every well: [[CENPO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
