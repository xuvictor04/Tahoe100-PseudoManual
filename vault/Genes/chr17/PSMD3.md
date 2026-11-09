---
symbol: "PSMD3"
type: "gene"
col: 2934
ensembl_id: "ENSG00000108344"
name: "proteasome 26S subunit, non-ATPase 3"
location: "17q21.1"
module: 64
arm: "+"
pooled_cpm: 55.24
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMD3

*proteasome 26S subunit, non-ATPase 3* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.66× (z +14.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.762× (z -4.1, q 0.020, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.344×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change); [[Rapamycin (drug)]] 0.5 µM in 1 line (SW 1271 0.0531×); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 0.439×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMT1]] (+0.68, fdr 7e-06), [[BRF2]] (+0.67, fdr 7e-06), [[ZNF761]] (+0.67, fdr 7e-06); moves opposite to [[CDC14A]] (-0.61, fdr 3e-05), [[PIGX]] (-0.59, fdr 3e-05), [[TAPT1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.66×** | +14.9 | 0e+00 | 47/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.47×** | +13.8 | 9e-41 | 46/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.60×** | +13.7 | 1e-40 | 48/48 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.05×** | +10.9 | 1e-25 | 45/47 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.01×** | +10.7 | 2e-24 | 46/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.86×** | +9.4 | 4e-19 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +9.2 | 2e-18 | 42/48 (C32, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.86×** | +9.1 | 5e-18 | 31/43 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.69×** | +8.0 | 7e-14 | 45/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.9 | 3e-10 | 38/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.53×** | +6.5 | 4e-09 | 36/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.3 | 1e-08 | 34/48 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.50×** | +5.7 | 5e-07 | 30/43 (A-427, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 8e-07 | 34/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.44×** | +5.3 | 3e-06 | 36/48 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 4e-04 | 31/48 (NCI-H1573, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.009 | 24/48 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.015 | 18/47 (NCI-H2030, SNU-423, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.034 | 21/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.043 | 16/48 (HepG2/C3A, BT-474, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.052 | 19/48 (Hs 766T, SK-MEL-2, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.36×** | +2.8 | 0.091 | 14/48 (LoVo, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2934.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.344×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change); [[Rapamycin (drug)]] 0.5 µM in 1 line (SW 1271 0.0531×); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 0.439×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.762×** | -4.1 | 0.020 | 31/48 (MIA PaCa-2, SW480, …) | all doses, flat | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.798× | -3.3 | 0.27 | 19/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.858× | -3.1 | 0.37 | 13/48 (SW480, SW 900, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 50.5 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 375 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.38× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.344× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 58.5 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 58.4 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.81× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 46.1 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.05× (z +11.6) | — |
| [[SW480 (line)]] | alt | 52.2 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.86× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 30.7 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 4.57× (z +10.1) | — |
| [[A498 (line)]] | wt | 65.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.35× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 41.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.73× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 50.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.33× (z +11.0) | — |
| [[KATO III (line)]] | alt | 88.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +10.3) | — |
| [[LoVo (line)]] | wt | 45.8 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.11× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 39.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.76× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 34.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.46× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 43.4 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.29× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 56.9 | 3 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.19× (z +9.2) | — |
| [[A549 (line)]] | wt | 44.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.92× (z +8.5) | — |
| [[C32 (line)]] | wt | 31.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.93× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 55.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.91× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 87.2 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.72× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 40.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.03× (z +9.1) | — |
| [[A-427 (line)]] | wt | 84.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.19× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[H4 (line)]] | wt | 63.5 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.36× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.8 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.78× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 48.4 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0531× (z -10.4) |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMT1]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Apoptosis |
| [[BRF2]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ZNF761]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[NSFL1C]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SAMD4B]] | +0.65 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CYB5R1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[AARS2]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[TMEM161A]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[PSMB1]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[TANGO2]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC14A]] | -0.61 | -0.56 / -0.45 | both halves | 3e-05 | pathway: APC/C-mediated degradation of cell cycle proteins |
| [[PIGX]] | -0.59 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TAPT1]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[NFKBID]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CMC4]] | -0.54 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[LHFPL6]] | -0.53 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[LINC00938]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[RNF170]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-42.0, -4.6); signed map (-23.6, -23.1). **Vector** length 86.1, 24.1% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.3 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.0 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +14.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.2 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -9.8 | -0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -2.9 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | -2.5 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:39,980,807-39,997,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S3, P58, Rpn3; previously TSTA2 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [O43242](https://www.uniprot.org/uniprotkb/O43242) (26S proteasome non-ATPase regulatory subunit 3):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [5709](https://www.ncbi.nlm.nih.gov/gene/5709):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9560) · Entrez [5709](https://www.ncbi.nlm.nih.gov/gene/5709) · UniProt [O43242](https://www.uniprot.org/uniprotkb/O43242) · Ensembl [ENSG00000108344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108344)

## Data

Gene col 2934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2934); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2934]; `tensor/DDL_lfc|DDL_z.npy` [2934]; `embed/gene_vectors.npy` [2934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2934 or target_col == 2934). Every well: [[PSMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
