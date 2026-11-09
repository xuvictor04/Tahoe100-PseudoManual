---
symbol: "HMGB1"
type: "gene"
col: 12123
ensembl_id: "ENSG00000189403"
name: "high mobility group box 1"
location: "13q12.3"
module: 22
arm: "+"
pooled_cpm: 141.61
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HMGB1

*high mobility group box 1* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.23× (z +13.1, q 1e-36, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.27× (z +6.5, q 8e-09, up in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H1792 12.5×, A549 11.3×, MIA PaCa-2 8.57×, SW480 7.14×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Auranofin (drug)]] 5 µM in 10 lines (A-172 8.13×, HOP62 6.89×, HT-29 6.62×, C32 4.79×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 2.98×, A549 2.60×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD4-AS1]] (+0.77, fdr 7e-06), [[STMN1]] (+0.71, fdr 7e-06), [[HCCS-DT]] (+0.64, fdr 7e-06); moves opposite to [[VPS28]] (-0.55, fdr 6e-05), [[MRPL10]] (-0.54, fdr 2e-04), [[MYG1]] (-0.54, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF367]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H1792 12.5×, A549 11.3×, MIA PaCa-2 8.57×, SW480 7.14×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Auranofin (drug)]] 5 µM in 10 lines (A-172 8.13×, HOP62 6.89×, HT-29 6.62×, C32 4.79×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 2.98×, A549 2.60×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **5.23×** | +13.1 | 1e-36 | 49/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.13×** | +10.8 | 8e-25 | 41/44 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.74×** | +9.7 | 6e-20 | 45/45 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.42×** | +7.0 | 3e-10 | 47/48 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +6.5 | 8e-09 | 46/48 (A-172, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.95×** | +5.1 | 3e-05 | 41/47 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.73×** | +4.4 | 9e-04 | 39/48 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.4 | 9e-04 | 38/49 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.9 | 0.006 | 39/47 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.41×** | +3.9 | 0.006 | 46/48 (SNU-1, HT-29, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | 1.48× | +3.1 | 0.10 | 35/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 177 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 93.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.58× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.24× (z +9.5) | — |
| [[SW480 (line)]] | alt | 199 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.06× (z +9.7) | — |
| [[A549 (line)]] | wt | 85.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.6) | — |
| [[C32 (line)]] | wt | 127 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.79× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 201 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.37× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 103 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.89× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 198 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 6.62× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.57× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 56.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 153 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.58× (z +11.0) | — |
| [[A-172 (line)]] | wt | 132 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.13× (z +14.8) | — |
| [[Hs 766T (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 110 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 91.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.62× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 128 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 163 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A498 (line)]] | wt | 218 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 84.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 66.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RPMI-7951 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW 900 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.56× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AsPC-1 (line)]] | alt | 83.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 140 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 81.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[COLO 205 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[J82 (line)]] | alt | 247 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SHP-77 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-1 (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW48 (line)]] | wt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 245 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 256 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD4-AS1]] | +0.77 | +0.84 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[STMN1]] | +0.71 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[HCCS-DT]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PRC1]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[HMGB3]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 | same gene group |
| [[NUSAP1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[C21orf58]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[NUCKS1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SMC4]] | +0.61 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TMPO]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[FOXM1]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS28]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[MRPL10]] | -0.54 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[MYG1]] | -0.54 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[POLR2C]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[EIF3M]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF367]] | C | ZNF367 activity raises HMGB1's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without ZNF367 | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[C21orf58]] | C | C21orf58 activity raises HMGB1's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without C21orf58 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[C5]] | C | C5 activity raises HMGB1's level | lines that do not express C5 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without C5 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLSPN, PRDM6, TCF19; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.0, -52.9); signed map (-47.2, -45.5). **Vector** length 82.2, 36.3% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.52 to 8); *Processing of antigen in germinal center B cells* (reactome, mean cos +0.50 to 9); *MHC class II antigen presentation* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +3.4 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.8 | -0.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | +0.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.2 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group box 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:30,456,704-30,617,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HMG3, SBP-1, DKFZp686A04236; previously HMG1 |
| Gene groups (HGNC) | Canonical high mobility group |
| Reactome | 44 pathways, smallest: Scavenging by Class B Receptors; Advanced glycosylation endproduct receptor signaling; Apoptosis induced DNA fragmentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P09429](https://www.uniprot.org/uniprotkb/P09429) (High mobility group protein B1):

> Multifunctional redox sensitive protein with various roles in different cellular compartments. In the nucleus is one of the major chromatin-associated non-histone proteins and acts as a DNA chaperone involved in replication, transcription, chromatin remodeling, V(D)J recombination, DNA repair and genome stability. Proposed to be an universal biosensor for nucleic acids. Promotes host inflammatory response to sterile and infectious signals and is involved in the coordination and integration of …

**Summary**, from NCBI Gene [3146](https://www.ncbi.nlm.nih.gov/gene/3146):

> This gene encodes a protein that belongs to the High Mobility Group-box superfamily. The encoded non-histone, nuclear DNA-binding protein regulates transcription, and is involved in organization of DNA. This protein plays a role in several cellular processes, including inflammation, cell differentiation and tumor cell migration. Multiple pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, …

**Accessions** — [HGNC:4983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4983) · Entrez [3146](https://www.ncbi.nlm.nih.gov/gene/3146) · UniProt [P09429](https://www.uniprot.org/uniprotkb/P09429) · Ensembl [ENSG00000189403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189403)

## Data

Gene col 12123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12123); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12123]; `tensor/DDL_lfc|DDL_z.npy` [12123]; `embed/gene_vectors.npy` [12123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12123 or target_col == 12123). Every well: [[HMGB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
