---
symbol: "GLIS3"
type: "gene"
col: 2837
ensembl_id: "ENSG00000107249"
name: "GLIS family zinc finger 3"
location: "9p24.2"
module: 13
arm: "+"
pooled_cpm: 251.73
n_lines_expressing: 29
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 43
direction_downstream: 26
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GLIS3

*GLIS family zinc finger 3* — 9p24.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 3.35×, KATO III 2.14×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 3.16×; ⚠ cell-cycle shift, explains ~36% of this change); [[Binimetinib (drug)]] 5 µM in 1 line (HEC-1-A 3.18×); [[Trametinib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.66×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 2.86×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.473× (z -12.0, q 2e-30, down in 20 of 27 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.434× (z -9.5, q 8e-19, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPPA]] (+0.70, fdr 7e-06), [[ADAMTS12]] (+0.65, fdr 1e-05), [[TFPI]] (+0.65, fdr 7e-06); moves opposite to [[IQANK1]] (-0.49, fdr 5e-05), [[DMTN]] (-0.49, fdr 4e-05), [[PCDH1]] (-0.48, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[NRP1]] → it (grade B ⚠); 26 go from it, the strongest it → [[NRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 3.35×, KATO III 2.14×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 3.16×; ⚠ cell-cycle shift, explains ~36% of this change); [[Binimetinib (drug)]] 5 µM in 1 line (HEC-1-A 3.18×); [[Trametinib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.66×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 2.86×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.23× | +3.4 | 0.42 | 8/27 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.32× | +3.2 | 0.42 | 19/27 (NCI-H1792, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.473×** | -12.0 | 2e-30 | 20/27 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.434×** | -9.5 | 8e-19 | 23/27 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.445×** | -9.2 | 8e-18 | 23/27 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.482×** | -8.3 | 2e-14 | 19/27 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.480×** | -8.0 | 1e-13 | 23/26 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.502×** | -7.8 | 5e-13 | 22/27 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -7.4 | 1e-11 | 23/27 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.526×** | -7.0 | 2e-10 | 20/27 (NCI-H460, SW 900, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -6.3 | 2e-08 | 18/27 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.623×** | -5.4 | 4e-06 | 14/27 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.616×** | -5.3 | 7e-06 | 20/26 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.659×** | -4.7 | 1e-04 | 17/27 (H4, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.678×** | -4.4 | 5e-04 | 23/27 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.664×** | -4.3 | 7e-04 | 23/26 (hTERT-HPNE, SW 900, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.506×** | -4.0 | 0.002 | 16/24 (LOX-IMVI, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.682×** | -3.6 | 0.012 | 14/27 (NCI-H2030, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.744×** | -3.2 | 0.041 | 14/27 (H4, hTERT-HPNE, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.052 | 18/27 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -3.1 | 0.054 | 17/27 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.763×** | -3.1 | 0.060 | 16/27 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.768×** | -3.0 | 0.069 | 16/28 (J82, RPMI-7951, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.070 | 9/27 (RPMI-7951, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 375 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -24.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -14.2) |
| [[HOP62 (line)]] | alt | 842 | 0 | 14 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 786 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -18.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -12.8) |
| [[SW 900 (line)]] | alt | 813 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0883× (z -16.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.200× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 280 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -14.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.194× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 331 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -19.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -14.7) |
| [[H4 (line)]] | wt | 492 | 0 | 8 (7 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.191× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 552 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -12.3) |
| [[HT-29 (line)]] | alt | 134 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.86× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.341× (z -9.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 518 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 169 | 5 (1 ⚠) | 0 | [[Binimetinib (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 606 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.173× (z -10.8) |
| [[LoVo (line)]] | wt | 98.6 | 1 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.234× (z -13.0) |
| [[SHP-77 (line)]] | alt | 148 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 379 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.8) |
| [[A498 (line)]] | wt | 645 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.274× (z -8.5) |
| [[J82 (line)]] | alt | 518 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -12.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 999 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -9.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 77.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.640× (z -9.1) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 49.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 44.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 40.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 52.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 57.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 49.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 679 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 48.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 27.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 19.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPPA]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS12]] | +0.65 | +0.69 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[TFPI]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ADAM12]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[NAV1]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MIR100HG]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PDE3A]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[VEGFC]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[OSMR]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[GRAMD1B]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[STEAP1B-AS1]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQANK1]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[DMTN]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PCDH1]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[FIG4]] | -0.47 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NOXA1]] | -0.47 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[PREPL]] | -0.46 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF33B]] | -0.46 | -0.49 / -0.39 | both halves | 5e-05 | same gene group |
| [[MIR3936HG]] | -0.45 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[EPS8L2]] | -0.45 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 12, C 31. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | NRP1 activity raises GLIS3's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 3.49× lower at baseline in the lines without NRP1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[SETBP1]] | B | SETBP1 activity raises GLIS3's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.66× lower at baseline in the lines without SETBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[PCDH1]] | B | PCDH1 activity lowers GLIS3's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.56× higher at baseline in the lines without PCDH1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[BMPER]] | B | BMPER activity raises GLIS3's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.99× lower at baseline in the lines without BMPER | 0.031 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[GJA1]] | B | GJA1 activity raises GLIS3's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without GJA1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[RFX8]] | B | RFX8 activity raises GLIS3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.87× lower at baseline in the lines without RFX8 | 0.045 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[ODAD2]] | B | ODAD2 activity raises GLIS3's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without ODAD2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5 |
| [[IQANK1]] | B | IQANK1 activity lowers GLIS3's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 4.03× higher at baseline in the lines without IQANK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[WNT5A]] | B | WNT5A activity strengthens GLIS3's drug response | lines that do not express WNT5A (13) vs lines expressing it (14) | the lines without WNT5A respond 0.44× as strongly (z diff +4.02); strongest at Homoharringtonine 5 µM: 0.71x vs 0.26x (z diff +6.0) | 0.063 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; artifact flags |
| [[TWIST2]] | B | TWIST2 activity raises GLIS3's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without TWIST2 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[ELL2]] | B | ELL2 activity raises GLIS3's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.76× lower at baseline in the lines without ELL2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[RFX8]] | B | RFX8 activity strengthens GLIS3's drug response | lines that do not express RFX8 (17) vs lines expressing it (10) | the lines without RFX8 respond 0.56× as strongly (z diff +3.40); strongest at Homoharringtonine 0.5 µM: 0.70x vs 0.29x (z diff +5.2) | 0.099 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; target measured in part of the lines; artifact flags |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 11, C 15. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | GLIS3 activity raises NRP1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.48× lower at baseline in the lines without GLIS3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[EXT1]] | B | GLIS3 activity raises EXT1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.76× lower at baseline in the lines without GLIS3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[ELL2]] | B | GLIS3 activity raises ELL2's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.02× lower at baseline in the lines without GLIS3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[STEAP1B]] | B | GLIS3 activity raises STEAP1B's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without GLIS3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[BMPER]] | B | GLIS3 activity raises BMPER's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.14× lower at baseline in the lines without GLIS3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM | B | GLIS3 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 1.22× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[MEG8]] | B | GLIS3 activity raises MEG8's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.16× lower at baseline in the lines without GLIS3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 5 µM | B | GLIS3 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 5 µM (makes them more sensitive) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| cells under [[Arbutin (drug)]] 5 µM | B | GLIS3 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 0.81× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[AGTR1]] | B | GLIS3 activity raises AGTR1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without GLIS3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | GLIS3 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 1.26× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[STEAP1B-AS1]] | C | GLIS3 activity raises STEAP1B-AS1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.13× lower at baseline in the lines without GLIS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.8, 17.8); signed map (26.1, 48.2). **Vector** length 116, 43.7% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -2.3 |
|  | [[Thymol (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.2 | -8.0 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | GLIS family zinc finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.2 — chr9:3,824,127-4,348,392 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33662; previously ZNF515 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEA6](https://www.uniprot.org/uniprotkb/Q8NEA6) (Zinc finger protein GLIS3):

> Acts both as a repressor and an activator of transcription. Binds to the consensus sequence 5'-GACCACCCAC-3' (By similarity).

**Summary**, from NCBI Gene [169792](https://www.ncbi.nlm.nih.gov/gene/169792):

> This gene is a member of the GLI-similar zinc finger protein family and encodes a nuclear protein with five C2H2-type zinc finger domains. This protein functions as both a repressor and activator of transcription and is specifically involved in the development of pancreatic beta cells, the thyroid, eye, liver and kidney. Mutations in this gene have been associated with neonatal diabetes and congenital hypothyroidism (NDH). Alternatively spliced variants that encode different protein isoforms …

**Accessions** — [HGNC:28510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28510) · Entrez [169792](https://www.ncbi.nlm.nih.gov/gene/169792) · UniProt [Q8NEA6](https://www.uniprot.org/uniprotkb/Q8NEA6) · Ensembl [ENSG00000107249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107249)

## Data

Gene col 2837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2837); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2837]; `tensor/DDL_lfc|DDL_z.npy` [2837]; `embed/gene_vectors.npy` [2837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2837 or target_col == 2837). Every well: [[GLIS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLIS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
