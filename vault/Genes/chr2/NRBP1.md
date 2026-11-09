---
symbol: "NRBP1"
type: "gene"
col: 3635
ensembl_id: "ENSG00000115216"
name: "nuclear receptor binding protein 1"
location: "2p23.3"
module: 1
arm: "-"
pooled_cpm: 77.33
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NRBP1

*nuclear receptor binding protein 1* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.62× (z +9.0, q 1e-16, up in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.37× (z +6.2, q 1e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.805× (z -4.2, q 0.012, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW480 0.385×, LS 180 0.280×, SW1417 0.355×, NCI-H2347 0.394×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.178×, SW480 0.426×, NCI-H2347 0.393×, LoVo 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.164×, NCI-H1573 0.379×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Entrectinib (drug)]] 5 µM in 1 line (SW 1088 0.0607×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.255×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (SW 1271 0.151×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB18]] (+0.56, fdr 1e-05), [[TRAF6]] (+0.54, fdr 3e-05), [[SAP30L]] (+0.53, fdr 9e-05); moves opposite to [[B3GNTL1]] (-0.57, fdr 4e-05), [[NOC3L]] (-0.54, fdr 1e-05), [[ERCC1]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.0 | 1e-16 | 37/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.8 | 2e-09 | 31/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 1e-07 | 29/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.1 | 1e-07 | 30/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 2e-07 | 30/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +6.0 | 2e-07 | 25/49 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 2e-05 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.1 | 3e-05 | 29/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.9 | 6e-05 | 2/50 (MIA PaCa-2, SW 1088) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +4.9 | 6e-05 | 30/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 3e-04 | 28/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.21×** | +3.7 | 0.010 | 20/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +3.5 | 0.019 | 23/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.5 | 0.019 | 18/49 (NCI-H2030, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +3.5 | 0.019 | 21/48 (NCI-H460, PANC-1, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.019 | 23/49 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.031 | 21/47 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.066 | 18/47 (CFPAC-1, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3635.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW480 0.385×, LS 180 0.280×, SW1417 0.355×, NCI-H2347 0.394×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.178×, SW480 0.426×, NCI-H2347 0.393×, LoVo 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.164×, NCI-H1573 0.379×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Entrectinib (drug)]] 5 µM in 1 line (SW 1088 0.0607×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.255×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (SW 1271 0.151×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -4.2 | 0.012 | 25/48 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.851× | -3.2 | 0.44 | 20/48 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | 0.847× | -3.0 | 0.50 | 20/45 (SW480, LS 180, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 93.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -19.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 78.8 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +11.8) | — |
| [[LoVo (line)]] | wt | 49.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +9.6) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 92.8 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.37× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[SW480 (line)]] | alt | 75.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.98× (z +10.3) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[LS 180 (line)]] | wt | 75.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.49× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[PANC-1 (line)]] | alt | 55.8 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +10.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 43.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.32× (z +8.8) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SW1417 (line)]] | alt | 92.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[AsPC-1 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[CFPAC-1 (line)]] | alt | 61.3 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +8.9) | — |
| [[H4 (line)]] | wt | 67.9 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.255× (z -10.1) |
| [[KATO III (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0607× (z -11.3) |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.151× (z -8.8) |
| [[A-172 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB18]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TRAF6]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[SAP30L]] | +0.53 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[RAB5B]] | +0.52 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SH3GLB1]] | +0.52 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MKRN1]] | +0.50 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CGRRF1]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[PINK1]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[FXR2]] | +0.49 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[SECISBP2L]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RAB6A]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TRAM1]] | +0.48 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNTL1]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NOC3L]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ERCC1]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ZNF121]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CEP83]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CASC19]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MAML2]] | -0.47 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[EGR1]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DPY19L2P1]] | -0.47 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ABCE1]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FOS]] | -0.47 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[DLC1]] | -0.46 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.325). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.3, -51.4); signed map (-22.4, 7.3). **Vector** length 88.5, 20.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | +5.8 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +6.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.4 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | +6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.9 | +1.8 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,427,790-27,442,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCON3, MUDPNP, MADM; previously NRBP |
| Gene groups (HGNC) | Pseudokinases; Nuclear receptor binding protein family |
| Reactome | 4 pathways, smallest: Nuclear Receptor transcription pathway; Dengue Virus-Host Interactions; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHY1](https://www.uniprot.org/uniprotkb/Q9UHY1) (Nuclear receptor-binding protein):

> Required for embryonic development (By similarity). Plays a role in intestinal epithelial cell fate and proliferation, thereby involved in the architectural development of the intestine potentially via the regulation of Wnt-responsive genes (By similarity). May play a role in subcellular trafficking between the endoplasmic reticulum and Golgi apparatus through interactions with the Rho-type GTPases. Binding to the NS3 protein of dengue virus type 2 appears to subvert this activity into the …

**Summary**, from NCBI Gene [29959](https://www.ncbi.nlm.nih.gov/gene/29959):

> Predicted to enable protein homodimerization activity and protein serine/threonine kinase activity. Involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Located in cytosol and endomembrane system. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7993) · Entrez [29959](https://www.ncbi.nlm.nih.gov/gene/29959) · UniProt [Q9UHY1](https://www.uniprot.org/uniprotkb/Q9UHY1) · Ensembl [ENSG00000115216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115216)

## Data

Gene col 3635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3635); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3635]; `tensor/DDL_lfc|DDL_z.npy` [3635]; `embed/gene_vectors.npy` [3635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3635 or target_col == 3635). Every well: [[NRBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
