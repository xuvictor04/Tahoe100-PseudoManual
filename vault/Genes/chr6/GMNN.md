---
symbol: "GMNN"
type: "gene"
col: 3356
ensembl_id: "ENSG00000112312"
name: "geminin DNA replication inhibitor"
location: "6p22.3"
module: 67
arm: "+"
pooled_cpm: 27.23
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# GMNN

*geminin DNA replication inhibitor* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (23 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.52× (z +10.6, q 2e-23, up in 39 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.33× (z +3.3, q 0.029, up in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 6 lines (PANC-1 4.23×, LS 180 4.89×, J82 3.43×, SHP-77 3.44×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (LS 180 4.83×, J82 3.34×, SHP-77 3.55×, PANC-1 3.27×; ⚠ cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 4.31×, RKO 3.95×, J82 2.30×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.631× (z -5.3, q 8e-05, down in 30 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.298×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.246×; ⚠ cell-cycle shift, would explain all of this change); [[vincristine (drug)]] 0.5 µM in 1 line (COLO 205 0.0657×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBL1]] (+0.77, fdr 7e-06), [[UBE2T]] (+0.76, fdr 7e-06), [[CENPM]] (+0.73, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 23 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 6 lines (PANC-1 4.23×, LS 180 4.89×, J82 3.43×, SHP-77 3.44×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (LS 180 4.83×, J82 3.34×, SHP-77 3.55×, PANC-1 3.27×; ⚠ cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 4.31×, RKO 3.95×, J82 2.30×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.52×** | +10.6 | 2e-23 | 39/46 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.15×** | +8.7 | 7e-16 | 42/47 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.07×** | +8.3 | 2e-14 | 33/47 (LS 180, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **2.03×** | +8.1 | 9e-14 | 41/46 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.99×** | +7.9 | 4e-13 | 38/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.89×** | +7.0 | 2e-10 | 33/47 (J82, SW1417, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.49×** | +6.5 | 6e-09 | 26/47 (SW1417, RKO, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **1.73×** | +6.1 | 9e-08 | 35/46 (LoVo, SNU-423, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.69×** | +5.7 | 6e-07 | 30/45 (SW480, J82, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.61×** | +5.5 | 3e-06 | 30/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.54×** | +4.9 | 4e-05 | 24/42 (A498, NCI-H1792, …) | two highest doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.34×** | +4.8 | 8e-05 | 27/47 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.49×** | +4.6 | 2e-04 | 23/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +4.5 | 3e-04 | 29/46 (J82, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.43×** | +4.1 | 0.001 | 23/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.029 | 19/47 (HOP62, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.298×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.246×; ⚠ cell-cycle shift, would explain all of this change); [[vincristine (drug)]] 0.5 µM in 1 line (COLO 205 0.0657×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -5.3 | 8e-05 | 30/46 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.765×** | -4.3 | 0.004 | 28/47 (RKO, SW480, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.546×** | -3.6 | 0.054 | 19/47 (HOP62, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.739× | -3.3 | 0.15 | 20/47 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.664× | -3.1 | 0.18 | 16/47 (KATO III, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Dabrafenib (drug)]] 5 µM |  | 0.597× | -3.1 | 0.18 | 9/47 (CFPAC-1, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.601× | -3.0 | 0.18 | 15/47 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.671× | -3.0 | 0.18 | 12/47 (NCI-H23, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 96.1 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[A-427 (line)]] | wt | 34.8 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.298× (z -11.2) |
| [[KATO III (line)]] | alt | 34.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.49× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[LS 180 (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.89× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.28× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[PANC-1 (line)]] | alt | 28.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.23× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SHP-77 (line)]] | alt | 56.5 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +9.8) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[SW480 (line)]] | alt | 35.7 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.10× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0657× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.177× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBL1]] | +0.77 | +0.68 / +0.77 | both halves | 7e-06 | pathway: G1/S Transition |
| [[UBE2T]] | +0.76 | +0.62 / +0.79 | both halves | 7e-06 | STRING 693 |
| [[CENPM]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ATAD2]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 | STRING 530 |
| [[BARD1]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SKA3]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[CENPW]] | +0.72 | +0.57 / +0.70 | both halves | 1e-05 | STRING 632 |
| [[BLM]] | +0.71 | +0.59 / +0.73 | both halves | 7e-06 | STRING 447 |
| [[NCAPH]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[PLK4]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[SLF1]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SPC24]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises GMNN's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without CDC25A | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises GMNN's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without E2F2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[PBK]] | C | PBK activity raises GMNN's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without PBK | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises GMNN's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises GMNN's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without MCM10 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises GMNN's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.76× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises GMNN's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 2.43× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PKMYT1]] | C | PKMYT1 activity raises GMNN's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without PKMYT1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.6, -51.3); signed map (-43.8, -39.6). **Vector** length 108, 31.7% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 12); *G2/M checkpoint* (hallmark, mean cos +0.59 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | +4.3 | +6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +4.1 | +10.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +3.2 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.1 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.0 | +8.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.1 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.5 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.4 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | geminin DNA replication inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,774,931-24,786,099 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Gem |
| Reactome | 15 pathways, smallest: Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis; Activation of the pre-replicative complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O75496](https://www.uniprot.org/uniprotkb/O75496) (Geminin):

> Inhibits DNA replication by preventing the incorporation of MCM complex into pre-replication complex (pre-RC). It is degraded during the mitotic phase of the cell cycle. Its destruction at the metaphase-anaphase transition permits replication in the succeeding cell cycle. Inhibits histone acetyltransferase activity of KAT7/HBO1 in a CDT1-dependent manner, inhibiting histone H4 acetylation and DNA replication licensing. Inhibits the transcriptional activity of a subset of Hox proteins, enrolling …

**Summary**, from NCBI Gene [51053](https://www.ncbi.nlm.nih.gov/gene/51053):

> This gene encodes a protein that plays a critical role in cell cycle regulation. The encoded protein inhibits DNA replication by binding to DNA replication factor Cdt1, preventing the incorporation of minichromosome maintenance proteins into the pre-replication complex. The encoded protein is expressed during the S and G2 phases of the cell cycle and is degraded by the anaphase-promoting complex during the metaphase-anaphase transition. Increased expression of this gene may play a role in …

**Accessions** — [HGNC:17493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17493) · Entrez [51053](https://www.ncbi.nlm.nih.gov/gene/51053) · UniProt [O75496](https://www.uniprot.org/uniprotkb/O75496) · Ensembl [ENSG00000112312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112312)

## Data

Gene col 3356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3356); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3356]; `tensor/DDL_lfc|DDL_z.npy` [3356]; `embed/gene_vectors.npy` [3356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3356 or target_col == 3356). Every well: [[GMNN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMNN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
