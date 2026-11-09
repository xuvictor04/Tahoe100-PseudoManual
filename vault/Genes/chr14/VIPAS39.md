---
symbol: "VIPAS39"
type: "gene"
col: 7519
ensembl_id: "ENSG00000151445"
name: "VPS33B interacting protein, apical-basolateral polarity regulator, spe-39 homolog"
location: "14q24.3"
module: 72
arm: "+"
pooled_cpm: 15.06
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# VIPAS39

*VPS33B interacting protein, apical-basolateral polarity regulator, spe-39 homolog* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.72× (z +8.5, q 9e-15, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.425× (z -13.4, q 4e-38, down in 39 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.775× (z -5.7, q 1e-06, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 5 lines (SW480 0.142×, J82 0.0701×, RKO 0.0755×, NCI-H460 0.231×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW480 0.0959×, HS-578T 0.106×, LS 180 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.0639×, KATO III 0.111×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (A549 0.227×); [[ULK-101 (drug)]] 0.5 µM in 1 line (HCT15 0.0630×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS39]] (+0.70, fdr 7e-06), [[MRPL18]] (+0.69, fdr 7e-06), [[RTCA]] (+0.65, fdr 7e-06); moves opposite to [[STIM2]] (-0.59, fdr 1e-05), [[RELB]] (-0.56, fdr 1e-05), [[PSPC1]] (-0.56, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +8.5 | 9e-15 | 28/47 (LoVo, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.74×** | +8.2 | 6e-14 | 30/47 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.29×** | +5.6 | 3e-06 | 25/48 (RKO, A498, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.5 | 5e-06 | 21/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.8 | 2e-04 | 20/45 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 10/47 (A498, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 17/48 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +4.0 | 0.005 | 9/48 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.011 | 13/48 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.26×** | +3.7 | 0.015 | 19/47 (BT-474, A-427, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.6 | 0.020 | 1/48 (HOP62) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.021 | 7/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.025 | 7/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.041 | 17/46 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.086 | 12/48 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 13 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7519.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 5 lines (SW480 0.142×, J82 0.0701×, RKO 0.0755×, NCI-H460 0.231×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW480 0.0959×, HS-578T 0.106×, LS 180 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.0639×, KATO III 0.111×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (A549 0.227×); [[ULK-101 (drug)]] 0.5 µM in 1 line (HCT15 0.0630×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.425×** | -13.4 | 4e-38 | 39/46 (SW480, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.436×** | -13.0 | 4e-36 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.482×** | -11.0 | 9e-26 | 34/43 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.522×** | -10.2 | 4e-22 | 33/48 (SW480, CHP-212, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.531×** | -9.9 | 4e-21 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.654×** | -9.4 | 6e-19 | 29/47 (hTERT-HPNE, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.646×** | -6.9 | 6e-10 | 24/39 (LOX-IMVI, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -5.7 | 1e-06 | 26/48 (NCI-H23, CHP-212, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.704×** | -5.3 | 8e-06 | 24/47 (NCI-H460, NCI-H1792, …) | top dose only | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.707×** | -5.0 | 3e-05 | 20/36 (SW480, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.551×** | -4.9 | 6e-05 | 20/48 (A549, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.756×** | -4.2 | 0.001 | 16/27 (MIA PaCa-2, Hs 766T, …) | all doses, flat | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -4.2 | 0.001 | 20/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.804×** | -3.4 | 0.025 | 17/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 16.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0959× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.3) ⚠ cell-cycle shift, explains ~85% of this change |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0770× (z -10.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[ULK-101 (drug)]] 0.5 µM 0.0630× (z -9.3) |
| [[KATO III (line)]] | alt | 15.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0639× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.7) ⚠ cell-cycle shift, explains ~85% of this change |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.5) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A549 (line)]] | wt | 14.0 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.227× (z -9.4) |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -9.0) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.136× (z -9.0) |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HT-29 (line)]] | alt | 8.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 8.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0701× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[RKO (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0755× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -8.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 | STRING 755 |
| [[MRPL18]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RTCA]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SLC30A6]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.63 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PSMD13]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[COX15]] | +0.62 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ZNF343]] | +0.62 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[ALKBH6]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[RARS2]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GFM2]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIM2]] | -0.59 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[RELB]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PSPC1]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[H2AZ2]] | -0.53 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[POGZ]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HES1]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CEP83]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[EML4]] | -0.52 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PKP4]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SLC35B2]] | -0.51 | -0.58 / -0.22 | both halves | 6e-04 |  |
| [[SCLT1]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NR4A1]] | -0.50 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VIPAS39's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM171A1]] | B | FAM171A1 activity raises VIPAS39's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 1.24× lower at baseline in the lines without FAM171A1 | 0.096 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, -9.9); signed map (-25.2, -25.9). **Vector** length 82.0, 16.2% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.0 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.0 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +3.4 | +5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.7 | -13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -4.3 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.3 | -9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | VPS33B interacting protein, apical-basolateral polarity regulator, spe-39 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,426,675-77,457,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VIPAR, VPS16B, SPE-39, SPE39, hSPE-39; previously C14orf133 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9C1](https://www.uniprot.org/uniprotkb/Q9H9C1) (Spermatogenesis-defective protein 39 homolog):

> Proposed to be involved in endosomal maturation implicating in part VPS33B. In epithelial cells, the VPS33B:VIPAS39 complex may play a role in the apical RAB11A-dependent recycling pathway and in the maintenance of the apical-basolateral polarity. May play a role in lysosomal trafficking, probably via association with the core HOPS complex in a discrete population of endosomes; the functions seems to be independent of VPS33B. May play a role in vesicular trafficking during spermatogenesis (By …

**Summary**, from NCBI Gene [63894](https://www.ncbi.nlm.nih.gov/gene/63894):

> Involved in endosome to lysosome transport and intracellular protein transport. Acts upstream of or within collagen metabolic process and peptidyl-lysine hydroxylation. Located in Golgi apparatus and endosome. Implicated in arthrogryposis, renal dysfunction, and cholestasis 2. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20347) · Entrez [63894](https://www.ncbi.nlm.nih.gov/gene/63894) · UniProt [Q9H9C1](https://www.uniprot.org/uniprotkb/Q9H9C1) · Ensembl [ENSG00000151445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151445)

## Data

Gene col 7519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7519); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7519]; `tensor/DDL_lfc|DDL_z.npy` [7519]; `embed/gene_vectors.npy` [7519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7519 or target_col == 7519). Every well: [[VIPAS39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIPAS39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
