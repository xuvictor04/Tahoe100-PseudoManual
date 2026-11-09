---
symbol: "TTN-AS1"
type: "gene"
col: 14125
ensembl_id: "ENSG00000237298"
name: "TTN antisense RNA 1"
location: "2q31.2"
module: 39
arm: "+"
pooled_cpm: 50.83
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TTN-AS1

*TTN antisense RNA 1* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +6.4, q 1e-07, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.388× (z -10.4, q 2e-22, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.802× (z -3.4, q 0.028, down in 25 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 0.0765×, NCI-H23 0.116×, SK-MEL-2 0.118×, CFPAC-1 0.223×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SNU-1 0.0547×, COLO 205 0.129×, MIA PaCa-2 0.109×, CFPAC-1 0.170×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 0.121×, LS 180 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.288×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.0765×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC1P4]] (+0.64, fdr 1e-05), [[LINC00907]] (+0.60, fdr 1e-05), [[ESRRB]] (+0.59, fdr 7e-06); moves opposite to [[SLC35D1]] (-0.54, fdr 3e-05), [[SEC61A2]] (-0.53, fdr 4e-05), [[PLPP1]] (-0.53, fdr 2e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +6.4 | 1e-07 | 35/43 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +5.5 | 1e-05 | 34/43 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.2 | 3e-05 | 34/42 (LoVo, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +4.6 | 5e-04 | 25/42 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.001 | 24/43 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.26×** | +3.5 | 0.037 | 25/43 (AsPC-1, LS 180, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.33× | +3.0 | 0.21 | 20/42 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14125.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 0.0765×, NCI-H23 0.116×, SK-MEL-2 0.118×, CFPAC-1 0.223×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SNU-1 0.0547×, COLO 205 0.129×, MIA PaCa-2 0.109×, CFPAC-1 0.170×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 0.121×, LS 180 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.288×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.0765×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.388×** | -10.4 | 2e-22 | 36/43 (KATO III, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.501×** | -7.6 | 9e-12 | 32/42 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.525×** | -6.5 | 1e-08 | 25/39 (CFPAC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -5.9 | 4e-07 | 34/42 (SNU-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.577×** | -5.8 | 7e-07 | 22/37 (NCI-H1792, LS 180, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.603×** | -5.6 | 3e-06 | 30/43 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.617×** | -5.1 | 3e-05 | 28/42 (RPMI-7951, COLO 205, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.635×** | -5.0 | 4e-05 | 32/42 (A-172, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.680×** | -4.1 | 0.003 | 23/43 (CFPAC-1, AN3 CA, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.699×** | -3.9 | 0.005 | 24/42 (SW480, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.717×** | -3.7 | 0.013 | 23/42 (SW480, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.802×** | -3.4 | 0.028 | 25/43 (CHP-212, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.758× | -3.0 | 0.10 | 22/43 (A-172, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 97.5 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.1) |
| [[SW480 (line)]] | alt | 87.7 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 75.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -15.2) ⚠ toxic |
| [[J82 (line)]] | alt | 49.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 25.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -18.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 71.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.23× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -14.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 48.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 65.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -11.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 42.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -16.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 57.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0547× (z -16.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 105 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0765× (z -13.1) |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0795× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.357× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -9.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -10.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC1P4]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[LINC00907]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ESRRB]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PHEX]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[XRCC4]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[LINC01031]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[LRGUK]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CDRT4]] | +0.57 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[UTP11]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ALDH8A1]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CLTC]] | +0.55 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[SCUBE2]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35D1]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SEC61A2]] | -0.53 | -0.61 / -0.43 | both halves | 4e-05 |  |
| [[PLPP1]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[CNNM2]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZNRF2P2]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D12]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LRP5L]] | -0.51 | -0.74 / -0.23 | both halves | 5e-04 |  |
| [[ZNF592]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[FAM76A]] | -0.50 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[PPM1D]] | -0.49 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[TAPT1]] | -0.49 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[RNF138]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TTN-AS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR4435-2HG]] | C | MIR4435-2HG activity raises TTN-AS1's level | lines that do not express MIR4435-2HG (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without MIR4435-2HG | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SLC26A2, EML6, ANAPC1P4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, -8.8); signed map (22.8, 3.7). **Vector** length 72.6, 16.5% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +3.5 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.9 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.3 | -7.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | TTN antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.2 — chr2:178,521,183-178,779,963 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100506866](https://www.ncbi.nlm.nih.gov/gene/100506866):

> This gene encodes a non-coding RNA transcribed from the opposite strand to the titin gene. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:44124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44124) · Entrez [100506866](https://www.ncbi.nlm.nih.gov/gene/100506866) · Ensembl [ENSG00000237298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237298)

## Data

Gene col 14125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14125); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14125]; `tensor/DDL_lfc|DDL_z.npy` [14125]; `embed/gene_vectors.npy` [14125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14125 or target_col == 14125). Every well: [[TTN-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTN-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
