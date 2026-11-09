---
symbol: "YBX1"
type: "gene"
col: 812
ensembl_id: "ENSG00000065978"
name: "Y-box binding protein 1"
location: "1p34.2"
module: 43
arm: "+"
pooled_cpm: 314.21
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# YBX1

*Y-box binding protein 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.18× (z +14.4, q 2e-44, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +8.1, q 7e-14, up in 46 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS2]] (+0.59, fdr 1e-05), [[RPL4]] (+0.58, fdr 1e-05), [[RPL3]] (+0.57, fdr 1e-05); moves opposite to [[CIAO1]] (-0.60, fdr 2e-04), [[NSUN5]] (-0.60, fdr 4e-04), [[PSMG3]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **5.18×** | +14.4 | 2e-44 | 49/49 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.47×** | +12.6 | 3e-34 | 44/44 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.50×** | +10.2 | 5e-22 | 45/45 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.1 | 7e-14 | 46/49 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +6.5 | 9e-09 | 44/50 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.85×** | +5.4 | 6e-06 | 46/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.75×** | +4.9 | 7e-05 | 41/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.74×** | +4.7 | 2e-04 | 41/47 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.3 | 0.001 | 37/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.61×** | +4.2 | 0.002 | 44/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.006 | 36/48 (C32, BT-474, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +3.8 | 0.006 | 29/38 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.48×** | +3.5 | 0.023 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +3.4 | 0.023 | 26/48 (NCI-H1792, SK-MEL-2, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.037 | 36/48 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.094 | 32/48 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 243 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 167 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.7) | — |
| [[A498 (line)]] | wt | 230 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.5) | — |
| [[C32 (line)]] | wt | 283 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 217 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.3) | — |
| [[KATO III (line)]] | alt | 229 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 435 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 254 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.83× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 164 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 216 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 345 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 356 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 407 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.1) | — |
| [[J82 (line)]] | alt | 356 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.0) | — |
| [[LoVo (line)]] | wt | 293 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.51× (z +18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 365 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 329 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 319 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 223 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 340 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 126 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.5× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 386 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 356 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 306 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 290 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 344 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 144 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.08× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RPMI-7951 (line)]] | alt | 317 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 267 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW1417 (line)]] | alt | 255 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 346 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 404 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 213 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 418 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[CHP-212 (line)]] | wt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 393 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 362 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 352 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 492 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 264 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW48 (line)]] | wt | 356 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 425 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 428 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 330 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 475 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS2]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 | pathway: Interferon Signaling; STRING 752 |
| [[RPL4]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 | STRING 571 |
| [[RPL3]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 | STRING 741 |
| [[HNRNPA1]] | +0.56 | +0.54 / +0.58 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 937 |
| [[CANX]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[ALB]] | +0.54 | +0.21 / +0.46 | both halves | 7e-04 |  |
| [[PCBP2]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions; STRING 870 |
| [[NPM1]] | +0.54 | +0.59 / +0.51 | both halves | 1e-05 | pathway: Interferon Signaling; STRING 812 |
| [[SDF4]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[AHSG]] | +0.54 | +0.17 / +0.45 | ⚠ not reproduced | 0.001 |  |
| [[PDIA3]] | +0.54 | +0.27 / +0.63 | both halves | 3e-04 | pathway: Dengue Virus Genome Translation and Replication |
| [[CRTAP]] | +0.54 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[RPL14]] | +0.53 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO1]] | -0.60 | -0.29 / -0.67 | both halves | 2e-04 |  |
| [[NSUN5]] | -0.60 | -0.26 / -0.65 | both halves | 4e-04 | STRING 473 |
| [[PSMG3]] | -0.58 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[RPP14]] | -0.52 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[VPS25]] | -0.51 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[RAD54L2]] | -0.51 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[BORCS8]] | -0.51 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[TMEM70]] | -0.50 | -0.19 / -0.50 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZSCAN18]] | -0.50 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[POLM]] | -0.50 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[ZNF579]] | -0.49 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[MRPL58]] | -0.49 | -0.12 / -0.69 | ⚠ one half (not replicated) | 0.002 |  |
| [[LRRC8E]] | -0.48 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[TRAPPC3]] | -0.48 | -0.25 / -0.51 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises YBX1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without CRTAP | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.259). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-30.8, -26.0); signed map (-22.3, -33.1). **Vector** length 72.3, 35.9% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | -0.5 |
|  | [[Decitabine (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.5 | -0.2 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | +1.5 | -0.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | -1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | +0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.0 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | Y-box binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,682,418-42,703,805 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YB-1, YB1, DBPB, NSEP-1, MDR-NF1, BP-8, CSDB, CSDA2; previously NSEP1 |
| Gene groups (HGNC) | Y-box binding proteins; U11/U12 di-snRNP; U11 small nuclear ribonucleoprotein; Cold shock domain containing |
| Reactome | 23 pathways, smallest: Assembly and Release of Dengue Virus Virions; Noncanonical activation of NOTCH3; NOTCH3 Activation and Transmission of Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [P67809](https://www.uniprot.org/uniprotkb/P67809) (Y-box-binding protein 1):

> DNA- and RNA-binding protein involved in various processes, such as translational repression, RNA stabilization, mRNA splicing, DNA repair and transcription regulation. Predominantly acts as a RNA-binding protein: binds preferentially to the 5'-[CU]CUGCG-3' RNA motif and specifically recognizes mRNA transcripts modified by C5-methylcytosine (m5C). Promotes mRNA stabilization: acts by binding to m5C-containing mRNAs and recruiting the mRNA stability maintainer ELAVL1, thereby preventing mRNA …

**Summary**, from NCBI Gene [4904](https://www.ncbi.nlm.nih.gov/gene/4904):

> This gene encodes a highly conserved cold shock domain protein that has broad nucleic acid binding properties. The encoded protein functions as both a DNA and RNA binding protein and has been implicated in numerous cellular processes including regulation of transcription and translation, pre-mRNA splicing, DNA reparation and mRNA packaging. This protein is also a component of messenger ribonucleoprotein (mRNP) complexes and may have a role in microRNA processing. This protein can be secreted …

**Accessions** — [HGNC:8014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8014) · Entrez [4904](https://www.ncbi.nlm.nih.gov/gene/4904) · UniProt [P67809](https://www.uniprot.org/uniprotkb/P67809) · Ensembl [ENSG00000065978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065978)

## Data

Gene col 812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 812); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 812]; `tensor/DDL_lfc|DDL_z.npy` [812]; `embed/gene_vectors.npy` [812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 812 or target_col == 812). Every well: [[YBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
