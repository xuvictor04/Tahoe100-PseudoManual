---
symbol: "MCM2"
type: "gene"
col: 1043
ensembl_id: "ENSG00000073111"
name: "minichromosome maintenance complex component 2"
location: "3q21.3"
module: 6
arm: "+"
pooled_cpm: 19.61
n_lines_expressing: 47
n_dd_up: 35
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM2

*minichromosome maintenance complex component 2* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (25 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.60× (z +15.8, q 0e+00, up in 34 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.63× (z +6.0, q 1e-07, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.765× (z -4.7, q 0.001, down in 23 of 45 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.801× (z -3.9, q 0.011, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM4]] (+0.89, fdr 7e-06), [[MCM5]] (+0.87, fdr 7e-06), [[MCM3]] (+0.87, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 8 go from it, the strongest it → [[GINS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **3.60×** | +15.8 | 0e+00 | 34/36 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **3.30×** | +14.1 | 5e-43 | 20/22 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.56×** | +10.7 | 1e-24 | 28/32 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.78×** | +6.8 | 1e-09 | 28/44 (J82, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.73×** | +6.7 | 2e-09 | 29/44 (J82, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.81×** | +6.7 | 3e-09 | 28/45 (J82, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.70×** | +6.3 | 2e-08 | 22/38 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 1e-07 | 25/44 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +6.0 | 2e-07 | 25/45 (A549, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.37×** | +5.5 | 2e-06 | 19/44 (J82, SHP-77, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **1.57×** | +5.3 | 6e-06 | 16/39 (A549, NCI-H1573, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.50×** | +5.0 | 3e-05 | 19/37 (BT-474, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.49×** | +4.9 | 4e-05 | 23/44 (A549, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.1 | 0.002 | 16/44 (H4, A549, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.24×** | +3.7 | 0.009 | 13/45 (HT-29, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.011 | 15/44 (J82, HS-578T, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.012 | 10/42 (J82, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.014 | 12/44 (A-427, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.015 | 12/41 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.026 | 10/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.026 | 4/43 (J82, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.052 | 5/44 (BT-474, J82, …) | inconsistent across doses | position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.057 | 4/45 (PANC-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.54×** | +2.8 | 0.085 | 4/40 (NCI-H2347, LS 180, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.765×** | -4.7 | 0.001 | 23/45 (RKO, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.695×** | -4.5 | 0.002 | 18/43 (LS 180, HOP62, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.715×** | -3.9 | 0.011 | 19/44 (A498, KATO III, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.643×** | -3.9 | 0.011 | 14/45 (COLO 205, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.801×** | -3.9 | 0.011 | 23/45 (Hs 766T, HCT15, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -3.8 | 0.012 | 18/45 (SW480, Panc 03.27, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.556×** | -3.8 | 0.012 | 10/45 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.739×** | -3.8 | 0.012 | 17/45 (COLO 205, A498, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.741×** | -3.7 | 0.012 | 15/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.733×** | -3.7 | 0.012 | 16/43 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.570×** | -3.6 | 0.014 | 11/44 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.038 | 12/45 (COLO 205, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.96 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 126 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +18.9) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A498 (line)]] | wt | 21.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.230× (z -9.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 17.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[A-172 (line)]] | wt | 21.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.277× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0520× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 5.59 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0518× (z -8.8) |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[LS 180 (line)]] | wt | 9.56 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.138× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -11.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SNU-1 (line)]] | wt | 9.77 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0618× (z -9.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[SW1417 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[SW480 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[A-427 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM4]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM5]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM3]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[CENPM]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 477 |
| [[ZWINT]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 446 |
| [[E2F2]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[E2F1]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 503 |
| [[MCM10]] | +0.83 | +0.81 / +0.85 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 997 |
| [[NCAPH2]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MYBL2]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 489 |
| [[CHEK1]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 870 |
| [[CDC45]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises MCM2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without CDC25A | 0.039 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises MCM2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without TCF19 | 0.059 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TP73]] | B | TP73 activity raises MCM2's level | lines that do not express TP73 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without TP73 | 0.075 | ⚠ within organs, on part of the lines; also absent: SPTB, PRR36, EMID1; maybe low, not absent |
| [[ZNF724]] | B | ZNF724 activity raises MCM2's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without ZNF724 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[SHMT1]] | C | SHMT1 activity raises MCM2's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.96× lower at baseline in the lines without SHMT1 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target |
| [[TP53]] | C | TP53 activity weakens MCM2's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 16 not recorded | the TP53-altered lines respond 1.25× as strongly (z diff -0.72); strongest at Topotecan (hydrochloride) 5 µM: 2.03x vs 1.03x (z diff -3.4) | 0.689 over the table, 0.043 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GINS1]] | C | MCM2 activity raises GINS1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.85× lower at baseline in the lines without MCM2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[SKA3]] | C | MCM2 activity raises SKA3's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without MCM2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[FOXM1]] | C | MCM2 activity raises FOXM1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without MCM2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[VRK1]] | C | MCM2 activity raises VRK1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without MCM2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[CENPH]] | C | MCM2 activity raises CENPH's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without MCM2 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent |
| [[PCNA]] | C | MCM2 activity raises PCNA's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without MCM2 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent |
| [[CLSPN]] | C | MCM2 activity raises CLSPN's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without MCM2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[BRCA1]] | C | MCM2 activity raises BRCA1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without MCM2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.855). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.0, -43.5); signed map (-37.0, -46.6). **Vector** length 115, 32.0% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homology Directed Repair* (reactome, mean cos +0.68 to 32); *Chromosome Maintenance* (reactome, mean cos +0.66 to 29); *HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA)* (reactome, mean cos +0.68 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +5.8 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +5.7 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +5.6 | +15.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | +4.0 | +6.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.9 | -3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.7 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:127,598,223-127,622,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D3S3194, KIAA0030, BM28, cdc19, DFNA70; previously CCNL1, CDCL1 |
| Gene groups (HGNC) | MCM family; minichromosome maintenance 2-7 complex |
| Hallmark sets | MTORC1_SIGNALING, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 20 pathways, smallest: Regulation of MITF-M-dependent genes involved in DNA replication, damage repair and senescence; Unwinding of DNA; Activation of the pre-replicative complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P49736](https://www.uniprot.org/uniprotkb/P49736) (DNA replication licensing factor MCM2):

> Acts as a component of the MCM2-7 complex (MCM complex) which is the replicative helicase essential for 'once per cell cycle' DNA replication initiation and elongation in eukaryotic cells. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built. The active ATPase sites in the MCM2-7 ring are formed through the interaction surfaces of two neighboring subunits such that a critical structure of a …

**Summary**, from NCBI Gene [4171](https://www.ncbi.nlm.nih.gov/gene/4171):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. This protein forms a complex with MCM4, 6, and 7, and has been shown to regulate the …

**Accessions** — [HGNC:6944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6944) · Entrez [4171](https://www.ncbi.nlm.nih.gov/gene/4171) · UniProt [P49736](https://www.uniprot.org/uniprotkb/P49736) · Ensembl [ENSG00000073111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073111)

## Data

Gene col 1043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1043); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1043]; `tensor/DDL_lfc|DDL_z.npy` [1043]; `embed/gene_vectors.npy` [1043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1043 or target_col == 1043). Every well: [[MCM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
