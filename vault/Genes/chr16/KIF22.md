---
symbol: "KIF22"
type: "gene"
col: 1261
ensembl_id: "ENSG00000079616"
name: "kinesin family member 22"
location: "16p11.2"
module: 67
arm: "+"
pooled_cpm: 32.7
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# KIF22

*kinesin family member 22* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.91× (z +9.5, q 1e-18, up in 39 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.59× (z +3.1, q 0.072, up in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.66×; ⚠ cell-cycle shift, explains ~90% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 2.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.607× (z -10.4, q 1e-22, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~79% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.688× (z -5.5, q 5e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AURKB]] (+0.92, fdr 7e-06), [[CDCA3]] (+0.91, fdr 7e-06), [[SPAG5]] (+0.90, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 15 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1261.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.66×; ⚠ cell-cycle shift, explains ~90% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 2.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.91×** | +9.5 | 1e-18 | 39/47 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.68×** | +7.6 | 7e-12 | 35/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **1.65×** | +7.4 | 4e-11 | 37/47 (PANC-1, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.53×** | +6.2 | 7e-08 | 27/45 (A-172, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.34×** | +5.6 | 2e-06 | 25/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~84% of this change | **1.42×** | +4.9 | 8e-05 | 27/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +4.7 | 2e-04 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.36×** | +4.5 | 4e-04 | 22/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +4.4 | 6e-04 | 25/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +4.4 | 6e-04 | 17/48 (PANC-1, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +4.1 | 0.002 | 22/41 (PANC-1, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +3.7 | 0.011 | 22/48 (SNU-423, NCI-H2030, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.28×** | +3.5 | 0.018 | 17/39 (A-172, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.69×** | +3.5 | 0.021 | 13/47 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.4 | 0.023 | 16/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.072 | 10/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.607×** | -10.4 | 1e-22 | 36/48 (A-427, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.571×** | -8.2 | 5e-14 | 38/48 (SNU-1, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.666×** | -6.0 | 4e-07 | 29/48 (KATO III, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.688×** | -5.5 | 5e-06 | 26/48 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.678×** | -5.4 | 7e-06 | 29/48 (AN3 CA, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -5.2 | 2e-05 | 31/48 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.790×** | -4.9 | 8e-05 | 27/48 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.756×** | -4.1 | 0.003 | 22/48 (HOP62, A498, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.678×** | -4.1 | 0.003 | 21/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.028 | 19/48 (A-172, HOP62, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.847× | -3.5 | 0.028 | 14/48 (Hs 766T, HOP62, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.4 | 0.035 | 21/48 (A-427, SNU-1, …) | all doses, flat | composition shift |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.742×** | -3.1 | 0.071 | 9/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | **0.623×** | -3.1 | 0.071 | 16/42 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.805×** | -3.1 | 0.077 | 14/47 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.078 | 12/47 (RKO, HEC-1-A, …) | two highest doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 39.5 | 0 | 6 (5 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.199× (z -12.7) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -8.7) |
| [[A-427 (line)]] | wt | 52.9 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -17.6) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -10.5) |
| [[A498 (line)]] | wt | 45.4 | 0 | 5 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.411× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.331× (z -10.3) |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -12.3) ⚠ cell-cycle shift, explains ~79% of this change |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0785× (z -12.1) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A549 (line)]] | wt | 29.3 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0796× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 33.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.153× (z -12.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[PANC-1 (line)]] | alt | 40.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.2) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0612× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~73% of this change |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.416× (z -8.7) ⚠ cell-cycle shift, explains ~79% of this change |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AURKB]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 666 |
| [[CDCA3]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 833 |
| [[SPAG5]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 629 |
| [[TACC3]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 892 |
| [[KIFC1]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 881 |
| [[KIF2C]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 916 |
| [[CDCA8]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 815 |
| [[CIT]] | +0.88 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SPC25]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 458 |
| [[KIF15]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 718 |
| [[RACGAP1]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 861 |
| [[GTSE1]] | +0.87 | +0.82 / +0.88 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KIF22's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without PIMREG | 0.057 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[LINC00520]] | B | LINC00520 activity lowers KIF22's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.36× higher at baseline in the lines without LINC00520 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[CDC20]] | C | CDC20 activity raises KIF22's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.932). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.5, -54.0); signed map (-47.4, -41.6). **Vector** length 125, 38.8% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.78 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.75 to 4); *Nucleosome assembly* (reactome, mean cos +0.75 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | +4.0 | +7.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.7 | +4.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +3.6 | +3.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.2 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +0.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -7.5 | -8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -7.1 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.5 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,790,727-29,805,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kid, OBP-1, OBP-2; previously KNSL4 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 13 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14807](https://www.uniprot.org/uniprotkb/Q14807) (Kinesin-like protein KIF22):

> Kinesin family member that is involved in spindle formation and the movements of chromosomes during mitosis and meiosis. Binds to microtubules and to DNA (By similarity). Plays a role in congression of laterally attached chromosomes in NDC80-depleted cells.

**Summary**, from NCBI Gene [3835](https://www.ncbi.nlm.nih.gov/gene/3835):

> The protein encoded by this gene is a member of the kinesin-like protein family. The family members are microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. The C-terminal half of this protein has been shown to bind DNA. Studies with the Xenopus homolog suggests its essential role in metaphase chromosome alignment and maintenance. Alternatively spliced transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:6391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6391) · Entrez [3835](https://www.ncbi.nlm.nih.gov/gene/3835) · UniProt [Q14807](https://www.uniprot.org/uniprotkb/Q14807) · Ensembl [ENSG00000079616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079616)

## Data

Gene col 1261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1261); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1261]; `tensor/DDL_lfc|DDL_z.npy` [1261]; `embed/gene_vectors.npy` [1261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1261 or target_col == 1261). Every well: [[KIF22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
