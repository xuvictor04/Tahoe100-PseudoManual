---
symbol: "KLC1"
type: "gene"
col: 4718
ensembl_id: "ENSG00000126214"
name: "kinesin light chain 1"
location: "14q32.33"
module: 2
arm: "+"
pooled_cpm: 210.48
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KLC1

*kinesin light chain 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.50× (z +8.7, q 1e-15, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.755× (z -5.9, q 2e-06, down in 29 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.830× (z -3.9, q 0.008, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.314×, A549 0.395×, HEC-1-A 0.478×, AsPC-1 0.441×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.257×, A-427 0.418×, NCI-H1573 0.386×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.464×, A549 0.471×; ⚠ cell-cycle shift, would explain all of this change); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (SW 1088 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB1BP1]] (+0.68, fdr 7e-06), [[CPNE2]] (+0.65, fdr 7e-06), [[RUBCN]] (+0.64, fdr 7e-06); moves opposite to [[ZNF608]] (-0.57, fdr 7e-06), [[MAP3K1]] (-0.56, fdr 1e-05), [[TIFA]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +8.7 | 1e-15 | 41/48 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +8.1 | 1e-13 | 43/48 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +7.2 | 8e-11 | 34/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 4e-10 | 36/48 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.8 | 2e-09 | 35/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 2e-09 | 37/48 (LoVo, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +5.1 | 2e-05 | 17/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.7 | 2e-04 | 29/48 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +4.1 | 0.003 | 23/47 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.7 | 0.011 | 20/48 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.015 | 20/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.5 | 0.019 | 20/47 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.022 | 20/48 (LoVo, SNU-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.049 | 19/47 (H4, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4718.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.314×, A549 0.395×, HEC-1-A 0.478×, AsPC-1 0.441×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.257×, A-427 0.418×, NCI-H1573 0.386×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.464×, A549 0.471×; ⚠ cell-cycle shift, would explain all of this change); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (SW 1088 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.755×** | -5.9 | 2e-06 | 29/44 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.774×** | -5.4 | 2e-05 | 31/48 (A-172, A549, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.795×** | -5.0 | 1e-04 | 29/49 (RKO, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.819×** | -4.1 | 0.007 | 23/45 (HEC-1-A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.835× | -3.9 | 0.008 | 21/48 (A549, PANC-1, …) | all doses, flat | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.008 | 23/48 (NCI-H1573, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | 0.843× | -3.6 | 0.025 | 21/47 (J82, MIA PaCa-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.731×** | -3.6 | 0.025 | 26/47 (AsPC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.4 | 0.035 | 12/48 (NCI-H2347, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.855× | -3.4 | 0.035 | 19/48 (RKO, A-172, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.866× | -3.0 | 0.12 | 13/48 (A549, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.907× | -3.0 | 0.12 | 1/48 (LS 180) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 258 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -16.4) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 105 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +10.5) | — |
| [[A-172 (line)]] | wt | 189 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -17.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 218 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.71× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LoVo (line)]] | wt | 200 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +9.1) | — |
| [[A-427 (line)]] | wt | 225 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[NCI-H1573 (line)]] | alt | 285 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HepG2_C3A (line)]] | wt | 142 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 126 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.86× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 253 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[LS 180 (line)]] | wt | 241 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +16.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 196 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.180× (z -8.8) |
| [[SW 1271 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.277× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 226 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 1.74× (z +8.6) | — |
| [[A498 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 225 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 219 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 198 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 175 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 215 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 181 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 375 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[CPNE2]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[RUBCN]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.62 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[RAB22A]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CCM2]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SVIL-AS1-1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[DIP2A]] | +0.59 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[WDR44]] | +0.59 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MICALL1]] | +0.58 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[UBE2F-SCLY]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TPD52L2]] | +0.57 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.57 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[MAP3K1]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TIFA]] | -0.55 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[TIPARP]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NCOA7]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EFNA1]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[C4orf33]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[IKBKE]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PDGFRL]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[REL]] | -0.49 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RSPH1]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MTUS1]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers KLC1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDGFRL]] | B | PDGFRL activity raises KLC1's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without PDGFRL | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2 |
| [[GPR161]] | B | GPR161 activity raises KLC1's level | lines that do not express GPR161 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without GPR161 | 0.095 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PPP2R3A, NKAIN1 |
| [[RSPH1]] | B | RSPH1 activity strengthens KLC1's drug response | lines that do not express RSPH1 (13) vs lines expressing it (36) | the lines without RSPH1 respond 0.86× as strongly (z diff +0.92); strongest at Ouabain (Octahydrate) 5 µM: 1.21x vs 1.45x (z diff +2.3) | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IKBKE]] | C | IKBKE activity raises KLC1's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.480). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-12.6, -0.3); signed map (-14.2, 17.4). **Vector** length 117, 38.5% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.2 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.5 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.5 | +5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.8 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -7.8 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | +0.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | -0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.2 | -3.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | kinesin light chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,561,896-103,714,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KNS2A, KLC, hKLC1S, hKLC1N, hKLC1P, hKLC1G, hKLC1R, hKLC1J; previously KNS2 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: RHO GTPases activate KTN1; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07866](https://www.uniprot.org/uniprotkb/Q07866) (Kinesin light chain 1):

> Kinesin is a microtubule-associated force-producing protein that may play a role in organelle transport. The light chain may function in coupling of cargo to the heavy chain or in the modulation of its ATPase activity (By similarity).

**Summary**, from NCBI Gene [3831](https://www.ncbi.nlm.nih.gov/gene/3831):

> Conventional kinesin is a tetrameric molecule composed of two heavy chains and two light chains, and transports various cargos along microtubules toward their plus ends. The heavy chains provide the motor activity, while the light chains bind to various cargos. This gene encodes a member of the kinesin light chain family. It associates with kinesin heavy chain through an N-terminal domain, and six tetratricopeptide repeat (TPR) motifs are thought to be involved in binding of cargos such as …

**Accessions** — [HGNC:6387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6387) · Entrez [3831](https://www.ncbi.nlm.nih.gov/gene/3831) · UniProt [Q07866](https://www.uniprot.org/uniprotkb/Q07866) · Ensembl [ENSG00000126214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126214)

## Data

Gene col 4718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4718); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4718]; `tensor/DDL_lfc|DDL_z.npy` [4718]; `embed/gene_vectors.npy` [4718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4718 or target_col == 4718). Every well: [[KLC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
