---
symbol: "PDCD7"
type: "gene"
col: 1624
ensembl_id: "ENSG00000090470"
name: "programmed cell death 7"
location: "15q22.31"
module: 11
arm: "+"
pooled_cpm: 36.86
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PDCD7

*programmed cell death 7* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +18.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.676× (z -5.4, q 3e-05, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.156×, NCI-H2030 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SNU-423 0.0430×; ⚠ toxic); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0927×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPRN]] (+0.75, fdr 7e-06), [[TOPORS]] (+0.71, fdr 7e-06), [[TERF2IP]] (+0.71, fdr 7e-06); moves opposite to [[MAPK9]] (-0.66, fdr 1e-05), [[NDRG3]] (-0.66, fdr 7e-06), [[YWHAQ]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +18.4 | 0e+00 | 47/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.24×** | +15.5 | 0e+00 | 47/48 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +12.3 | 3e-32 | 45/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.97×** | +8.9 | 9e-17 | 45/48 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.6 | 2e-12 | 37/47 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +6.0 | 2e-07 | 34/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.9 | 3e-07 | 26/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +5.6 | 2e-06 | 31/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.5 | 3e-06 | 32/48 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.2 | 1e-05 | 34/48 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.8 | 8e-05 | 28/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.4 | 5e-04 | 31/47 (HepG2/C3A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.36×** | +4.2 | 0.001 | 25/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.031 | 17/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **1.26×** | +3.1 | 0.064 | 21/47 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.092 | 16/48 (A-172, A498, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.092 | 11/48 (SK-MEL-2, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1624.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.156×, NCI-H2030 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SNU-423 0.0430×; ⚠ toxic); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0927×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.676×** | -5.4 | 3e-05 | 36/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -5.3 | 3e-05 | 32/48 (KATO III, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +15.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 34.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +17.0) | — |
| [[C32 (line)]] | wt | 37.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 32.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 39.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.2) | — |
| [[LoVo (line)]] | wt | 62.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +15.1) | — |
| [[LS 180 (line)]] | wt | 38.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 31.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.7) | — |
| [[SW480 (line)]] | alt | 45.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.3) | — |
| [[A549 (line)]] | wt | 42.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 20.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 37.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +13.7) | — |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.1) | — |
| [[KATO III (line)]] | alt | 52.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 37.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 40.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 33.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 46.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 29.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.5) | [[Lonafarnib (drug)]] 5 µM 0.0430× (z -12.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 36.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[A498 (line)]] | wt | 30.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0927× (z -10.5) |
| [[C-33 A (line)]] | alt | 35.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.5) | — |
| [[H4 (line)]] | wt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 68.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +11.4) | — |
| [[J82 (line)]] | alt | 34.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 40.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.5) | — |
| [[A-427 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPRN]] | +0.75 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[TBCC]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[IRX5]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RSF1]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PPCS]] | +0.69 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.68 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[PPIG]] | +0.68 | +0.73 / +0.65 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[REST]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.66 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[NDRG3]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.66 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[RAD23B]] | -0.65 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[AGO1]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.63 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.62 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[NXPE3]] | -0.62 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[CTC1]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[MRPL42]] | -0.62 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[HDAC1]] | -0.62 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[PPT1]] | -0.62 | -0.59 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDCD7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.3, 4.3); signed map (3.0, -16.6). **Vector** length 107, 30.1% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.5 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +18.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.2 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.3 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.7 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -8.6 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.2 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.2 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,117,379-65,133,808 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HES18, ES18, 59K |
| Gene groups (HGNC) | U11/U12 di-snRNP; U11 small nuclear ribonucleoprotein |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8D1](https://www.uniprot.org/uniprotkb/Q8N8D1) (Programmed cell death protein 7):

> Promotes apoptosis when overexpressed.

**Summary**, from NCBI Gene [10081](https://www.ncbi.nlm.nih.gov/gene/10081):

> This gene encodes a 59 kDa protein that is associated with the U11 small nuclear ribonucleoprotein (snRNP), which is a component of the minor U12-type spliceosome responsible for catalyzing pre-mRNA splicing of U12-type introns. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:8767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8767) · Entrez [10081](https://www.ncbi.nlm.nih.gov/gene/10081) · UniProt [Q8N8D1](https://www.uniprot.org/uniprotkb/Q8N8D1) · Ensembl [ENSG00000090470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090470)

## Data

Gene col 1624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1624); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1624]; `tensor/DDL_lfc|DDL_z.npy` [1624]; `embed/gene_vectors.npy` [1624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1624 or target_col == 1624). Every well: [[PDCD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
