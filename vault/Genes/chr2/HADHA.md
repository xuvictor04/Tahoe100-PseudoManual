---
symbol: "HADHA"
type: "gene"
col: 1412
ensembl_id: "ENSG00000084754"
name: "hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit alpha"
location: "2p23.3"
module: 29
arm: "+"
pooled_cpm: 128.61
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# HADHA

*hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit alpha* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +16.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +9.9, q 1e-20, up in 44 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.141×; ⚠ toxic); [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0727×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CANX]] (+0.57, fdr 1e-05), [[LAMP2]] (+0.57, fdr 1e-05), [[TLN1]] (+0.56, fdr 7e-05); moves opposite to [[SNHG15]] (-0.62, fdr 1e-05), [[RRP1]] (-0.50, fdr 3e-05), [[SNHG17]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +16.9 | 0e+00 | 49/49 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +16.6 | 0e+00 | 41/44 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.9 | 1e-20 | 44/49 (SW1417, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.68×** | +8.2 | 3e-14 | 39/45 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.5 | 8e-09 | 35/50 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.0 | 1e-07 | 29/48 (SNU-423, SW 900, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.31×** | +4.9 | 9e-05 | 35/48 (LS 180, HT-29, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.7 | 2e-04 | 28/48 (SW1417, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 31/48 (HOP62, NCI-H2030, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.24×** | +3.8 | 0.007 | 29/48 (HT-29, LS 180, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.20×** | +3.3 | 0.052 | 22/48 (COLO 205, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.21×** | +3.2 | 0.057 | 20/48 (SW 900, PANC-1, …) | top dose only | composition shift |
| [[Thymol (drug)]] 5 µM |  | 1.13× | +3.2 | 0.059 | 1/48 (H4) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.19× | +3.1 | 0.077 | 21/48 (NCI-H1573, HT-29, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1412.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.141×; ⚠ toxic); [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0727×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.4 | 0.007 | 0/50 | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.829× | -3.4 | 0.20 | 25/49 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.829× | -3.0 | 0.51 | 22/48 (AN3 CA, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 171 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +16.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 97.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.4) | — |
| [[J82 (line)]] | alt | 77.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 104 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 115 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +12.0) | — |
| [[A-172 (line)]] | wt | 120 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +14.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 99.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.9) | — |
| [[KATO III (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 142 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 94.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.5) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.141× (z -12.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 114 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +12.5) | — |
| [[SW480 (line)]] | alt | 139 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +8.6) | — |
| [[A498 (line)]] | wt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +13.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +15.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.39× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 99.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +15.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +17.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +16.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 148 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +15.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +15.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +15.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 94.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 94.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +11.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 1 | — | [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM 0.0727× (z -10.1) |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 167 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 98.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CANX]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TLN1]] | +0.56 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[CPNE3]] | +0.55 | +0.46 / +0.58 | both halves | 2e-05 | pathway: Glycerophospholipid biosynthesis |
| [[GNS]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CUL4B]] | +0.54 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[LRP11]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[EIF2AK1]] | +0.53 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[YBX1]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[WNK1]] | +0.52 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[AIDA]] | +0.52 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[VPS35]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG15]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[RRP1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SNHG17]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[NSUN5]] | -0.50 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[TAF1A]] | -0.48 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[RBM14]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[EXOSC4]] | -0.47 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[CYB561D1]] | -0.47 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[AKIRIN2]] | -0.47 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[SRSF2]] | -0.47 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[YRDC]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[NSUN5P1-1]] | -0.46 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HADHA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TP53]] | C | TP53 activity weakens HADHA's drug response | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | the TP53-altered lines respond 1.13× as strongly (z diff -0.86); strongest at Idarubicin (hydrochloride) 5 µM: 1.54x vs 1.35x (z diff -2.4) | 0.763 over the table, 0.052 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.8, -19.4); signed map (-22.7, -32.1). **Vector** length 95.9, 26.2% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.5 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -0.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.9 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.7 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,190,635-26,244,672 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GBP, LCEH, LCHAD, MTPA |
| Gene groups (HGNC) | Enoyl-CoA hydratases; Oxidoreductases; Acyltransferases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: Beta oxidation of palmitoyl-CoA to myristoyl-CoA; Beta oxidation of lauroyl-CoA to decanoyl-CoA-CoA; Beta oxidation of hexanoyl-CoA to butanoyl-CoA |
| Matched by | ensembl_id |

**Function**, from UniProt [P40939](https://www.uniprot.org/uniprotkb/P40939) (Trifunctional enzyme subunit alpha, mitochondrial):

> Mitochondrial trifunctional enzyme catalyzes the last three of the four reactions of the mitochondrial beta-oxidation pathway. The mitochondrial beta-oxidation pathway is the major energy-producing process in tissues and is performed through cycles of four consecutive reactions. Each beta-oxidation cycle shortens the fatty acyl-CoA by two carbons, yielding one acetyl-CoA (for the citric acid cycle), one FADH(2), and one NADH (which donate electrons to the respiratory chain for ATP production). …

**Summary**, from NCBI Gene [3030](https://www.ncbi.nlm.nih.gov/gene/3030):

> This gene encodes the alpha subunit of the mitochondrial trifunctional protein, which catalyzes the last three steps of mitochondrial beta-oxidation of long chain fatty acids. The mitochondrial membrane-bound heterocomplex is composed of four alpha and four beta subunits, with the alpha subunit catalyzing the 3-hydroxyacyl-CoA dehydrogenase and enoyl-CoA hydratase activities. Mutations in this gene result in trifunctional protein deficiency or LCHAD deficiency. The genes of the alpha and beta …

**Accessions** — [HGNC:4801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4801) · Entrez [3030](https://www.ncbi.nlm.nih.gov/gene/3030) · UniProt [P40939](https://www.uniprot.org/uniprotkb/P40939) · Ensembl [ENSG00000084754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084754)

## Data

Gene col 1412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1412); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1412]; `tensor/DDL_lfc|DDL_z.npy` [1412]; `embed/gene_vectors.npy` [1412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1412 or target_col == 1412). Every well: [[HADHA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HADHA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
