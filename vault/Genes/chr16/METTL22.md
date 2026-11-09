---
symbol: "METTL22"
type: "gene"
col: 860
ensembl_id: "ENSG00000067365"
name: "methyltransferase 22, Kin17 lysine"
location: "16p13.2"
module: 89
arm: "+"
pooled_cpm: 19.43
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# METTL22

*methyltransferase 22, Kin17 lysine* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.48× (z +8.2, q 9e-14, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.441× (z -14.2, q 6e-43, down in 34 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.859× (z -3.7, q 0.012, down in 12 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LS 180 0.0516×, NCI-H1573 0.0751×, LoVo 0.0824×, AsPC-1 0.116×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (HOP62 0.0482×, KATO III 0.131×, HEC-1-A 0.167×, SNU-423 0.167×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1792 0.0501×, SW480 0.258×, HCT15 0.117×; ⚠ toxic; transcription drop); [[Bendamustine (drug)]] 5 µM in 2 lines (C32 0.148×, SW48 0.0955×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.181×); [[Pralsetinib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0583×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLL]] (+0.77, fdr 7e-06), [[ALKBH3]] (+0.69, fdr 7e-06), [[ZNF133]] (+0.68, fdr 7e-06); moves opposite to [[TJP1]] (-0.65, fdr 1e-05), [[KLF12]] (-0.56, fdr 1e-05), [[DIAPH1]] (-0.55, fdr 1e-04).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +8.2 | 9e-14 | 34/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.31×** | +6.7 | 5e-09 | 29/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.5 | 2e-08 | 26/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.41×** | +6.0 | 4e-07 | 29/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +5.9 | 5e-07 | 28/47 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +5.5 | 3e-06 | 24/45 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.096 | 16/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.13 | 1/46 (HT-29) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.13 | 7/48 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.15 | 17/48 (hTERT-HPNE, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 860.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LS 180 0.0516×, NCI-H1573 0.0751×, LoVo 0.0824×, AsPC-1 0.116×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (HOP62 0.0482×, KATO III 0.131×, HEC-1-A 0.167×, SNU-423 0.167×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1792 0.0501×, SW480 0.258×, HCT15 0.117×; ⚠ toxic; transcription drop); [[Bendamustine (drug)]] 5 µM in 2 lines (C32 0.148×, SW48 0.0955×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.181×); [[Pralsetinib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.441×** | -14.2 | 6e-43 | 34/42 (LS 180, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.460×** | -12.4 | 5e-33 | 28/37 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.554×** | -9.8 | 2e-20 | 20/32 (HOP62, KATO III, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.793×** | -5.7 | 2e-06 | 24/48 (H4, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.728×** | -5.5 | 5e-06 | 23/48 (SW 1088, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.772×** | -4.5 | 7e-04 | 20/48 (AN3 CA, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.775×** | -4.2 | 0.002 | 21/46 (SNU-423, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.1 | 0.002 | 2/48 (SW48, CHP-212) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.781×** | -4.1 | 0.002 | 19/47 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -3.7 | 0.012 | 12/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.809×** | -3.7 | 0.013 | 12/48 (LOX-IMVI, SW 1088, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.867× | -3.5 | 0.022 | 9/48 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.818×** | -3.5 | 0.022 | 10/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | 0.836× | -3.1 | 0.078 | 11/45 (SNU-423, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 0.05 µM |  | **0.831×** | -3.0 | 0.092 | 15/48 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 32.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.181× (z -9.6) |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Pralsetinib (drug)]] 5 µM 0.0583× (z -8.9) |
| [[SW48 (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0933× (z -10.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.0955× (z -10.0) |
| [[SW480 (line)]] | alt | 23.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 15.6 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.148× (z -10.4) |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0482× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0824× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0516× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0751× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0501× (z -20.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLL]] | +0.77 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.68 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[TMEM94]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[USP30]] | +0.65 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TEFM]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZSCAN25]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MAFIP]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.64 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[CIAO3]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.63 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.63 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP1]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[KLF12]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.55 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[STIM2]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[CRY1]] | -0.54 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[EPB41L2]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SGMS2]] | -0.53 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[WWC2]] | -0.53 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[ZSWIM6]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PRKCA]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TPM4]] | -0.53 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[CALM2]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers METTL22's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises METTL22's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.1, -6.1); signed map (-14.6, -18.0). **Vector** length 70.4, 11.7% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.3 | +6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.1 | +5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.9 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -4.0 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.0 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 22, Kin17 lysine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:8,621,683-8,649,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12433, MGC2654; previously C16orf68 |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUU2](https://www.uniprot.org/uniprotkb/Q9BUU2) (Methyltransferase-like protein 22):

> Protein N-lysine methyltransferase. Trimethylates KIN at Lys-135 (in vitro).

**Summary**, from NCBI Gene [79091](https://www.ncbi.nlm.nih.gov/gene/79091):

> This gene encodes a member of the non-histone lysine methyltransferases. It interacts with its substrate, Kin17, which is involved in DNA repair and replication and mRNA processing. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:28368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28368) · Entrez [79091](https://www.ncbi.nlm.nih.gov/gene/79091) · UniProt [Q9BUU2](https://www.uniprot.org/uniprotkb/Q9BUU2) · Ensembl [ENSG00000067365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067365)

## Data

Gene col 860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 860); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 860]; `tensor/DDL_lfc|DDL_z.npy` [860]; `embed/gene_vectors.npy` [860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 860 or target_col == 860). Every well: [[METTL22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
