---
symbol: "TAF1"
type: "gene"
col: 7153
ensembl_id: "ENSG00000147133"
name: "TATA-box binding protein associated factor 1"
location: "Xq13.1"
module: 11
arm: "+"
pooled_cpm: 157.41
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TAF1

*TATA-box binding protein associated factor 1* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +14.4, q 2e-44, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.683× (z -7.6, q 2e-11, down in 31 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.872× (z -4.2, q 0.002, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.407×, SK-MEL-2 0.447×, LOX-IMVI 0.418×, NCI-H460 0.510×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.366×, SK-MEL-2 0.461×; ⚠ cell-cycle shift, explains ~28% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.445×, NCI-H23 0.493×; ⚠ cell-cycle shift, would explain all of this change); [[Capmatinib (drug)]] 5 µM in 1 line (CHP-212 0.0927×); [[Altretamine (drug)]] 0.05 µM in 1 line (SW 1088 0.101×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.669×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSRP1]] (+0.71, fdr 7e-06), [[MDM4]] (+0.63, fdr 1e-05), [[REXO1]] (+0.63, fdr 1e-05); moves opposite to [[GM2A]] (-0.61, fdr 1e-05), [[TWSG1]] (-0.60, fdr 1e-05), [[LAPTM4A]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +14.4 | 2e-44 | 38/48 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +11.7 | 2e-29 | 40/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +5.3 | 2e-05 | 35/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.55×** | +4.9 | 1e-04 | 38/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.5 | 7e-04 | 26/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.013 | 22/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.029 | 21/47 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.3 | 0.080 | 0/50 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7153.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.407×, SK-MEL-2 0.447×, LOX-IMVI 0.418×, NCI-H460 0.510×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.366×, SK-MEL-2 0.461×; ⚠ cell-cycle shift, explains ~28% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.445×, NCI-H23 0.493×; ⚠ cell-cycle shift, would explain all of this change); [[Capmatinib (drug)]] 5 µM in 1 line (CHP-212 0.0927×); [[Altretamine (drug)]] 0.05 µM in 1 line (SW 1088 0.101×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.669×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.683×** | -7.6 | 2e-11 | 31/45 (A-427, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.737×** | -6.6 | 1e-08 | 32/49 (C-33 A, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -6.0 | 4e-07 | 34/47 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.794×** | -4.8 | 3e-04 | 27/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.810×** | -4.4 | 0.001 | 26/50 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.816×** | -4.2 | 0.002 | 24/44 (KATO III, C32, …) | all doses, flat | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.872× | -4.2 | 0.002 | 14/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.828×** | -4.1 | 0.004 | 23/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.878× | -4.0 | 0.005 | 20/49 (A549, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.9 | 0.006 | 16/48 (RKO, SNU-423, …) | rises with dose | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.039 | 22/48 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.857× | -3.3 | 0.041 | 15/48 (SW 1088, RPMI-7951, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -3.3 | 0.043 | 10/48 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.859× | -3.3 | 0.043 | 10/48 (HEC-1-A, AN3 CA, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.043 | 19/48 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | 0.856× | -3.2 | 0.045 | 14/48 (KATO III, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 231 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.445× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 220 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 272 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.563× (z -9.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 215 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[RKO (line)]] | wt | 138 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 171 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 181 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LoVo (line)]] | wt | 121 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.1) | — |
| [[LOX-IMVI (line)]] | wt | 198 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 88.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -12.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 173 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 297 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 87.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.4) | — |
| [[H4 (line)]] | wt | 192 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 176 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 138 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +17.9) | — |
| [[LS 180 (line)]] | wt | 140 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 60.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.9) | — |
| [[A498 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 94.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0927× (z -9.3) |
| [[HT-29 (line)]] | alt | 172 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[MIA PaCa-2 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.527× (z -8.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 129 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.96× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.128× (z -13.9) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.3) | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.101× (z -9.2) |
| [[SW1417 (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -9.5) ⚠ toxic |
| [[SW48 (line)]] | wt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.3) | — |
| [[A-172 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | +0.71 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[MDM4]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[REXO1]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ICE2]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H18]] | +0.61 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[UTP14A]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[CDK11A]] | +0.60 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NOP14]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[NOL8]] | +0.60 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[AFG3L1P]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[DDX27]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GM2A]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.60 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[NPTN]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[USP3]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[FAM210B]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[GGH]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[DHRS1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PEBP1]] | -0.55 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[STAM]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TMED4]] | -0.54 | -0.57 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.0, 1.2); signed map (4.6, -24.4). **Vector** length 112, 32.3% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +4.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -3.7 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,366,136-71,532,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NSCL2, TAFII250, KAT4, DYT3/TAF1; previously TAF2A, BA2R, CCG1, CCGS, DYT3 |
| Gene groups (HGNC) | Lysine acetyltransferases; Bromodomain containing; General transcription factor IID complex subunits; TATA-box binding protein associated factor 1 family |
| Reactome | 19 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [P21675](https://www.uniprot.org/uniprotkb/P21675) (Transcription initiation factor TFIID subunit 1):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF1 is the largest …

**Summary**, from NCBI Gene [6872](https://www.ncbi.nlm.nih.gov/gene/6872):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is the basal transcription factor TFIID, which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11535) · Entrez [6872](https://www.ncbi.nlm.nih.gov/gene/6872) · UniProt [P21675](https://www.uniprot.org/uniprotkb/P21675) · Ensembl [ENSG00000147133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147133)

## Data

Gene col 7153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7153); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7153]; `tensor/DDL_lfc|DDL_z.npy` [7153]; `embed/gene_vectors.npy` [7153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7153 or target_col == 7153). Every well: [[TAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
