---
symbol: "DONSON"
type: "gene"
col: 8221
ensembl_id: "ENSG00000159147"
name: "DNA replication fork stabilization factor DONSON"
location: "21q22.11"
module: 71
arm: "+"
pooled_cpm: 29.92
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DONSON

*DNA replication fork stabilization factor DONSON* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +16.1, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.783× (z -5.5, q 2e-05, down in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.801× (z -4.9, q 1e-04, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.151×, C-33 A 0.235×, A-172 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.0803×, A-172 0.409×; ⚠ cell-cycle shift, explains ~30% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.398×, A-172 0.539×; ⚠ cell-cycle shift, explains ~23% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.137×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0942×); [[Brimonidine (drug)]] 0.5 µM in 1 line (BT-474 0.282×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCLAF]] (+0.67, fdr 7e-06), [[DYRK4]] (+0.66, fdr 7e-06), [[DSN1]] (+0.66, fdr 7e-06); moves opposite to [[N6AMT1]] (-0.57, fdr 2e-05), [[ZNF780A]] (-0.56, fdr 1e-05), [[ZNF502]] (-0.55, fdr 2e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RHBDL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +16.1 | 0e+00 | 40/48 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.46×** | +8.2 | 1e-13 | 29/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.41×** | +7.4 | 3e-11 | 26/46 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.36×** | +6.8 | 1e-09 | 25/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.36×** | +6.6 | 6e-09 | 25/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.31×** | +6.1 | 1e-07 | 21/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.31×** | +6.0 | 1e-07 | 18/42 (SNU-423, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.29×** | +5.5 | 3e-06 | 23/47 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.27×** | +5.4 | 3e-06 | 20/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +5.0 | 3e-05 | 19/47 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +5.0 | 3e-05 | 19/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.3 | 9e-04 | 12/40 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.002 | 14/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.21×** | +4.0 | 0.002 | 16/42 (SNU-423, SHP-77, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | 1.19× | +4.0 | 0.002 | 13/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.011 | 12/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.037 | 1/48 (SW1417) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.038 | 7/46 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.053 | 4/48 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.10× | +2.9 | 0.073 | 5/48 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.088 | 1/48 (SNU-423) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8221.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.151×, C-33 A 0.235×, A-172 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.0803×, A-172 0.409×; ⚠ cell-cycle shift, explains ~30% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.398×, A-172 0.539×; ⚠ cell-cycle shift, explains ~23% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.137×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0942×); [[Brimonidine (drug)]] 0.5 µM in 1 line (BT-474 0.282×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.783×** | -5.5 | 2e-05 | 21/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.840× | -5.4 | 2e-05 | 20/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -4.9 | 1e-04 | 18/48 (A-172, NCI-H2347, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.643×** | -4.9 | 1e-04 | 21/47 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.870× | -4.3 | 0.002 | 14/48 (SNU-1, HCT15, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.861× | -3.3 | 0.065 | 12/48 (Panc 03.27, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.856× | -3.3 | 0.065 | 16/48 (BT-474, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -3.3 | 0.065 | 20/47 (HS-578T, HOP62, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.855× | -3.2 | 0.079 | 12/47 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.867× | -3.2 | 0.088 | 17/47 (A-427, A-172, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.088 | 5/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.864× | -3.1 | 0.10 | 8/48 (Panc 03.27, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 43.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0803× (z -24.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.137× (z -9.7) |
| [[A-172 (line)]] | wt | 65.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 30.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.282× (z -8.6) |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.5) | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0942× (z -8.6) |
| [[PANC-1 (line)]] | alt | 19.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.4) | — |
| [[SW480 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.73× (z +10.5) ⚠ toxic; cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCLAF]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[DYRK4]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DSN1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CMC2]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[LIN54]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CHAF1B]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 | STRING 664 |
| [[RAD54L]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[IFI27L1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PSMC3IP]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[CCNE2]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 | STRING 437 |
| [[C21orf58]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[CENPJ]] | +0.61 | +0.58 / +0.64 | both halves | 8e-06 | STRING 519 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N6AMT1]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 | STRING 524 |
| [[ZNF780A]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ZNF502]] | -0.55 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[CHURC1]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RAD50]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[RPL7L1]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[LDAH]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MGA]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RRP15]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ZNF480]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[BBS10]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHBDL3]] | B | RHBDL3 activity raises DONSON's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without RHBDL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DONSON's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.1, -49.0); signed map (-41.8, -41.0). **Vector** length 86.5, 17.5% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +16.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.7 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.4 | +8.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.6 | +3.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.5 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.1 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.3 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DNA replication fork stabilization factor DONSON |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,559,542-33,588,706 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B17, C2TA, DKFZP434M035; previously C21orf60 |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYP3](https://www.uniprot.org/uniprotkb/Q9NYP3) (Protein downstream neighbor of Son):

> Replisome component that maintains genome stability by protecting stalled or damaged replication forks. After the induction of replication stress, required for the stabilization of stalled replication forks, the efficient activation of the intra-S-phase and G/2M cell-cycle checkpoints and the maintenance of genome stability.

**Summary**, from NCBI Gene [29980](https://www.ncbi.nlm.nih.gov/gene/29980):

> This gene lies downstream of the SON gene and spans 10 kb on chromosome 21. The function of this gene is unknown. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2993) · Entrez [29980](https://www.ncbi.nlm.nih.gov/gene/29980) · UniProt [Q9NYP3](https://www.uniprot.org/uniprotkb/Q9NYP3) · Ensembl [ENSG00000159147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159147)

## Data

Gene col 8221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8221); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8221]; `tensor/DDL_lfc|DDL_z.npy` [8221]; `embed/gene_vectors.npy` [8221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8221 or target_col == 8221). Every well: [[DONSON — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DONSON.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
