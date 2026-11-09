---
symbol: "LIN7C"
type: "gene"
col: 7329
ensembl_id: "ENSG00000148943"
name: "lin-7 cell polarity scaffold C"
location: "11p14.1"
module: 25
arm: "+"
pooled_cpm: 52.16
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# LIN7C

*lin-7 cell polarity scaffold C* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +11.5, q 9e-28, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (CHP-212 0.0643×); [[Bendamustine (drug)]] 5 µM in 1 line (CHP-212 0.0691×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4H]] (+0.82, fdr 7e-06), [[TWF1]] (+0.79, fdr 7e-06), [[NRAS]] (+0.79, fdr 7e-06); moves opposite to [[RPL36AL]] (-0.76, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[SNHG9]] (-0.73, fdr 4e-05), [[TMEM258]] (-0.71, fdr 1e-05), [[SNHG19]] (-0.71, fdr 8e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MSX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +11.5 | 9e-28 | 44/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +10.8 | 7e-25 | 37/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.9 | 9e-21 | 44/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.4 | 2e-11 | 35/44 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.78×** | +7.2 | 9e-11 | 44/48 (A-172, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.1 | 1e-10 | 39/47 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +6.8 | 7e-10 | 44/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +6.5 | 7e-09 | 42/48 (A-172, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +6.4 | 7e-09 | 42/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.58×** | +5.7 | 8e-07 | 41/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +5.3 | 5e-06 | 36/48 (NCI-H1573, BT-474, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +5.0 | 3e-05 | 41/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.6 | 2e-04 | 34/49 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 2e-04 | 35/48 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 32/48 (Panc 03.27, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.002 | 26/48 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.002 | 30/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.012 | 30/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.054 | 23/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.060 | 20/48 (LoVo, SW48, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.067 | 18/48 (A-172, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.067 | 21/48 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7329.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (CHP-212 0.0643×); [[Bendamustine (drug)]] 5 µM in 1 line (CHP-212 0.0691×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.625× | -3.7 | 0.11 | 32/48 (H4, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.666× | -3.2 | 0.36 | 21/48 (NCI-H1573, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.786× | -3.0 | 0.41 | 27/47 (SW 1271, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 46.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 31.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.3) | — |
| [[A-172 (line)]] | wt | 41.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.7) | — |
| [[A549 (line)]] | wt | 39.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 61.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 2 | — | [[Pemetrexed (drug)]] 5 µM 0.0643× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 49.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 33.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) | — |
| [[KATO III (line)]] | alt | 41.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.84× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +8.8) | — |
| [[A498 (line)]] | wt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 70.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +10.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 61.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 73.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 89.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[LoVo (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 60.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 42.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 42.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 49.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4H]] | +0.82 | +0.59 / +0.84 | both halves | 7e-06 |  |
| [[TWF1]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[NRAS]] | +0.79 | +0.62 / +0.78 | both halves | 7e-06 | pathway: Activation of NMDA receptors and postsynaptic events |
| [[OCRL]] | +0.77 | +0.59 / +0.85 | both halves | 7e-06 |  |
| [[NONO]] | +0.77 | +0.60 / +0.84 | both halves | 7e-06 |  |
| [[PRELID3B]] | +0.77 | +0.64 / +0.84 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.76 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.76 | +0.52 / +0.84 | both halves | 1e-05 |  |
| [[AKAP11]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[GMFB]] | +0.75 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.73 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[SF3B4]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36AL]] ⚠ | -0.76 | -0.52 / -0.81 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | -0.73 | -0.41 / -0.80 | both halves | 4e-05 |  |
| [[TMEM258]] | -0.71 | -0.52 / -0.78 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.71 | -0.57 / -0.72 | both halves | 8e-06 |  |
| [[LINC00685]] | -0.71 | -0.45 / -0.78 | both halves | 3e-05 |  |
| [[COX6B1]] | -0.71 | -0.49 / -0.75 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.70 | -0.56 / -0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PTMAP2]] ⚠ | -0.69 | -0.53 / -0.73 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | -0.69 | -0.42 / -0.73 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DCTN6-DT]] | -0.69 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[RPL36]] | -0.69 | -0.57 / -0.72 | both halves | 9e-06 |  |
| [[ZBTB7A]] | -0.68 | -0.49 / -0.76 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.68 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[ING2]] | -0.68 | -0.38 / -0.75 | both halves | 6e-05 |  |
| [[COMMD6]] | -0.68 | -0.52 / -0.75 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.68 | -0.51 / -0.72 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | MSX1 activity lowers LIN7C's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without MSX1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.888). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.9, -20.6); signed map (-16.4, -37.3). **Vector** length 112, 33.7% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.0 | +3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.9 | +3.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.7 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.4 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.3 | -3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.2 | -3.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | lin-7 cell polarity scaffold C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:27,494,418-27,506,769 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MALS-3, LIN-7C, LIN-7-C, VELI3, FLJ11215 |
| Gene groups (HGNC) | PDZ domain containing; Crumbs complex components |
| Reactome | 9 pathways, smallest: Dopamine Neurotransmitter Release Cycle; Assembly and cell surface presentation of NMDA receptors; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUP9](https://www.uniprot.org/uniprotkb/Q9NUP9) (Protein lin-7 homolog C):

> Plays a role in establishing and maintaining the asymmetric distribution of channels and receptors at the plasma membrane of polarized cells. Forms membrane-associated multiprotein complexes that may regulate delivery and recycling of proteins to the correct membrane domains. The tripartite complex composed of LIN7 (LIN7A, LIN7B or LIN7C), CASK and APBA1 associates with the motor protein KIF17 to transport vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules …

**Summary**, from NCBI Gene [55327](https://www.ncbi.nlm.nih.gov/gene/55327):

> Enables L27 domain binding activity and cytoskeletal protein binding activity. Involved in morphogenesis of an epithelial sheet. Located in cell-cell junction; cytoplasm; and plasma membrane. Part of MPP7-DLG1-LIN7 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17789) · Entrez [55327](https://www.ncbi.nlm.nih.gov/gene/55327) · UniProt [Q9NUP9](https://www.uniprot.org/uniprotkb/Q9NUP9) · Ensembl [ENSG00000148943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148943)

## Data

Gene col 7329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7329); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7329]; `tensor/DDL_lfc|DDL_z.npy` [7329]; `embed/gene_vectors.npy` [7329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7329 or target_col == 7329). Every well: [[LIN7C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN7C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
