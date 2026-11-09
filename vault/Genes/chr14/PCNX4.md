---
symbol: "PCNX4"
type: "gene"
col: 4761
ensembl_id: "ENSG00000126773"
name: "pecanex 4"
location: "14q23.1"
module: 17
arm: "-"
pooled_cpm: 159.86
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PCNX4

*pecanex 4* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.21× (z +4.5, q 0.003, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 2.01×, LOX-IMVI 1.69×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.569× (z -13.5, q 7e-39, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HELQ]] (+0.54, fdr 4e-05), [[PPP3CB]] (+0.54, fdr 1e-05), [[PIGL]] (+0.54, fdr 3e-05); moves opposite to [[MPP1]] (-0.56, fdr 4e-05), [[CAPN5]] (-0.55, fdr 1e-04), [[ARHGEF10L]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 2.01×, LOX-IMVI 1.69×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +4.5 | 0.003 | 23/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.038 | 13/48 (SNU-423, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.064 | 14/47 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.11× | +3.4 | 0.086 | 8/48 (Hs 766T, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.10× | +3.2 | 0.17 | 1/49 (AN3 CA) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.569×** | -13.5 | 7e-39 | 42/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -13.1 | 6e-37 | 34/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -13.1 | 7e-37 | 46/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -12.0 | 8e-31 | 41/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -11.4 | 3e-28 | 41/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -9.9 | 6e-21 | 37/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.663×** | -9.1 | 6e-18 | 30/45 (C-33 A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.709×** | -8.2 | 1e-14 | 33/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.529×** | -8.0 | 9e-14 | 37/45 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -7.9 | 2e-13 | 36/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -7.7 | 9e-13 | 31/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -7.3 | 1e-11 | 28/48 (SW480, SW48, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.822×** | -6.6 | 2e-09 | 26/49 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -5.9 | 1e-07 | 29/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.829×** | -4.5 | 3e-04 | 24/48 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -3.7 | 0.005 | 9/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.027 | 18/49 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Allopurinol (drug)]] 0.05 µM |  | 0.882× | -3.0 | 0.063 | 12/48 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.794×** | -2.9 | 0.088 | 12/48 (RKO, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 220 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -24.5) |
| [[RKO (line)]] | wt | 403 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -16.9) |
| [[A-427 (line)]] | wt | 160 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.418× (z -13.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -10.0) |
| [[PANC-1 (line)]] | alt | 145 | 0 | 9 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.506× (z -12.8) |
| [[A549 (line)]] | wt | 175 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -21.8) |
| [[HEC-1-A (line)]] | alt | 229 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.1) |
| [[SW480 (line)]] | alt | 182 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -15.4) |
| [[C-33 A (line)]] | alt | 333 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 263 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.356× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 210 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -17.3) |
| [[SW48 (line)]] | wt | 148 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.238× (z -12.4) |
| [[HOP62 (line)]] | alt | 199 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.414× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 179 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.653× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 199 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.434× (z -9.6) |
| [[LoVo (line)]] | wt | 123 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.376× (z -12.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.524× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 240 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -20.9) |
| [[AN3 CA (line)]] | alt | 159 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -10.4) |
| [[BT-474 (line)]] | alt | 78.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.373× (z -9.4) |
| [[H4 (line)]] | wt | 252 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -10.7) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.372× (z -8.7) |
| [[J82 (line)]] | alt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 256 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.480× (z -9.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -9.1) |
| [[SNU-1 (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.227× (z -18.4) |
| [[SW 900 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -12.4) |
| [[A-172 (line)]] | wt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.0) | — |
| [[A498 (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[CHP-212 (line)]] | wt | 247 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0605× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[hTERT-HPNE (line)]] | wt | 197 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.7) |
| [[LS 180 (line)]] | wt | 97.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.481× (z -8.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.391× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -8.5) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.6) |
| [[SW 1088 (line)]] | alt | 182 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -8.9) |
| [[C32 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELQ]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PPP3CB]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PIGL]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[C10orf88]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[OPA3]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NCOA5]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ATF1]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[JPX]] | +0.52 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SATB2]] | +0.52 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[HCG18]] | +0.52 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.51 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[ERCC6L2]] | +0.51 | +0.48 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP1]] | -0.56 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[CAPN5]] | -0.55 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[ARHGEF10L]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[FAM102A]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CD99P1]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[IDH1]] | -0.50 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[YPEL2]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[OTULIN]] | -0.49 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SEMA4D]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[USP3]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MICE]] | -0.48 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[AHDC1]] | -0.47 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity lowers PCNX4's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.53× higher at baseline in the lines without IRF6 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MSRB3]] | B | MSRB3 activity raises PCNX4's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MSRB3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[IRF6]] | B | IRF6 activity weakens PCNX4's drug response | lines that do not express IRF6 (31) vs lines expressing it (17) | the lines without IRF6 respond 1.26× as strongly (z diff -1.49); strongest at Dinaciclib 0.05 µM: 0.60x vs 0.88x (z diff -3.1) | 0.093 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.231). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (0.6, 5.5); signed map (13.1, -0.5). **Vector** length 110, 33.1% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.5 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.8 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +6.3 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.5 | +2.3 |
| fall | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.7 | -8.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -12.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | -3.4 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | pecanex 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,091,911-60,169,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf135, PCNXL4 |
| Gene groups (HGNC) | Pecanex family |
| Matched by | ensembl_id |

UniProt [Q63HM2](https://www.uniprot.org/uniprotkb/Q63HM2) carries no function annotation.

**Summary**, from NCBI Gene [64430](https://www.ncbi.nlm.nih.gov/gene/64430):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20349) · Entrez [64430](https://www.ncbi.nlm.nih.gov/gene/64430) · UniProt [Q63HM2](https://www.uniprot.org/uniprotkb/Q63HM2) · Ensembl [ENSG00000126773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126773)

## Data

Gene col 4761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4761); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4761]; `tensor/DDL_lfc|DDL_z.npy` [4761]; `embed/gene_vectors.npy` [4761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4761 or target_col == 4761). Every well: [[PCNX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
