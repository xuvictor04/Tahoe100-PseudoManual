---
symbol: "UBE2C"
type: "gene"
col: 10556
ensembl_id: "ENSG00000175063"
name: "ubiquitin conjugating enzyme E2 C"
location: "20q13.12"
module: 22
arm: "+"
pooled_cpm: 44.44
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# UBE2C

*ubiquitin conjugating enzyme E2 C* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.86× (z +5.8, q 3e-06, up in 30 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 2.84×, NCI-H2030 2.59×, LOX-IMVI 3.12×, A549 2.82×, …; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 4.76×, NCI-H23 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 6.20×, NCI-H23 3.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.540× (z -8.1, q 3e-13, down in 34 of 46 measured lines) ⚠ cell-cycle shift, explains ~90% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -6.7, q 4e-09, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA8]] (+0.90, fdr 7e-06), [[KIF2C]] (+0.89, fdr 7e-06), [[RACGAP1]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 2.84×, NCI-H2030 2.59×, LOX-IMVI 3.12×, A549 2.82×, …; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 4.76×, NCI-H23 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 6.20×, NCI-H23 3.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.86×** | +5.8 | 3e-06 | 30/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.52×** | +5.5 | 9e-06 | 28/46 (PANC-1, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.76×** | +5.3 | 2e-05 | 36/46 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.72×** | +4.5 | 9e-04 | 29/45 (A-427, NCI-H23, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.4 | 0.001 | 29/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.37×** | +4.2 | 0.002 | 28/45 (C32, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.52×** | +3.8 | 0.012 | 24/46 (PANC-1, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.49×** | +3.7 | 0.014 | 23/46 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.45×** | +3.5 | 0.028 | 25/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~76% of this change | **1.45×** | +3.4 | 0.041 | 24/45 (NCI-H23, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.43×** | +3.4 | 0.041 | 19/46 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.540×** | -8.1 | 3e-13 | 34/46 (LOX-IMVI, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.461×** | -7.2 | 2e-10 | 39/46 (LS 180, H4, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -6.7 | 4e-09 | 33/45 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.501×** | -6.1 | 2e-07 | 35/46 (H4, HT-29, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -5.5 | 5e-06 | 28/46 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -5.3 | 1e-05 | 30/46 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.614×** | -4.5 | 5e-04 | 30/46 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.646×** | -4.1 | 0.004 | 28/46 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.651×** | -4.0 | 0.004 | 21/45 (H4, A498, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.651×** | -4.0 | 0.004 | 27/46 (HCT15, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.740×** | -3.9 | 0.004 | 26/46 (SW48, H4, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.752×** | -3.7 | 0.009 | 24/46 (HCT15, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.680×** | -3.6 | 0.015 | 25/46 (NCI-H2347, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.689×** | -3.5 | 0.022 | 24/46 (SNU-1, A-172, …) | two highest doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.495×** | -3.4 | 0.024 | 22/46 (NCI-H2347, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -3.1 | 0.054 | 21/46 (SW1417, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.717×** | -3.0 | 0.081 | 18/45 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +1.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 61.9 | 0 | 6 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0173× (z -16.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -13.6) |
| [[A-427 (line)]] | wt | 38.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Selinexor (drug)]] 5 µM 0.270× (z -11.3) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.298× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 31.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.0974× (z -18.0) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.165× (z -11.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[NCI-H23 (line)]] | alt | 59.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.54× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.430× (z -8.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A498 (line)]] | wt | 53.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -17.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A549 (line)]] | wt | 25.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.332× (z -9.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[KATO III (line)]] | alt | 37.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.76× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.164× (z -8.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H2030 (line)]] | alt | 83.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 97.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -8.8) |
| [[PANC-1 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.411× (z -8.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SW48 (line)]] | wt | 40.4 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.254× (z -9.6) |
| [[A-172 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA8]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 966 |
| [[KIF2C]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 954 |
| [[RACGAP1]] | +0.88 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 732 |
| [[CCNB2]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 968 |
| [[DLGAP5]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | STRING 968 |
| [[NDC80]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 870 |
| [[TOP2A]] | +0.87 | +0.87 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 973 |
| [[CCNB1]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 990 |
| [[BIRC5]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 992 |
| [[GTSE1]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 710 |
| [[KIF18A]] | +0.87 | +0.83 / +0.85 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 514 |
| [[CKAP2]] | +0.87 | +0.86 / +0.82 | both halves | 7e-06 | STRING 674 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises UBE2C's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without PIMREG | 0.087 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.900). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -56.7); signed map (-50.5, -42.8). **Vector** length 118, 39.4% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.68 to 48); *E2F targets* (hallmark, mean cos +0.68 to 46); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.72 to 33).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.5 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +3.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +3.4 | +5.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.2 | +1.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | -6.7 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -6.6 | -7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -6.3 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -3.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | -5.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,812,576-45,816,957 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBCH10 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 44 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [O00762](https://www.uniprot.org/uniprotkb/O00762) (Ubiquitin-conjugating enzyme E2 C):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-11'- and 'Lys-48'-linked polyubiquitination. Acts as an essential factor of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated ubiquitin ligase that controls progression through mitosis. Acts by initiating 'Lys-11'-linked polyubiquitin chains on APC/C substrates, leading to the degradation of APC/C substrates by the proteasome and promoting mitotic exit.

**Summary**, from NCBI Gene [11065](https://www.ncbi.nlm.nih.gov/gene/11065):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, ubiquitin-conjugating enzymes, and ubiquitin-protein ligases. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein is required for the destruction of mitotic cyclins and for cell cycle progression, and may be involved in …

**Accessions** — [HGNC:15937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15937) · Entrez [11065](https://www.ncbi.nlm.nih.gov/gene/11065) · UniProt [O00762](https://www.uniprot.org/uniprotkb/O00762) · Ensembl [ENSG00000175063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175063)

## Data

Gene col 10556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10556); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10556]; `tensor/DDL_lfc|DDL_z.npy` [10556]; `embed/gene_vectors.npy` [10556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10556 or target_col == 10556). Every well: [[UBE2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
