---
symbol: "NIBAN2"
type: "gene"
col: 5914
ensembl_id: "ENSG00000136830"
name: "niban apoptosis regulator 2"
location: "9q34.11"
module: 174
arm: "+"
pooled_cpm: 156.91
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 52
n_dd_up_clean: 2
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 31
direction_downstream: 33
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# NIBAN2

*niban apoptosis regulator 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.40× (z +5.2, q 1e-04, up in 29 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 1 line (Hs 766T 3.47×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 3.45×); [[Clobetasol propionate (drug)]] 5 µM in 1 line (Hs 766T 3.29×).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.152× (z -40.2, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPCAL1]] (+0.76, fdr 7e-06), [[PTPN12]] (+0.73, fdr 7e-06), [[ACOT7]] (+0.72, fdr 7e-06); moves opposite to [[ZSCAN31]] (-0.57, fdr 2e-05), [[FAM111A-DT]] (-0.55, fdr 1e-05), [[DRAM1]] (-0.55, fdr 8e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[MLPH]] → it (grade B ⚠); 33 go from it, the strongest it → [[ITGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 1 line (Hs 766T 3.47×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 3.45×); [[Clobetasol propionate (drug)]] 5 µM in 1 line (Hs 766T 3.29×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 1e-04 | 29/42 (RKO, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.097 | 20/43 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.25× | +3.2 | 0.19 | 22/42 (RKO, NCI-H460, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.50× | +3.2 | 0.19 | 23/43 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.49× | +3.1 | 0.19 | 19/43 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.152×** | -40.2 | 0e+00 | 42/43 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.251×** | -20.1 | 0e+00 | 43/43 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.424×** | -18.3 | 0e+00 | 42/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.313×** | -17.5 | 0e+00 | 42/42 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.404×** | -13.6 | 3e-40 | 40/43 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.420×** | -12.6 | 3e-34 | 41/42 (HepG2/C3A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.471×** | -11.3 | 7e-28 | 39/43 (NCI-H1573, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.487×** | -10.4 | 1e-23 | 38/43 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.524×** | -9.7 | 1e-20 | 39/43 (BT-474, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.526×** | -9.7 | 3e-20 | 37/43 (SK-MEL-2, NCI-H1573, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -9.1 | 7e-18 | 36/42 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -8.8 | 5e-17 | 36/45 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.678×** | -8.2 | 7e-15 | 35/43 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.623×** | -7.1 | 5e-11 | 34/43 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.407×** | -7.1 | 5e-11 | 32/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.636×** | -6.8 | 4e-10 | 36/43 (HOP62, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.637×** | -6.8 | 4e-10 | 35/43 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.648×** | -6.3 | 1e-08 | 33/43 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -6.3 | 1e-08 | 32/43 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.661×** | -6.2 | 1e-08 | 36/44 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.716×** | -6.2 | 1e-08 | 33/43 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 265 | 0 | 24 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -33.2) |
| [[SK-MEL-2 (line)]] | alt | 178 | 0 | 24 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -28.7) |
| [[Hs 766T (line)]] | wt | 236 | 11 | 6 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.47× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -28.0) |
| [[C32 (line)]] | wt | 238 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -28.8) |
| [[BT-474 (line)]] | alt | 299 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -29.5) |
| [[MIA PaCa-2 (line)]] | alt | 250 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -35.6) |
| [[SW48 (line)]] | wt | 303 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 269 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -35.0) |
| [[CFPAC-1 (line)]] | alt | 215 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.8) |
| [[J82 (line)]] | alt | 269 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -34.3) |
| [[PANC-1 (line)]] | alt | 108 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -28.6) |
| [[HT-29 (line)]] | alt | 320 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -26.8) |
| [[KATO III (line)]] | alt | 212 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -30.7) |
| [[NCI-H460 (line)]] | wt | 143 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -29.9) |
| [[Panc 03.27 (line)]] | alt | 224 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -26.8) |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0845× (z -36.3) |
| [[HEC-1-A (line)]] | alt | 126 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -22.6) |
| [[RKO (line)]] | wt | 125 | 1 | 8 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.77× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -20.1) |
| [[H4 (line)]] | wt | 188 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -26.6) |
| [[LoVo (line)]] | wt | 146 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -23.4) |
| [[NCI-H2347 (line)]] | alt | 177 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -29.0) |
| [[A549 (line)]] | wt | 129 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -29.0) |
| [[COLO 205 (line)]] | alt | 215 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -34.7) |
| [[HS-578T (line)]] | alt | 140 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -19.3) |
| [[SW 900 (line)]] | alt | 109 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -19.8) |
| [[SW480 (line)]] | alt | 111 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -22.5) |
| [[HCT15 (line)]] | alt | 168 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.7) |
| [[LS 180 (line)]] | wt | 120 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -32.2) |
| [[SNU-423 (line)]] | alt | 177 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -21.5) |
| [[SW1417 (line)]] | alt | 126 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -17.8) |
| [[A-172 (line)]] | wt | 183 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -25.1) |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -25.6) |
| [[SW 1271 (line)]] | alt | 297 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -16.5) |
| [[A498 (line)]] | wt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -10.4) |
| [[CHP-212 (line)]] | wt | 87.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 69.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0850× (z -19.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 50.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 41.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0933× (z -17.8) |
| [[SW 1088 (line)]] | alt | 213 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0824× (z -11.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.6) |
| [[A-427 (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 34.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPCAL1]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.73 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ACOT7]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PHC2]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SLCO4A1]] | +0.71 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[TGM2]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[CAPRIN2]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[EHBP1L1]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[VASP]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN31]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[FAM111A-DT]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DRAM1]] | -0.55 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[TCEAL1]] | -0.53 | -0.56 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 26, C 5. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLPH]] | B | MLPH activity raises NIBAN2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 3.07× lower at baseline in the lines without MLPH | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[LINC02320]] | B | LINC02320 activity raises NIBAN2's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without LINC02320 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[MLPH]] | B | MLPH activity strengthens NIBAN2's drug response | lines that do not express MLPH (9) vs lines expressing it (35) | the lines without MLPH respond 0.67× as strongly (z diff +2.40); strongest at Panobinostat 5 µM: 0.79x vs 0.39x (z diff +5.2) | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32; target measured in part of the lines; artifact flags |
| [[PLEK2]] | B | PLEK2 activity raises NIBAN2's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without PLEK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TREM1]] | B | TREM1 activity raises NIBAN2's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without TREM1 | 0.019 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[TOR4A]] | B | TOR4A activity raises NIBAN2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without TOR4A | 0.023 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[ABHD17C]] | B | ABHD17C activity raises NIBAN2's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without ABHD17C | 0.023 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[LINC02320]] | B | LINC02320 activity strengthens NIBAN2's drug response | lines that do not express LINC02320 (15) vs lines expressing it (29) | the lines without LINC02320 respond 0.80× as strongly (z diff +1.83); strongest at Panobinostat 5 µM: 0.60x vs 0.39x (z diff +2.8) | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088; target measured in part of the lines; artifact flags |
| [[SLCO4A1]] | B | SLCO4A1 activity raises NIBAN2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without SLCO4A1 | 0.030 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[SERPINA1]] | B | SERPINA1 activity raises NIBAN2's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 1.72× lower at baseline in the lines without SERPINA1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3 |
| [[EMP1]] | B | EMP1 activity raises NIBAN2's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without EMP1 | 0.042 | ⚠ within organs, on part of the lines |
| [[SH3TC2]] | B | SH3TC2 activity raises NIBAN2's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without SH3TC2 | 0.043 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 29, C 4. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | B | NIBAN2 activity raises ITGA2's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 6.55× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[MT2A]] | B | NIBAN2 activity raises MT2A's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 4.18× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TOR4A]] | B | NIBAN2 activity raises TOR4A's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.61× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[MT1X]] | B | NIBAN2 activity raises MT1X's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.60× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[STX1A]] | B | NIBAN2 activity raises STX1A's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.26× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[KCNN4]] | B | NIBAN2 activity raises KCNN4's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.24× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[ITGB5]] | B | NIBAN2 activity raises ITGB5's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.11× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[PLEC]] | B | NIBAN2 activity raises PLEC's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TBC1D8]] | B | NIBAN2 activity raises TBC1D8's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[ACTN1]] | B | NIBAN2 activity raises ACTN1's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.73× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[PTPN12]] | B | NIBAN2 activity raises PTPN12's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TRIOBP]] | B | NIBAN2 activity raises TRIOBP's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.1, 5.3); signed map (7.1, 48.1). **Vector** length 124, 50.0% of its response variance represented; |z| ≥ 3 in 1,940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +7.0 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.5 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.4 | -11.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.7 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +3.0 | +1.3 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -8.9 | -6.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.8 | -6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.2 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.9 | -6.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.7 | -8.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.6 | -5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -7.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | niban apoptosis regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,505,339-127,578,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434H0820, FLJ13518, FLJ22151, FLJ22298, bA356B19.6, MINERVA; previously C9orf88, FAM129B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96TA1](https://www.uniprot.org/uniprotkb/Q96TA1) (Protein Niban 2):

> May play a role in apoptosis suppression. May promote melanoma cell invasion in vitro.

**Summary**, from NCBI Gene [64855](https://www.ncbi.nlm.nih.gov/gene/64855):

> Enables transcription coactivator activity. Involved in several processes, including gonadotropin secretion; negative regulation of DNA biosynthetic process; and regulation of DNA-templated transcription. Located in several cellular components, including adherens junction; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25282) · Entrez [64855](https://www.ncbi.nlm.nih.gov/gene/64855) · UniProt [Q96TA1](https://www.uniprot.org/uniprotkb/Q96TA1) · Ensembl [ENSG00000136830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136830)

## Data

Gene col 5914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5914); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5914]; `tensor/DDL_lfc|DDL_z.npy` [5914]; `embed/gene_vectors.npy` [5914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5914 or target_col == 5914). Every well: [[NIBAN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIBAN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
