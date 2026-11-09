---
symbol: "PDXDC2P"
type: "gene"
col: 14924
ensembl_id: "ENSG00000255185"
name: "pyridoxal dependent decarboxylase domain containing 2, pseudogene"
location: "16q22.1"
module: 56
arm: "+"
pooled_cpm: 51.15
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 42
n_dd_up_clean: 0
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PDXDC2P

*pyridoxal dependent decarboxylase domain containing 2, pseudogene* — 16q22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (16 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.357× (z -13.2, q 4e-37, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC1]] (+0.96, fdr 7e-06), [[PDXDC2P-NPIPB14P]] (+0.92, fdr 7e-06, ⚠ same locus), [[COG6]] (+0.82, fdr 7e-06), [[NDEL1]] (+0.80, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.357×** | -13.2 | 4e-37 | 45/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.365×** | -12.9 | 1e-35 | 36/46 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.401×** | -11.3 | 4e-27 | 33/37 (A498, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.426×** | -10.5 | 1e-23 | 39/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.447×** | -10.3 | 6e-23 | 35/47 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.571×** | -10.1 | 3e-22 | 33/47 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.425×** | -10.1 | 3e-22 | 31/40 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.505×** | -8.8 | 1e-16 | 40/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.640×** | -8.1 | 4e-14 | 43/48 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.558×** | -7.5 | 4e-12 | 36/46 (KATO III, A-172, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -7.4 | 7e-12 | 27/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -7.0 | 9e-11 | 33/46 (HOP62, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.568×** | -7.0 | 1e-10 | 35/48 (hTERT-HPNE, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.703×** | -6.4 | 8e-09 | 36/48 (RPMI-7951, hTERT-HPNE, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.621×** | -6.1 | 4e-08 | 29/48 (HS-578T, A498, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.752×** | -5.1 | 9e-06 | 30/48 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -5.0 | 1e-05 | 31/48 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.661×** | -4.9 | 3e-05 | 32/47 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.580×** | -3.6 | 0.006 | 23/47 (RKO, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.755×** | -3.6 | 0.007 | 22/48 (LS 180, NCI-H23, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.008 | 24/48 (HOP62, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 68.6 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.155× (z -14.2) |
| [[A498 (line)]] | wt | 118 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -18.2) |
| [[HOP62 (line)]] | alt | 76.1 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.149× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 63.9 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0442× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.108× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 46.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.3) |
| [[HT-29 (line)]] | alt | 83.3 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.3) |
| [[A-172 (line)]] | wt | 48.4 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.217× (z -12.5) |
| [[KATO III (line)]] | alt | 90.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.4) |
| [[LoVo (line)]] | wt | 81.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.249× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 73.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.5) |
| [[H4 (line)]] | wt | 80.3 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -10.2) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.205× (z -9.7) |
| [[J82 (line)]] | alt | 42.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 49.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 43.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -23.2) |
| [[SW480 (line)]] | alt | 68.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 34.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.176× (z -9.9) |
| [[COLO 205 (line)]] | alt | 96.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.224× (z -10.0) |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -10.4) |
| [[LS 180 (line)]] | wt | 66.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 58.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.291× (z -9.5) |
| [[RKO (line)]] | wt | 36.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.9) |
| [[SW 900 (line)]] | alt | 50.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.244× (z -9.2) |
| [[SW1417 (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 32.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.264× (z -9.6) |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0997× (z -8.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0913× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0465× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1088 (line)]] | alt | 92.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.7) |
| [[SW48 (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC1]] | +0.96 | +0.95 / +0.95 | both halves | 7e-06 | **novel candidate** |
| [[PDXDC2P-NPIPB14P]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[COG6]] | +0.82 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.80 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.80 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[COPA]] | +0.78 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.77 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.77 | +0.81 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PDXDC2P's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.1% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CREB3L1]] | B | CREB3L1 activity raises PDXDC2P's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without CREB3L1 | 0.048 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[GALNT3]] | B | GALNT3 activity raises PDXDC2P's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.58× lower at baseline in the lines without GALNT3 | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[CREB3L1]] | B | CREB3L1 activity strengthens PDXDC2P's drug response | lines that do not express CREB3L1 (24) vs lines expressing it (25) | the lines without CREB3L1 respond 0.74× as strongly (z diff +1.90); strongest at Homoharringtonine 0.5 µM: 0.53x vs 0.34x (z diff +3.4) | 0.059 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; artifact flags |
| [[PLPP4]] | B | PLPP4 activity raises PDXDC2P's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.06× lower at baseline in the lines without PLPP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[TTC28]] | B | TTC28 activity lowers PDXDC2P's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.66× higher at baseline in the lines without TTC28 | 0.096 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -33.4); signed map (-50.0, 10.2). **Vector** length 115, 38.4% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.69 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.69 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.69 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.2 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.8 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.8 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -2.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.8 | -13.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.7 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -10.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | pyridoxal dependent decarboxylase domain containing 2, pseudogene |
| Locus type | pseudogene |
| Location | 16q22.1 — chr16:70,010,751-70,065,776 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZp761H1120; previously PDXDC2 |
| Matched by | ensembl_id |

UniProt [Q6P474](https://www.uniprot.org/uniprotkb/Q6P474) carries no function annotation.

**Summary**, from NCBI Gene [109731405](https://www.ncbi.nlm.nih.gov/gene/109731405):

> Predicted to enable carboxy-lyase activity and pyridoxal phosphate binding activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27559) · Entrez [109731405](https://www.ncbi.nlm.nih.gov/gene/109731405) · UniProt [Q6P474](https://www.uniprot.org/uniprotkb/Q6P474) · Ensembl [ENSG00000255185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255185)

## Data

Gene col 14924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14924); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14924]; `tensor/DDL_lfc|DDL_z.npy` [14924]; `embed/gene_vectors.npy` [14924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14924 or target_col == 14924). Every well: [[PDXDC2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDXDC2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
