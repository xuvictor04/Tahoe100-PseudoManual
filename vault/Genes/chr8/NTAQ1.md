---
symbol: "NTAQ1"
type: "gene"
col: 8013
ensembl_id: "ENSG00000156795"
name: "N-terminal glutamine amidase 1"
location: "8q24.13"
module: 199
arm: "+"
pooled_cpm: 17.49
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# NTAQ1

*N-terminal glutamine amidase 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.16× (z +13.0, q 8e-36, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.329× (z -26.6, q 0e+00, down in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.495× (z -11.9, q 3e-30, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP93]] (+0.74, fdr 7e-06), [[FAM20B]] (+0.71, fdr 7e-06), [[VKORC1L1]] (+0.68, fdr 7e-06); moves opposite to [[C11orf58]] (-0.66, fdr 7e-06), [[ZNF764]] (-0.66, fdr 1e-05), [[SGO1-AS1]] (-0.64, fdr 1e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +13.0 | 8e-36 | 40/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +11.3 | 3e-27 | 40/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +10.8 | 7e-25 | 39/47 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +7.0 | 4e-10 | 24/46 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.1 | 1e-07 | 27/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.4 | 7e-04 | 12/47 (HT-29, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 7e-04 | 13/44 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.003 | 11/46 (NCI-H2347, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.003 | 12/47 (J82, A549, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +3.4 | 0.046 | 13/48 (C-33 A, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~97% of this change | 1.20× | +3.0 | 0.13 | 16/42 (H4, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8013.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.329×** | -26.6 | 0e+00 | 38/46 (PANC-1, HT-29, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.354×** | -16.9 | 0e+00 | 39/46 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.495×** | -11.9 | 3e-30 | 33/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -9.8 | 3e-20 | 29/45 (C-33 A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.578×** | -9.3 | 2e-18 | 28/45 (PANC-1, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.369×** | -8.8 | 1e-16 | 36/46 (NCI-H23, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.609×** | -8.4 | 4e-15 | 27/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -6.6 | 3e-09 | 25/47 (HT-29, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -6.6 | 3e-09 | 25/47 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -6.1 | 8e-08 | 26/42 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.579×** | -4.8 | 7e-05 | 21/43 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.776×** | -4.1 | 0.002 | 18/41 (J82, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.824×** | -3.3 | 0.044 | 16/47 (RKO, J82, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.088 | 6/47 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.6 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -23.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.291× (z -9.6) |
| [[HT-29 (line)]] | alt | 41.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -21.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -10.3) |
| [[A498 (line)]] | wt | 23.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -20.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.308× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 20.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -19.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 21.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Rosiglitazone (drug)]] 5 µM 0.197× (z -8.7) |
| [[SW 900 (line)]] | alt | 6.75 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0806× (z -9.8) |
| [[SW480 (line)]] | alt | 15.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -15.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0890× (z -9.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0845× (z -9.2) |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 9.43 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 7.25 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.226× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0876× (z -9.9) |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 10.2 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0599× (z -9.5) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | +0.74 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[VKORC1L1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[FAR1]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[WDR5]] | +0.67 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CPSF4]] | +0.66 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[EEF1E1]] | +0.64 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[TREX2]] | +0.64 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[MTERF3]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TCF3]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TBC1D24]] | +0.63 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PEMT]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.66 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.66 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.64 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ZFHX2]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.64 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.64 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[HHLA3]] | -0.64 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.64 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[DPY19L2P2]] | -0.64 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[LARP7]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[XRN1]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity weakens NTAQ1's drug response | lines that do not express NT5M (7) vs lines expressing it (41) | the lines without NT5M respond 1.22× as strongly (z diff -0.65); strongest at Belinostat 5 µM: 2.71x vs 1.84x (z diff -2.8) | 0.013 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[LGALS3]] | B | LGALS3 activity lowers NTAQ1's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without LGALS3 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[HDAC6]] | B | HDAC6 activity lowers NTAQ1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.5, -28.0); signed map (-43.4, -15.6). **Vector** length 87.6, 18.3% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +10.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +13.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | -0.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.4 | -26.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.1 | -16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.6 | -9.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | N-terminal glutamine amidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,416,726-123,470,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10204; previously C8orf32, WDYHV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HA8](https://www.uniprot.org/uniprotkb/Q96HA8) (Protein N-terminal glutamine amidohydrolase):

> Mediates the side-chain deamidation of N-terminal glutamine residues to glutamate, an important step in N-end rule pathway of protein degradation. Conversion of the resulting N-terminal glutamine to glutamate renders the protein susceptible to arginylation, polyubiquitination and degradation as specified by the N-end rule. Does not act on substrates with internal or C-terminal glutamine and does not act on non-glutamine residues in any position. Does not deaminate acetylated N-terminal …

**Summary**, from NCBI Gene [55093](https://www.ncbi.nlm.nih.gov/gene/55093):

> Predicted to enable protein-N-terminal glutamine amidohydrolase activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25490) · Entrez [55093](https://www.ncbi.nlm.nih.gov/gene/55093) · UniProt [Q96HA8](https://www.uniprot.org/uniprotkb/Q96HA8) · Ensembl [ENSG00000156795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156795)

## Data

Gene col 8013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8013); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8013]; `tensor/DDL_lfc|DDL_z.npy` [8013]; `embed/gene_vectors.npy` [8013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8013 or target_col == 8013). Every well: [[NTAQ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTAQ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
