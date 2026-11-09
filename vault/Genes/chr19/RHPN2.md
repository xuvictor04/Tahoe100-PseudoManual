---
symbol: "RHPN2"
type: "gene"
col: 5258
ensembl_id: "ENSG00000131941"
name: "rhophilin Rho GTPase binding protein 2"
location: "19q13.11"
module: 194
arm: "-"
pooled_cpm: 136.55
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 42
direction_downstream: 7
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# RHPN2

*rhophilin Rho GTPase binding protein 2* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.66× (z +10.8, q 3e-24, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.370× (z -29.7, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFD]] (+0.71, fdr 1e-05), [[SPATA13]] (+0.68, fdr 1e-05), [[CARHSP1]] (+0.66, fdr 5e-05); moves opposite to [[PRDM5]] (-0.65, fdr 3e-05), [[CSTF3]] (-0.63, fdr 1e-04), [[ZNF621]] (-0.61, fdr 2e-05).
> It sits in the **-** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[CLDN4]] → it (grade B ⚠); 7 go from it, the strongest it → [[CTNND1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +10.8 | 3e-24 | 28/44 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +8.6 | 3e-15 | 27/44 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.7 | 3e-12 | 26/44 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.3 | 6e-11 | 26/44 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +4.5 | 6e-04 | 15/45 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.007 | 14/44 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.050 | 10/45 (CFPAC-1, SW 900, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | 1.18× | +3.3 | 0.063 | 10/45 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.092 | 12/44 (HOP62, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.370×** | -29.7 | 0e+00 | 43/45 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -15.1 | 0e+00 | 40/44 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.478×** | -15.0 | 0e+00 | 33/38 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -14.8 | 0e+00 | 34/44 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.624×** | -14.1 | 5e-43 | 29/44 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.528×** | -13.5 | 2e-39 | 35/44 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.509×** | -13.2 | 8e-38 | 35/40 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.656×** | -12.6 | 2e-34 | 34/44 (SW1417, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -12.1 | 7e-32 | 37/46 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.625×** | -9.5 | 9e-20 | 30/44 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -8.9 | 4e-17 | 31/43 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -8.7 | 1e-16 | 32/44 (BT-474, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -6.6 | 1e-09 | 26/44 (NCI-H1573, SW48, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.779×** | -5.0 | 2e-05 | 23/43 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.787×** | -5.0 | 2e-05 | 27/44 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.793×** | -4.9 | 4e-05 | 22/44 (SW 900, CFPAC-1, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.006 | 20/44 (NCI-H2347, SW 1271, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.841× | -3.6 | 0.007 | 18/44 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.722×** | -3.6 | 0.008 | 19/45 (KATO III, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.788×** | -3.6 | 0.008 | 20/44 (BT-474, AsPC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 243 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -22.1) |
| [[CFPAC-1 (line)]] | alt | 280 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -28.2) |
| [[HT-29 (line)]] | alt | 452 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -25.8) |
| [[KATO III (line)]] | alt | 241 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -18.6) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -24.5) |
| [[SW1417 (line)]] | alt | 295 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -32.2) |
| [[AsPC-1 (line)]] | alt | 315 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -25.5) |
| [[LS 180 (line)]] | wt | 302 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 175 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -24.4) |
| [[LoVo (line)]] | wt | 421 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -19.2) |
| [[A549 (line)]] | wt | 183 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -13.7) |
| [[COLO 205 (line)]] | alt | 229 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 259 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -22.0) |
| [[PANC-1 (line)]] | alt | 164 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -23.5) |
| [[SW 900 (line)]] | alt | 104 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -21.0) |
| [[HOP62 (line)]] | alt | 59.1 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 83.5 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -19.6) |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -15.2) |
| [[A498 (line)]] | wt | 146 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.5) |
| [[HCT15 (line)]] | alt | 199 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 64.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -11.6) |
| [[SW48 (line)]] | wt | 79.3 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -10.0) |
| [[A-172 (line)]] | wt | 69.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -17.8) |
| [[SW480 (line)]] | alt | 103 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -27.0) |
| [[A-427 (line)]] | wt | 47.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -15.9) |
| [[Hs 766T (line)]] | wt | 47.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 94.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -22.0) |
| [[SNU-423 (line)]] | alt | 43.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.4) |
| [[C32 (line)]] | wt | 71.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.3) |
| [[AN3 CA (line)]] | alt | 71.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.5) |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -12.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 48.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 48.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0848× (z -8.6) |
| [[RKO (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 27.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | +0.71 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SPATA13]] | +0.68 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.66 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[RAB11FIP1]] | +0.65 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TC2N]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[GPRC5A]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[EPHB3]] | +0.63 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[EPB41L1]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CASP9]] | +0.63 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[IFFO2]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RASSF7]] | +0.62 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[TJP3]] | +0.62 | +0.47 / +0.58 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*31 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM5]] | -0.65 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.63 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[ZNF621]] | -0.61 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[UNC50]] | -0.61 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.61 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | -0.60 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[DPH5-DT]] | -0.60 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[MSANTD2]] | -0.60 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[UBE3B]] | -0.59 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.59 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANGEL2]] | -0.59 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SPRY3]] | -0.59 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.58 | -0.54 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 41, C 1. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN4]] | B | CLDN4 activity raises RHPN2's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without CLDN4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[CDH1]] | B | CDH1 activity raises RHPN2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.44× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[NCMAP]] | B | NCMAP activity raises RHPN2's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without NCMAP | 0.001 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises RHPN2's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without GPRC5A | 0.002 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[TC2N]] | B | TC2N activity raises RHPN2's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without TC2N | 0.003 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[GRB7]] | B | GRB7 activity raises RHPN2's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.10× lower at baseline in the lines without GRB7 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[ST14]] | B | ST14 activity raises RHPN2's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.45× lower at baseline in the lines without ST14 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ELF3]] | B | ELF3 activity raises RHPN2's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.71× lower at baseline in the lines without ELF3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[FA2H]] | B | FA2H activity raises RHPN2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.77× lower at baseline in the lines without FA2H | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[TJP3]] | B | TJP3 activity raises RHPN2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without TJP3 | 0.008 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[CLMN]] | B | CLMN activity raises RHPN2's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.95× lower at baseline in the lines without CLMN | 0.010 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[KCNK1]] | B | KCNK1 activity raises RHPN2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.63× lower at baseline in the lines without KCNK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTNND1]] | C | RHPN2 activity raises CTNND1's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without RHPN2 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |
| [[CDC42SE2]] | C | RHPN2 activity raises CDC42SE2's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without RHPN2 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |
| [[KIAA1522]] | C | RHPN2 activity raises KIAA1522's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without RHPN2 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |
| [[RASSF7]] | C | RHPN2 activity raises RASSF7's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without RHPN2 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent; co-absent with the target |
| [[ARHGEF3]] | C | RHPN2 activity raises ARHGEF3's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 2.56× lower at baseline in the lines without RHPN2 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |
| [[CLMN]] | C | RHPN2 activity raises CLMN's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without RHPN2 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |
| [[SYNGR2]] | C | RHPN2 activity raises SYNGR2's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without RHPN2 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **-** arm (projection on the module's main direction -0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.8, 34.4); signed map (-18.6, 34.2). **Vector** length 132, 42.3% of its response variance represented; |z| ≥ 3 in 1,360 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +10.0 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.7 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +9.4 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +7.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -15.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -14.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -29.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -8.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | rhophilin Rho GTPase binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,978,592-33,064,888 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 7 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; RHOB GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUC4](https://www.uniprot.org/uniprotkb/Q8IUC4) (Rhophilin-2):

> Binds specifically to GTP-Rho. May function in a Rho pathway to limit stress fiber formation and/or increase the turnover of F-actin structures in the absence of high levels of RhoA activity.

**Summary**, from NCBI Gene [85415](https://www.ncbi.nlm.nih.gov/gene/85415):

> This gene encodes a member of the rhophilin family of Ras-homologous (Rho)-GTPase binding proteins. The encoded protein binds both GTP- and GDP-bound RhoA and GTP-bound RhoB and may be involved in the organization of the actin cytoskeleton. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:19974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19974) · Entrez [85415](https://www.ncbi.nlm.nih.gov/gene/85415) · UniProt [Q8IUC4](https://www.uniprot.org/uniprotkb/Q8IUC4) · Ensembl [ENSG00000131941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131941)

## Data

Gene col 5258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5258); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5258]; `tensor/DDL_lfc|DDL_z.npy` [5258]; `embed/gene_vectors.npy` [5258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5258 or target_col == 5258). Every well: [[RHPN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHPN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
