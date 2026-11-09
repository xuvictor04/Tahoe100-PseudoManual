---
symbol: "DNAJC21"
type: "gene"
col: 9688
ensembl_id: "ENSG00000168724"
name: "DnaJ heat shock protein family (Hsp40) member C21"
location: "5p13.2"
module: 20
arm: "-"
pooled_cpm: 86.48
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DNAJC21

*DnaJ heat shock protein family (Hsp40) member C21* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +15.2, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.64× (z +7.7, q 2e-12, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.760× (z -4.0, q 0.039, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.156×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.330×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITSN2]] (+0.69, fdr 7e-06), [[UPF3B]] (+0.62, fdr 1e-05), [[UBXN2A]] (+0.61, fdr 1e-05); moves opposite to [[ATP5F1B]] (-0.60, fdr 1e-05), [[PHB1]] (-0.58, fdr 3e-05), [[MDH2]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HACD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.01×** | +15.2 | 0e+00 | 46/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.96×** | +10.4 | 1e-22 | 44/49 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.89×** | +9.5 | 6e-19 | 36/43 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +8.0 | 3e-13 | 42/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +7.7 | 2e-12 | 40/48 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +6.5 | 6e-09 | 32/45 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.50×** | +6.3 | 3e-08 | 41/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.47×** | +6.0 | 2e-07 | 35/48 (SW480, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.7 | 6e-07 | 33/47 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.7 | 6e-07 | 40/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 37/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.35×** | +4.6 | 2e-04 | 35/48 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.37×** | +4.6 | 2e-04 | 36/47 (AsPC-1, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +4.6 | 2e-04 | 26/49 (NCI-H460, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.34×** | +4.5 | 2e-04 | 28/48 (C32, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 5e-04 | 32/48 (SNU-423, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.156×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.330×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.760×** | -4.0 | 0.039 | 29/47 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.867× | -3.1 | 0.30 | 9/48 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.680× | -3.1 | 0.30 | 23/48 (HOP62, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.818× | -3.1 | 0.30 | 20/48 (LOX-IMVI, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 90.6 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 77.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 69.2 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.8) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[HEC-1-A (line)]] | alt | 65.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 81.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 93.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 69.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 38.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.7) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[LoVo (line)]] | wt | 91.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 72.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 87.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 190 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 61.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 76.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 88.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 51.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 69.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 61.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 78.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 88.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H596 (line)]] | alt | 77.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.156× (z -11.3) |
| [[SNU-1 (line)]] | wt | 77.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 58.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITSN2]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[UPF3B]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[UBXN2A]] | +0.61 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[GATAD1]] | +0.60 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[WBP4]] | +0.59 | +0.67 / +0.53 | both halves | 1e-05 | same gene group |
| [[NFKBIB]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.57 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.57 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[CHMP4A]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[RAB13]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MAFG]] | +0.56 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[SNRNP27]] | +0.55 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | -0.60 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[PHB1]] | -0.58 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[MDH2]] | -0.54 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[FKBP1A]] | -0.53 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TBRG4]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[C19orf48]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[C1QBP]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PAICS]] | -0.49 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NIF3L1]] | -0.49 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[ALG3]] | -0.48 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[TUBB]] | -0.48 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.48 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACD1]] | B | HACD1 activity raises DNAJC21's level | lines that do not express HACD1 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without HACD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLSTN3, CDR2L, PIM1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.6, -15.7); signed map (3.6, -12.3). **Vector** length 92.3, 27.7% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.3 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.8 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:34,929,559-34,958,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GS3, DNAJA5, JJJ1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers matrin-type; DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5F1R6](https://www.uniprot.org/uniprotkb/Q5F1R6) (DnaJ homolog subfamily C member 21):

> May act as a co-chaperone for HSP70. May play a role in ribosomal RNA (rRNA) biogenesis, possibly in the maturation of the 60S subunit. Binds the precursor 45S rRNA.

**Summary**, from NCBI Gene [134218](https://www.ncbi.nlm.nih.gov/gene/134218):

> This gene encodes a member of the DNAJ heat shock protein 40 family of proteins that is characterized by two N-terminal tetratricopeptide repeat domains and a C-terminal DNAJ domain. This protein binds the precursor 45S ribosomal RNA and may be involved in early nuclear ribosomal RNA biogenesis and maturation of the 60S ribosomal subunit. Mutations in this gene result in Bone marrow failure syndrome 3. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:27030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27030) · Entrez [134218](https://www.ncbi.nlm.nih.gov/gene/134218) · UniProt [Q5F1R6](https://www.uniprot.org/uniprotkb/Q5F1R6) · Ensembl [ENSG00000168724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168724)

## Data

Gene col 9688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9688); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9688]; `tensor/DDL_lfc|DDL_z.npy` [9688]; `embed/gene_vectors.npy` [9688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9688 or target_col == 9688). Every well: [[DNAJC21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
