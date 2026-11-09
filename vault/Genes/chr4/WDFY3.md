---
symbol: "WDFY3"
type: "gene"
col: 8734
ensembl_id: "ENSG00000163625"
name: "WD repeat and FYVE domain containing 3"
location: "4q21.23"
module: 46
arm: "+"
pooled_cpm: 209.24
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# WDFY3

*WD repeat and FYVE domain containing 3* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.37× (z +6.1, q 6e-07, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.243× (z -27.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOA2]] (+0.76, fdr 7e-06), [[ARID1B]] (+0.72, fdr 1e-05), [[TLK2]] (+0.71, fdr 3e-05); moves opposite to [[CMIP]] (-0.59, fdr 4e-05), [[SLC25A32]] (-0.58, fdr 3e-05), [[MIER2]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.1 | 6e-07 | 32/47 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.010 | 27/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.023 | 33/48 (A-427, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.15× | +3.8 | 0.023 | 15/47 (LoVo, A-427, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.026 | 24/47 (SW 900, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.070 | 28/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.243×** | -27.1 | 0e+00 | 47/47 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.273×** | -24.8 | 0e+00 | 47/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.315×** | -22.1 | 0e+00 | 47/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.348×** | -19.4 | 0e+00 | 43/43 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.377×** | -16.9 | 0e+00 | 48/48 (RKO, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.415×** | -15.6 | 0e+00 | 43/44 (CHP-212, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.488×** | -13.7 | 7e-41 | 47/47 (NCI-H23, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.587×** | -10.2 | 2e-22 | 46/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -8.9 | 3e-17 | 44/46 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -7.9 | 1e-13 | 43/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.705×** | -6.7 | 1e-09 | 44/47 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -4.5 | 3e-04 | 21/47 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.848× | -4.4 | 4e-04 | 24/47 (NCI-H1792, LoVo, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -3.8 | 0.005 | 30/48 (C-33 A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.867× | -3.8 | 0.005 | 8/47 (HT-29, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 366 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -23.3) |
| [[HOP62 (line)]] | alt | 229 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -25.8) |
| [[HT-29 (line)]] | alt | 224 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -29.0) |
| [[NCI-H1573 (line)]] | alt | 352 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.306× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 259 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -20.9) |
| [[C32 (line)]] | wt | 218 | 0 | 8 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.306× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 250 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -18.9) |
| [[HCT15 (line)]] | alt | 335 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -15.6) |
| [[LoVo (line)]] | wt | 186 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -28.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.285× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 159 | 1 (1 ⚠) | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -19.8) |
| [[SNU-423 (line)]] | alt | 152 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -28.4) |
| [[SW480 (line)]] | alt | 138 | 1 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.19× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.141× (z -29.8) |
| [[A-172 (line)]] | wt | 237 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -19.7) |
| [[A549 (line)]] | wt | 209 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -24.8) |
| [[H4 (line)]] | wt | 244 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 230 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 203 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 197 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0665× (z -35.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 175 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -24.8) |
| [[RPMI-7951 (line)]] | alt | 219 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -15.5) |
| [[SW 900 (line)]] | alt | 191 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -15.8) |
| [[SW1417 (line)]] | alt | 176 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -22.8) |
| [[A498 (line)]] | wt | 224 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -20.9) |
| [[AsPC-1 (line)]] | alt | 194 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -21.2) |
| [[C-33 A (line)]] | alt | 289 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -19.9) |
| [[CHP-212 (line)]] | wt | 283 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0381× (z -28.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.161× (z -17.0) |
| [[HS-578T (line)]] | alt | 165 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -24.0) |
| [[hTERT-HPNE (line)]] | wt | 245 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -18.2) |
| [[LS 180 (line)]] | wt | 244 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.185× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -20.5) |
| [[PANC-1 (line)]] | alt | 172 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -20.8) |
| [[RKO (line)]] | wt | 279 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -22.0) |
| [[SK-MEL-2 (line)]] | alt | 182 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -18.2) |
| [[SW48 (line)]] | wt | 290 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.216× (z -15.9) |
| [[A-427 (line)]] | wt | 184 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.446× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 190 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -23.0) |
| [[NCI-H2030 (line)]] | alt | 207 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.493× (z -9.5) |
| [[SHP-77 (line)]] | alt | 237 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -18.2) |
| [[SNU-1 (line)]] | wt | 289 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -12.5) |
| [[AN3 CA (line)]] | alt | 372 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -11.6) |
| [[BT-474 (line)]] | alt | 226 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.8) |
| [[COLO 205 (line)]] | alt | 228 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -25.9) |
| [[Hs 766T (line)]] | wt | 142 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -20.8) |
| [[J82 (line)]] | alt | 129 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -17.2) |
| [[SW 1271 (line)]] | alt | 208 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -9.6) |
| [[KATO III (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA2]] | +0.76 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ARID1B]] | +0.72 | +0.57 / +0.65 | both halves | 1e-05 | same gene group |
| [[TLK2]] | +0.71 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[RAF1]] | +0.65 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HOXB7]] | +0.64 | +0.29 / +0.49 | both halves | 3e-04 |  |
| [[CREBBP]] | +0.63 | +0.29 / +0.55 | both halves | 2e-04 |  |
| [[MKLN1]] | +0.62 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ACOT2]] | +0.61 | +0.30 / +0.44 | both halves | 2e-04 |  |
| [[DECR1]] | +0.61 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[KANSL1]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PCMTD1]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[DHRS4]] | +0.60 | +0.40 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | -0.59 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SLC25A32]] | -0.58 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MIER2]] | -0.58 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[KCTD20]] | -0.58 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[EHD4]] | -0.54 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[TXNL4A]] | -0.54 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[IER2]] | -0.52 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[GNB1L]] | -0.52 | -0.27 / -0.43 | both halves | 3e-04 | same gene group |
| [[TAF1A]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[DGKD]] | -0.51 | -0.18 / -0.35 | ⚠ not reproduced | 1e-03 |  |
| [[BCAN-AS2]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[AP1M1]] | -0.51 | -0.24 / -0.32 | both halves | 4e-04 |  |
| [[DDX19A]] | -0.51 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[N4BP3]] | -0.50 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises WDFY3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.6, 14.4); signed map (27.8, -23.3). **Vector** length 102, 39.1% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.3 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.1 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.6 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +8.5 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -13.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -22.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -27.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat and FYVE domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:84,668,765-84,966,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0993, ALFY, ZFYVE25 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; WD repeat domain containing; BEACH domain containing ; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZQ1](https://www.uniprot.org/uniprotkb/Q8IZQ1) (WD repeat and FYVE domain-containing protein 3):

> Required for selective macroautophagy (aggrephagy). Acts as an adapter protein by linking specific proteins destined for degradation to the core autophagic machinery members, such as the ATG5-ATG12-ATG16L E3-like ligase, SQSTM1 and LC3. Along with p62/SQSTM1, involved in the formation and autophagic degradation of cytoplasmic ubiquitin-containing inclusions (p62 bodies, ALIS/aggresome-like induced structures). Along with SQSTM1, required to recruit ubiquitinated proteins to PML bodies in the …

**Summary**, from NCBI Gene [23001](https://www.ncbi.nlm.nih.gov/gene/23001):

> This gene encodes a phosphatidylinositol 3-phosphate-binding protein that functions as a master conductor for aggregate clearance by autophagy. This protein shuttles from the nuclear membrane to colocalize with aggregated proteins, where it complexes with other autophagic components to achieve macroautophagy-mediated clearance of these aggregated proteins. However, it is not necessary for starvation-induced macroautophagy. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:20751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20751) · Entrez [23001](https://www.ncbi.nlm.nih.gov/gene/23001) · UniProt [Q8IZQ1](https://www.uniprot.org/uniprotkb/Q8IZQ1) · Ensembl [ENSG00000163625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163625)

## Data

Gene col 8734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8734); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8734]; `tensor/DDL_lfc|DDL_z.npy` [8734]; `embed/gene_vectors.npy` [8734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8734 or target_col == 8734). Every well: [[WDFY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDFY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
