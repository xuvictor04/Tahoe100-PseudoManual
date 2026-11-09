---
symbol: "CDV3"
type: "gene"
col: 1667
ensembl_id: "ENSG00000091527"
name: "CDV3 homolog"
location: "3q22.1"
module: 98
arm: "+"
pooled_cpm: 132.07
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# CDV3

*CDV3 homolog* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +13.7, q 5e-40, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.07× (z +13.0, q 3e-36, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.359×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (RKO 0.264×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.370×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSTL3]] (+0.65, fdr 7e-06), [[CLIP1]] (+0.63, fdr 1e-05), [[TRIM47]] (+0.60, fdr 1e-05); moves opposite to [[EFHC1]] (-0.61, fdr 1e-05), [[PIH1D1]] (-0.60, fdr 1e-05), [[SPICE1]] (-0.60, fdr 2e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FSTL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.74×** | +13.7 | 5e-40 | 43/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +13.0 | 3e-36 | 43/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +10.1 | 1e-21 | 42/47 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +9.8 | 2e-20 | 39/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +9.6 | 9e-20 | 44/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.59×** | +8.3 | 8e-15 | 37/49 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +7.9 | 2e-13 | 42/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +7.4 | 8e-12 | 41/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.7 | 1e-09 | 27/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +6.4 | 7e-09 | 38/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.43×** | +6.4 | 7e-09 | 41/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.1 | 6e-08 | 26/49 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +5.7 | 7e-07 | 33/49 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 8e-07 | 35/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +5.3 | 4e-06 | 36/47 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.51×** | +5.2 | 6e-06 | 36/48 (Panc 03.27, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 34/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **1.60×** | +4.4 | 3e-04 | 39/46 (NCI-H1573, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 9e-04 | 27/48 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 26/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.001 | 28/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 28/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.359×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (RKO 0.264×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.370×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 191 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.19× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 74.5 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.82× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 97.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +19.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 84.8 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 123 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +18.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 77.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.62× (z +12.5) | — |
| [[A-172 (line)]] | wt | 132 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 94.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 94.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.88× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 190 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.97× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.68× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 166 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +10.6) | — |
| [[A498 (line)]] | wt | 189 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +10.8) | — |
| [[A549 (line)]] | wt | 104 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.50× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 104 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 143 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 78.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 207 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 135 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 174 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.89× (z +9.5) | — |
| [[H4 (line)]] | wt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 97.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 146 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.07× (z +10.2) | — |
| [[A-427 (line)]] | wt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.21× (z +10.6) | — |
| [[C32 (line)]] | wt | 70.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +8.9) | — |
| [[J82 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 147 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.11× (z +9.4) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 141 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.24× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -12.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 168 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.264× (z -8.9) |
| [[SHP-77 (line)]] | alt | 78.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 199 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 72.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSTL3]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CLIP1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TRIM47]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[GLRX2]] | +0.58 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[NPIPB4]] | +0.57 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[NOP14]] | +0.57 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[ANKLE2]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[KLF6]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[GPATCH4]] | +0.56 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[POGK]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HACD1]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PIH1D1]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.60 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[ADIPOR1]] | -0.58 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[HDAC1]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[RPA1]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NUDT21]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SNX1]] | -0.56 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[GGH]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[TMED4]] | -0.55 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[TMEM67]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[BRK1]] | -0.55 | -0.65 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL3]] | B | FSTL3 activity raises CDV3's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.21× lower at baseline in the lines without FSTL3 | 0.082 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.6, -23.1); signed map (11.5, -7.4). **Vector** length 105, 35.4% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.1 | +13.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.2 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.6 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +7.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | +1.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | CDV3 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:133,573,686-133,590,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H41 |
| Matched by | ensembl_id |

UniProt [Q9UKY7](https://www.uniprot.org/uniprotkb/Q9UKY7) carries no function annotation.

**Summary**, from NCBI Gene [55573](https://www.ncbi.nlm.nih.gov/gene/55573):

> Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26928) · Entrez [55573](https://www.ncbi.nlm.nih.gov/gene/55573) · UniProt [Q9UKY7](https://www.uniprot.org/uniprotkb/Q9UKY7) · Ensembl [ENSG00000091527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091527)

## Data

Gene col 1667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1667); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1667]; `tensor/DDL_lfc|DDL_z.npy` [1667]; `embed/gene_vectors.npy` [1667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1667 or target_col == 1667). Every well: [[CDV3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDV3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
