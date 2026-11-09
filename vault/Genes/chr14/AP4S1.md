---
symbol: "AP4S1"
type: "gene"
col: 1969
ensembl_id: "ENSG00000100478"
name: "adaptor related protein complex 4 subunit sigma 1"
location: "14q12"
module: 35
arm: "+"
pooled_cpm: 15.52
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# AP4S1

*adaptor related protein complex 4 subunit sigma 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.90× (z +41.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.521× (z -11.9, q 5e-30, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBLD]] (+0.82, fdr 7e-06), [[USP34-DT]] (+0.77, fdr 1e-05), [[PPP2R3C]] (+0.75, fdr 1e-05); moves opposite to [[WRAP73]] (-0.69, fdr 3e-05), [[PAFAH1B3]] (-0.67, fdr 1e-04), [[RRP1B]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.90×** | +41.1 | 0e+00 | 47/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +18.4 | 0e+00 | 43/46 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +15.4 | 0e+00 | 40/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +13.4 | 1e-38 | 35/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +10.8 | 6e-25 | 29/40 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +10.3 | 5e-23 | 30/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.7 | 8e-13 | 15/27 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 3e-04 | 16/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.5 | 4e-04 | 14/34 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.001 | 14/47 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.8 | 0.007 | 11/48 (Hs 766T, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.015 | 9/48 (A-427, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.068 | 6/47 (NCI-H1792, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -11.9 | 5e-30 | 41/47 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -10.9 | 2e-25 | 39/48 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -10.7 | 3e-24 | 38/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -7.3 | 4e-11 | 25/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.719×** | -5.8 | 8e-07 | 22/44 (A549, SNU-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.751×** | -5.2 | 2e-05 | 15/47 (SW1417, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.797×** | -4.0 | 0.005 | 16/46 (LS 180, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.815×** | -3.7 | 0.014 | 13/47 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.023 | 4/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.5 | 0.025 | 2/48 (MIA PaCa-2, HCT15) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.12 | 9/48 (AN3 CA, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 12.0 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.155× (z -9.9) |
| [[BT-474 (line)]] | alt | 46.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +17.9) | — |
| [[HOP62 (line)]] | alt | 18.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +16.1) | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +11.5) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.109× (z -10.4) |
| [[SW480 (line)]] | alt | 16.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +19.3) | — |
| [[A-172 (line)]] | wt | 7.59 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +13.3) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.142× (z -10.1) |
| [[C32 (line)]] | wt | 14.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +14.4) | — |
| [[H4 (line)]] | wt | 12.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +10.1) | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0692× (z -10.5) |
| [[HS-578T (line)]] | alt | 7.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.32× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +18.4) | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +11.7) | [[Bortezomib (drug)]] 0.05 µM 0.0477× (z -16.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A498 (line)]] | wt | 5.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +12.6) | — |
| [[A549 (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +13.2) | — |
| [[C-33 A (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 7.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.89× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 8.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +11.4) | — |
| [[J82 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.9) | — |
| [[KATO III (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +13.9) | — |
| [[LoVo (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +19.5) | — |
| [[LS 180 (line)]] | wt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +16.4) | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +18.7) | — |
| [[RKO (line)]] | wt | 9.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.23× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +15.1) | — |
| [[SW48 (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +11.3) | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | +0.82 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[USP34-DT]] | +0.77 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[PPP2R3C]] | +0.75 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.73 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | +0.73 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[VPS52]] | +0.73 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ATXN1L]] | +0.72 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.71 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[LINC01829]] | +0.71 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[ZNF341-AS1]] | +0.71 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.71 | +0.66 / +0.24 | both halves | 5e-04 |  |
| [[DENND6A-AS1]] | +0.71 | +0.72 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.69 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | -0.67 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RRP1B]] | -0.66 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[THEM6]] | -0.66 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[RSAD1]] | -0.65 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[MAST3]] | -0.64 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[SMYD3]] | -0.64 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[NAA40]] | -0.64 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.63 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[C20orf27]] | -0.63 | -0.59 / -0.21 | both halves | 7e-04 |  |
| [[PPP1CC]] | -0.62 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[USP2]] | -0.61 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AP4S1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises AP4S1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.4, 10.6); signed map (22.8, -7.6). **Vector** length 102, 22.3% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.6 | +41.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +18.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +15.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.3 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.5 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.6 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.3 | -10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.2 | -10.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.4 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 4 subunit sigma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:31,025,106-31,130,996 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLA20, AP47B, SPG52 |
| Gene groups (HGNC) | Adaptor related protein complex 4 |
| Reactome | 4 pathways, smallest: Lysosome Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y587](https://www.uniprot.org/uniprotkb/Q9Y587) (AP-4 complex subunit sigma-1):

> Component of the adaptor protein complex 4 (AP-4). Adaptor protein complexes are vesicle coat components involved both in vesicle formation and cargo selection. They control the vesicular transport of proteins in different trafficking pathways. AP-4 forms a non clathrin-associated coat on vesicles departing the trans-Golgi network (TGN) and may be involved in the targeting of proteins from the trans-Golgi network (TGN) to the endosomal-lysosomal system. It is also involved in protein sorting to …

**Summary**, from NCBI Gene [11154](https://www.ncbi.nlm.nih.gov/gene/11154):

> This gene encodes a member of the adaptor complexes small subunit protein family. These proteins are components of the heterotetrameric adaptor protein complexes, which play important roles in the secretory and endocytic pathways by mediating vesicle formation and sorting of integral membrane proteins. The encoded protein is the small subunit of adaptor protein complex-4, which is associated with both clathrin- and nonclathrin-coated vesicles. Mutations in this gene are associated with spastic …

**Accessions** — [HGNC:575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:575) · Entrez [11154](https://www.ncbi.nlm.nih.gov/gene/11154) · UniProt [Q9Y587](https://www.uniprot.org/uniprotkb/Q9Y587) · Ensembl [ENSG00000100478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100478)

## Data

Gene col 1969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1969); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1969]; `tensor/DDL_lfc|DDL_z.npy` [1969]; `embed/gene_vectors.npy` [1969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1969 or target_col == 1969). Every well: [[AP4S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP4S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
