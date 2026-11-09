---
symbol: "PTPN4"
type: "gene"
col: 1521
ensembl_id: "ENSG00000088179"
name: "protein tyrosine phosphatase non-receptor type 4"
location: "2q14.2"
module: 18
arm: "+"
pooled_cpm: 88.78
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PTPN4

*protein tyrosine phosphatase non-receptor type 4* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.53× (z +7.5, q 3e-11, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.534× (z -10.7, q 4e-24, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -8.2, q 6e-14, down in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW48 0.0583×, NCI-H23 0.116×, SW1417 0.174×, LS 180 0.178×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 5 lines (SW480 0.364×, SK-MEL-2 0.379×, A-427 0.477×, SHP-77 0.444×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LOX-IMVI 0.476×, PANC-1 0.547×, NCI-H2030 0.416×, NCI-H23 0.600×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.399×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA8]] (+0.71, fdr 7e-06), [[CDIN1]] (+0.65, fdr 1e-05), [[ME1]] (+0.61, fdr 1e-05); moves opposite to [[LINC01128]] (-0.56, fdr 1e-05), [[ARHGAP1]] (-0.50, fdr 3e-05), [[PPP1R13L]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +7.5 | 3e-11 | 44/48 (A-172, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +6.5 | 2e-08 | 37/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.19× | +4.5 | 0.002 | 21/48 (J82, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.011 | 28/48 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +3.6 | 0.029 | 23/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.6 | 0.029 | 23/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.037 | 23/47 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.037 | 23/48 (J82, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.064 | 13/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.093 | 18/48 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.41×** | +3.1 | 0.093 | 18/44 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.093 | 18/48 (NCI-H2347, CFPAC-1, …) | top dose only | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.13× | +3.1 | 0.093 | 9/48 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.094 | 10/48 (C32, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW48 0.0583×, NCI-H23 0.116×, SW1417 0.174×, LS 180 0.178×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 5 lines (SW480 0.364×, SK-MEL-2 0.379×, A-427 0.477×, SHP-77 0.444×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LOX-IMVI 0.476×, PANC-1 0.547×, NCI-H2030 0.416×, NCI-H23 0.600×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.399×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -10.7 | 4e-24 | 35/44 (SW48, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.531×** | -10.6 | 6e-24 | 35/49 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -8.2 | 6e-14 | 37/49 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.610×** | -8.1 | 6e-14 | 30/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.674×** | -7.0 | 3e-10 | 29/47 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -6.2 | 5e-08 | 30/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.730×** | -5.3 | 9e-06 | 32/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.757×** | -5.0 | 5e-05 | 26/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.765×** | -4.8 | 1e-04 | 26/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.799×** | -3.9 | 0.007 | 23/47 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~78% of this change | **0.818×** | -3.6 | 0.017 | 26/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -3.1 | 0.11 | 21/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.845× | -3.0 | 0.11 | 19/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 124 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 94.0 | 0 | 8 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -11.1) |
| [[LS 180 (line)]] | wt | 175 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 6 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 112 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -13.7) |
| [[LoVo (line)]] | wt | 151 | 1 (1 ⚠) | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.18× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -12.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 83.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 100 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 138 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -8.7) |
| [[C-33 A (line)]] | alt | 158 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.399× (z -9.5) |
| [[SNU-1 (line)]] | wt | 104 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 140 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0583× (z -24.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -13.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 62.7 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -10.1) ⚠ toxic |
| [[RKO (line)]] | wt | 82.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -14.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 87.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.379× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 95.9 | 1 | 1 (1 ⚠) | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 3.05× (z +8.9) | [[Pentoxifylline (drug)]] 0.05 µM 0.217× (z -12.2) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 97.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -8.6) |
| [[SW1417 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -20.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 50.7 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 2.50× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0924× (z -9.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 76.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 95.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -12.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 86.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.152× (z -8.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 34.5 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.299× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 89.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW 900 (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.136× (z -10.1) ⚠ toxic |
| [[A549 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA8]] | +0.71 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[ME1]] | +0.61 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[IDE]] | +0.60 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[CLASP2]] | +0.59 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[PIR]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LRRC8D]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TTC39C]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[DENND1B]] | +0.57 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MRTFB]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01128]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ARHGAP1]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R13L]] | -0.50 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SLC35F5]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TRIOBP]] | -0.48 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ELL]] | -0.46 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[FBXL12]] | -0.46 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MXRA7]] | -0.46 | -0.45 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity raises PTPN4's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without NFIA | 0.003 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[KLHL13]] | B | KLHL13 activity raises PTPN4's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without KLHL13 | 0.027 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[PIR]] | B | PIR activity raises PTPN4's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without PIR | 0.074 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.5, -34.3); signed map (-13.2, -51.1). **Vector** length 113, 34.2% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.4 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.0 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:119,759,922-119,984,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPMEG |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type; PDZ domain containing; FERM domain containing |
| Reactome | 9 pathways, smallest: MECP2 regulates neuronal receptors and channels; Interleukin-37 signaling; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P29074](https://www.uniprot.org/uniprotkb/P29074) (Tyrosine-protein phosphatase non-receptor type 4):

> Phosphatase that plays a role in immunity, learning, synaptic plasticity or cell homeostasis. Regulates neuronal cell homeostasis by protecting neurons against apoptosis. Negatively regulates TLR4-induced interferon beta production by dephosphorylating adapter TICAM2 and inhibiting subsequent TRAM-TRIF interaction. Also dephosphorylates the immunoreceptor tyrosine-based activation motifs/ITAMs of the TCR zeta subunit and thereby negatively regulates TCR-mediated signaling pathway (By …

**Summary**, from NCBI Gene [5775](https://www.ncbi.nlm.nih.gov/gene/5775):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This protein contains a C-terminal PTP domain and an N-terminal domain homologous to the band 4.1 superfamily of cytoskeletal-associated proteins. This PTP has been shown to interact with glutamate receptor delta 2 and epsilon …

**Accessions** — [HGNC:9656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9656) · Entrez [5775](https://www.ncbi.nlm.nih.gov/gene/5775) · UniProt [P29074](https://www.uniprot.org/uniprotkb/P29074) · Ensembl [ENSG00000088179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088179)

## Data

Gene col 1521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1521); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1521]; `tensor/DDL_lfc|DDL_z.npy` [1521]; `embed/gene_vectors.npy` [1521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1521 or target_col == 1521). Every well: [[PTPN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
