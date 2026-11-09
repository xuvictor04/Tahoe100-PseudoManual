---
symbol: "ADAM23"
type: "gene"
col: 3605
ensembl_id: "ENSG00000114948"
name: "ADAM metallopeptidase domain 23"
location: "2q33.3"
module: 102
arm: "+"
pooled_cpm: 21.98
n_lines_expressing: 24
n_dd_up: 38
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# ADAM23

*ADAM metallopeptidase domain 23* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +25.0, q 0e+00, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.888× (z -6.4, q 8e-08, down in 3 of 22 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.797× (z -3.6, q 0.079, down in 4 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 0.158×, A-427 0.206×, LOX-IMVI 0.274×, NCI-H23 0.322×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.133×, C-33 A 0.102×, A-172 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.156×, LOX-IMVI 0.291×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.194×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H661 0.0702×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (NCI-H661 0.0724×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBPMS2]] (+0.64, fdr 1e-05), [[C12orf56]] (+0.58, fdr 1e-05), [[CHMP1B2P]] (+0.57, fdr 1e-05); moves opposite to [[SENP2]] (-0.48, fdr 3e-05), [[ZNF33A]] (-0.45, fdr 6e-05), [[STK19]] (-0.43, fdr 1e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[NBPF20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +25.0 | 0e+00 | 12/21 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +19.8 | 0e+00 | 22/22 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.32×** | +13.5 | 3e-39 | 21/22 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +12.1 | 2e-31 | 8/22 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +11.9 | 1e-30 | 4/21 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.90×** | +10.3 | 1e-22 | 10/21 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.1 | 5e-22 | 5/17 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.9 | 3e-17 | 12/21 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +8.9 | 5e-17 | 17/22 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +7.6 | 1e-12 | 14/22 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.59×** | +7.5 | 4e-12 | 13/22 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.5 | 4e-12 | 11/22 (A549, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +7.1 | 4e-11 | 13/22 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.55×** | +7.1 | 7e-11 | 10/22 (C32, NCI-H1792, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +6.8 | 3e-10 | 6/22 (NCI-H1792, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 2e-07 | 10/22 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 6e-07 | 11/22 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 1e-05 | 12/22 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.3 | 4e-04 | 9/22 (NCI-H1792, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +4.2 | 7e-04 | 13/22 (LOX-IMVI, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 0.158×, A-427 0.206×, LOX-IMVI 0.274×, NCI-H23 0.322×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.133×, C-33 A 0.102×, A-172 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.156×, LOX-IMVI 0.291×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.194×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H661 0.0702×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (NCI-H661 0.0724×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -6.4 | 8e-08 | 3/22 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.797×** | -3.6 | 0.079 | 4/22 (NCI-H2030, A-172, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.800× | -3.3 | 0.15 | 0/22 | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.809× | -3.3 | 0.15 | 1/22 (SW 900) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.821× | -3.2 | 0.15 | 0/22 | two highest doses |  |
| [[Sunitinib (drug)]] 0.5 µM |  | 0.821× | -3.2 | 0.15 | 3/22 (NCI-H1573, SW 1271, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.817× | -3.0 | 0.20 | 0/22 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 68.4 | 2 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -23.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 147 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +14.9) | — |
| [[A549 (line)]] | wt | 28.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 65.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -21.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 10.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 70.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -16.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 46.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -11.5) |
| [[C-33 A (line)]] | alt | 76.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[C32 (line)]] | wt | 26.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 8.61 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.90× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.91× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0702× (z -8.7) |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.585× (z -12.4) ⚠ position not correctable |
| [[hTERT-HPNE (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0853× (z -10.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[AN3 CA (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPMS2]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[C12orf56]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CHMP1B2P]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DOCK3]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MARK1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ADCY1]] | +0.55 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[BVES-AS1]] | +0.54 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PHF21B]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LRRN2]] | +0.52 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[KALRN]] | +0.52 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CRMP1]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[MEGF11]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP2]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ZNF33A]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[STK19]] | -0.43 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[TOGARAM1]] | -0.43 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[CWC25]] | -0.43 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[RAB11B-AS1]] | -0.42 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[MMUT]] | -0.42 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[ZBTB5]] | -0.42 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAM23's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[B4GALNT1]] | C | B4GALNT1 activity raises ADAM23's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 5.10× lower at baseline in the lines without B4GALNT1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBPF20]] | B | ADAM23 activity raises NBPF20's level | lines that do not express ADAM23 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without ADAM23 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, GALNT13, CNRIP1 |
| [[B4GALNT1]] | C | ADAM23 activity raises B4GALNT1's level | lines that do not express ADAM23 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without ADAM23 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, GALNT13, CNRIP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.7, 35.8); signed map (27.0, 23.8). **Vector** length 71.5, 20.1% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +6.3 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -6.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -1.9 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:206,443,532-206,621,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDC3 |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 1 pathways, smallest: LGI-ADAM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O75077](https://www.uniprot.org/uniprotkb/O75077) (Disintegrin and metalloproteinase domain-containing protein 23):

> May play a role in cell-cell and cell-matrix interactions. This is a non-catalytic metalloprotease-like protein.

**Summary**, from NCBI Gene [8745](https://www.ncbi.nlm.nih.gov/gene/8745):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. It is reported that inactivation of this gene is associated with tumorigenesis in human cancers. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:202) · Entrez [8745](https://www.ncbi.nlm.nih.gov/gene/8745) · UniProt [O75077](https://www.uniprot.org/uniprotkb/O75077) · Ensembl [ENSG00000114948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114948)

## Data

Gene col 3605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3605); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3605]; `tensor/DDL_lfc|DDL_z.npy` [3605]; `embed/gene_vectors.npy` [3605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3605 or target_col == 3605). Every well: [[ADAM23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
